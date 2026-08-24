import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

configs = [
    ('tu-sach', 'Tủ Sách Tài Chính', 'tu-sach'),
    ('phan-tich', 'Bản Tin Vĩ Mô', 'phan-tich'),
    ('hoc-tap', 'Học Tập', 'hoc-tap'),
]

for folder, menu_name, menu_id in configs:
    files = glob.glob(f'{folder}/*.html')
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            txt = fp.read()
        
        matches = re.findall(r'(<(?:div|nav)\s+class="breadcrumb">.*?</(?:div|nav)>)', txt, re.DOTALL)
        if matches:
            print(f'[{f}]:\n{matches[0].strip()}\n')
