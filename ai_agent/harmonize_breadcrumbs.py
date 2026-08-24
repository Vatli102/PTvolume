import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update tu-sach
for f in glob.glob('tu-sach/*.html'):
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    
    # Fix breadcrumb link and text
    txt = re.sub(
        r'<a href="\.\./index\.html#(?:library|psychology|tu-sach)">.*?</a>',
        '<a href="../index.html#tu-sach">Tủ Sách Tài Chính</a>',
        txt
    )
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(txt)
    print(f'Harmonized breadcrumbs in {f}')

# 2. Update phan-tich
for f in glob.glob('phan-tich/*.html'):
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    
    txt = re.sub(
        r'<a href="\.\./index\.html#phan-tich">.*?</a>',
        '<a href="../index.html#phan-tich">Bản Tin Vĩ Mô</a>',
        txt
    )
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(txt)
    print(f'Harmonized breadcrumbs in {f}')

# 3. Update hoc-tap
for f in glob.glob('hoc-tap/*.html'):
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    
    txt = re.sub(
        r'<a href="\.\./index\.html#hoc-tap">.*?</a>',
        '<a href="../index.html#hoc-tap">Học Tập</a>',
        txt
    )
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(txt)
    print(f'Harmonized breadcrumbs in {f}')

print('All breadcrumbs synchronized with website menu!')
