import os
import sys
import re
from datetime import datetime, timezone
import xml.etree.ElementTree as ET

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")
POSTS_DIR = os.path.join(BASE_DIR, "posts")
PAGES_DIR = os.path.join(BASE_DIR, "pages")
BASE_URL = "https://ptvolume.com"

def get_page_info(file_path: str):
    title = ""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            m = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
            if m:
                title = m.group(1).split("|")[0].strip()
    except Exception:
        pass
    return title

def generate_sitemap() -> str:
    """
    Generates standard sitemap.xml for PTvolume.com
    scanning all pages and posts.
    """
    today_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml"',
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
        '',
        '    <!-- Trang chu PTvolume.com -->',
        '    <url>',
        f'        <loc>{BASE_URL}/</loc>',
        f'        <lastmod>{today_iso}</lastmod>',
        '        <changefreq>daily</changefreq>',
        '        <priority>1.0</priority>',
        '    </url>',
        '',
        '    <!-- Bai viet phan tich & Chuyen muc -->'
    ]

    # Add all posts
    if os.path.exists(POSTS_DIR):
        post_files = sorted(
            [f for f in os.listdir(POSTS_DIR) if f.endswith(".html")],
            reverse=True
        )
        for post_file in post_files:
            file_path = os.path.join(POSTS_DIR, post_file)
            title = get_page_info(file_path) or "Phân tích kỹ thuật PTvolume"
            # Get file modification date or fallback to today
            try:
                mtime = os.path.getmtime(file_path)
                mod_date = datetime.fromtimestamp(mtime, tz=timezone.utc).strftime("%Y-%m-%d")
            except Exception:
                mod_date = today_iso
                
            xml_lines.append('    <url>')
            xml_lines.append(f'        <loc>{BASE_URL}/posts/{post_file}</loc>')
            xml_lines.append(f'        <lastmod>{mod_date}</lastmod>')
            xml_lines.append('        <changefreq>weekly</changefreq>')
            xml_lines.append('        <priority>0.9</priority>')
            xml_lines.append('    </url>')

    xml_lines.append('')
    xml_lines.append('    <!-- Trang thong tin cot loi -->')
    
    core_pages = [
        ("about.html", "0.8", "monthly"),
        ("contact.html", "0.8", "monthly"),
        ("disclaimer.html", "0.6", "monthly"),
        ("privacy.html", "0.6", "monthly"),
        ("terms.html", "0.6", "monthly")
    ]
    
    for page_name, priority, changefreq in core_pages:
        file_path = os.path.join(PAGES_DIR, page_name)
        mod_date = today_iso
        if os.path.exists(file_path):
            try:
                mtime = os.path.getmtime(file_path)
                mod_date = datetime.fromtimestamp(mtime, tz=timezone.utc).strftime("%Y-%m-%d")
            except Exception:
                mod_date = today_iso
                
        xml_lines.append('    <url>')
        xml_lines.append(f'        <loc>{BASE_URL}/pages/{page_name}</loc>')
        xml_lines.append(f'        <lastmod>{mod_date}</lastmod>')
        xml_lines.append(f'        <changefreq>{changefreq}</changefreq>')
        xml_lines.append(f'        <priority>{priority}</priority>')
        xml_lines.append('    </url>')

    xml_lines.append('')
    xml_lines.append('</urlset>')
    
    sitemap_content = "\n".join(xml_lines)
    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
        
    print(f"[+] Successfully generated/updated sitemap at {SITEMAP_PATH}")
    return sitemap_content

if __name__ == "__main__":
    generate_sitemap()
