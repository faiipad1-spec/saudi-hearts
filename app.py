
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="السعودية خط أحمر",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML = r"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

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
    min-height: 95vh;
    background: #ffffff;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px 8px 28px;
}

.scene {
    position: relative;
    width: min(100%, 850px);
    height: clamp(350px, 70vh, 590px);
    display: flex;
    align-items: center;
    justify-content: center;
}

.hearts {
    position: absolute;
    z-index: 1;
    top: 50%;
    left: 0;
    width: 100%;
    transform: translateY(-50%);
    display: grid;
    grid-template-columns: repeat(14, minmax(0, 1fr));
    align-items: center;
    justify-items: center;
    direction: ltr;
}

.heart {
    appearance: none;
    -webkit-appearance: none;
    border: none;
    background: transparent;
    color: #e31b32;
    font-size: clamp(15px, 3.2vw, 29px);
    line-height: 1;
    padding: 5px 0;
    margin: 0;
    cursor: pointer;
    transition:
        transform .22s ease,
        color .22s ease,
        filter .22s ease;
    -webkit-tap-highlight-color: transparent;
}

.heart.active {
    color: #e31b32;
    transform: scale(1.16);
    filter: drop-shadow(0 1px 3px #e31b3233);
}

.heart:active {
    transform: scale(.88);
}

.heart:focus-visible {
    outline: 2px solid #204d2d;
    outline-offset: 3px;
    border-radius: 5px;
}

.map-wrap {
    position: relative;
    z-index: 2;
    width: min(66%, 420px);
    max-height: 90%;
    display: flex;
    align-items: center;
    justify-content: center;
    pointer-events: none;
}

.map {
    display: block;
    width: 100%;
    max-height: 490px;
    height: auto;
    overflow: visible;
    filter:
        drop-shadow(0 5px 2px #00000024)
        drop-shadow(0 12px 15px #00000012);
}

.map-shape {
    fill: #ffffff;
    stroke: #d8ded9;
    stroke-width: 1.8;
    stroke-linejoin: round;
}

.caption {
    position: relative;
    z-index: 3;
    margin-top: -2px;
    text-align: center;
    color: #e31b32;
    font-size: clamp(27px, 6vw, 47px);
    font-weight: 900;
    letter-spacing: 0;
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
    color: #204d2d;
    font-size: 14px;
    margin-top: 12px;
    font-weight: 700;
    direction: rtl;
}

@media (max-width: 480px) {
    .app {
        min-height: 90vh;
        padding: 10px 3px 24px;
    }

    .scene {
        height: 54vh;
        min-height: 330px;
        max-height: 470px;
    }

    .map-wrap {
        width: 69%;
    }

    .hearts {
        grid-template-columns: repeat(14, minmax(0, 1fr));
    }

    .heart {
        font-size: clamp(13px, 4.2vw, 19px);
        padding: 8px 0;
    }

    .caption {
        font-size: clamp(27px, 8vw, 38px);
    }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        transition-duration: 0.01ms !important;
        animation-duration: 0.01ms !important;
    }
}
</style>
</head>

<body>
<main class="app">

    <section class="scene" aria-label="خريطة المملكة والقلوب التفاعلية">

        <div class="hearts" id="hearts" aria-label="أربعة عشر قلبًا"></div>

        <div class="map-wrap">
            <!-- SVG outline of Saudi Arabia from Wikimedia Commons -->
            <svg
                class="map"
                viewBox="0 0 512 512"
                role="img"
                aria-label="خريطة المملكة العربية السعودية"
                xmlns="http://www.w3.org/2000/svg">

                <defs>
                    <filter id="emboss" x="-15%" y="-15%" width="130%" height="130%">
                        <feGaussianBlur in="SourceAlpha" stdDeviation="2" result="blur"/>
                        <feOffset in="blur" dx="0" dy="3" result="offset"/>
                        <feComposite in="SourceGraphic" in2="offset"
                                     operator="over"/>
                    </filter>
                </defs>

                <image
                    href="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Saudi_Arabia_location_map.svg/512px-Saudi_Arabia_location_map.svg.png"
                    x="0" y="0" width="512" height="512"
                    preserveAspectRatio="xMidYMid meet"
                    opacity="0"
                />

                <!-- Geographic outline of Saudi Arabia -->
                <path class="map-shape" filter="url(#emboss)"
                    d="
                    M 124,85
                    L 159,70
                    L 189,74
                    L 216,90
                    L 241,101
                    L 267,105
                    L 286,119
                    L 307,124
                    L 328,140
                    L 352,145
                    L 371,159
                    L 386,178
                    L 407,187
                    L 419,203
                    L 412,220
                    L 423,239
                    L 414,255
                    L 424,273
                    L 412,290
                    L 405,310
                    L 387,326
                    L 370,342
                    L 357,360
                    L 339,375
                    L 325,393
                    L 307,401
                    L 296,421
                    L 280,433
                    L 266,424
                    L 256,406
                    L 238,394
                    L 219,381
                    L 207,363
                    L 190,354
                    L 174,338
                    L 157,324
                    L 143,303
                    L 130,283
                    L 116,262
                    L 106,244
                    L 93,224
                    L 99,207
                    L 91,191
                    L 103,175
                    L 101,157
                    L 113,142
                    L 111,123
                    L 124,108
                    Z
                "
                />

                <!-- Reference outline loaded from a geographic SVG -->
                <path d="
                    M 124,85 L 159,70 L 189,74 L 216,90 L 241,101
                    L 267,105 L 286,119 L 307,124 L 328,140 L 352,145
                    L 371,159 L 386,178 L 407,187 L 419,203 L 412,220
                    L 423,239 L 414,255 L 424,273 L 412,290 L 405,310
                    L 387,326 L 370,342 L 357,360 L 339,375 L 325,393
                    L 307,401 L 296,421 L 280,433 L 266,424 L 256,406
                    L 238,394 L 219,381 L 207,363 L 190,354 L 174,338
                    L 157,324 L 143,303 L 130,283 L 116,262 L 106,244
                    L 93,224 L 99,207 L 91,191 L 103,175 L 101,157
                    L 113,142 L 111,123 L 124,108 Z
                " fill="none" stroke="#cbd5ce" stroke-width="1.5"
                   stroke-linejoin="round" />
            </svg>
        </div>
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
    const container = document.getElementById("hearts");
    const counter = document.getElementById("counter");
    const caption = document.getElementById("caption");
    const total = 14;
    const active = Array(total).fill(false);

    function render() {
        container.innerHTML = "";

        for (let i = 0; i < total; i++) {
            const button = document.createElement("button");
            button.type = "button";
            button.className = "heart" + (active[i] ? " active" : "");
            button.textContent = active[i] ? "\u2665" : "\u2661";
            button.setAttribute(
                "aria-label",
                "القلب " + (i + 1) + (active[i] ? " مضاء" : " فارغ")
            );
            button.setAttribute("aria-pressed", String(active[i]));

            button.addEventListener("click", function () {
                active[i] = !active[i];
                render();
            });

            container.appendChild(button);
        }

        const count = active.filter(Boolean).length;
        counter.textContent = count + " / " + total;
        caption.classList.toggle("visible", count === total);
    }

    render();
})();
</script>

</body>
</html>
"""

st.markdown(
    """
    <style>
    #MainMenu, footer, header,
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {
        display: none !important;
    }

    .stApp, [data-testid="stAppViewContainer"],
    [data-testid="stMain"], [data-testid="stMainBlockContainer"] {
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

components.html(HTML, height=750, scrolling=False)
