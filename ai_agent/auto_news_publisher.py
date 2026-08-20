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
You are the Chief Macro Strategist & Head of Technical Order Flow at PTvolume.com.
Synthesize the following live global market news into a master daily market analysis report for international traders and institutional investors.

MANDATORY RULES:
1. LANGUAGE: 100% fluent, high-level financial English (Investopedia / Bloomberg / Financial Times style).
2. TRADING FRAMEWORK: Naked Chart Price Action, Volume Spread Analysis (VSA), Wyckoff accumulation/distribution, and Smart Money liquidity concepts. No lagging indicators (RSI/MACD).
3. OUTPUT FORMAT: Output ONLY valid, parseable JSON with NO markdown code fences.

JSON SCHEMA TO RETURN:
{{
  "title": "A captivating, high-impact institutional headline (max 90 chars)",
  "slug": "url-friendly-slug-lowercase-with-hyphens",
  "meta_description": "Precise 1-2 sentence SEO meta description highlighting key market themes and technical order flow.",
  "category": "Daily Market Intelligence",
  "badge": "Institutional Macro & Order Flow",
  "read_time": "6 min read",
  "lead_excerpt": "A concise 2-3 sentence executive summary of today's dominant macroeconomic forces and trading implications.",
  "html_body": "The complete HTML formatted body of the article. Use semantic HTML (<h2>, <h3>, <p>, <ul>, <li>, <strong>, <em>, <div class=\\"highlight-box\\">). DO NOT include the main <h1> title or outer <html>/<head>/<body> tags.",
  "initial_comments": [
    {{
      "name": "Marcus Vance (Senior FX Trader)",
      "date": "Today, 08:30 UTC",
      "text": "Insightful breakdown on the DXY liquidity sweep. The Effort vs. Result dynamic on the 4H chart aligns exactly with Wyckoff Phase C."
    }},
    {{
      "name": "Elena Rostova (Macro Quant)",
      "date": "Today, 09:15 UTC",
      "text": "Great risk-to-reward parameters on Gold. Waiting for the low-volume test bar before confirming entry."
    }}
  ]
}}

CONTENT STRUCTURE REQUIREMENTS FOR 'html_body':
1. Executive Market Pulse (3 core drivers shaping today's global order flow).
2. Central Bank Dynamics & Macro Catalysts (Fed, ECB, BOJ, Treasury yields, Inflation).
3. Multi-Asset Impact Matrix (Forex Majors, Spot Gold XAU/USD, Crude Oil, US Indices).
4. Order Flow & Volume Spread Analysis (Smart Money accumulation/distribution footprints, Effort vs Result, Upthrust/Spring setups).
5. Tactical Execution Plan & Key Levels (Clear support/resistance zones, invalidation points, strict R:R >= 1:2.5).
6. Include a callout block with:
<div class="highlight-box">
  <h3><i class="fa-solid fa-crosshairs"></i> Institutional Execution Parameters</h3>
  <ul>
    <li><i class="fa-solid fa-check"></i> <strong>Primary Macro Bias:</strong> ...</li>
    <li><i class="fa-solid fa-check"></i> <strong>Key Catalysts:</strong> ...</li>
    <li><i class="fa-solid fa-check"></i> <strong>Technical Invalidation:</strong> ...</li>
    <li><i class="fa-solid fa-check"></i> <strong>Target Risk-to-Reward:</strong> Minimum 1:2.5 R:R</li>
  </ul>
</div>
7. Capital Discipline & Risk Management Mandate.

CURRENT LIVE MARKET HEADLINES:
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
<html lang="en">
<head>
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
            <a href="../index.html" class="btn">
                <i class="fa-solid fa-arrow-left"></i> Return to Homepage
            </a>
        </div>
    </header>

    <main class="article-container">
        <div class="breadcrumb">
            <a href="../index.html">Home</a>
            <i class="fa-solid fa-chevron-right" style="font-size: 0.7rem;"></i>
            <a href="../index.html#market-analysis">Market Analysis</a>
            <i class="fa-solid fa-chevron-right" style="font-size: 0.7rem;"></i>
            <span>Daily Intelligence</span>
        </div>

        <span class="article-badge"><i class="fa-solid fa-globe"></i> __BADGE__</span>
        
        <h1 class="article-title">__TITLE__</h1>

        <div class="article-meta">
            <span><i class="fa-regular fa-user"></i> Written by: <strong>PTvolume Institutional Desk</strong></span>
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
                <i class="fa-regular fa-comments" style="color: #00E5FF;"></i> Institutional Trader Exchange (<span id="commentCount">__COMMENT_COUNT__</span>)
            </h3>

            <form class="comment-form" id="commentForm" onsubmit="addComment(event)">
                <div class="form-group">
                    <label class="form-label">Trader Name / Institutional Handle:</label>
                    <input type="text" id="commentName" class="form-control" placeholder="e.g. Liam - FX Flow Trader" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Your Technical Perspective or Order Flow Analysis:</label>
                    <textarea id="commentContent" class="form-control" placeholder="Share your observations regarding today's price action and volume distribution..." required></textarea>
                </div>
                <button type="submit" class="btn">
                    <i class="fa-regular fa-paper-plane"></i> Submit Comment
                </button>
            </form>

            <div class="comment-list" id="commentList">
__COMMENTS_HTML__
            </div>
        </section>
    </main>

    <footer>
        <div class="footer-links">
            <a href="../pages/about.html">About PTvolume</a>
            <a href="../pages/contact.html">Contact</a>
            <a href="../pages/terms.html">Terms of Service</a>
            <a href="../pages/privacy.html">Privacy Policy</a>
            <a href="../pages/disclaimer.html">Risk Disclaimer</a>
        </div>
        <p>© 2026 PTvolume.com. All rights reserved. Naked Chart • Volume Spread Analysis • Wyckoff Order Flow.</p>
    </footer>

    <script>
        function addComment(e) {
            e.preventDefault();
            const nameInput = document.getElementById("commentName");
            const contentInput = document.getElementById("commentContent");

            const name = nameInput.value.trim();
            const content = contentInput.value.trim();

            if (!name || !content) return;

            const now = new Date();
            const timeString = now.toUTCString().slice(5, 22) + ' UTC';

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

            alert("Your comment has been submitted successfully to the community exchange!");
        }

        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
    </script>
</body>
</html>
"""

def build_post_html(data: Dict[str, Any], date_str: str) -> str:
    title = data.get("title", "Daily Global Market Intelligence | PTvolume")
    meta_desc = data.get("meta_description", "Daily institutional macroeconomic and technical order flow analysis.")
    badge = data.get("badge", "Daily Market Intelligence")
    read_time = data.get("read_time", "6 min read")
    html_body = data.get("html_body", "")
    comments = data.get("initial_comments", [])
    
    comments_html = ""
    for c in comments:
        comments_html += f"""
                <div class="comment-item">
                    <div class="comment-top">
                        <span class="comment-author"><i class="fa-solid fa-circle-user"></i> {c.get('name', 'Trader')}</span>
                        <span class="comment-date">{c.get('date', 'Today')}</span>
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
        badge = post_data.get("badge", "Daily Market Intelligence")
        read_time = post_data.get("read_time", "6 min read")
        post_rel_path = f"posts/{post_filename}"

        lead_story_regex = r'(<article class="lead-story">[\s\S]*?</article>)'
        
        new_lead_story = f"""<article class="lead-story">
            <div class="lead-image-box">
                <img src="assets/images/logo.jpg" alt="Institutional Market Analysis">
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
                    <span>Written by <strong class="byline-author">PTvolume Research Group</strong></span>
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
    date_str = today.strftime("%B %d, %Y")
    date_slug = today.strftime("%Y-%m-%d")
    
    slug = payload.get("slug", "daily-market-intelligence").strip()
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

    print("\n" + "=" * 70)
    print(f"PUBLISHED SUCCESSFULLY: {payload.get('title')}")
    print(f"File: posts/{post_filename}")
    print("=" * 70 + "\n")
    return True

if __name__ == "__main__":
    success = run_auto_publisher()
    if not success:
        sys.exit(1)
