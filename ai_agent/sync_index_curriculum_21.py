# -*- coding: utf-8 -*-
"""
Cập nhật danh mục chuẩn 21 bài học vào index.html
TUYỆT ĐỐI KHÔNG CHẠY GIT PUSH.
"""
import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from reorder_lessons_1_to_21 import rebuild_all_21_lessons

INDEX_PATH = r"D:\PHAN DUA CẤM XÓA\AI_Agent_Trading\index.html"

def update_index_with_21_lessons():
    lessons = rebuild_all_21_lessons()
    
    # Gom nhóm theo 5 học phần
    modules = [
        {"num": 1, "name": "Học Phần 1: Nền Tảng Naked Price Action", "icon": "fa-solid fa-chart-line", "color": "#00E5FF", "lessons": []},
        {"num": 2, "name": "Học Phần 2: Volume Spread Analysis (VSA Mastery)", "icon": "fa-solid fa-chart-column", "color": "#F0B90B", "lessons": []},
        {"num": 3, "name": "Học Phần 3: Phương Pháp Wyckoff & Bẫy Thanh Khoản", "icon": "fa-solid fa-cubes", "color": "#089981", "lessons": []},
        {"num": 4, "name": "Học Phần 4: Bộ 3 Setup Bắn Tỉa Điểm Vào Lệnh Thực Chiến", "icon": "fa-solid fa-crosshairs", "color": "#2962FF", "lessons": []},
        {"num": 5, "name": "Học Phần 5: Quản Trị Rủi Ro & Tâm Lý Giao Dịch Sinh Tồn", "icon": "fa-solid fa-shield-halved", "color": "#FF707E", "lessons": []},
    ]
    
    for l in lessons:
        n = l["num"]
        if n <= 5:
            modules[0]["lessons"].append(l)
        elif n <= 9:
            modules[1]["lessons"].append(l)
        elif n <= 13:
            modules[2]["lessons"].append(l)
        elif n <= 16:
            modules[3]["lessons"].append(l)
        else:
            modules[4]["lessons"].append(l)

    # 4 Featured Lead Cards
    featured = [
        lessons[0],   # Bài 1: Biểu đồ trần
        lessons[1],   # Bài 2: Cấu trúc thị trường
        lessons[10],  # Bài 11: 5 Pha tích lũy Wyckoff & Spring
        lessons[13],  # Bài 14: Setup 1 Đảo chiều
    ]
    
    lead_cards = []
    card_colors = ["#00E5FF", "#F0B90B", "#26E7A6", "#6095FF"]
    card_badges = ["Naked Chart • Bài 1", "Market Structure • Bài 2", "Wyckoff • Bài 11", "Sniper Setup • Bài 14"]
    
    for idx, f in enumerate(featured):
        col = card_colors[idx]
        bad = card_badges[idx]
        lead_cards.append(f'''
            <div class="analysis-lead-card" style="margin-bottom:0; border-color:rgba(0, 229, 255, 0.3); display:flex; flex-direction:column; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);">
                <div class="analysis-lead-img" style="flex:none; height:160px; position:relative;">
                    <img src="{f['image'].replace('../', '')}" alt="{f['title']}" style="height:100%; object-fit:cover;">
                    <div class="watermark-box" style="position:absolute; bottom:8px; right:8px; margin:0; padding:2px 8px; border-radius:4px; font-size:0.68rem; background:rgba(11,14,20,0.7); backdrop-filter:blur(4px);"><i class="fa-solid fa-shield-halved"></i> PTvolume.com</div>
                </div>
                <div class="analysis-lead-content" style="flex:1; display:flex; flex-direction:column; justify-content:space-between;">
                    <div>
                        <div class="analysis-category" style="color:{col};"><i class="fa-solid fa-graduation-cap"></i> {bad}</div>
                        <h3 class="analysis-lead-title" style="font-size:1.05rem; margin:8px 0 10px;">
                            <a href="hoc-tap/{f['slug']}.html">{f['title']}</a>
                        </h3>
                        <p class="analysis-lead-excerpt" style="font-size:0.83rem; line-height:1.55; margin-bottom:12px;">
                            {f['desc']}
                        </p>
                    </div>
                    <div>
                        <a href="hoc-tap/{f['slug']}.html" class="btn-hero-primary" style="padding:8px 14px; font-size:0.8rem; background:{col}; color:#000; font-weight:700; width:100%; text-align:center; justify-content:center;">
                            <i class="fa-solid fa-graduation-cap"></i> Vào Học Ngay <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>
        ''')

    modules_html = []
    for m in modules:
        lessons_li = []
        for l in m["lessons"]:
            lessons_li.append(f'''
                <li style="display:flex; align-items:center; justify-content:space-between; padding:10px 14px; border-bottom:1px solid #1c2436; font-size:0.88rem;">
                    <div style="display:flex; align-items:center; gap:10px;">
                        <span style="display:inline-block; background:{m['color']}22; color:{m['color']}; border:1px solid {m['color']}55; padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:700; min-width:65px; text-align:center;">Bài {l['num']}</span>
                        <a href="hoc-tap/{l['slug']}.html" style="color:#CAD4E0; font-weight:600; text-decoration:none;" onmouseover="this.style.color='#00E5FF'" onmouseout="this.style.color='#CAD4E0'">{l['title']}</a>
                    </div>
                    <a href="hoc-tap/{l['slug']}.html" style="color:{m['color']}; font-size:0.8rem; font-weight:700; display:inline-flex; align-items:center; gap:4px; text-decoration:none;">Vào học <i class="fa-solid fa-chevron-right" style="font-size:0.7rem;"></i></a>
                </li>
            ''')
        
        modules_html.append(f'''
            <div style="background:#141822; border:1px solid #222938; border-radius:10px; margin-bottom:16px; overflow:hidden;">
                <div style="background:#10141D; padding:12px 18px; border-bottom:1px solid #222938; display:flex; align-items:center; gap:10px; font-weight:800; color:{m['color']}; font-size:1.02rem;">
                    <i class="{m['icon']}"></i> {m['name']} ({len(m['lessons'])} Bài)
                </div>
                <ul style="list-style:none; padding:0; margin:0;">
                    {''.join(lessons_li)}
                </ul>
            </div>
        ''')

    curriculum_section = f'''
                    <!-- HỌC PHẦN 3: CHUYÊN SÂU NAKED CHART, VSA & WYCKOFF (TRỌN BỘ 21 BÀI) -->
                    <div class="section-header-bar" style="margin-top:28px; border-top:1px dashed var(--border-color); padding-top:28px;">
                        <div class="section-headline">
                            <div class="section-kicker" style="color:var(--accent-gold);"><i class="fa-solid fa-crown"></i> Học Phần 3 • Đỉnh Cao Phân Tích Kỹ Thuật</div>
                            <h3 class="section-title" style="font-size:1.45rem;">💎 Khóa Học: Làm Chủ Biểu Đồ Trần, VSA &amp; Phương Pháp Wyckoff Thực Chiến</h3>
                            <p class="section-subtitle">Giáo trình toàn thư 21 bài học: Phân tích không chỉ báo trễ, theo dấu dòng tiền Smart Money và tối ưu điểm vào lệnh R:R cao.</p>
                        </div>
                    </div>

                    <!-- 4 BÀI HỌC TIÊU BIỂU DẠNG CARD -->
                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:18px; margin-bottom:28px;">
                        {''.join(lead_cards)}
                    </div>

                    <!-- DANH MỤC TRỌN BỘ 21 BÀI HỌC DẠNG SYLLABUS -->
                    <div style="margin-top:20px; margin-bottom:36px;">
                        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:16px;">
                            <h4 style="font-size:1.15rem; color:#fff; display:flex; align-items:center; gap:8px;">
                                <i class="fa-solid fa-list-check" style="color:var(--cyan);"></i> Sơ Đồ Danh Mục Trọn Bộ 21 Bài Học (Từ Bài 1 &ndash; Bài 21)
                            </h4>
                            <span style="font-size:0.8rem; color:var(--text-muted);"><i class="fa-solid fa-circle-check" style="color:#089981;"></i> Đã biên soạn đầy đủ 21/21 bài</span>
                        </div>
                        {''.join(modules_html)}
                    </div>
    '''

    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r'<!-- HỌC PHẦN 3: CHUYÊN SÂU NAKED CHART, VSA & WYCKOFF.*?</div>\s*</section>', re.DOTALL)
    
    new_html = curriculum_section + "\n                </section>"
    
    if pattern.search(content):
        updated = pattern.sub(new_html, content)
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            f.write(updated)
        print("Đã cập nhật thành công trọn bộ danh mục 21 bài học vào index.html!")
    else:
        print("Không tìm thấy pattern Học phần 3 trong index.html!")

if __name__ == "__main__":
    update_index_with_21_lessons()
