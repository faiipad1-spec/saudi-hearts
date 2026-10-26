
import json
import math
import urllib.request

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="السعودية خط أحمر",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# تحميل الحدود الجغرافية للمملكة وتحويلها إلى مسار SVG.
@st.cache_data(ttl=86400, show_spinner=False)
def get_saudi_map():
    url = (
        "https://raw.githubusercontent.com/"
        "datasets/geo-countries/master/data/countries.geojson"
    )

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "SaudiHeartsApp/1.0"},
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))

    feature = None

    for item in data["features"]:
        props = item.get("properties", {})
        values = [
            str(v).strip().lower()
            for v in props.values()
            if isinstance(v, str)
        ]

        if (
            "saudi arabia" in values
            or props.get("ISO3166-1-Alpha-3") == "SAU"
            or props.get("ADM0_A3") == "SAU"
        ):
            feature = item
            break

    if feature is None:
        raise ValueError("Saudi Arabia was not found in the GeoJSON data.")

    geometry = feature["geometry"]

    if geometry["type"] == "Polygon":
        polygons = [geometry["coordinates"]]
    elif geometry["type"] == "MultiPolygon":
        polygons = geometry["coordinates"]
    else:
        raise ValueError("Unsupported map geometry.")

    all_points = [
        point
        for polygon in polygons
        for ring in polygon
        for point in ring
    ]

    if not all_points:
        raise ValueError("Map coordinates are empty.")

    mean_lat = sum(p[1] for p in all_points) / len(all_points)
    lon_factor = math.cos(math.radians(mean_lat))

    projected = [
        (lon * lon_factor, lat)
        for lon, lat in all_points
    ]

    min_x = min(p[0] for p in projected)
    max_x = max(p[0] for p in projected)
    min_y = min(p[1] for p in projected)
    max_y = max(p[1] for p in projected)

    width = 600
    height = 700
    padding = 24

    scale = min(
        (width - 2 * padding) / (max_x - min_x),
        (height - 2 * padding) / (max_y - min_y),
    )

    drawn_width = (max_x - min_x) * scale
    drawn_height = (max_y - min_y) * scale

    offset_x = (width - drawn_width) / 2
    offset_y = (height - drawn_height) / 2

    def project(lon, lat):
        x = lon * lon_factor
        return (
            offset_x + (x - min_x) * scale,
            offset_y + (max_y - lat) * scale,
        )

    paths = []

    for polygon in polygons:
        rings = []

        for ring in polygon:
            if len(ring) < 3:
                continue

            points = [project(lon, lat) for lon, lat in ring]

            rings.append(
                "M "
                + " L ".join(
                    f"{x:.2f},{y:.2f}" for x, y in points
                )
                + " Z"
            )

        paths.extend(rings)

    return " ".join(paths)


try:
    map_path = get_saudi_map()
except Exception:
    st.error(
        "تعذر تحميل الخريطة الجغرافية. "
        "تحققي من اتصال الإنترنت ثم أعيدي تحميل التطبيق."
    )
    st.stop()


html = r"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<style>
* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
    background: #ffffff;
    font-family: Tahoma, Arial, sans-serif;
}

body {
    overflow-x: hidden;
}

.app {
    width: 100%;
    min-height: 720px;
    background: #ffffff;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 15px 4px 28px;
}

.scene {
    width: min(100%, 900px);
    min-height: 570px;
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(180px, 2fr) minmax(0, 1fr);
    align-items: center;
    justify-items: center;
    direction: ltr;
    gap: 5px;
}

.hearts {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    align-content: center;
    justify-items: center;
    align-items: center;
    gap: 28px 4px;
    direction: ltr;
    z-index: 3;
}

.heart {
    appearance: none;
    -webkit-appearance: none;
    border: 0;
    background: transparent;
    color: #e31837;
    font-family: Arial, sans-serif;
    font-size: clamp(22px, 3.5vw, 34px);
    line-height: 1;
    padding: 6px 2px;
    margin: 0;
    cursor: pointer;
    transition: transform .22s ease, color .22s ease;
    -webkit-tap-highlight-color: transparent;
    touch-action: manipulation;
}

.heart.active {
    color: #e31837;
    transform: scale(1.18);
}

.heart:active {
    transform: scale(.88);
}

.heart:focus-visible {
    outline: 2px solid #204d2d;
    outline-offset: 3px;
}

.map-wrap {
    width: 100%;
    height: 520px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    z-index: 2;
    pointer-events: none;
}

.map {
    display: block;
    width: 100%;
    height: 100%;
    overflow: visible;
    filter:
        drop-shadow(0 3px 2px #00000018)
        drop-shadow(0 10px 13px #00000010);
}

.map-shape {
    fill: #ffffff;
    stroke: #cfd8d1;
    stroke-width: 2.2;
    stroke-linejoin: round;
    stroke-linecap: round;
    fill-rule: evenodd;
}

.caption {
    margin-top: 0;
    text-align: center;
    color: #e31837;
    font-size: clamp(28px, 5.5vw, 47px);
    font-weight: 900;
    line-height: 1.5;
    opacity: 0;
    transform: translateY(8px);
    transition: opacity .45s ease, transform .45s ease;
}

.caption.visible {
    opacity: 1;
    transform: translateY(0);
}

.counter {
    margin-top: 12px;
    color: #204d2d;
    font-size: 14px;
    font-weight: bold;
    direction: rtl;
}

@media (max-width: 480px) {
    .app {
        min-height: 90vh;
        padding: 12px 3px 22px;
    }

    .scene {
        min-height: 440px;
        grid-template-columns: minmax(0, 1fr) minmax(0, 1.8fr) minmax(0, 1fr);
        gap: 2px;
    }

    .hearts {
        grid-template-columns: 1fr;
        gap: 24px;
    }

    .heart {
        font-size: clamp(22px, 6vw, 28px);
        padding: 7px 0;
    }

    .map-wrap {
        height: 410px;
    }

    .caption {
        font-size: clamp(27px, 8vw, 38px);
    }
}

@media (max-width: 350px) {
    .scene {
        grid-template-columns: minmax(0, .85fr) minmax(0, 1.8fr) minmax(0, .85fr);
    }

    .heart {
        font-size: 20px;
    }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        transition-duration: .01ms !important;
    }
}
</style>
</head>

<body>
<main class="app">

    <section class="scene"
             aria-label="خريطة المملكة والقلوب التفاعلية">

        <!-- سبعة قلوب على اليسار -->
        <div class="hearts" id="hearts-left"></div>

        <!-- الخريطة في المنتصف -->
        <div class="map-wrap">
            <svg class="map"
                 viewBox="0 0 600 700"
                 role="img"
                 aria-label="خريطة المملكة العربية السعودية"
                 xmlns="http://www.w3.org/2000/svg">
                <path class="map-shape"
                      d="__SAUDI_MAP_PATH__"/>
            </svg>
        </div>

        <!-- سبعة قلوب على اليمين -->
        <div class="hearts" id="hearts-right"></div>

    </section>

    <div class="caption" id="caption" aria-live="polite">
        السعودية خط أحمر
    </div>

    <div class="counter" id="counter" aria-live="polite">
        0 / 14
    </div>

</main>

<script>
(function () {
    const left = document.getElementById("hearts-left");
    const right = document.getElementById("hearts-right");
    const caption = document.getElementById("caption");
    const counter = document.getElementById("counter");

    const total = 14;
    const active = Array(total).fill(false);

    function render() {
        left.innerHTML = "";
        right.innerHTML = "";

        for (let i = 0; i < total; i++) {
            const button = document.createElement("button");

            button.type = "button";
            button.className =
                "heart" + (active[i] ? " active" : "");

            button.textContent = active[i] ? "\u2665" : "\u2661";

            button.setAttribute(
                "aria-label",
                "القلب " + (i + 1)
            );

            button.setAttribute(
                "aria-pressed",
                String(active[i])
            );

            button.addEventListener("click", function () {
                active[i] = !active[i];
                render();
            });

            if (i < 7) {
                left.appendChild(button);
            } else {
                right.appendChild(button);
            }
        }

        const count = active.filter(Boolean).length;

        counter.textContent = count + " / " + total;

        caption.classList.toggle(
            "visible",
            count === total
        );
    }

    render();
})();
</script>

</body>
</html>
"""

html = html.replace("__SAUDI_MAP_PATH__", map_path)

st.markdown(
    """
    <style>
    #MainMenu,
    footer,
    header,
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {
        display: none !important;
    }

    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"] {
        background: #ffffff !important;
    }

    [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        max-width: 100% !important;
    }

    iframe {
        border: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(
    html,
    height=760,
    scrolling=False,
)
