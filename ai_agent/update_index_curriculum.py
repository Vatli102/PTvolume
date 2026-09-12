# -*- coding: utf-8 -*-
"""
Cập nhật danh mục trọn bộ 20 bài học của Khóa học vào index.html
Bản quyền PTvolume.com
"""
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

INDEX_PATH = r"D:\PHAN DUA CẤM XÓA\AI_Agent_Trading\index.html"

# Danh sách 20 bài học để hiển thị trên Trang Chủ
CURRICULUM_MODULES = [
    {
        "module": "Học Phần 1: Nền Tảng Naked Price Action",
        "icon": "fa-solid fa-chart-line",
        "color": "#00E5FF",
        "lessons": [
            ("Bài 1 (P1)", "khoa-hoc-vsa-wyckoff-bai-1-bieu-do-tran-the-naked-chart-phan-1.html", "Biểu Đồ Trần &ndash; Khám Phá Bản Năng Của Giá"),
            ("Bài 1 (P2)", "khoa-hoc-vsa-wyckoff-bai-1-cau-truc-thi-truong-va-vung-cung-cau-phan-2.html", "Cấu Trúc Thị Trường &ndash; Đỉnh/Đáy Swing &amp; Vùng Cung Cầu"),
            ("Bài 2", "khoa-hoc-vsa-wyckoff-bai-2-ngon-ngu-nen-don-va-cum-nen-dao-chieu-sat-thu.html", "Ngôn Ngữ Nến Đơn &amp; Cụm Nến Đảo Chiều (Pin Bar, Engulfing, Fakey)"),
            ("Bài 3", "khoa-hoc-vsa-wyckoff-bai-3-vung-nen-tich-luy-build-up-va-true-breakout.html", "Vùng Nén Tích Lũy (Build-Up) &amp; True Breakout vs Fakeout"),
            ("Bài 4", "khoa-hoc-vsa-wyckoff-bai-4-nghe-thuat-phan-tich-da-khung-thoi-gian.html", "Nghệ Thuật Phân Tích Đa Khung Thời Gian (Top-Down Analysis)")
        ]
    },
    {
        "module": "Học Phần 2: Volume Spread Analysis (VSA Mastery)",
        "icon": "fa-solid fa-chart-column",
        "color": "#F0B90B",
        "lessons": [
            ("Bài 5", "khoa-hoc-vsa-wyckoff-bai-5-vsa-can-ban-spread-va-khoi-luong.html", "VSA Căn Bản &ndash; Mối Tương Quan Giữa Spread &amp; Volume"),
            ("Bài 6", "khoa-hoc-vsa-wyckoff-bai-6-doc-vi-nen-no-demand-va-upthrust.html", "Đọc Vị Nến Cạn Cầu (No Demand) &amp; Nến Thử Cầu (Upthrust)"),
            ("Bài 7", "khoa-hoc-vsa-wyckoff-bai-7-doc-vi-nen-no-supply-va-stopping-volume.html", "Đọc Vị Nến Cạn Cung (No Supply) &amp; Dừng Giá (Stopping Volume)"),
            ("Bài 8", "khoa-hoc-vsa-wyckoff-bai-8-hap-thu-cung-absorption-va-phan-phoi-am-tham.html", "Hiện Tượng Hấp Thụ Cung (Absorption) &amp; Phân Phối (Churning)")
        ]
    },
    {
        "module": "Học Phần 3: Phương Pháp Wyckoff & Bẫy Thanh Khoản",
        "icon": "fa-solid fa-cubes",
        "color": "#089981",
        "lessons": [
            ("Bài 9", "khoa-hoc-vsa-wyckoff-bai-9-ba-quy-luat-song-con-cua-richard-wyckoff.html", "Ba Quy Luật Sống Còn Của Richard Wyckoff"),
            ("Bài 10", "khoa-hoc-vsa-wyckoff-bai-10-boc-tach-5-pha-tich-luy-wyckoff-va-cu-ru-bo-spring.html", "5 Pha Tích Lũy Wyckoff &amp; Tuyệt Kỹ Bắt Cú Rũ Bỏ Spring (Pha C)"),
            ("Bài 11", "khoa-hoc-vsa-wyckoff-bai-11-boc-tach-5-pha-phan-phoi-wyckoff-va-bay-utad.html", "5 Pha Phân Phối Wyckoff &amp; Bẫy Mua Đỉnh UTAD (Pha C)"),
            ("Bài 12", "khoa-hoc-vsa-wyckoff-bai-12-bay-thanh-khoan-liquidity-hunt-va-stop-hunt.html", "Bẫy Thanh Khoản (Liquidity Hunts) &amp; Stop Hunt Của Cá Mập")
        ]
    },
    {
        "module": "Học Phần 4: Bộ 3 Setup Bắn Tỉa Điểm Vào Lệnh Thực Chiến",
        "icon": "fa-solid fa-crosshairs",
        "color": "#2962FF",
        "lessons": [
            ("Bài 13", "khoa-hoc-vsa-wyckoff-bai-13-setup-1-ban-tia-dao-chieu-cung-cau-vsa.html", "Setup 1 &ndash; Bắn Tỉa Đảo Chiều Vùng Cung Cầu: Rejection + VSA"),
            ("Bài 14", "khoa-hoc-vsa-wyckoff-bai-14-setup-2-thuan-xu-huong-pullback-flip-zone.html", "Setup 2 &ndash; Thuận Xu Hướng Sau Cú Test Cạn Kiệt Flip Zone"),
            ("Bài 15", "khoa-hoc-vsa-wyckoff-bai-15-setup-3-bat-diem-but-pha-vung-nen-build-up.html", "Setup 3 &ndash; Bắt Điểm Bứt Phá Vùng Nén (Build-Up Breakout)")
        ]
    },
    {
        "module": "Học Phần 5: Quản Trị Rủi Ro & Tâm Lý Giao Dịch Sinh Tồn",
        "icon": "fa-solid fa-shield-halved",
        "color": "#FF707E",
        "lessons": [
            ("Bài 16", "khoa-hoc-vsa-wyckoff-bai-16-structural-stop-loss-cat-lo-theo-cau-truc.html", "Structural Stop Loss &ndash; Nghệ Thuật Cắt Lỗ Cấu Trúc"),
            ("Bài 17", "khoa-hoc-vsa-wyckoff-bai-17-nghe-thuat-gong-loi-trailing-stop-toi-uu-rr.html", "Nghệ Thuật Gồng Lời (Trailing Stop) Theo Swing Points"),
            ("Bài 18", "khoa-hoc-vsa-wyckoff-bai-18-toan-hoc-xac-suat-va-quan-tri-vi-the-position-sizing.html", "Toán Học Xác Suất &ndash; Vì Sao Thắng 40% Vẫn Kiếm Lợi Nhuận Khủng?"),
            ("Bài 19", "khoa-hoc-vsa-wyckoff-bai-19-tam-ly-trading-in-the-zone-cai-nghien-fomo.html", "Tâm Lý Trading In The Zone &ndash; Cai Nghiện FOMO"),
            ("Bài 20", "khoa-hoc-vsa-wyckoff-bai-20-mindmap-toan-thu-va-10-case-study-thuc-te.html", "Bản Đồ Tư Duy (Mindmap) Toàn Thư + 10 Case Study Thực Tế")
        ]
    }
]

def build_curriculum_html():
    cards_html = []
    
    # 4 Featured Lead Cards
    featured = [
        ("Naked Chart • Bài 1 (P1)", "hoc-tap/khoa-hoc-vsa-wyckoff-bai-1-bieu-do-tran-the-naked-chart-phan-1.html", "Bài 1: Biểu Đồ Trần &ndash; Khám Phá Bản Năng Của Giá", "assets/images/naked_chart_vs_indicators.svg", "Lột trần bẫy chỉ báo trễ, giải phẫu 3 thành tố nến nguyên bản và quy luật nỗ lực - kết quả.", "#00E5FF"),
        ("Market Structure • Bài 1 (P2)", "hoc-tap/khoa-hoc-vsa-wyckoff-bai-1-cau-truc-thi-truong-va-vung-cung-cau-phan-2.html", "Bài 1: Cấu Trúc Thị Trường &amp; Vùng Cung Cầu", "assets/images/market_structure_bos_choch.svg", "Xác định Đỉnh/Đáy Swing High/Low, Break of Structure (BOS) và điểm bắn tỉa Flip Zone.", "#F0B90B"),
        ("Wyckoff • Bài 10", "hoc-tap/khoa-hoc-vsa-wyckoff-bai-10-boc-tach-5-pha-tich-luy-wyckoff-va-cu-ru-bo-spring.html", "Bài 10: 5 Pha Tích Lũy Wyckoff &amp; Tuyệt Kỹ Spring", "assets/images/wyckoff_accumulation_schematic.svg", "Bóc tách 5 pha tích lũy của nhà tạo lập và tuyệt kỹ vào lệnh chân sóng lớn tại cú rũ bỏ Spring.", "#26E7A6"),
        ("Sniper Setup • Bài 13", "hoc-tap/khoa-hoc-vsa-wyckoff-bai-13-setup-1-ban-tia-dao-chieu-cung-cau-vsa.html", "Bài 13: Setup 1 &ndash; Bắn Tỉa Đảo Chiều Vùng Cung Cầu", "assets/images/naked_vsa_trading_setups.svg", "Công thức vào lệnh đảo chiều xác suất cao với nến Pin Bar Kangaroo Tail và VSA Volume.", "#6095FF")
    ]
    
    lead_cards = []
    for f in featured:
        lead_cards.append(f'''
            <div class="analysis-lead-card" style="margin-bottom:0; border-color:rgba(0, 229, 255, 0.3); display:flex; flex-direction:column; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);">
                <div class="analysis-lead-img" style="flex:none; height:160px; position:relative;">
                    <img src="{f[3]}" alt="{f[2]}" style="height:100%; object-fit:cover;">
                    <div class="watermark-box" style="position:absolute; bottom:8px; right:8px; margin:0; padding:2px 8px; border-radius:4px; font-size:0.68rem; background:rgba(11,14,20,0.7); backdrop-filter:blur(4px);"><i class="fa-solid fa-shield-halved"></i> PTvolume.com</div>
                </div>
                <div class="analysis-lead-content" style="flex:1; display:flex; flex-direction:column; justify-content:space-between;">
                    <div>
                        <div class="analysis-category" style="color:{f[5]};"><i class="fa-solid fa-graduation-cap"></i> {f[0]}</div>
                        <h3 class="analysis-lead-title" style="font-size:1.05rem; margin:8px 0 10px;">
                            <a href="{f[1]}">{f[2]}</a>
                        </h3>
                        <p class="analysis-lead-excerpt" style="font-size:0.83rem; line-height:1.55; margin-bottom:12px;">
                            {f[4]}
                        </p>
                    </div>
                    <div>
                        <a href="{f[1]}" class="btn-hero-primary" style="padding:8px 14px; font-size:0.8rem; background:{f[5]}; color:#000; font-weight:700; width:100%; text-align:center; justify-content:center;">
                            <i class="fa-solid fa-graduation-cap"></i> Vào Học Ngay <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>
        ''')

    # Accordion / Syllabus Table for all 20 lessons
    modules_html = []
    for m in CURRICULUM_MODULES:
        lessons_li = []
        for l in m["lessons"]:
            lessons_li.append(f'''
                <li style="display:flex; align-items:center; justify-content:space-between; padding:10px 14px; border-bottom:1px solid #1c2436; font-size:0.88rem;">
                    <div style="display:flex; align-items:center; gap:10px;">
                        <span style="display:inline-block; background:{m['color']}22; color:{m['color']}; border:1px solid {m['color']}55; padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:700; min-width:75px; text-align:center;">{l[0]}</span>
                        <a href="hoc-tap/{l[1]}" style="color:#CAD4E0; font-weight:600; text-decoration:none;" onmouseover="this.style.color='#00E5FF'" onmouseout="this.style.color='#CAD4E0'">{l[2]}</a>
                    </div>
                    <a href="hoc-tap/{l[1]}" style="color:{m['color']}; font-size:0.8rem; font-weight:700; display:inline-flex; align-items:center; gap:4px; text-decoration:none;">Vào học <i class="fa-solid fa-chevron-right" style="font-size:0.7rem;"></i></a>
                </li>
            ''')
        
        modules_html.append(f'''
            <div style="background:#141822; border:1px solid #222938; border-radius:10px; margin-bottom:16px; overflow:hidden;">
                <div style="background:#10141D; padding:12px 18px; border-bottom:1px solid #222938; display:flex; align-items:center; gap:10px; font-weight:800; color:{m['color']}; font-size:1.02rem;">
                    <i class="{m['icon']}"></i> {m['module']}
                </div>
                <ul style="list-style:none; padding:0; margin:0;">
                    {''.join(lessons_li)}
                </ul>
            </div>
        ''')

    curriculum_section = f'''
                    <!-- HỌC PHẦN 3: CHUYÊN SÂU NAKED CHART, VSA & WYCKOFF (TRỌN BỘ 20 BÀI) -->
                    <div class="section-header-bar" style="margin-top:28px; border-top:1px dashed var(--border-color); padding-top:28px;">
                        <div class="section-headline">
                            <div class="section-kicker" style="color:var(--accent-gold);"><i class="fa-solid fa-crown"></i> Học Phần 3 • Đỉnh Cao Phân Tích Kỹ Thuật</div>
                            <h3 class="section-title" style="font-size:1.45rem;">💎 Khóa Học: Làm Chủ Biểu Đồ Trần, VSA &amp; Phương Pháp Wyckoff Thực Chiến</h3>
                            <p class="section-subtitle">Giáo trình toàn thư 20 bài học: Phân tích không chỉ báo trễ, theo dấu dòng tiền Smart Money và tối ưu điểm vào lệnh R:R cao.</p>
                        </div>
                    </div>

                    <!-- 4 BÀI HỌC TIÊU BIỂU DẠNG CARD -->
                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:18px; margin-bottom:28px;">
                        {''.join(lead_cards)}
                    </div>

                    <!-- DANH MỤC TRỌN BỘ 20 BÀI HỌC DẠNG SYLLABUS -->
                    <div style="margin-top:20px; margin-bottom:36px;">
                        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:16px;">
                            <h4 style="font-size:1.15rem; color:#fff; display:flex; align-items:center; gap:8px;">
                                <i class="fa-solid fa-list-check" style="color:var(--cyan);"></i> Sơ Đồ Danh Mục Trọn Bộ 20 Bài Học (Từ A &ndash; Z)
                            </h4>
                            <span style="font-size:0.8rem; color:var(--text-muted);"><i class="fa-solid fa-circle-check" style="color:#089981;"></i> Đã biên soạn đầy đủ 20/20 bài</span>
                        </div>
                        {''.join(modules_html)}
                    </div>
    '''
    return curriculum_section

def update_index():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Tìm vị trí Học Phần 3 và thay thế
    pattern = re.compile(r'<!-- HỌC PHẦN 3: CHUYÊN SÂU NAKED CHART, VSA & WYCKOFF -->.*?</div>\s*</section>', re.DOTALL)
    
    new_html = build_curriculum_html() + "\n                </section>"
    
    if pattern.search(content):
        updated = pattern.sub(new_html, content)
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            f.write(updated)
        print("Đã cập nhật thành công trọn bộ danh mục 20 bài học vào index.html!")
    else:
        print("Không tìm thấy pattern Học phần 3 trong index.html, kiểm tra lại vị trí.")

if __name__ == "__main__":
    update_index()
