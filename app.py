import streamlit as st
import streamlit.components.v1 as components

# ضبط إعدادات الصفحة لتكون بعرض الشاشة وبدون القوائم الافتراضية لـ Streamlit
st.set_page_config(
    page_title="السعودية خط أحمر",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# كود HTML + CSS + JS الشامل لإدارة الواجهة والتفاعلية
html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>السعودية خط أحمر</title>
    <!-- استدعاء خط Amiri و Cairo للجملة العربية -->
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Cairo:wght@900&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body, html {
            width: 100%;
            height: 100vh;
            overflow: hidden;
            background-color: #ffffff; /* خلفية بيضاء */
            font-family: 'Cairo', 'Amiri', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* إخفاء شريط التمرير */
        ::-webkit-scrollbar {
            display: none;
        }

        /* الحاوية الرئيسية */
        .main-container {
            position: relative;
            width: 100%;
            max-width: 900px;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        /* صف القلوب الخلفي */
        .hearts-layer {
            position: absolute;
            top: 45%;
            left: 0;
            width: 100%;
            transform: translateY(-50%);
            display: flex;
            justify-content: space-evenly;
            align-items: center;
            z-index: 1;
            padding: 0 10px;
        }

        /* زر القلب */
        .heart-btn {
            background: none;
            border: none;
            cursor: pointer;
            outline: none;
            transition: transform 0.2s ease, filter 0.2s ease;
            padding: 2px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .heart-btn:hover {
            transform: scale(1.15);
        }

        .heart-btn:active {
            transform: scale(0.95);
        }

        .heart-icon {
            width: 28px;
            height: 28px;
            fill: none;
            stroke: #e60000;
            stroke-width: 2.5;
            transition: all 0.3s ease;
        }

        /* حالة القلب النشط/المكتمل */
        .heart-btn.active .heart-icon {
            fill: #e60000;
            stroke: #e60000;
            animation: pulse 0.4s ease-in-out;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.3); }
            100% { transform: scale(1); }
        }

        /* حاوية الخريطة الطبقية */
        .map-container {
            position: relative;
            z-index: 2; /* الخريطة تظهر فوق القلوب */
            width: 85%;
            max-width: 520px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
            /* تأثير 3D بارز ونحتي للخريطة */
            filter: drop-shadow(0px 10px 15px rgba(0, 70, 30, 0.35))
                    drop-shadow(0px 2px 4px rgba(0, 0, 0, 0.2));
        }

        .map-svg {
            width: 100%;
            height: auto;
            max-height: 55vh;
            /* لون أخضر ملكي داكن للمملكة */
            fill: #1b4d2e;
            transition: fill 0.3s ease;
        }

        .map-svg:hover {
            fill: #143d24;
        }

        /* حاوية العبارة العربية */
        .text-container {
            position: absolute;
            bottom: 12%;
            z-index: 3;
            text-align: center;
            min-height: 80px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .saudi-title {
            color: #e60000;
            font-size: 3.2rem;
            font-weight: 900;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.15);
            opacity: 0;
            transform: translateY(20px) scale(0.9);
            transition: opacity 0.6s ease, transform 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            pointer-events: none;
            user-select: none;
            white-space: nowrap;
        }

        /* ظهور الجملة عند تفعيل كافة القلوب */
        .saudi-title.show {
            opacity: 1;
            transform: translateY(0) scale(1);
        }

        /* التجاوب مع شاشات الجوال و iPhone */
        @media (max-width: 600px) {
            .heart-icon {
                width: 20px;
                height: 20px;
                stroke-width: 2;
            }
            .map-container {
                width: 92%;
            }
            .saudi-title {
                font-size: 2.2rem;
            }
            .hearts-layer {
                padding: 0 4px;
            }
        }
    </style>
</head>
<body>

<div class="main-container">

    <!-- صف القلوب الـ 14 الأفقية خلف الخريطة -->
    <div class="hearts-layer" id="heartsLayer">
        <!-- سيتم توليد الـ 14 قلب تلقائياً بواسطة JavaScript -->
    </div>

    <!-- خريطة المملكة العربية السعودية الرسمية الدقيقة (SVG) -->
    <div class="map-container">
        <svg class="map-svg" viewBox="0 0 800 650" xmlns="http://www.w3.org/2000/svg">
            <path d="M 688,272 L 675,280 L 660,295 L 642,305 L 620,320 L 595,340 L 560,375 L 530,410 L 490,455 L 450,490 L 415,510 L 385,515 L 360,505 L 340,480 L 325,450 L 315,420 L 300,395 L 285,380 L 270,375 L 245,385 L 220,395 L 195,400 L 170,395 L 150,380 L 135,355 L 130,330 L 135,300 L 145,275 L 155,250 L 160,225 L 155,200 L 140,180 L 120,165 L 105,150 L 95,130 L 100,110 L 115,95 L 135,85 L 160,80 L 190,82 L 225,90 L 260,105 L 295,120 L 330,135 L 370,145 L 410,150 L 450,155 L 490,158 L 530,160 L 565,165 L 600,175 L 630,190 L 655,210 L 675,235 Z" />
            <!-- التفاصيل الحدودية والدقيقة لخريطة السعودية -->
            <path d="M 190,82 L 230,60 L 275,45 L 320,40 L 365,42 L 400,50 L 430,65 L 455,85 L 470,110 L 485,135 L 490,158 Z" />
            <path d="M 600,175 L 635,160 L 670,155 L 705,165 L 730,185 L 745,210 L 750,235 L 740,255 L 715,270 L 688,272 Z" />
            <path d="M 490,455 L 530,470 L 570,490 L 610,515 L 640,545 L 660,580 L 650,600 L 620,605 L 580,590 L 535,560 L 495,525 L 465,495 Z" />
            <path d="M 130,330 L 110,350 L 95,380 L 90,410 L 100,435 L 120,450 L 145,455 L 170,445 L 195,425 L 210,405 Z" />
        </svg>
    </div>

    <!-- النصوص الظاهرة بعد الضغط على كافة القلوب -->
    <div class="text-container">
        <h1 class="saudi-title" id="saudiText">السعودية خط أحمر</h1>
    </div>

</div>

<script>
    const TOTAL_HEARTS = 14;
    const heartsLayer = document.getElementById('heartsLayer');
    const saudiText = document.getElementById('saudiText');
    
    // مصفوفة لتتبع حالة القلوب (true = ممتلئ, false = مفرغ)
    let heartStates = new Array(TOTAL_HEARTS).fill(false);

    // SVG للقلب المفرغ والممتلئ
    const heartSVG = `
        <svg class="heart-icon" viewBox="0 0 24 24">
            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
        </svg>
    `;

    // إنشاء الـ 14 قلباً
    for (let i = 0; i < TOTAL_HEARTS; i++) {
        const btn = document.createElement('button');
        btn.className = 'heart-btn';
        btn.setAttribute('aria-label', `قلب ${i + 1}`);
        btn.innerHTML = heartSVG;
        btn.dataset.index = i;

        btn.addEventListener('click', () => toggleHeart(i, btn));
        heartsLayer.appendChild(btn);
    }

    function toggleHeart(index, element) {
        // تبديل الحالة
        heartStates[index] = !heartStates[index];

        if (heartStates[index]) {
            element.classList.add('active');
        } else {
            element.classList.remove('active');
        }

        checkAllHearts();
    }

    function checkAllHearts() {
        // التاكد من أن جميع الـ 14 قلباً تم الضغط عليها وممتلئة
        const allActive = heartStates.every(state => state === true);

        if (allActive) {
            saudiText.classList.add('show');
        } else {
            saudiText.classList.remove('show');
        }
    }
</script>

</body>
</html>
"""

# إخفاء عناصر Streamlit الافتراضية بالكامل للحصول على تجربة صفحة واحدة غاطسة
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        div.block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# عرض المكون التفاهلي ملء الشاشة
components.html(html_code, height=1000, scrolling=False)
