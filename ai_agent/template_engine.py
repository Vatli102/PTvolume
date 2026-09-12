# -*- coding: utf-8 -*-
"""
Trình render HTML template chuẩn mực cho PTvolume.com
Sử dụng phương pháp replace placeholder {{TAG}} an toàn tuyệt đối với CSS và JavaScript.
"""

def generate_lesson_html(data):
    takeaways_html = "\n".join([
        f'<li><i class="fa-solid fa-circle-check"></i> <strong>{t[0]}</strong> {t[1]}</li>'
        for t in data["takeaways"]
    ])
    
    comments_html = "\n".join([
        f'''<div class="comment-item">
            <div class="comment-top">
                <span class="comment-author"><i class="fa-solid fa-circle-user"></i> {c[0]}</span>
                <span class="comment-date">{c[1]}</span>
            </div>
            <div class="comment-text">{c[2]}</div>
        </div>'''
        for c in data["comments"]
    ])

    meta_title = data["title"].replace("&ndash;", "-").replace("&amp;", "&")

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-T0JM1RNTZ9"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());

      gtag('config', 'G-T0JM1RNTZ9');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{meta_title} | PTvolume</title>
    <meta name="description" content="{data['desc']}">
    <link rel="icon" type="image/jpeg" href="../assets/images/logo.jpg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Merriweather:ital,wght@0,400;0,700;1,400&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <style>
        :root {{
            --bg-main: #0B0E14;
            --bg-card: #141822;
            --bg-card-hover: #1A2130;
            --border-color: #222938;
            --primary: #2962FF;
            --primary-glow: rgba(41, 98, 255, 0.25);
            --bullish: #089981;
            --bearish: #F23645;
            --text-main: #F0F3FA;
            --text-muted: #8E9BAE;
            --text-light: #CAD4E0;
            --accent-gold: #F0B90B;
            --accent-cyan: #00E5FF;
            --font-editorial: 'Merriweather', Georgia, serif;
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: var(--font-sans);
        }}

        *, body, p, div, span, h1, h2, h3, h4, h5, h6, table, td, th {{
            -webkit-user-select: text !important;
            -moz-user-select: text !important;
            -ms-user-select: text !important;
            user-select: text !important;
        }}

        body {{
            background-color: var(--bg-main);
            color: var(--text-main);
            line-height: 1.85;
        }}

        a {{
            text-decoration: none;
            color: inherit;
        }}

        header {{
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(11, 14, 20, 0.95);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border-color);
        }}

        .nav-container {{
            max-width: 1100px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 24px;
        }}

        .logo {{
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 800;
            font-size: 1.35rem;
            color: #fff;
        }}

        .logo img {{
            width: 40px;
            height: 40px;
            border-radius: 8px;
            object-fit: cover;
            border: 1px solid rgba(41, 98, 255, 0.4);
        }}

        .logo-text .brand {{
            font-size: 1.2rem;
            font-weight: 800;
        }}

        .logo-text .brand span {{
            color: var(--accent-cyan);
        }}

        .nav-right {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .lang-switcher {{
            display: inline-flex;
            align-items: center;
            background: #080B10;
            border: 1px solid var(--border-color);
            border-radius: 20px;
            padding: 2px;
            gap: 2px;
        }}

        .lang-btn {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 4px 10px;
            border-radius: 16px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            transition: all 0.2s ease;
        }}

        .lang-btn.active, .lang-btn:hover {{
            background: var(--primary);
            color: #fff;
        }}

        .btn {{
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.85rem;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: var(--primary);
            color: #fff;
            border: none;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .btn:hover {{
            background: #1e4bd8;
            transform: translateY(-1px);
        }}

        .article-container {{
            max-width: 940px;
            margin: 40px auto 80px;
            padding: 0 24px;
        }}

        .breadcrumb {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 20px;
            flex-wrap: wrap;
        }}

        .breadcrumb a:hover {{
            color: var(--accent-cyan);
        }}

        .article-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            background: rgba(0, 229, 255, 0.15);
            color: var(--accent-cyan);
            border: 1px solid rgba(0, 229, 255, 0.35);
            margin-bottom: 16px;
        }}

        .article-title {{
            font-family: var(--font-editorial);
            font-size: 2.1rem;
            line-height: 1.38;
            color: #fff;
            margin-bottom: 18px;
            font-weight: 700;
        }}

        .article-meta {{
            display: flex;
            align-items: center;
            gap: 16px;
            font-size: 0.85rem;
            color: var(--text-muted);
            padding-bottom: 20px;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 32px;
            flex-wrap: wrap;
        }}

        .article-meta span {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}

        .article-body {{
            font-family: var(--font-editorial);
            font-size: 1.08rem;
            color: var(--text-light);
            line-height: 1.95;
            text-align: justify;
            text-justify: inter-word;
        }}

        .article-body p {{
            margin-bottom: 24px;
            text-align: justify;
            text-justify: inter-word;
        }}

        .article-body h2 {{
            font-family: var(--font-sans);
            font-size: 1.42rem;
            color: #fff;
            margin: 42px 0 18px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 10px;
            border-left: 4px solid var(--accent-cyan);
            padding-left: 14px;
            text-align: left;
        }}

        .article-body h3 {{
            font-family: var(--font-sans);
            font-size: 1.18rem;
            color: var(--accent-gold);
            margin: 30px 0 14px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
            text-align: left;
        }}

        .article-body ul, .article-body ol {{
            margin-bottom: 26px;
            padding-left: 24px;
            text-align: justify;
            text-justify: inter-word;
        }}

        .article-body li {{
            margin-bottom: 12px;
            text-align: justify;
            text-justify: inter-word;
        }}

        .article-body strong {{
            color: #fff;
            font-family: inherit;
        }}

        .article-body blockquote {{
            background: #141822;
            border-left: 4px solid var(--accent-cyan);
            padding: 18px 22px;
            margin: 26px 0;
            border-radius: 0 8px 8px 0;
            font-style: italic;
            color: #F0F3FA;
            text-align: justify;
            text-justify: inter-word;
        }}

        .watermark-box {{
            position: relative;
            margin: 28px 0 32px;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            background: #080B10;
            text-align: center;
        }}

        .watermark-box img {{
            max-width: 100%;
            height: auto;
            display: inline-block;
            margin: 0 auto;
            border-radius: 6px;
        }}

        .watermark-caption {{
            font-family: var(--font-sans);
            font-size: 0.82rem;
            color: var(--text-muted);
            padding: 8px 14px;
            background: #10141D;
            border-top: 1px solid var(--border-color);
            text-align: center;
            font-style: italic;
        }}

        .watermark-stamp {{
            position: absolute;
            bottom: 42px;
            right: 18px;
            background: rgba(11, 14, 20, 0.65);
            backdrop-filter: blur(6px);
            border: 1px solid rgba(0, 229, 255, 0.3);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--accent-cyan);
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 6px;
            pointer-events: none;
        }}

        .takeaways-box {{
            background: #141822;
            border: 1px solid rgba(0, 229, 255, 0.4);
            border-radius: 12px;
            padding: 24px 28px;
            margin: 32px 0 36px;
        }}

        .takeaways-title {{
            font-family: var(--font-sans);
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--accent-cyan);
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .takeaways-list {{
            list-style: none;
            padding-left: 0;
            margin-bottom: 0;
        }}

        .takeaways-list li {{
            position: relative;
            padding-left: 28px;
            margin-bottom: 14px;
            font-family: var(--font-sans);
            font-size: 0.96rem;
            line-height: 1.65;
            color: var(--text-light);
            text-align: justify;
            text-justify: inter-word;
        }}

        .takeaways-list li i {{
            position: absolute;
            left: 0;
            top: 4px;
            color: var(--accent-cyan);
            font-size: 0.9rem;
        }}

        .highlight-box {{
            background: #141822;
            border: 1px solid rgba(240, 185, 11, 0.35);
            border-radius: 12px;
            padding: 24px;
            margin: 32px 0;
            text-align: justify;
            text-justify: inter-word;
        }}

        .highlight-box h3 {{
            color: var(--accent-gold);
            margin-top: 0;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .step-card {{
            background: #141822;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 22px;
            margin-bottom: 22px;
            border-left: 4px solid var(--primary);
        }}

        .step-card p {{
            text-align: justify;
            text-justify: inter-word;
            margin-bottom: 0;
        }}

        .step-card h4 {{
            color: #fff;
            font-size: 1.1rem;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: var(--font-sans);
        }}

        .data-table-wrapper {{
            overflow-x: auto;
            margin: 28px 0;
            border: 1px solid var(--border-color);
            border-radius: 8px;
        }}

        table.data-table {{
            width: 100%;
            border-collapse: collapse;
            font-family: var(--font-sans);
            font-size: 0.92rem;
            text-align: left;
        }}

        table.data-table th {{
            background: #141822;
            color: var(--accent-cyan);
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
            font-weight: 700;
        }}

        table.data-table td {{
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
            color: var(--text-light);
            text-align: justify;
            text-justify: inter-word;
        }}

        table.data-table tr:hover td {{
            background: rgba(41, 98, 255, 0.05);
        }}

        .nav-lesson-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin: 40px 0;
        }}

        @media (max-width: 700px) {{
            .nav-lesson-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        .nav-lesson-card {{
            background: linear-gradient(135deg, #101624 0%, #152238 100%);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 18px 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.2s ease;
        }}

        .nav-lesson-card:hover {{
            border-color: var(--accent-cyan);
            transform: translateY(-2px);
        }}

        .comments-section {{
            margin-top: 50px;
            padding-top: 36px;
            border-top: 1px solid var(--border-color);
        }}

        .comments-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 24px;
        }}

        .comments-title {{
            font-family: var(--font-sans);
            font-size: 1.35rem;
            font-weight: 700;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .comment-box {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 24px;
            margin-bottom: 30px;
        }}

        .form-group {{
            margin-bottom: 16px;
        }}

        .form-label {{
            display: block;
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-light);
            margin-bottom: 8px;
        }}

        .form-control {{
            width: 100%;
            background: #080B10;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 10px 14px;
            color: #fff;
            font-size: 0.9rem;
            transition: all 0.2s ease;
        }}

        .form-control:focus {{
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 2px var(--primary-glow);
        }}

        textarea.form-control {{
            min-height: 100px;
            resize: vertical;
        }}

        .comment-list {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}

        .comment-item {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 16px 20px;
        }}

        .comment-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
            font-size: 0.82rem;
        }}

        .comment-author {{
            font-weight: 700;
            color: var(--accent-cyan);
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .comment-date {{
            color: var(--text-muted);
        }}

        .comment-text {{
            font-size: 0.92rem;
            color: var(--text-light);
            line-height: 1.6;
            text-align: justify;
            text-justify: inter-word;
        }}

        footer {{
            background: #080B10;
            border-top: 1px solid var(--border-color);
            padding: 40px 24px;
            text-align: center;
            font-size: 0.85rem;
            color: var(--text-muted);
        }}

        .footer-links {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }}

        .footer-links a:hover {{
            color: #fff;
        }}
    </style>
</head>
<body>

    <header>
        <div class="nav-container">
            <a href="../index.html" class="logo">
                <img src="../assets/images/logo.jpg" alt="Logo PT VOLUME">
                <div class="logo-text">
                    <span class="brand">PT<span>VOLUME</span></span>
                </div>
            </a>
            
            <div class="nav-right">
                <div class="lang-switcher">
                    <button class="lang-btn active" onclick="setLanguage('vi')" id="btn-lang-vi" title="Tiếng Việt">VI</button>
                    <button class="lang-btn" onclick="setLanguage('en')" id="btn-lang-en" title="English">EN</button>
                </div>
                <a href="../index.html" class="btn">
                    <i class="fa-solid fa-arrow-left"></i> Về Trang Chủ
                </a>
            </div>
        </div>
    </header>

    <main class="article-container">
        <div class="breadcrumb">
            <a href="../index.html">Trang Chủ</a>
            <i class="fa-solid fa-chevron-right" style="font-size: 0.7rem;"></i>
            <a href="../index.html#hoc-tap">Học Tập</a>
            <i class="fa-solid fa-chevron-right" style="font-size: 0.7rem;"></i>
            <span>{data['badge']}</span>
        </div>

        <span class="article-badge"><i class="fa-solid fa-graduation-cap"></i> {data['badge']}</span>
        
        <h1 class="article-title">{data['title']}</h1>

        <div class="article-meta">
            <span><i class="fa-regular fa-calendar"></i> {data['date']}</span>
            <span><i class="fa-solid fa-clock"></i> {data['read_time']}</span>
            <span><i class="fa-solid fa-user-pen"></i> PTvolume Institutional Desk</span>
            <span><i class="fa-solid fa-eye"></i> {data['views']}</span>
        </div>

        <!-- EXECUTIVE SUMMARY -->
        <div class="takeaways-box">
            <div class="takeaways-title">
                <i class="fa-solid fa-bolt"></i> TÓM TẮT CỐT LÕI (EXECUTIVE SUMMARY)
            </div>
            <ul class="takeaways-list">
                {takeaways_html}
            </ul>
        </div>

        <div class="article-body">
            <blockquote>
                "{data['quote']}"
                <br><br>
                — <strong>{data['quote_author']}</strong>
            </blockquote>

            <div class="watermark-box">
                <img src="{data['image']}" alt="{data['title']}">
                <div class="watermark-stamp"><i class="fa-solid fa-shield-halved"></i> PTvolume.com</div>
                <div class="watermark-caption">{data['image_caption']}</div>
            </div>

            {data['html_content']}

            <!-- NEXT / PREV LESSON NAVIGATION -->
            <div class="nav-lesson-grid">
                <a href="{data['prev_slug']}.html" class="nav-lesson-card">
                    <span style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;"><i class="fa-solid fa-arrow-left"></i> Bài Trước</span>
                    <strong style="font-size:0.95rem; color:var(--accent-cyan); margin-top:6px;">{data['prev_title']}</strong>
                </a>
                <a href="{data['next_slug']}.html" class="nav-lesson-card" style="text-align:right;">
                    <span style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Bài Kế Tiếp <i class="fa-solid fa-arrow-right"></i></span>
                    <strong style="font-size:0.95rem; color:var(--accent-gold); margin-top:6px;">{data['next_title']}</strong>
                </a>
            </div>

            <!-- COMMENTS SECTION -->
            <div class="comments-section">
                <div class="comments-header">
                    <div class="comments-title">
                        <i class="fa-regular fa-comments" style="color:var(--accent-cyan);"></i> Thảo Luận Kỹ Thuật Cùng Cộng Đồng (<span id="commentCount">3</span>)
                    </div>
                </div>

                <div class="comment-box">
                    <form id="commentForm" onsubmit="addComment(event)">
                        <div class="form-group">
                            <label class="form-label" for="commentName"><i class="fa-solid fa-user"></i> Tên của bạn / Biệt danh Trader</label>
                            <input type="text" id="commentName" class="form-control" placeholder="VD: Hoàng Long - Naked Chart Trader" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label" for="commentContent"><i class="fa-solid fa-comment-dots"></i> Góc nhìn kỹ thuật hoặc câu hỏi thực chiến của bạn</label>
                            <textarea id="commentContent" class="form-control" rows="3" placeholder="Chia sẻ góc nhìn hoặc đặt câu hỏi kỹ thuật về bài học này..." required></textarea>
                        </div>
                        <button type="submit" class="btn" style="background:var(--accent-cyan); color:#000; font-weight:700;">
                            <i class="fa-solid fa-paper-plane"></i> Gửi Bình Luận Ngay
                        </button>
                    </form>
                </div>

                <div class="comment-list" id="commentList">
                    {comments_html}
                </div>
            </div>

        </div>
    </main>

    <footer>
        <div class="footer-links">
            <a href="../pages/about.html">Về Chúng Tôi</a>
            <a href="../pages/contact.html">Liên Hệ Hỗ Trợ</a>
            <a href="../pages/disclaimer.html">Tuyên Bố Rủi Ro (Disclaimer)</a>
            <a href="../pages/privacy.html">Chính Sách Bảo Mật</a>
            <a href="../pages/terms.html">Điều Khoản Sử Dụng</a>
        </div>
        <p>© 2026 PTvolume.com. Toàn bộ bản quyền được bảo lưu. Naked Chart • VSA • Phương Pháp Wyckoff.</p>
        <p style="font-size: 0.75rem; color: #505D75; margin-top: 8px;">Nội dung phục vụ mục đích giáo dục &amp; nghiên cứu tài chính, không cấu thành lời khuyên đầu tư tài chính trực tiếp.</p>
    </footer>

    <div id="google_translate_element" style="display:none;"></div>

    <script>
        function googleTranslateElementInit() {{
            new google.translate.TranslateElement({{
                pageLanguage: 'vi',
                includedLanguages: 'en,vi',
                autoDisplay: false
            }}, 'google_translate_element');
        }}

        function setLanguage(lang) {{
            localStorage.setItem('ptvolume_lang', lang);
            updateLangButtons(lang);

            document.cookie = "googtrans=/vi/" + lang + "; path=/;";
            if (window.location.hostname && window.location.hostname !== '') {{
                document.cookie = "googtrans=/vi/" + lang + "; path=/; domain=" + window.location.hostname;
            }}

            const select = document.querySelector('.goog-te-combo');
            if (select) {{
                select.value = lang;
                select.dispatchEvent(new Event('change'));
            }} else {{
                window.location.reload();
            }}
        }}

        function updateLangButtons(lang) {{
            const btnVi = document.getElementById('btn-lang-vi');
            const btnEn = document.getElementById('btn-lang-en');
            if (btnVi && btnEn) {{
                if (lang === 'en') {{
                    btnEn.classList.add('active');
                    btnVi.classList.remove('active');
                }} else {{
                    btnVi.classList.add('active');
                    btnEn.classList.remove('active');
                }}
            }}
        }}

        function applyStoredLanguage() {{
            const currentLang = localStorage.getItem('ptvolume_lang') || 'vi';
            updateLangButtons(currentLang);
            if (currentLang === 'en') {{
                let attempts = 0;
                const checkCombo = setInterval(() => {{
                    const select = document.querySelector('.goog-te-combo');
                    if (select) {{
                        select.value = 'en';
                        select.dispatchEvent(new Event('change'));
                        clearInterval(checkCombo);
                    }}
                    attempts++;
                    if (attempts > 30) clearInterval(checkCombo);
                }}, 200);
            }}
        }}

        const POST_SLUG = "{data['slug']}";

        function loadSavedComments() {{
            const saved = JSON.parse(localStorage.getItem('ptvolume_comments_' + POST_SLUG) || '[]');
            const commentList = document.getElementById("commentList");
            if (commentList && saved.length > 0) {{
                saved.forEach(item => {{
                    const newComment = document.createElement("div");
                    newComment.className = "comment-item";
                    newComment.innerHTML = `
                        <div class="comment-top">
                            <span class="comment-author"><i class="fa-solid fa-circle-user"></i> ${{escapeHtml(item.name)}}</span>
                            <span class="comment-date">${{escapeHtml(item.date)}}</span>
                        </div>
                        <div class="comment-text">${{escapeHtml(item.content)}}</div>
                    `;
                    commentList.prepend(newComment);
                }});
                const countElem = document.getElementById("commentCount");
                if (countElem) {{
                    countElem.innerText = parseInt(countElem.innerText || 3) + saved.length;
                }}
            }}
        }}

        function addComment(e) {{
            e.preventDefault();
            const nameInput = document.getElementById("commentName");
            const contentInput = document.getElementById("commentContent");
            if (!nameInput || !contentInput) return;
            const name = nameInput.value.trim();
            const content = contentInput.value.trim();
            if (!name || !content) return;

            const now = new Date();
            const timeString = now.toLocaleDateString('vi-VN') + ' ' + now.toLocaleTimeString('vi-VN');

            const commentList = document.getElementById("commentList");
            const newComment = document.createElement("div");
            newComment.className = "comment-item";
            newComment.innerHTML = `
                <div class="comment-top">
                    <span class="comment-author"><i class="fa-solid fa-circle-user"></i> ${{escapeHtml(name)}}</span>
                    <span class="comment-date">${{timeString}}</span>
                </div>
                <div class="comment-text">${{escapeHtml(content)}}</div>
            `;
            commentList.prepend(newComment);

            const countElem = document.getElementById("commentCount");
            if (countElem) countElem.innerText = parseInt(countElem.innerText || 3) + 1;

            const saved = JSON.parse(localStorage.getItem('ptvolume_comments_' + POST_SLUG) || '[]');
            saved.push({{ name, content, date: timeString }});
            localStorage.setItem('ptvolume_comments_' + POST_SLUG, JSON.stringify(saved));

            nameInput.value = "";
            contentInput.value = "";
            alert("Bình luận của bạn đã được đăng thành công!");
        }}

        function escapeHtml(text) {{
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            applyStoredLanguage();
            loadSavedComments();
        }});
    </script>
    <script src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>

</body>
</html>"""
    return html

print("Loaded safe template_engine with f-string rendering.")
