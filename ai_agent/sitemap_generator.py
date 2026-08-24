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
CATEGORY_DIRS = [
    ("tu-sach", "0.95", "weekly"),
    ("phan-tich", "0.9", "weekly"),
    ("hoc-tap", "0.9", "weekly"),
]
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
    scanning all pages and category folders (tu-sach, phan-tich, hoc-tap).
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
        '    <!-- Bai viet theo Chuyen muc Menu -->'
    ]

    # Add all category articles
    for folder_name, priority, changefreq in CATEGORY_DIRS:
        folder_path = os.path.join(BASE_DIR, folder_name)
        if os.path.exists(folder_path):
            files = sorted(
                [f for f in os.listdir(folder_path) if f.endswith(".html")],
                reverse=True
            )
            for file_name in files:
                file_path = os.path.join(folder_path, file_name)
                try:
                    mtime = os.path.getmtime(file_path)
                    mod_date = datetime.fromtimestamp(mtime, tz=timezone.utc).strftime("%Y-%m-%d")
                except Exception:
                    mod_date = today_iso
                    
                xml_lines.append('    <url>')
                xml_lines.append(f'        <loc>{BASE_URL}/{folder_name}/{file_name}</loc>')
                xml_lines.append(f'        <lastmod>{mod_date}</lastmod>')
                xml_lines.append(f'        <changefreq>{changefreq}</changefreq>')
                xml_lines.append(f'        <priority>{priority}</priority>')
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
