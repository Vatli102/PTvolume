import os
import sys
import re
import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

# Reconfigure stdout for UTF-8 in Windows console
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

# Load .env
ENV_PATHS = [
    os.path.join(os.path.dirname(__file__), ".env"),
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env")),
]
for ep in ENV_PATHS:
    if os.path.exists(ep):
        load_dotenv(ep, override=True)

from google import genai
from google.genai import types

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
POSTS_DIR = os.path.join(BASE_DIR, "posts")
INDEX_HTML = os.path.join(BASE_DIR, "index.html")
POSTS_INDEX_JSON = os.path.join(POSTS_DIR, "posts.json")

os.makedirs(POSTS_DIR, exist_ok=True)

try:
    from sitemap_generator import generate_sitemap
except ImportError:
    try:
        from ai_agent.sitemap_generator import generate_sitemap
    except ImportError:
        generate_sitemap = None

RSS_FEEDS = [
    {
        "name": "Reuters / Bloomberg / Financial Press",
        "url": "https://news.google.com/rss/search?q=(Reuters+OR+Bloomberg+OR+%22Wall+Street+Journal%22+OR+%22Financial+Times%22)+AND+(Forex+OR+Gold+OR+Fed+OR+Dollar+OR+Inflation+OR+Markets)&hl=en-US&gl=US&ceid=US:en"
    },
    {
        "name": "CNBC Markets",
        "url": "https://www.cnbc.com/id/10000664/device/rss/rss.html"
    },
    {
        "name": "Yahoo Finance Markets",
        "url": "https://finance.yahoo.com/news/rssindex"
    },
    {
        "name": "BBC Business & Global Economy",
        "url": "https://feeds.bbci.co.uk/news/business/rss.xml"
    }
]

def fetch_rss_items(url: str, source_name: str, max_items: int = 15) -> List[Dict[str, str]]:
    items = []
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
        with urllib.request.urlopen(req, timeout=12) as response:
            content = response.read()
            root = ET.fromstring(content)
            
            for elem in root.findall(".//item"):
                title_elem = elem.find("title")
                link_elem = elem.find("link")
                pubdate_elem = elem.find("pubDate")
                desc_elem = elem.find("description")
                
                title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""
                link = link_elem.text.strip() if link_elem is not None and link_elem.text else ""
                pubdate = pubdate_elem.text.strip() if pubdate_elem is not None and pubdate_elem.text else ""
                desc = desc_elem.text.strip() if desc_elem is not None and desc_elem.text else ""
                
                desc = re.sub(r'<[^>]+>', ' ', desc)
                desc = re.sub(r'\s+', ' ', desc).strip()
                
                if title and len(title) > 15:
                    items.append({
                        "source": source_name,
                        "title": title,
                        "link": link,
                        "pubDate": pubdate,
                        "summary": desc[:300]
                    })
                if len(items) >= max_items:
                    break
    except Exception as e:
        print(f"  [!] Failed fetching RSS from '{source_name}': {e}")
    return items

def gather_top_market_news() -> List[Dict[str, str]]:
    print("[*] Aggregating live financial news from global institutional sources...")
    all_news = []
    seen_titles = set()
    
    for feed in RSS_FEEDS:
        items = fetch_rss_items(feed["url"], feed["name"])
        for item in items:
            norm_title = re.sub(r'[^a-zA-Z0-9]', '', item["title"].lower())[:40]
            if norm_title not in seen_titles:
                seen_titles.add(norm_title)
                all_news.append(item)
                
    print(f"[+] Successfully retrieved {len(all_news)} unique global market headlines.")
    return all_news[:25]

def get_gemini_client():
    for ep in ENV_PATHS:
        if os.path.exists(ep):
            load_dotenv(ep, override=True)
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not key or key.startswith("AIzaSy..."):
        return None
    try:
        return genai.Client(api_key=key)
    except Exception as e:
        print(f"[!] Failed to initialize Gemini Client: {e}")
        return None

def generate_article_payload(news_items: List[Dict[str, str]]) -> Optional[Dict[str, Any]]:
    client = get_gemini_client()
    if not client:
        print("[!] Error: GEMINI_API_KEY is not set or invalid.")
        return None
        
    news_text = ""
    for idx, item in enumerate(news_items, 1):
        news_text += f"{idx}. [{item['source']}] {item['title']}\n   Summary: {item['summary']}\n   Date: {item['pubDate']}\n\n"
        
    prompt = f"""
Bạn là Trưởng ban Chiến lược Vĩ mô & Phân tích Dòng tiền Thể chế tại PTvolume.com.
Hãy tổng hợp tin tức tài chính quốc tế mới nhất dưới đây thành một bài phân tích thị trường chuyên sâu hàng ngày bằng TIẾNG VIỆT dành cho cộng đồng nhà giao dịch độc lập.

QUY TẮC BẮT BUỘC:
1. NGÔN NGỮ: Tiếng Việt chuẩn mực, văn phong tài chính vĩ mô chuyên nghiệp phong cách Investopedia/Bloomberg.
   - Giữ nguyên các thuật ngữ giao dịch quốc tế không dịch thô: Price Action, Wyckoff, VSA, Order Flow, Supply & Demand, Smart Money, Entry, Stop Loss, Take Profit, Risk-to-Reward (R:R), Fair Value Gap (FVG), Upthrust, Spring, No Demand/No Supply.
2. PHƯƠNG PHÁP: Naked Chart Price Action, Volume Spread Analysis (VSA), Chu kỳ Tích lũy/Phân phối Wyckoff và Dòng tiền lớn (Smart Money). Tuyệt đối không dùng chỉ báo trễ (RSI/MACD).
3. ĐỊNH DẠNG ĐẦU RA: Trả về DUY NHẤT một chuỗi JSON hợp lệ, KHÔNG bọc trong markdown code fence.

JSON SCHEMA:
{{
  "title": "Tiêu đề bài viết hấp dẫn, chuẩn phong cách thể chế (tối đa 90 ký tự)",
  "slug": "slug-tieng-anh-viet-thuong-khong-dau-ngan-cach-bang-dau-gach-ngang",
  "meta_description": "Mô tả SEO 1-2 câu tóm tắt trọng tâm kinh tế vĩ mô và dòng tiền kỹ thuật.",
  "category": "Bản Tin Thị Trường Hàng Ngày",
  "badge": "Dòng Tiền Vĩ Mô & Khối Lượng Thể Chế",
  "read_time": "6 phút đọc",
  "lead_excerpt": "Đoạn tóm tắt mở đầu súc tích (2-3 câu) về động lực vĩ mô chi phối và hàm ý giao dịch hôm nay.",
  "html_body": "Nội dung HTML đầy đủ của bài viết (dùng <h2>, <h3>, <p>, <ul>, <li>, <strong>, <em>, <div class=\\"highlight-box\\">). KHÔNG chứa thẻ <h1> tiêu đề chính hay thẻ <html>/<body> ngoài.",
  "initial_comments": [
    {{
      "name": "Tên trader và vai trò chuyên môn (VD: Hoàng Nam - London FX Flow / Minh Trí - VSA Trader)",
      "date": "Thời gian (VD: Hôm nay, 08:15 UTC)",
      "text": "Bình luận thảo luận chuyên sâu, phản biện hoặc xác nhận một mức giá, pha Wyckoff hoặc dữ liệu cụ thể trong bài viết NÀY."
    }},
    {{
      "name": "Tên trader thứ hai và vai trò (VD: Kenji Takahashi - Macro Desk)",
      "date": "Thời gian (VD: Hôm nay, 09:30 UTC)",
      "text": "Câu hỏi hoặc góc nhìn kỹ thuật về quản trị rủi ro và điểm vào lệnh của bài viết."
    }}
  ]
}}

CẤU TRÚC NỘI DUNG 'html_body':
1. Nhịp Đập Thị Trường & 3 Động Lực Cốt Lõi.
2. Diễn Biến Ngân Hàng Trung Ương & Xúc Tác Vĩ Mô (Fed, ECB, BOJ, Lợi suất trái phiếu, Lạm phát).
3. Ma Trận Tác Động Đa Tài Sản (Forex, Vàng Spot XAU/USD, Dầu thô, Chỉ số chứng khoán Mỹ).
4. Phân Tích Dòng Lệnh & Volume Spread Analysis (Dấu chân Smart Money, Nỗ lực vs Kết quả, bẫy giá Upthrust/Spring).
5. Kế Hoạch Vào Lệnh Thực Chiến & Mức Giá Then Chốt.
6. Khung Highlight tham số vào lệnh:
<div class="highlight-box">
  <h3><i class="fa-solid fa-crosshairs"></i> Thông Số Vào Lệnh Thực Chiến</h3>
  <ul>
    <li><i class="fa-solid fa-check"></i> <strong>Thiên hướng vĩ mô:</strong> ...</li>
    <li><i class="fa-solid fa-check"></i> <strong>Vùng giá kích hoạt:</strong> ...</li>
    <li><i class="fa-solid fa-check"></i> <strong>Điểm cắt lỗ (SL):</strong> ...</li>
    <li><i class="fa-solid fa-check"></i> <strong>Mục tiêu chốt lời (TP):</strong> Tỷ lệ R:R tối thiểu 1:2.5</li>
  </ul>
</div>
7. Kỷ Luật Vốn & Nguyên Tắc Quản Trị Rủi Ro.

TIN TỨC THỜI SỰ QUỐC TẾ THU THẬP ĐƯỢC:
{news_text}
"""

    models_to_try = ["gemini-3.6-flash", "gemini-flash-latest", "gemini-2.5-flash", "gemini-2.5-pro"]
    
    for model_name in models_to_try:
        try:
            print(f"[*] Requesting market synthesis from Gemini model: '{model_name}'...")
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.35,
                    response_mime_type="application/json"
                )
            )
            raw_text = response.text.strip()
            if raw_text.startswith("```"):
                raw_text = re.sub(r'^```json\s*', '', raw_text)
                raw_text = re.sub(r'^```\s*', '', raw_text)
                raw_text = re.sub(r'\s*```$', '', raw_text)
            
            data = json.loads(raw_text)
            return data
        except Exception as e:
            print(f"  [!] Model '{model_name}' encountered an error: {e}")
            
    return None

HTML_TEMPLATE = """<!DOCTYPE html>
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
    <title>__TITLE__ | PTvolume</title>
    <meta name="description" content="__META_DESC__">
    <link rel="icon" type="image/jpeg" href="../assets/images/logo.jpg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Merriweather:ital,wght@0,400;0,700;1,400&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
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

        input, textarea {
            -webkit-user-select: text !important;
            -moz-user-select: text !important;
            -ms-user-select: text !important;
            user-select: text !important;
        }

        body {
            background-color: var(--bg-main);
            color: var(--text-main);
            line-height: 1.8;
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
            color: #00E5FF;
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
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            border: none;
            background: var(--primary);
            color: #fff;
            transition: all 0.2s ease;
        }

        .btn:hover {
            background: #1e4bd8;
            transform: translateY(-1px);
        }

        .article-container {
            max-width: 860px;
            margin: 50px auto 60px;
            padding: 0 24px;
        }

        .breadcrumb {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 24px;
        }

        .breadcrumb a:hover {
            color: #00E5FF;
        }

        .article-badge {
            display: inline-block;
            padding: 4px 14px;
            border-radius: 20px;
            background: rgba(240, 185, 11, 0.15);
            border: 1px solid rgba(240, 185, 11, 0.3);
            color: var(--accent-gold);
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 16px;
        }

        h1.article-title {
            font-family: var(--font-editorial);
            font-size: 2.35rem;
            font-weight: 700;
            line-height: 1.35;
            margin-bottom: 20px;
            color: #fff;
            letter-spacing: -0.5px;
        }

        .article-meta {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
            padding-bottom: 24px;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 36px;
            font-size: 0.88rem;
            color: var(--text-muted);
        }

        .article-body {
            font-size: 1.08rem;
            color: var(--text-light);
        }

        .article-body h2 {
            font-family: var(--font-editorial);
            font-size: 1.5rem;
            font-weight: 700;
            color: #fff;
            margin: 40px 0 16px;
            padding-left: 14px;
            border-left: 4px solid var(--primary);
        }

        .article-body h3 {
            font-size: 1.2rem;
            font-weight: 600;
            color: #00E5FF;
            margin: 28px 0 12px;
        }

        .article-body p {
            margin-bottom: 20px;
        }

        .article-body ul, .article-body ol {
            margin: 16px 0 24px 24px;
        }

        .article-body li {
            margin-bottom: 10px;
        }

        .watermark-box {
            position: relative;
            margin: 32px 0;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            background: #080B10;
        }

        .watermark-box img {
            width: 100%;
            display: block;
            object-fit: cover;
        }

        .watermark-stamp {
            position: absolute;
            bottom: 14px;
            right: 14px;
            background: rgba(11, 14, 20, 0.85);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: rgba(255, 255, 255, 0.75);
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            pointer-events: none;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .highlight-box {
            background: rgba(41, 98, 255, 0.08);
            border: 1px solid rgba(41, 98, 255, 0.3);
            border-radius: 10px;
            padding: 24px;
            margin: 32px 0;
        }

        .highlight-box h3 {
            color: #fff;
            margin-top: 0;
            margin-bottom: 14px;
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.15rem;
        }

        .highlight-box ul {
            margin: 0;
            padding-left: 0;
            list-style: none;
        }

        .highlight-box li {
            margin-bottom: 10px;
            display: flex;
            align-items: flex-start;
            gap: 10px;
        }

        .highlight-box li i {
            color: var(--bullish);
            margin-top: 5px;
        }

        /* Comments Section */
        .comment-section {
            margin-top: 60px;
            padding-top: 40px;
            border-top: 1px solid var(--border-color);
        }

        .comment-header {
            font-size: 1.35rem;
            font-weight: 700;
            color: #fff;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .comment-form {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 36px;
        }

        .form-group {
            margin-bottom: 16px;
        }

        .form-label {
            display: block;
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 6px;
            font-weight: 500;
        }

        .form-control {
            width: 100%;
            background: var(--bg-main);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 12px 16px;
            color: var(--text-main);
            font-size: 0.95rem;
            outline: none;
            transition: border-color 0.2s ease;
        }

        .form-control:focus {
            border-color: var(--primary);
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
            border-radius: 10px;
            padding: 18px 20px;
        }

        .comment-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 8px;
        }

        .comment-author {
            font-weight: 600;
            color: #00E5FF;
            font-size: 0.92rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .comment-date {
            font-size: 0.78rem;
            color: var(--text-muted);
        }

        .comment-text {
            font-size: 0.95rem;
            color: var(--text-light);
            line-height: 1.6;
        }

        footer {
            background: #080B10;
            border-top: 1px solid var(--border-color);
            padding: 40px 24px;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.88rem;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }

        .footer-links a:hover {
            color: #00E5FF;
        }

        /* Hide Google Translate Toolbars & Overlays */
        .goog-te-banner-frame.skiptranslate { display: none !important; }
        body { top: 0px !important; }
        .goog-tooltip, .goog-tooltip:hover { display: none !important; }
        .goog-text-highlight { background-color: transparent !important; border: none !important; box-shadow: none !important; }
        #goog-gt-tt, .goog-te-balloon-frame { display: none !important; }
        .goog-te-gadget { display: none !important; }
    </style>
</head>
<body>

    <header>
        <div class="nav-container">
            <a href="../index.html" class="logo">
                <img src="../assets/images/logo.jpg" alt="PTvolume Logo">
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
            <a href="../index.html#market-analysis">Phân Tích Thị Trường</a>
            <i class="fa-solid fa-chevron-right" style="font-size: 0.7rem;"></i>
            <span>Bản Tin Dòng Tiền</span>
        </div>

        <span class="article-badge"><i class="fa-solid fa-globe"></i> __BADGE__</span>
        
        <h1 class="article-title">__TITLE__</h1>

        <div class="article-meta">
            <span><i class="fa-regular fa-user"></i> Biên soạn: <strong>Nhóm Phân Tích Thể Chế PTvolume</strong></span>
            <span>•</span>
            <span><i class="fa-regular fa-calendar"></i> __DATE_STR__</span>
            <span>•</span>
            <span><i class="fa-regular fa-clock"></i> __READ_TIME__</span>
        </div>

        <div class="article-body">
            <div class="watermark-box">
                <img src="../assets/images/logo.jpg" alt="PTvolume Institutional Market Intelligence" style="max-height: 380px; object-fit: cover;">
                <div class="watermark-stamp">
                    <i class="fa-solid fa-shield-halved"></i> PTvolume.com
                </div>
            </div>

            __HTML_BODY__
        </div>

        <section class="comment-section">
            <h3 class="comment-header">
                <i class="fa-regular fa-comments" style="color: #00E5FF;"></i> Thảo Luận Kỹ Thuật Cộng Đồng (<span id="commentCount">__COMMENT_COUNT__</span>)
            </h3>

            <form class="comment-form" id="commentForm" onsubmit="addComment(event)">
                <div class="form-group">
                    <label class="form-label">Tên Trader / Nickname:</label>
                    <input type="text" id="commentName" class="form-control" placeholder="VD: Hoàng Nam - FX Flow Trader" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Góc nhìn kỹ thuật hoặc phân tích dòng tiền của bạn:</label>
                    <textarea id="commentContent" class="form-control" placeholder="Chia sẻ quan sát của bạn về hành động giá và khối lượng hôm nay..." required></textarea>
                </div>
                <button type="submit" class="btn">
                    <i class="fa-regular fa-paper-plane"></i> Gửi Bình Luận
                </button>
            </form>

            <div class="comment-list" id="commentList">
__COMMENTS_HTML__
            </div>
        </section>
    </main>

    <footer>
        <div class="footer-links">
            <a href="../pages/about.html">Về PTvolume</a>
            <a href="../pages/contact.html">Liên Hệ</a>
            <a href="../pages/terms.html">Điều Khoản</a>
            <a href="../pages/privacy.html">Bảo Mật</a>
            <a href="../pages/disclaimer.html">Cảnh Báo Rủi Ro</a>
        </div>
        <p>© 2026 PTvolume.com. Toàn bộ bản quyền được bảo lưu. Naked Chart • VSA • Phương Pháp Wyckoff.</p>
    </footer>

    <!-- Hidden Google Translate Element -->
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
            if (lang === 'vi') {
                document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
                document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=" + location.hostname;
                document.cookie = "googtrans=/vi/vi; path=/;";
                document.cookie = "googtrans=/vi/vi; path=/; domain=" + location.hostname;
                localStorage.setItem('ptvolume_lang', 'vi');
                location.reload();
            } else if (lang === 'en') {
                document.cookie = "googtrans=/vi/en; path=/;";
                document.cookie = "googtrans=/vi/en; path=/; domain=" + location.hostname;
                localStorage.setItem('ptvolume_lang', 'en');
                location.reload();
            }
        }

        document.addEventListener('DOMContentLoaded', () => {
            const currentLang = localStorage.getItem('ptvolume_lang') || 'vi';
            const btnVi = document.getElementById('btn-lang-vi');
            const btnEn = document.getElementById('btn-lang-en');
            if (btnVi && btnEn) {
                if (currentLang === 'en') {
                    btnEn.classList.add('active');
                    btnVi.classList.remove('active');
                } else {
                    btnVi.classList.add('active');
                    btnEn.classList.remove('active');
                }
            }
        });

        function addComment(e) {
            e.preventDefault();
            const nameInput = document.getElementById("commentName");
            const contentInput = document.getElementById("commentContent");

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
            countElem.innerText = parseInt(countElem.innerText) + 1;

            nameInput.value = "";
            contentInput.value = "";

            alert("Bình luận của bạn đã được gửi thành công!");
        }

        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
    </script>
    <script src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>

</body>
</html>
"""

def build_post_html(data: Dict[str, Any], date_str: str) -> str:
    title = data.get("title", "Bản Tin Dòng Tiền Thị Trường Quốc Tế | PTvolume")
    meta_desc = data.get("meta_description", "Phân tích kinh tế vĩ mô và dòng tiền kỹ thuật hàng ngày.")
    badge = data.get("badge", "Dòng Tiền Vĩ Mô & Khối Lượng Thể Chế")
    read_time = data.get("read_time", "6 phút đọc")
    html_body = data.get("html_body", "")
    comments = data.get("initial_comments", [])
    
    comments_html = ""
    for c in comments:
        comments_html += f"""
                <div class="comment-item">
                    <div class="comment-top">
                        <span class="comment-author"><i class="fa-solid fa-circle-user"></i> {c.get('name', 'Trader')}</span>
                        <span class="comment-date">{c.get('date', 'Hôm nay')}</span>
                    </div>
                    <div class="comment-text">
                        {c.get('text', '')}
                    </div>
                </div>"""
                
    comment_count = str(len(comments))

    page = HTML_TEMPLATE
    page = page.replace("__TITLE__", title)
    page = page.replace("__META_DESC__", meta_desc)
    page = page.replace("__BADGE__", badge)
    page = page.replace("__DATE_STR__", date_str)
    page = page.replace("__READ_TIME__", read_time)
    page = page.replace("__HTML_BODY__", html_body)
    page = page.replace("__COMMENT_COUNT__", comment_count)
    page = page.replace("__COMMENTS_HTML__", comments_html)
    
    return page

def update_homepage(post_data: Dict[str, Any], post_filename: str, date_str: str):
    if not os.path.exists(INDEX_HTML):
        print(f"[!] Warning: {INDEX_HTML} not found.")
        return

    try:
        with open(INDEX_HTML, "r", encoding="utf-8") as f:
            content = f.read()

        title = post_data.get("title", "")
        excerpt = post_data.get("lead_excerpt", "")
        badge = post_data.get("badge", "Dòng Tiền Vĩ Mô & Khối Lượng Thể Chế")
        read_time = post_data.get("read_time", "6 phút đọc")
        post_rel_path = f"posts/{post_filename}"

        lead_story_regex = r'(<article class="lead-story">[\s\S]*?</article>)'
        
        new_lead_story = f"""<article class="lead-story">
            <div class="lead-image-box">
                <img src="assets/images/logo.jpg" alt="Phân Tích Dòng Tiền Tổ Chức">
                <div class="watermark-stamp">
                    <i class="fa-solid fa-shield-halved"></i> PTvolume.com
                </div>
            </div>
            <div class="lead-content">
                <span class="category-tag">{badge}</span>
                <h1 class="lead-title">
                    <a href="{post_rel_path}">{title}</a>
                </h1>
                <p class="lead-excerpt">
                    {excerpt}
                </p>
                <div class="byline">
                    <span>Biên soạn bởi <strong class="byline-author">Nhóm Nghiên Cứu PTvolume</strong></span>
                    <span>•</span>
                    <span>{date_str}</span>
                    <span>•</span>
                    <span><i class="fa-regular fa-clock"></i> {read_time}</span>
                </div>
            </div>
        </article>"""

        if re.search(lead_story_regex, content):
            updated_content = re.sub(lead_story_regex, new_lead_story, content, count=1)
            with open(INDEX_HTML, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"[+] Successfully updated homepage lead story in {INDEX_HTML}")
        else:
            print("[!] Could not match lead-story regex in index.html")

    except Exception as e:
        print(f"[!] Failed to update index.html: {e}")

def update_posts_json(post_info: Dict[str, Any]):
    try:
        posts = []
        if os.path.exists(POSTS_INDEX_JSON):
            with open(POSTS_INDEX_JSON, "r", encoding="utf-8") as f:
                posts = json.load(f)
        
        posts.insert(0, post_info)
        posts = posts[:100]

        with open(POSTS_INDEX_JSON, "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)
        print(f"[+] Updated posts archive in {POSTS_INDEX_JSON}")
    except Exception as e:
        print(f"[!] Failed to update posts.json: {e}")

def run_auto_publisher():
    print("=" * 70)
    print("PTvolume.com AUTO NEWS PUBLISHER: GLOBAL MARKET INTELLIGENCE")
    print("=" * 70)
    
    # 1. Fetch live news
    news_items = gather_top_market_news()
    if not news_items:
        print("[!] No news items retrieved. Aborting.")
        return False

    # 2. Synthesize with Gemini
    payload = generate_article_payload(news_items)
    if not payload:
        print("[!] Failed to generate article payload from Gemini. Aborting.")
        return False

    # 3. Create post HTML
    today = datetime.now(timezone.utc)
    date_str = today.strftime("%d Tháng %m, %Y")
    date_slug = today.strftime("%Y-%m-%d")
    
    slug = payload.get("slug", "ban-tin-dong-tien-thi-truong").strip()
    slug = re.sub(r'[^a-zA-Z0-9\-]', '', slug).lower()
    post_filename = f"{date_slug}-{slug}.html"
    post_filepath = os.path.join(POSTS_DIR, post_filename)

    post_html = build_post_html(payload, date_str)
    
    with open(post_filepath, "w", encoding="utf-8") as f:
        f.write(post_html)
    print(f"[+] Created article file: {post_filepath}")

    # 4. Update index.html
    update_homepage(payload, post_filename, date_str)

    # 5. Update posts.json
    update_posts_json({
        "title": payload.get("title"),
        "slug": slug,
        "filename": post_filename,
        "date": date_str,
        "date_iso": today.isoformat(),
        "badge": payload.get("badge"),
        "excerpt": payload.get("lead_excerpt"),
        "read_time": payload.get("read_time")
    })

    # 6. Automatically update sitemap.xml for Google Crawlers
    if generate_sitemap:
        try:
            generate_sitemap()
            print("[+] Updated sitemap.xml for fast Google indexing.")
        except Exception as e:
            print(f"[!] Warning: Failed to update sitemap: {e}")

    print("\n" + "=" * 70)
    print(f"PUBLISHED SUCCESSFULLY: {payload.get('title')}")
    print(f"File: posts/{post_filename}")
    print("=" * 70 + "\n")
    return True

if __name__ == "__main__":
    success = run_auto_publisher()
    if not success:
        sys.exit(1)
