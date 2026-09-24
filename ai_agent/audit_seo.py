# -*- coding: utf-8 -*-
import os
import glob
import re
from bs4 import BeautifulSoup

lessons_dir = r"hoc-tap"
files = sorted(
    glob.glob(os.path.join(lessons_dir, "khoa-hoc-vsa-bai-*.html")),
    key=lambda x: int(re.search(r"bai-(\d+)", x).group(1)) if re.search(r"bai-(\d+)", x) else 999
)

print(f"TONG SO BAI HOC VSA: {len(files)}")
print("=" * 115)
print(f"| {'Bai':<7} | {'Kich thuoc':<10} | {'So tu':<8} | {'Title (Ky tu)':<14} | {'Meta Desc':<11} | {'H2 / H3':<9} | {'Danh gia SEO':<16} |")
print("|" + "-" * 9 + "|" + "-" * 12 + "|" + "-" * 10 + "|" + "-" * 16 + "|" + "-" * 13 + "|" + "-" * 11 + "|" + "-" * 18 + "|")

total_words = 0
for f in files:
    fname = os.path.basename(f)
    match = re.search(r"bai-(\d+)", fname)
    bai_no = f"Bai {match.group(1)}" if match else fname[:10]
    size_kb = os.path.getsize(f) / 1024
    
    with open(f, "r", encoding="utf-8") as fp:
        html = fp.read()
    
    soup = BeautifulSoup(html, "html.parser")
    
    title_text = soup.title.string.strip() if soup.title and soup.title.string else ""
    meta_desc = ""
    meta_desc_tag = soup.find("meta", attrs={"name": "description"})
    if meta_desc_tag and meta_desc_tag.get("content"):
        meta_desc = meta_desc_tag["content"].strip()
    
    h2_count = len(soup.find_all("h2"))
    h3_count = len(soup.find_all("h3"))
    
    article = soup.find("article") or soup.find("main") or soup.body
    if article:
        temp_soup = BeautifulSoup(str(article), "html.parser")
        for tag in temp_soup(["script", "style", "nav", "header", "footer"]):
            tag.extract()
        text = temp_soup.get_text(separator=" ")
    else:
        text = soup.get_text(separator=" ")
        
    words = [w for w in re.split(r"\s+", text) if len(w) > 0]
    word_count = len(words)
    total_words += word_count
    
    seo_eval = "Xuat sac (A+)" if word_count >= 1500 and 100 <= len(meta_desc) <= 170 and h2_count >= 3 else "Dat chuan (A)" if word_count >= 1000 else "Can bo sung"
    
    print(f"| {bai_no:<7} | {size_kb:6.1f} KB   | {word_count:<8} | {len(title_text):<14} | {len(meta_desc):<11} | {h2_count}/{h3_count:<7} | {seo_eval:<16} |")

print("=" * 115)
print(f"Tong so tu toan bo 21 bai hoc: {total_words:,} tu (Trung binh ~{total_words//len(files):,} tu/bai)")
