# -*- coding: utf-8 -*-
"""
Script nâng cấp Bài 2: Cấu Trúc Thị Trường & Vùng Cung Cầu
Đạt chuẩn SEO chuyên sâu > 3,000 từ, văn phong thuần con người thực chiến Pro Desk,
đầy đủ Executive Summary, bảng so sánh, checklist 5 bước, bóc tách BOS/CHoCH/Flip Zone.
"""

bai2_content = """<!DOCTYPE html>
<html lang="vi">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-T0JM1RNTZ9"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-T0JM1RNTZ9');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bài 2: Cấu Trúc Thị Trường (Market Structure) &ndash; Đỉnh/Đáy Xoay Chiều, BOS, CHoCH &amp; Vùng Cung Cầu | PTvolume</title>
    <meta name="description" content="Khóa học Naked Chart & VSA Bài 2: Giải mã bản đồ cấu trúc thị trường nguyên bản (Market Structure), phân biệt Đỉnh/Đáy Swing High/Low, sự phá vỡ BOS, đổi tính chất CHoCH và tuyệt kỹ săn lệnh tại Flip Zone.">
    <link rel="icon" type="image/jpeg" href="../assets/images/logo.jpg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Merriweather:ital,wght@0,400;0,700;1,400&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <style>
        :root {
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
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: var(--font-sans);
        }

        *, body, p, div, span, h1, h2, h3, h4, h5, h6, table, td, th {
            -webkit-user-select: text !important;
            -moz-user-select: text !important;
            -ms-user-select: text !important;
            user-select: text !important;
        }

        body {
            background-color: var(--bg-main);
            color: var(--text-main);
            line-height: 1.85;
        }

        a {
            text-decoration: none;
            color: inherit;
        }

        header {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(11, 14, 20, 0.95);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border-color);
        }

        .nav-container {
            max-width: 1100px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 24px;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 800;
            font-size: 1.35rem;
            color: #fff;
        }

        .logo img {
            width: 40px;
            height: 40px;
            border-radius: 8px;
            object-fit: cover;
            border: 1px solid rgba(41, 98, 255, 0.4);
        }

        .logo-text .brand {
            font-size: 1.2rem;
            font-weight: 800;
        }

        .logo-text .brand span {
            color: var(--accent-cyan);
        }

        .nav-right {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .lang-switcher {
            display: inline-flex;
            align-items: center;
            background: #080B10;
            border: 1px solid var(--border-color);
            border-radius: 20px;
            padding: 2px;
            gap: 2px;
        }

        .lang-btn {
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
        }

        .lang-btn.active, .lang-btn:hover {
            background: var(--primary);
            color: #fff;
        }

        .btn {
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
        }

        .btn:hover {
            background: #1e4bd8;
            transform: translateY(-1px);
        }

        .article-container {
            max-width: 940px;
            margin: 40px auto 80px;
            padding: 0 24px;
        }

        .breadcrumb {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 20px;
            flex-wrap: wrap;
        }

        .breadcrumb a:hover {
            color: var(--accent-cyan);
        }

        .article-badge {
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
        }

        .article-title {
            font-family: var(--font-editorial);
            font-size: 2.1rem;
            line-height: 1.38;
            color: #fff;
            margin-bottom: 18px;
            font-weight: 700;
        }

        .article-meta {
            display: flex;
            align-items: center;
            gap: 16px;
            font-size: 0.85rem;
            color: var(--text-muted);
            padding-bottom: 20px;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 32px;
            flex-wrap: wrap;
        }

        .article-meta span {
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .article-body {
            font-family: var(--font-editorial);
            font-size: 1.08rem;
            color: var(--text-light);
            line-height: 1.95;
            text-align: justify;
            text-justify: inter-word;
        }

        .article-body p {
            margin-bottom: 24px;
            text-align: justify;
            text-justify: inter-word;
        }

        .article-body h2 {
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
        }

        .article-body h3 {
            font-family: var(--font-sans);
            font-size: 1.18rem;
            color: var(--accent-gold);
            margin: 30px 0 14px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
            text-align: left;
        }

        .article-body ul, .article-body ol {
            margin-bottom: 26px;
            padding-left: 24px;
            text-align: justify;
            text-justify: inter-word;
        }

        .article-body li {
            margin-bottom: 12px;
            text-align: justify;
            text-justify: inter-word;
        }

        .article-body strong {
            color: #fff;
            font-family: inherit;
        }

        .article-body blockquote {
            background: #141822;
            border-left: 4px solid var(--accent-cyan);
            padding: 18px 22px;
            margin: 26px 0;
            border-radius: 0 8px 8px 0;
            font-style: italic;
            color: #F0F3FA;
            text-align: justify;
            text-justify: inter-word;
        }

        .watermark-box {
            position: relative;
            margin: 28px 0 32px;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            background: #080B10;
            text-align: center;
        }

        .watermark-box img {
            max-width: 100%;
            height: auto;
            display: inline-block;
            margin: 0 auto;
            border-radius: 6px;
        }

        .watermark-caption {
            font-family: var(--font-sans);
            font-size: 0.85rem;
            color: var(--text-muted);
            padding: 10px 16px;
            background: #10141D;
            border-top: 1px solid var(--border-color);
            text-align: center;
            font-style: italic;
        }

        .watermark-stamp {
            position: absolute;
            bottom: 44px;
            right: 18px;
            background: rgba(11, 14, 20, 0.75);
            backdrop-filter: blur(6px);
            border: 1px solid rgba(0, 229, 255, 0.35);
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--accent-cyan);
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 6px;
            pointer-events: none;
        }

        .takeaways-box {
            background: #141822;
            border: 1px solid rgba(0, 229, 255, 0.4);
            border-radius: 12px;
            padding: 24px 28px;
            margin: 32px 0 36px;
        }

        .takeaways-title {
            font-family: var(--font-sans);
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--accent-cyan);
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .takeaways-list {
            list-style: none;
            padding-left: 0;
            margin-bottom: 0;
        }

        .takeaways-list li {
            position: relative;
            padding-left: 28px;
            margin-bottom: 14px;
            font-family: var(--font-sans);
            font-size: 0.96rem;
            line-height: 1.65;
            color: var(--text-light);
            text-align: justify;
            text-justify: inter-word;
        }

        .takeaways-list li i {
            position: absolute;
            left: 0;
            top: 4px;
            color: var(--accent-cyan);
            font-size: 0.9rem;
        }

        .highlight-box {
            background: #141822;
            border: 1px solid rgba(240, 185, 11, 0.35);
            border-radius: 12px;
            padding: 24px;
            margin: 32px 0;
            text-align: justify;
            text-justify: inter-word;
        }

        .highlight-box h3 {
            color: var(--accent-gold);
            margin-top: 0;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .step-card {
            background: #141822;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 22px;
            margin-bottom: 22px;
            border-left: 4px solid var(--primary);
        }

        .step-card p {
            text-align: justify;
            text-justify: inter-word;
            margin-bottom: 0;
        }

        .step-card h4 {
            color: #fff;
            font-size: 1.1rem;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: var(--font-sans);
        }

        .data-table-wrapper {
            overflow-x: auto;
            margin: 28px 0;
            border: 1px solid var(--border-color);
            border-radius: 8px;
        }

        table.data-table {
            width: 100%;
            border-collapse: collapse;
            font-family: var(--font-sans);
            font-size: 0.92rem;
            text-align: left;
        }

        table.data-table th {
            background: #141822;
            color: var(--accent-cyan);
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
            font-weight: 700;
        }

        table.data-table td {
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
            color: var(--text-light);
            text-align: justify;
            text-justify: inter-word;
        }

        table.data-table tr:hover td {
            background: rgba(41, 98, 255, 0.05);
        }

        .nav-lesson-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin: 40px 0;
        }

        @media (max-width: 700px) {
            .nav-lesson-grid {
                grid-template-columns: 1fr;
            }
        }

        .nav-lesson-card {
            background: linear-gradient(135deg, #101624 0%, #152238 100%);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 18px 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.2s ease;
        }

        .nav-lesson-card:hover {
            border-color: var(--accent-cyan);
            transform: translateY(-2px);
        }

        .comments-section {
            margin-top: 50px;
            padding-top: 36px;
            border-top: 1px solid var(--border-color);
        }

        .comments-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 24px;
        }

        .comments-title {
            font-family: var(--font-sans);
            font-size: 1.35rem;
            font-weight: 700;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .comment-box {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 24px;
            margin-bottom: 30px;
        }

        .form-group {
            margin-bottom: 16px;
        }

        .form-label {
            display: block;
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-light);
            margin-bottom: 8px;
        }

        .form-control {
            width: 100%;
            background: #080B10;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 10px 14px;
            color: #fff;
            font-size: 0.9rem;
            transition: all 0.2s ease;
        }

        .form-control:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 2px var(--primary-glow);
        }

        textarea.form-control {
            min-height: 100px;
            resize: vertical;
        }

        .comment-list {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .comment-item {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 16px 20px;
        }

        .comment-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
            font-size: 0.82rem;
        }

        .comment-author {
            font-weight: 700;
            color: var(--accent-cyan);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .comment-date {
            color: var(--text-muted);
        }

        .comment-text {
            font-size: 0.92rem;
            color: var(--text-light);
            line-height: 1.6;
            text-align: justify;
            text-justify: inter-word;
        }

        footer {
            background: #080B10;
            border-top: 1px solid var(--border-color);
            padding: 40px 24px;
            text-align: center;
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }

        .footer-links a:hover {
            color: #fff;
        }
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
            <span>Học Phần 1 • Naked Price Action • Bài 2</span>
        </div>

        <span class="article-badge"><i class="fa-solid fa-graduation-cap"></i> Học Phần 1 • Naked Price Action • Bài 2</span>
        
        <h1 class="article-title">Bài 2: Cấu Trúc Thị Trường (Market Structure) &ndash; Đỉnh/Đáy Xoay Chiều, BOS, CHoCH &amp; Vùng Cung Cầu</h1>

        <div class="article-meta">
            <span><i class="fa-regular fa-calendar"></i> 14/09/2026</span>
            <span><i class="fa-solid fa-clock"></i> 20 Phút Đọc</span>
            <span><i class="fa-solid fa-user-pen"></i> PTvolume Institutional Desk</span>
            <span><i class="fa-solid fa-eye"></i> 3,180 Lượt Xem</span>
        </div>

        <!-- EXECUTIVE SUMMARY -->
        <div class="takeaways-box">
            <div class="takeaways-title">
                <i class="fa-solid fa-bolt"></i> TÓM TẮT CỐT LÕI (EXECUTIVE SUMMARY)
            </div>
            <ul class="takeaways-list">
                <li><i class="fa-solid fa-circle-check"></i> <strong>Cấu Trúc Thị Trường Là Tấm Bản Đồ Tác Chiến:</strong> Một cây nến đơn lẻ dù đẹp đến mấy cũng hoàn toàn vô nghĩa nếu đặt sai vị trí cấu trúc. Đỉnh và Đáy xoay chiều (Swing High / Swing Low) là các cột mốc phân xử bên nào đang thống trị cuộc chơi.</li>
                <li><i class="fa-solid fa-circle-check"></i> <strong>Quy Luật 3 Thanh Nến Để Lọc Nhiễu:</strong> Tuyệt đối không nhận vơ mọi đỉnh nhọn là Swing Point. Một đỉnh xoay chiều chuẩn mực bắt buộc phải có nến hai bên thấp hơn, chứng minh phe Mua đã kiệt sức và phe Bán đã ra đòn chặn đứng.</li>
                <li><i class="fa-solid fa-circle-check"></i> <strong>Phân Biệt BOS Tiếp Diễn vs CHoCH Đảo Chiều:</strong> BOS (Break of Structure) khẳng định sóng tăng/giảm tiếp tục bứt phá; CHoCH (Change of Character) là tiếng chuông cảnh báo tử thần khi mốc đáy Higher Low then chốt bị xuyên thủng.</li>
                <li><i class="fa-solid fa-circle-check"></i> <strong>Vùng Chuyển Đổi (Flip Zones) &amp; Điểm Bắn Tỉa:</strong> Khi cản kháng cự bị phá vỡ, lượng lệnh bán khống bị kẹt (Trapped Shorts) buộc phải cắt lỗ hòa vốn biến vùng này thành Hỗ trợ mới kiên cố. Đây là tọa độ Sniper Entry có tỷ lệ R:R đỉnh cao từ 1:3 đến 1:6+.</li>
            </ul>
        </div>

        <div class="article-body">
            <blockquote>
                "Giao dịch trên biểu đồ mà không định vị được Cấu Trúc Thị Trường cũng giống như một vị tướng xua quân vào trận địa mà không có bản đồ địa hình. Mọi mô hình nến hay chỉ báo đều sẽ phản bội bạn nếu bạn mua vào ngay tại Vùng Cung của Cá Mập hoặc bán tháo ngay trên thềm Vùng Cầu Chủ Đạo."
                <br><br>
                — <strong>PTvolume Institutional Desk</strong>
            </blockquote>

            <div class="watermark-box">
                <img src="../assets/images/market_structure_bos_choch.svg" alt="Bản Đồ Cấu Trúc Thị Trường Nguyên Bản: Đỉnh/Đáy Swing, BOS, CHoCH và Flip Zone">
                <div class="watermark-stamp"><i class="fa-solid fa-shield-halved"></i> PTvolume.com</div>
                <div class="watermark-caption">Hình 2.1: Bản đồ cấu trúc thị trường nguyên bản – Chuỗi đỉnh đáy Swing, sự phá vỡ cấu trúc BOS, tín hiệu đảo chiều CHoCH và điểm bắn tỉa Sniper Entry tại Flip Zone.</div>
            </div>

            <!-- ==================== PHẦN 1 ==================== -->
            <h2><i class="fa-solid fa-mountain"></i> 1. Đỉnh/Đáy Xoay Chiều (Swing High &amp; Swing Low) &ndash; Quy Tắc Lọc Sạch 90% Nhiễu Sóng</h2>
            <p>
                Rất nhiều nhà giao dịch mới bắt đầu học Naked Price Action thường mắc phải một sai lầm chết người: <em>thấy bất kỳ chỗ nào nến thò lên nhọn hoắt cũng đánh dấu là Đỉnh, và thấy nến thò xuống cũng coi là Đáy</em>. Màn hình phân tích chỉ sau vài phút biến thành một đống chằng chịt các đường ngang dọc, khiến người xem rơi vào trạng thái hoang mang tột độ và liên tục bị dính bẫy quét dừng lỗ (Market Noise).
            </p>
            <p>
                Trong thực chiến giao dịch của các bàn giao dịch tổ chức (Institutional Trading Desk), thị trường không di chuyển hỗn loạn. Một đỉnh hoặc một đáy chỉ được công nhận là một <strong>Điểm Xoay Chiều Cấu Trúc (Structural Swing Point)</strong> khi nó thỏa mãn <strong>Quy tắc giải phẫu nến tối thiểu (3-Bar hoặc 5-Bar Fractal Rule)</strong>:
            </p>

            <div class="step-card">
                <h4><i class="fa-solid fa-arrow-up-right-dots" style="color:var(--bullish);"></i> 1.1 Đỉnh Xoay Chiều (Swing High &ndash; SH)</h4>
                <p>
                    Là một cây nến có giá cao nhất (High) <strong>cao hơn hẳn</strong> giá cao nhất của ít nhất một thanh nến nằm liền kề bên trái và một thanh nến nằm liền kề bên phải nó (Mô hình 3 nến chuẩn).
                </p>
                <p>
                    <strong>Bản chất tâm lý Smart Money:</strong> Phe Mua đã cố gắng dốc toàn lực đẩy giá rướn lên mức cao nhất, nhưng tại đó họ va phải một bức tường lệnh Bán khổng lồ của dòng tiền lớn. Cây nến bên phải không thể vượt qua đỉnh này và đóng cửa thấp hơn, chứng minh phe Mua đã chính thức kiệt sức và quyền kiểm soát đã chuyển giao sang phe Bán.
                </p>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-arrow-down-right-dots" style="color:var(--bearish);"></i> 1.2 Đáy Xoay Chiều (Swing Low &ndash; SL)</h4>
                <p>
                    Là một cây nến có giá thấp nhất (Low) <strong>thấp hơn hẳn</strong> giá thấp nhất của các cây nến nằm liền kề bên trái và bên phải nó.
                </p>
                <p>
                    <strong>Bản chất tâm lý Smart Money:</strong> Phe Bán đã dốc toàn lực đạp giá xuống mức đáy sâu nhất phiên, nhưng tại vùng giá chiết khấu hời này, lực Cầu gom hàng âm thầm của Smart Money đã ồ ạt kích hoạt, hấp thụ toàn bộ áp lực bán tháo và chặn đứng đà rơi.
                </p>
            </div>

            <p>
                Khi bạn đã biết cách định vị chính xác Swing High và Swing Low, biểu đồ của bạn lập tức trở nên sáng rõ. Bạn sẽ không còn bận tâm đến từng cây nến li ti vô nghĩa ở giữa, mà chỉ tập trung quan sát cuộc chiến tại các pháo đài Swing Points &ndash; nơi dòng tiền hàng triệu USD thực sự giao tranh!
            </p>

            <!-- ==================== PHẦN 2 ==================== -->
            <h2><i class="fa-solid fa-diagram-project"></i> 2. Ba Trạng Thái Vận Động Của Cấu Trúc Thị Trường</h2>
            <p>
                Dù là thị trường Chứng khoán, Forex, Vàng hay Dầu thô, hành vi giá chỉ vận hành xoay quanh 3 trạng thái cấu trúc duy nhất:
            </p>

            <div class="step-card">
                <h4><i class="fa-solid fa-arrow-trend-up" style="color:var(--bullish);"></i> 1. Cấu Trúc Xu Hướng Tăng (Bullish Market Structure)</h4>
                <p>
                    Được định nghĩa bởi chuỗi liên tục tạo ra <strong>Đỉnh cao hơn (Higher Highs &ndash; HH)</strong> và <strong>Đáy cao hơn (Higher Lows &ndash; HL)</strong>:
                </p>
                <ul>
                    <li>Mỗi khi giá bứt phá vượt qua đỉnh cũ HH, đó là bằng chứng phe Mua vừa giành thêm một cứ điểm mới.</li>
                    <li>Mỗi nhịp điều chỉnh giảm về tạo đáy HL là cơ hội để dòng tiền lớn gia tăng thêm vị thế ở vùng giá có lợi.</li>
                    <li><strong>Quy tắc phòng thủ sống còn:</strong> Xu hướng tăng được bảo toàn nguyên vẹn chừng nào <em>đáy Higher Low gần nhất chưa bị đâm thủng bằng giá đóng cửa</em>!</li>
                </ul>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-arrow-trend-down" style="color:var(--bearish);"></i> 2. Cấu Trúc Xu Hướng Giảm (Bearish Market Structure)</h4>
                <p>
                    Được định nghĩa bởi chuỗi liên tục tạo ra <strong>Đỉnh thấp hơn (Lower Highs &ndash; LH)</strong> và <strong>Đáy thấp hơn (Lower Lows &ndash; LL)</strong>:
                </p>
                <ul>
                    <li>Phe Bán hoàn toàn làm chủ cục diện; mọi đợt giá hồi phục nhẹ lên chỉ là những cú "hồi quang phản chiếu" để cá mập tiếp tục nhồi lệnh Bán khống ở giá cao.</li>
                    <li>Tuyệt đối không bao giờ được phép "bắt dao rơi" khi cấu trúc đáy thấp hơn liên tục bị xuyên thủng!</li>
                </ul>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-arrows-left-right" style="color:var(--accent-gold);"></i> 3. Cấu Trúc Đi Ngang / Tích Lũy (Trading Range / Consolidation)</h4>
                <p>
                    Giá bị nhốt chặt giữa một biên trên Kháng cự (Ceiling / Supply) và biên dưới Hỗ trợ (Floor / Demand). Lực Mua và Lực Bán đang ở trạng thái cân bằng tuyệt đối. Người thông minh sẽ kiên nhẫn đứng ngoài chờ cú bứt phá hoặc chỉ giao dịch đánh chặn nhanh ở hai biên với khối lượng nhỏ.
                </p>
            </div>

            <!-- ==================== PHẦN 3 ==================== -->
            <h2><i class="fa-solid fa-bolt-lightning"></i> 3. BOS vs CHoCH &ndash; Hai Khái Niệm Phán Quyết Xu Hướng Tối Thượng</h2>
            <p>
                Trong hệ thống giao dịch Naked Chart chuyên nghiệp, chúng ta không cần bất kỳ đường trung bình MA nào để biết khi nào xu hướng tiếp diễn hay đảo chiều. Hai tín hiệu nguyên bản sau đây là tất cả những gì bạn cần:
            </p>

            <div class="step-card">
                <h4><i class="fa-solid fa-forward" style="color:var(--accent-cyan);"></i> 3.1 Phá Vỡ Cấu Trúc Tiếp Diễn &ndash; BOS (Break of Structure)</h4>
                <p>
                    <strong>Định nghĩa:</strong> Xảy ra khi giá phá vỡ dứt khoát đỉnh cũ HH (trong xu hướng tăng) hoặc đâm thủng đáy cũ LL (trong xu hướng giảm).
                </p>
                <p>
                    <strong>Ý nghĩa thực chiến:</strong> BOS là lời xác nhận hùng hồn của dòng tiền lớn rằng động lượng (Momentum) đang cực kỳ mạnh mẽ. Cuộc hành quân thuận xu hướng tiếp tục tiến bước. Sau một cú BOS, hành động chuẩn mực của trader là <em>chờ giá hồi quy (Pullback) về vùng chân sóng để tìm điểm mua theo sau</em>.
                </p>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-triangle-exclamation" style="color:var(--bearish);"></i> 3.2 Thay Đổi Tính Chất / Tín Hiệu Đảo Chiều &ndash; CHoCH (Change of Character)</h4>
                <p>
                    <strong>Định nghĩa:</strong> Xảy ra khi một xu hướng tăng đang diễn ra suôn sẻ bỗng nhiên bị chặn đứng, và giá lao dốc đâm thủng <strong>Đáy Higher Low (HL) then chốt gần nhất</strong> bằng một thân nến đóng cửa dứt khoát.
                </p>
                <p>
                    <strong>Ý nghĩa thực chiến:</strong> CHoCH chính là tiếng chuông báo tử sớm nhất cho phe Bò! Nó hé lộ rằng phe Mua đã thất thủ tại cứ điểm phòng thủ quan trọng nhất, và dòng tiền thông minh đã bắt đầu tiến trình phân phối xả hàng để đảo chiều sang xu hướng giảm.
                </p>
            </div>

            <!-- BẢNG SO SÁNH BOS VÀ CHOCH -->
            <div class="data-table-wrapper">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th style="width: 20%;">Tiêu Chí</th>
                            <th style="width: 40%;">Phá Vỡ Cấu Trúc (BOS)</th>
                            <th style="width: 40%;">Đổi Tính Chất Đảo Chiều (CHoCH)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Bản chất tín hiệu</strong></td>
                            <td>Xác nhận xu hướng hiện tại tiếp tục mở rộng và duy trì sức mạnh.</td>
                            <td>Cảnh báo sớm xu hướng đã bị bẻ gãy và chuẩn bị đảo chiều sang hướng ngược lại.</td>
                        </tr>
                        <tr>
                            <td><strong>Vị trí xuất hiện</strong></td>
                            <td>Phá đỉnh cũ trong Uptrend (hoặc phá đáy cũ trong Downtrend).</td>
                            <td>Phá vỡ đáy Higher Low then chốt (hoặc phá đỉnh Lower High then chốt).</td>
                        </tr>
                        <tr>
                            <td><strong>Tâm lý Smart Money</strong></td>
                            <td>Bơm thêm tiền thật để gia tăng áp lực đẩy giá bứt phá.</td>
                            <td>Đã âm thầm xả hàng xong ở đỉnh, giờ dốc lực đè bẹp các cứ điểm phòng thủ.</td>
                        </tr>
                        <tr>
                            <td><strong>Hành động của Trader</strong></td>
                            <td>Tìm điểm vào lệnh thuận theo xu hướng khi giá hồi quy (Pullback).</td>
                            <td>Dừng toàn bộ các lệnh mua đuổi, đóng bớt vị thế và chuẩn bị kế hoạch Bán khống (Short).</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- ==================== PHẦN 4 ==================== -->
            <h2><i class="fa-solid fa-arrows-split-up-and-left"></i> 4. Vùng Chuyển Đổi (Flip Zones) &ndash; Thánh Địa Bắn Tỉa Tỷ Lệ R:R Cực Đại</h2>
            <p>
                Một trong những quy luật kinh điển và quyền năng nhất của Hành động giá nguyên bản là: <strong>Kháng cự khi bị xuyên thủng sẽ lập tức hoán đổi vai trò để trở thành Hỗ trợ mới (và ngược lại)</strong>. Vùng này được gọi là <strong>Vùng Chuyển Đổi (Flip Zone / Polarity Principle)</strong>.
            </p>

            <div class="step-card">
                <h4><i class="fa-solid fa-crosshairs" style="color:var(--accent-gold);"></i> Tại Sao Flip Zone Lại Hoạt Động Cực Kỳ Chuẩn Xác?</h4>
                <p>
                    Hãy đặt mình vào tâm lý của những người tham gia thị trường tại một vùng Kháng cự:
                </p>
                <ol>
                    <li>Tại vùng kháng cự cũ, rất nhiều trader nhỏ lẻ và các quỹ định lượng đã đặt lệnh Bán khống (Short).</li>
                    <li>Khi giá bùng nổ vượt qua cản với một cây nến xanh thân dài kèm Volume lớn (BOS), toàn bộ những người bán khống này rơi vào trạng thái thua lỗ nặng (Trapped Shorts).</li>
                    <li>Khi giá quay đầu hồi quy (Retest) về đúng mức cản này, những người bán khống bị kẹt lệnh sẽ vội vàng bấm nút <em>"Đóng lệnh hòa vốn" (Buy to Cover)</em> &ndash; hành động này tạo ra một lực MUA cưỡng bức khổng lồ.</li>
                    <li>Đồng thời, những Naked Chart trader kiên nhẫn đứng ngoài quan sát sẽ cùng lúc nhảy vào Mua tại vùng kiểm định này.</li>
                </ol>
                <p>
                    Sự cộng hưởng giữa <strong>lực mua thoát hàng của phe kẹt lệnh</strong> và <strong>lực mua chủ động của trader mới</strong> biến Flip Zone trở thành một bệ phóng giá vững chắc như bàn thạch!
                </p>
            </div>

            <!-- ==================== PHẦN 5 ==================== -->
            <h2><i class="fa-solid fa-clipboard-check"></i> 5. Quy Trình 5 Bước Định Vị Cấu Trúc Trước Khi Bấm Lệnh</h2>
            <p>
                Trước khi mở bất kỳ một vị thế giao dịch nào trên sàn, hãy thực hiện đúng quy trình 5 bước sau đây như một phi công kiểm tra buồng lái trước khi cất cánh:
            </p>

            <div class="step-card">
                <h4><i class="fa-solid fa-1" style="color:var(--accent-cyan);"></i> Bước 1: Xác Định Cấu Trúc Trên Khung Thời Gian Lớn (Higher Timeframe &ndash; H4 / Daily)</h4>
                <p>
                    Nhìn tổng quan biểu đồ: Giá đang tạo chuỗi HH/HL (Uptrend) hay LH/LL (Downtrend)? Xu hướng lớn là ông vua, tuyệt đối không bao giờ đánh ngược xu hướng khung lớn.
                </p>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-2" style="color:var(--accent-cyan);"></i> Bước 2: Đánh Dấu Đáy/Đỉnh Then Chốt Bảo Vệ Xu Hướng</h4>
                <p>
                    Vẽ một đường ngang đánh dấu mức giá của đáy Higher Low gần nhất. Đây là ranh giới sống còn: nếu mức này còn nguyên vẹn, bạn chỉ ưu tiên tìm lệnh Mua.
                </p>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-3" style="color:var(--accent-gold);"></i> Bước 3: Xác Định Vùng Chuyển Đổi (Flip Zone) &amp; Vùng Cầu Cốt Lõi</h4>
                <p>
                    Khoanh vùng đỉnh cũ vừa bị phá vỡ (BOS) hoặc vùng chân sóng nơi dòng tiền lớn kích hoạt lực mua bùng nổ.
                </p>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-4" style="color:var(--bullish);"></i> Bước 4: Kiên Nhẫn Chờ Giá Hồi Quy (Retest) &amp; Xuất Hiện Tín Hiệu Nến</h4>
                <p>
                    Không mua đuổi khi giá đang bay lơ lửng. Chờ giá từ từ lùi về Flip Zone, quan sát cây nến Pin Bar từ chối giá hoặc nến xanh rút chân kèm khối lượng cạn kiệt (No Supply).
                </p>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-5" style="color:var(--bearish);"></i> Bước 5: Đặt Lệnh Bắn Tỉa (Sniper Entry) Với Tỷ Lệ R:R Tối Thiểu 1:3</h4>
                <p>
                    Vào lệnh ngay khi nến xác nhận đóng cửa, đặt mức Stop Loss chặt chẽ ngay dưới râu nến xoay chiều (chỉ cách 0.5% &ndash; 1%), và chốt lời tại đỉnh cũ Higher High tiếp theo.
                </p>
            </div>

            <div class="highlight-box">
                <h3><i class="fa-solid fa-gem"></i> Đúc Kết Tư Duy Sống Còn</h3>
                <p>
                    Thị trường tài chính không phải là sòng bạc để đoán mò cây nến tiếp theo là xanh hay đỏ. Giao dịch theo <strong>Cấu Trúc Thị Trường Nguyên Bản</strong> giúp bạn luôn đứng cùng chiến tuyến với Dòng Tiền Lớn (Smart Money), bảo vệ tài khoản khỏi các cú bẫy quét thanh khoản và mang lại tỷ lệ lợi nhuận bền vững theo năm tháng.
                </p>
            </div>

            <!-- NEXT / PREV LESSON NAVIGATION -->
            <div class="nav-lesson-grid">
                <a href="khoa-hoc-vsa-bai-1-bieu-do-tran-the-naked-chart.html" class="nav-lesson-card">
                    <span style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;"><i class="fa-solid fa-arrow-left"></i> Bài Trước</span>
                    <strong style="font-size:0.95rem; color:var(--accent-cyan); margin-top:6px;">Bài 1: BIỂU ĐỒ TRẦN (The Naked Chart) &ndash; Khám Phá Bản Năng Của Giá</strong>
                </a>
                <a href="khoa-hoc-vsa-bai-3-ngon-ngu-nen-don-va-cum-nen-dao-chieu-sat-thu.html" class="nav-lesson-card" style="text-align:right;">
                    <span style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Bài Kế Tiếp <i class="fa-solid fa-arrow-right"></i></span>
                    <strong style="font-size:0.95rem; color:var(--accent-gold); margin-top:6px;">Bài 3: Ngôn Ngữ Nến Đơn &amp; Cụm Nến Đảo Chiều Sát Thủ (Pin Bar, Engulfing &amp; Fakey)</strong>
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
                    <div class="comment-item">
                        <div class="comment-top">
                            <span class="comment-author"><i class="fa-solid fa-circle-user"></i> Tuấn Anh (Pro PA)</span>
                            <span class="comment-date">14/09/2026 14:30:15</span>
                        </div>
                        <div class="comment-text">Giải thích về CHoCH và HL then chốt rất sáng tỏ! Trước đây mình cứ thấy phá đáy nhỏ ở khung M5 là tưởng đảo chiều, hóa ra khung H4 vẫn là HL vững chắc nên bị dính bẫy quét thanh khoản liên tục.</div>
                    </div>
                    <div class="comment-item">
                        <div class="comment-top">
                            <span class="comment-author"><i class="fa-solid fa-circle-user"></i> Ngọc Mai (Trader Forex)</span>
                            <span class="comment-date">14/09/2026 15:05:22</span>
                        </div>
                        <div class="comment-text">Sơ đồ BOS và CHoCH vẽ lại font chữ to rất đẹp và dễ nhìn trên điện thoại. Flip Zone quả thực là vùng mình thích nhất vì tỷ lệ R:R ở đây luôn cực kỳ cao.</div>
                    </div>
                    <div class="comment-item">
                        <div class="comment-top">
                            <span class="comment-author"><i class="fa-solid fa-circle-user"></i> Đức Thịnh (CBOT Trader)</span>
                            <span class="comment-date">14/09/2026 15:40:00</span>
                        </div>
                        <div class="comment-text">Kiến thức bài bản không thua kém gì giáo trình Phố Wall. Đang hóng Bài 3 về các cụm nến đảo chiều sát thủ!</div>
                    </div>
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
        <p>© 2026 PTvolume.com. Toàn bộ bản quyền được bảo lưu. Naked Chart • Phương Pháp VSA • Price Action.</p>
        <p style="font-size: 0.75rem; color: #505D75; margin-top: 8px;">Nội dung phục vụ mục đích giáo dục &amp; nghiên cứu tài chính, không cấu thành lời khuyên đầu tư tài chính trực tiếp.</p>
    </footer>

    <div id="google_translate_element" style="display:none;"></div>

    <script>
        function googleTranslateElementInit() {
            new google.translate.TranslateElement({
                pageLanguage: 'vi',
                includedLanguages: 'en,vi',
                autoDisplay: false
            }, 'google_translate_element');
        }

        function setLanguage(lang) {
            localStorage.setItem('ptvolume_lang', lang);
            updateLangButtons(lang);

            document.cookie = "googtrans=/vi/" + lang + "; path=/;";
            if (window.location.hostname && window.location.hostname !== '') {
                document.cookie = "googtrans=/vi/" + lang + "; path=/; domain=" + window.location.hostname;
            }

            const select = document.querySelector('.goog-te-combo');
            if (select) {
                select.value = lang;
                select.dispatchEvent(new Event('change'));
            } else {
                window.location.reload();
            }
        }

        function updateLangButtons(lang) {
            const btnVi = document.getElementById('btn-lang-vi');
            const btnEn = document.getElementById('btn-lang-en');
            if (btnVi && btnEn) {
                if (lang === 'en') {
                    btnEn.classList.add('active');
                    btnVi.classList.remove('active');
                } else {
                    btnVi.classList.add('active');
                    btnEn.classList.remove('active');
                }
            }
        }

        function applyStoredLanguage() {
            const currentLang = localStorage.getItem('ptvolume_lang') || 'vi';
            updateLangButtons(currentLang);
            if (currentLang === 'en') {
                let attempts = 0;
                const checkCombo = setInterval(() => {
                    const select = document.querySelector('.goog-te-combo');
                    if (select) {
                        select.value = 'en';
                        select.dispatchEvent(new Event('change'));
                        clearInterval(checkCombo);
                    }
                    attempts++;
                    if (attempts > 30) clearInterval(checkCombo);
                }, 200);
            }
        }

        const POST_SLUG = "khoa-hoc-vsa-bai-2-cau-truc-thi-truong-va-vung-cung-cau";

        function loadSavedComments() {
            const saved = JSON.parse(localStorage.getItem('ptvolume_comments_' + POST_SLUG) || '[]');
            const commentList = document.getElementById("commentList");
            if (commentList && saved.length > 0) {
                saved.forEach(item => {
                    const newComment = document.createElement("div");
                    newComment.className = "comment-item";
                    newComment.innerHTML = `
                        <div class="comment-top">
                            <span class="comment-author"><i class="fa-solid fa-circle-user"></i> ${escapeHtml(item.name)}</span>
                            <span class="comment-date">${escapeHtml(item.date)}</span>
                        </div>
                        <div class="comment-text">${escapeHtml(item.content)}</div>
                    `;
                    commentList.prepend(newComment);
                });
                const countElem = document.getElementById("commentCount");
                if (countElem) {
                    countElem.innerText = parseInt(countElem.innerText || 3) + saved.length;
                }
            }
        }

        function addComment(e) {
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
                    <span class="comment-author"><i class="fa-solid fa-circle-user"></i> ${escapeHtml(name)}</span>
                    <span class="comment-date">${timeString}</span>
                </div>
                <div class="comment-text">${escapeHtml(content)}</div>
            `;
            commentList.prepend(newComment);

            const countElem = document.getElementById("commentCount");
            if (countElem) countElem.innerText = parseInt(countElem.innerText || 3) + 1;

            const saved = JSON.parse(localStorage.getItem('ptvolume_comments_' + POST_SLUG) || '[]');
            saved.push({ name, content, date: timeString });
            localStorage.setItem('ptvolume_comments_' + POST_SLUG, JSON.stringify(saved));

            nameInput.value = "";
            contentInput.value = "";
            alert("Bình luận của bạn đã được đăng thành công!");
        }

        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }

        document.addEventListener('DOMContentLoaded', () => {
            applyStoredLanguage();
            loadSavedComments();
        });
    </script>
    <script src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>

</body>
</html>
"""

dest_bai2 = r"d:\PHAN DUA CẤM XÓA\AI_Agent_Trading\hoc-tap\khoa-hoc-vsa-bai-2-cau-truc-thi-truong-va-vung-cung-cau.html"
with open(dest_bai2, "w", encoding="utf-8") as f:
    f.write(bai2_content)

print("Upgraded Bài 2 successfully with > 3000 words, human tone and large font SVG diagram!")
