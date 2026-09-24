# -*- coding: utf-8 -*-
import os
import glob
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 100)
print("CHI TIẾT RÀ SOÁT TỪNG BÀI TRONG KHÓA HỌC VSA 21 BÀI (PTvolume.com)")
print("=" * 100)

for i in range(1, 22):
    pattern = f'hoc-tap/khoa-hoc-vsa-bai-{i}-*.html'
    matches = glob.glob(pattern)
    if not matches:
        continue
    fpath = matches[0]
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Extract body between article-body and nav-lesson-grid / comments-section
    m = re.search(r'<div class="article-body">(.*?)(?:<div class="nav-lesson-grid"|<div class="comments-section")', content, re.DOTALL)
    body_text = m.group(1) if m else ''
    clean_body = re.sub(r'<[^>]+>', ' ', body_text)
    words = len(clean_body.split())
    
    # Extract all img src
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', body_text)
    
    img_status = []
    for img in imgs:
        clean_img = img.split('?')[0].replace('../', '')
        exists = os.path.exists(clean_img)
        img_status.append((clean_img, exists))
        
    print(f"\n[BÀI {i:>2}] {fname}")
    print(f"  + Độ dài phần thân (Core Body Words): {words:>4} từ")
    print(f"  + Số lượng hình ảnh: {len(imgs)}")
    for c_img, ex in img_status:
        status_str = "TỒN TẠI (OK)" if ex else "KHÔNG TỒN TẠI (MISSING 404!)"
        print(f"      - [{status_str}] {c_img}")

