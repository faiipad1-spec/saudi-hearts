import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="السعودية خط أحمر",
    page_icon="♥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's chrome so the embedded experience fills the screen.
st.markdown(
    """
    <style>
      #MainMenu, footer, header, [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display:none !important;}
      html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"],
      [data-testid="stMainBlockContainer"], .stApp {
        background:#204D2D !important;
        margin:0 !important; padding:0 !important;
      }
      [data-testid="stMainBlockContainer"] {
        max-width:none !important; width:100% !important;
        padding:0 !important; margin:0 !important;
      }
      iframe {border:0 !important; display:block;}
    </style>
    """,
    unsafe_allow_html=True,
)

page = r"""
<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover">
<style>
  :root { --green:#204D2D; --red:#ff263b; }
  * { box-sizing:border-box; }
  html, body {
    width:100%; height:100%; margin:0; overflow:hidden;
    background:var(--green); color:#fff;
    font-family:Tahoma, Arial, sans-serif;
    -webkit-tap-highlight-color:transparent;
  }
  .stage {
    position:relative; width:100%; height:100svh; min-height:440px;
    display:flex; align-items:center; justify-content:center;
    isolation:isolate; overflow:hidden; background:var(--green);
  }
  .heart-row {
    position:absolute; z-index:1; top:47%; left:0; right:0;
    transform:translateY(-50%);
    display:flex; direction:ltr; justify-content:space-evenly; align-items:center;
    gap:clamp(5px, 1.7vw, 24px); padding:0 clamp(8px, 2vw, 28px);
    pointer-events:auto;
  }
  .heart {
    flex:0 0 auto; width:clamp(22px, 3.25vw, 43px); height:clamp(22px, 3.25vw, 43px);
    padding:0; border:0; background:transparent; color:var(--red);
    cursor:pointer; display:grid; place-items:center;
    filter:drop-shadow(0 2px 3px rgba(0,0,0,.18));
    transition:transform .22s ease, filter .22s ease;
    touch-action:manipulation;
  }
  .heart svg { width:100%; height:100%; overflow:visible; }
  .heart svg path {
    fill:transparent; stroke:currentColor; stroke-width:2.1;
    stroke-linejoin:round; transition:fill .22s ease, stroke-width .22s ease;
  }
  .heart.active { transform:scale(1.13); filter:drop-shadow(0 0 8px rgba(255,38,59,.28)); }
  .heart.active svg path { fill:var(--red); stroke-width:1.5; }
  .heart:focus-visible { outline:2px solid white; outline-offset:5px; border-radius:5px; }
  .heart.pop { animation:pop .32s ease-out; }
  @keyframes pop { 0%{transform:scale(1)} 45%{transform:scale(1.32)} 100%{transform:scale(1.13)} }
  .composition {
    position:relative; z-index:2; width:min(72vw, 690px);
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    transform:translateY(-1%);
    pointer-events:none;
  }
  .map-wrap { width:100%; filter: drop-shadow(0 16px 11px rgba(0,0,0,.28)); }
  .map { display:block; width:100%; height:auto; overflow:visible; }
  .map .land {
    fill:#1B4327;
    stroke:#2B6038; stroke-width:2.2; stroke-linejoin:round;
    filter:url(#emboss);
  }
  .map .inner-shade { fill:url(#landShade); opacity:.7; }
  h1 {
    color:var(--red); font-size:clamp(27px, 4.2vw, 54px);
    line-height:1.35; margin:clamp(10px, 2.1vh, 24px) 0 0;
    font-weight:900; letter-spacing:0; text-align:center;
    text-shadow:0 2px 0 rgba(90,0,0,.18);
    white-space:nowrap;
  }
  @media (max-width:600px) {
    .stage { min-height:430px; }
    .heart-row { top:45%; gap:clamp(2px, .9vw, 7px); padding:0 5px; }
    .heart { width:clamp(19px, 5.15vw, 29px); height:clamp(19px, 5.15vw, 29px); }
    .composition { width:min(88vw, 470px); transform:translateY(-2%); }
    h1 { font-size:clamp(25px, 7vw, 37px); margin-top:17px; }
  }
  @media (max-height:520px) and (orientation:landscape) {
    .composition { width:min(52vw, 430px); }
    .heart-row { top:44%; }
    h1 { font-size:clamp(22px, 4vw, 34px); margin-top:8px; }
  }
  @media (prefers-reduced-motion:reduce) {
    *, *::before, *::after { animation:none !important; transition:none !important; }
  }
</style>
</head>
<body>
<main class="stage" aria-label="السعودية خط أحمر">
  <div class="heart-row" id="heartRow" aria-label="قلوب تفاعلية"></div>

  <section class="composition" aria-label="خريطة المملكة العربية السعودية">
    <div class="map-wrap">
      <!-- Simplified geographic outline silhouette of Saudi Arabia, embedded as SVG (no external asset). -->
      <svg class="map" viewBox="0 0 600 500" role="img" aria-label="Silhouette of Saudi Arabia" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="landShade" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" stop-color="#2A5B35"/>
            <stop offset=".48" stop-color="#214B2D"/>
            <stop offset="1" stop-color="#153820"/>
          </linearGradient>
          <filter id="emboss" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur in="SourceAlpha" stdDeviation="5" result="blur"/>
            <feOffset dx="-3" dy="-4" result="lightOffset"/>
            <feComposite in="SourceAlpha" in2="lightOffset" operator="arithmetic" k2="-1" k3="1" result="lightEdge"/>
            <feColorMatrix in="lightEdge" type="matrix"
              values="0 0 0 0 .20  0 0 0 0 .38  0 0 0 0 .23  0 0 0 .45 0" result="light"/>
            <feOffset in="SourceAlpha" dx="4" dy="5" result="darkOffset"/>
            <feGaussianBlur in="darkOffset" stdDeviation="4" result="darkBlur"/>
            <feComposite in="darkBlur" in2="SourceAlpha" operator="out" result="darkEdge"/>
            <feColorMatrix in="darkEdge" type="matrix"
              values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .45 0" result="shadow"/>
            <feMerge><feMergeNode in="shadow"/><feMergeNode in="light"/><feMergeNode in="SourceGraphic"/></feMerge>
          </filter>
        </defs>
        <g transform="translate(12 8)">
          <path class="land" d="M132,35
            L164,44 188,39 211,53 234,52 252,69 278,73 297,89
            318,91 337,111 359,119 380,136 403,143 421,161
            445,169 461,187 481,196 493,218 487,238 474,253
            469,274 453,289 447,309 431,326 419,349 402,367
            391,389 370,400 353,421 330,431 312,417 291,411
            274,397 253,392 238,378 218,370 205,351 186,342
            173,322 156,312 148,292 134,278 128,255 115,239
            109,217 95,201 91,181 101,166 99,147 111,131
            107,111 119,93 115,76 128,61 Z"/>
          <path class="inner-shade" d="M132,35
            L164,44 188,39 211,53 234,52 252,69 278,73 297,89
            318,91 337,111 359,119 380,136 403,143 421,161
            445,169 461,187 481,196 493,218 487,238 474,253
            469,274 453,289 447,309 431,326 419,349 402,367
            391,389 370,400 353,421 330,431 312,417 291,411
            274,397 253,392 238,378 218,370 205,351 186,342
            173,322 156,312 148,292 134,278 128,255 115,239
            109,217 95,201 91,181 101,166 99,147 111,131
            107,111 119,93 115,76 128,61 Z"/>
        </g>
      </svg>
    </div>
    <h1 dir="rtl">السعودية خط أحمر</h1>
  </section>
</main>
<script>
  const row = document.getElementById('heartRow');
  const heartSvg = '<svg viewBox="0 0 32 29" aria-hidden="true"><path d="M16 26.2 3.5 14.3C-3.2 7.5 6.5-1.4 13.1 5.1L16 8l2.9-2.9C25.5-1.4 35.2 7.5 28.5 14.3Z"/></svg>';
  // A generous row creates visible hearts on both sides of the overlaid map.
  const count = window.matchMedia('(max-width: 600px)').matches ? 17 : 21;
  for (let i = 0; i < count; i++) {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'heart';
    button.innerHTML = heartSvg;
    button.setAttribute('aria-label', 'تفعيل القلب ' + (i + 1));
    button.setAttribute('aria-pressed', 'false');
    button.addEventListener('click', () => {
      const active = button.classList.toggle('active');
      button.classList.remove('pop');
      // Restart the short activation animation on every toggle.
      void button.offsetWidth;
      if (active) button.classList.add('pop');
      button.setAttribute('aria-pressed', String(active));
      button.setAttribute('aria-label', (active ? 'إلغاء تفعيل القلب ' : 'تفعيل القلب ') + (i + 1));
    });
    row.appendChild(button);
  }
</script>
</body>
</html>
"""

components.html(page, height=800, scrolling=False)
