# -*- coding: utf-8 -*-
"""
Bộ công cụ tạo đồ họa biểu đồ tài chính siêu nét (Ultra HD Pro Financial Graphics Engine)
Render toàn bộ hệ thống hình ảnh chuẩn HD/2K cho PTvolume.com bằng Matplotlib + Pillow.
100% không bị lỗi font, không bị đè chữ, bố cục thoáng đạt, màu sắc Dark Theme hiện đại.
"""
import sys
import os
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Thư mục chứa tài nguyên hình ảnh
ASSETS_DIR = r"d:\PHAN DUA CẤM XÓA\AI_Agent_Trading\assets\images"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Cấu hình font chữ an toàn tuyệt đối, không thiếu glyph
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Segoe UI', 'Helvetica', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

def setup_figure(w=16, h=9, bg_color="#0B0E14"):
    """Tạo khung vẽ chuẩn tỉ lệ 16:9 với độ phân giải siêu nét 150 DPI"""
    fig, ax = plt.subplots(figsize=(w, h), dpi=150)
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    return fig, ax

def add_watermark(ax):
    """Đóng dấu thương hiệu PTvolume.com tinh tế, sang trọng"""
    badge = patches.FancyBboxPatch(
        (35, 2), 30, 4,
        boxstyle="round,pad=0.5,rounding_size=1.5",
        facecolor="#141822",
        edgecolor="#00E5FF",
        linewidth=1.2,
        alpha=0.9
    )
    ax.add_patch(badge)
    ax.text(50, 4, "PTvolume.com  *  Naked Price Action & VSA Pro", 
            color="#CAD4E0", fontsize=11, fontweight='bold', ha='center', va='center')

# ==============================================================================
# HÌNH 1.1: BẪY CHỈ BÁO VS BIỂU ĐỒ TRẦN REAL-TIME
# ==============================================================================
def render_indicator_trap():
    fig, ax = setup_figure()
    
    # Tiêu đề chính
    title_box = patches.FancyBboxPatch((10, 91), 80, 6.5, boxstyle="round,pad=0.8,rounding_size=2", facecolor="#141824", edgecolor="#2962FF", linewidth=1.8)
    ax.add_patch(title_box)
    ax.text(50, 94.2, "BAN CHAT: MA TRAN CHI BAO DI CHAM vs BIEU DO TRAN REAL-TIME", color="#FFFFFF", fontsize=16, fontweight='bold', ha='center', va='center')

    # CỘT TRÁI: MA TRẬN CHỈ BÁO (BẪY ĐI CHẬM)
    card_left = patches.FancyBboxPatch((4, 10), 44, 78, boxstyle="round,pad=1,rounding_size=2", facecolor="#101520", edgecolor="#F23645", linewidth=2)
    ax.add_patch(card_left)
    
    hdr_left = patches.FancyBboxPatch((4, 81), 44, 7, boxstyle="round,pad=0.5,rounding_size=1", facecolor="#2A0C12", edgecolor="#F23645", linewidth=1.2)
    ax.add_patch(hdr_left)
    ax.text(26, 84.5, "[X] MA TRAN CHI BAO (TRE 7 - 10 NEN)", color="#FFA4AC", fontsize=13, fontweight='bold', ha='center', va='center')

    # Khung chart trái
    chart_bg1 = patches.FancyBboxPatch((6, 26), 40, 52, boxstyle="round,pad=0.5,rounding_size=1", facecolor="#080C14", edgecolor="#32141C", linewidth=1)
    ax.add_patch(chart_bg1)

    # Nến mờ phía sau
    candles_x1 = [10, 14, 18, 22, 26, 30, 34, 38, 42]
    for x in candles_x1[:4]:
        ax.plot([x, x], [35 + (x-10)*2, 45 + (x-10)*3], color="#089981", linewidth=2, alpha=0.4)
        ax.add_patch(patches.Rectangle((x-1, 38 + (x-10)*2.5), 2, 6, facecolor="#089981", alpha=0.4))
    
    # Nến sập sau đỉnh
    for x in candles_x1[4:]:
        ax.plot([x, x], [60 - (x-26)*3, 70 - (x-26)*3], color="#F23645", linewidth=2)
        ax.add_patch(patches.Rectangle((x-1, 62 - (x-26)*3), 2, 7, facecolor="#F23645"))

    # Các đường chỉ báo trễ cắt lộn xộn
    x_curve = np.linspace(8, 44, 100)
    y_ma20 = 40 + 25 * np.exp(-((x_curve - 28)**2) / 60)
    y_ma50 = 38 + 22 * np.exp(-((x_curve - 32)**2) / 80)
    y_ma200 = 36 + 15 * np.exp(-((x_curve - 36)**2) / 120)
    
    ax.plot(x_curve, y_ma20, color="#F0B90B", linewidth=2.5, label="MA20")
    ax.plot(x_curve, y_ma50, color="#E040FB", linewidth=2.5, label="MA50")
    ax.plot(x_curve, y_ma200, color="#00E5FF", linewidth=2.5, label="MA200")

    # Điểm cắt trễ ngay tại đỉnh
    ax.plot([30], [62], marker='o', markersize=12, color="#FF5252")
    trap_badge = patches.FancyBboxPatch((14, 68), 26, 7, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#2E0A12", edgecolor="#FF5252", linewidth=1.5)
    ax.add_patch(trap_badge)
    ax.text(27, 71.5, "[X] CHI BAO BAO MUA = DU DINH!", color="#FF5252", fontsize=10.5, fontweight='bold', ha='center', va='center')

    # Kết luận chân thẻ trái
    ftr_left = patches.FancyBboxPatch((6, 13), 40, 10, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#1F0A10", edgecolor="#F23645", linewidth=1.2)
    ax.add_patch(ftr_left)
    ax.text(26, 19.5, "Do tre toan hoc khien ban luon Mua o Dinh & Ban o Day.", color="#FFA4AC", fontsize=10.5, ha='center', va='center')
    ax.text(26, 15.5, "Tin hieu da nhau chan chat gay te liet tam ly.", color="#FF707E", fontsize=11, fontweight='bold', ha='center', va='center')


    # CỘT PHẢI: BIỂU ĐỒ TRẦN REAL-TIME
    card_right = patches.FancyBboxPatch((52, 10), 44, 78, boxstyle="round,pad=1,rounding_size=2", facecolor="#101520", edgecolor="#00E5FF", linewidth=2)
    ax.add_patch(card_right)
    
    hdr_right = patches.FancyBboxPatch((52, 81), 44, 7, boxstyle="round,pad=0.5,rounding_size=1", facecolor="#08282E", edgecolor="#00E5FF", linewidth=1.2)
    ax.add_patch(hdr_right)
    ax.text(74, 84.5, "[V] BIEU DO TRAN (THOI GIAN THUC)", color="#00E5FF", fontsize=13, fontweight='bold', ha='center', va='center')

    # Khung chart phải
    chart_bg2 = patches.FancyBboxPatch((54, 26), 40, 52, boxstyle="round,pad=0.5,rounding_size=1", facecolor="#080C14", edgecolor="#162E44", linewidth=1)
    ax.add_patch(chart_bg2)

    # Đường cản kháng cự ngang
    ax.plot([56, 92], [52, 52], color="#00E5FF", linewidth=2, linestyle='--')
    ax.text(58, 54, "CAN KHANG CU (RESISTANCE)", color="#00E5FF", fontsize=10, fontweight='bold')

    # Nến gom hàng
    ax.add_patch(patches.Rectangle((57, 42), 2, 6, facecolor="#089981"))
    ax.add_patch(patches.Rectangle((61, 40), 2, 7, facecolor="#F23645"))
    ax.add_patch(patches.Rectangle((65, 43), 2, 6, facecolor="#089981"))

    # NẾN BREAKOUT BÙNG NỔ
    ax.plot([70, 70], [45, 62], color="#26E7A6", linewidth=3)
    ax.add_patch(patches.Rectangle((68.5, 47), 3, 14, facecolor="#089981", edgecolor="#26E7A6", linewidth=1.5))
    
    # Điểm Sniper Entry
    ax.plot([70], [62], marker='o', markersize=10, color="#00E5FF")
    sniper_tag = patches.FancyBboxPatch((60, 68), 26, 7, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#07242E", edgecolor="#00E5FF", linewidth=1.5)
    ax.add_patch(sniper_tag)
    ax.text(73, 71.5, ">> SNIPER ENTRY CHAN SONG <<", color="#00E5FF", fontsize=10, fontweight='bold', ha='center', va='center')

    # Nến tăng tiếp diễn
    ax.add_patch(patches.Rectangle((73, 58), 2, 8, facecolor="#089981"))
    ax.add_patch(patches.Rectangle((77, 63), 2, 8, facecolor="#089981"))
    ax.add_patch(patches.Rectangle((81, 68), 2, 7, facecolor="#089981"))

    # Nến chốt lời đỉnh
    ax.plot([86, 86], [68, 79], color="#F0B90B", linewidth=2)
    ax.add_patch(patches.Rectangle((85, 72), 2, 4, facecolor="#F23645"))
    ax.text(86, 81, "Chot Loi (R:R 1:5)", color="#F0B90B", fontsize=9.5, fontweight='bold', ha='center')

    # Cột Volume VSA phía dưới
    ax.plot([56, 92], [36, 36], color="#1C2D44", linewidth=1)
    ax.add_patch(patches.Rectangle((57.5, 28), 1.5, 5, facecolor="#089981"))
    ax.add_patch(patches.Rectangle((61.5, 28), 1.5, 4, facecolor="#F23645"))
    ax.add_patch(patches.Rectangle((65.5, 28), 1.5, 5, facecolor="#089981"))
    # VOL KHỦNG BÙNG NỔ TẠI ĐIỂM MUA
    ax.add_patch(patches.Rectangle((69, 28), 2.5, 12, facecolor="#00E5FF", edgecolor="#26E7A6", linewidth=1))
    ax.text(70.2, 41, "VOL LON", color="#00E5FF", fontsize=8.5, fontweight='bold', ha='center')

    ax.add_patch(patches.Rectangle((73.5, 28), 1.5, 6, facecolor="#089981"))
    ax.add_patch(patches.Rectangle((77.5, 28), 1.5, 5, facecolor="#089981"))
    ax.add_patch(patches.Rectangle((81.5, 28), 1.5, 4, facecolor="#089981"))

    # Kết luận chân thẻ phải
    ftr_right = patches.FancyBboxPatch((54, 13), 40, 10, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#0A241C", edgecolor="#26E7A6", linewidth=1.2)
    ax.add_patch(ftr_right)
    ax.text(74, 19.5, "Bat tron 100% than song ngay khi nen vuot can kem Volume.", color="#26E7A6", fontsize=10.5, ha='center', va='center')
    ax.text(74, 15.5, "Cat lo sieu ngan (0.5%) * Ty le R:R dinh cao tu 1:3 den 1:6+.", color="#00E5FF", fontsize=11, fontweight='bold', ha='center', va='center')

    add_watermark(ax)
    out_path = os.path.join(ASSETS_DIR, "naked_chart_indicator_trap.png")
    plt.savefig(out_path, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Rendered: {out_path}")

# ==============================================================================
# HÌNH 1.2: KHÔNG GIAN BÀN LÀM VIỆC NAKED CHART PRO DESK
# ==============================================================================
def render_clean_workspace():
    fig, ax = setup_figure()
    
    # Tiêu đề
    title_box = patches.FancyBboxPatch((10, 91), 80, 6.5, boxstyle="round,pad=0.8,rounding_size=2", facecolor="#141824", edgecolor="#00E5FF", linewidth=1.8)
    ax.add_patch(title_box)
    ax.text(50, 94.2, "BAN LAM VIEC BIEU DO TRAN: 3 THANH PHAN COT LOI", color="#FFFFFF", fontsize=16, fontweight='bold', ha='center', va='center')

    # Khung Terminal
    term_box = patches.FancyBboxPatch((6, 12), 88, 76, boxstyle="round,pad=1,rounding_size=2", facecolor="#101520", edgecolor="#00E5FF", linewidth=2)
    ax.add_patch(term_box)

    # 1. VÙNG CUNG (SUPPLY ZONE) TRÊN ĐỈNH
    supply_box = patches.FancyBboxPatch((10, 70), 80, 10, boxstyle="round,pad=0.5,rounding_size=1", facecolor="#2A0B12", edgecolor="#F23645", linewidth=1.5, linestyle='--')
    ax.add_patch(supply_box)
    ax.text(14, 75, "[!] VUNG CUNG (SUPPLY ZONE) - Noi ca map xa hang chan gia", color="#FF707E", fontsize=12, fontweight='bold', va='center')

    # 2. KHU VỰC NẾN GIÁ CHẠY Ở GIỮA
    candles = [
        (16, 32, 8, "#089981"),
        (22, 36, 10, "#089981"),
        (28, 42, 8, "#F23645"),
        (34, 46, 12, "#089981"),
        (42, 54, 15, "#089981"),  # Breakout
        (50, 62, 10, "#089981"),
        (58, 68, 8, "#089981"),
        (66, 70, 6, "#F23645"),   # Rejection Pin bar
        (74, 62, 12, "#F23645"),
        (82, 52, 14, "#F23645")
    ]
    for x, y, h, c in candles:
        ax.plot([x, x], [y-3, y+h+3], color=c, linewidth=2)
        ax.add_patch(patches.Rectangle((x-1.5, y), 3, h, facecolor=c))

    # Nhãn nến OHLC
    ax.text(42, 49, "NEN GIA OHLC", color="#00E5FF", fontsize=11, fontweight='bold', ha='center')
    ax.text(66, 79, "Tu Choi Vung Cung (Pin Bar)", color="#FF5252", fontsize=11, fontweight='bold', ha='center')

    # 3. VÙNG CẦU (DEMAND ZONE) DƯỚI ĐÁY
    demand_box = patches.FancyBboxPatch((10, 24), 80, 10, boxstyle="round,pad=0.5,rounding_size=1", facecolor="#08281E", edgecolor="#089981", linewidth=1.5, linestyle='--')
    ax.add_patch(demand_box)
    ax.text(14, 29, "[*] VUNG CAU (DEMAND ZONE) - Noi ca map gom hang chan song", color="#26E7A6", fontsize=12, fontweight='bold', va='center')

    # 4. KHỐI LƯỢNG VSA Ở DƯỚI CÙNG
    ax.plot([10, 90], [21, 21], color="#1C2D44", linewidth=1.5)
    ax.text(12, 17, ">> COT KHOI LUONG VSA:", color="#F0B90B", fontsize=11, fontweight='bold')
    
    vol_bars = [(16, 4, "#089981"), (22, 5, "#089981"), (28, 3, "#F23645"), (34, 6, "#089981"), 
                (42, 9, "#00E5FF"), (50, 6, "#089981"), (58, 5, "#089981"), (66, 8, "#F23645"),
                (74, 6, "#F23645"), (82, 7, "#F23645")]
    for x, vh, c in vol_bars:
        ax.add_patch(patches.Rectangle((x-1, 13), 2, vh, facecolor=c))

    add_watermark(ax)
    out_path = os.path.join(ASSETS_DIR, "naked_chart_clean_workspace.png")
    plt.savefig(out_path, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Rendered: {out_path}")

# ==============================================================================
# HÌNH 1.3: 3 BƯỚC THIẾT LẬP TRADINGVIEW
# ==============================================================================
def render_setup_3_steps():
    fig, ax = setup_figure()
    
    # Tiêu đề
    title_box = patches.FancyBboxPatch((10, 91), 80, 6.5, boxstyle="round,pad=0.8,rounding_size=2", facecolor="#141824", edgecolor="#2962FF", linewidth=1.8)
    ax.add_patch(title_box)
    ax.text(50, 94.2, "3 BUOC THIET LAP BIEU DO TRAN CHUAN MUC TREN TRADINGVIEW", color="#FFFFFF", fontsize=16, fontweight='bold', ha='center', va='center')

    # BƯỚC 1
    c1 = patches.FancyBboxPatch((4, 10), 29, 78, boxstyle="round,pad=1,rounding_size=1.5", facecolor="#101520", edgecolor="#FF5252", linewidth=2)
    ax.add_patch(c1)
    ax.add_patch(patches.Circle((18.5, 75), 6, facecolor="#280A10", edgecolor="#FF5252", linewidth=2))
    ax.text(18.5, 75, "01", color="#FF5252", fontsize=16, fontweight='bold', ha='center', va='center')
    ax.text(18.5, 63, "XOA SACH CHI BAO", color="#FFFFFF", fontsize=13, fontweight='bold', ha='center')
    ax.text(18.5, 59, "(Remove All Indicators)", color="#FFA4AC", fontsize=10.5, ha='center')
    
    # Mô phỏng menu
    ax.add_patch(patches.FancyBboxPatch((7, 32), 23, 20, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#080C14", edgecolor="#32141C", linewidth=1))
    ax.text(18.5, 45, "Nhap chuot phai -> Chon:", color="#CAD4E0", fontsize=10, ha='center')
    ax.add_patch(patches.FancyBboxPatch((8, 35), 21, 6, boxstyle="round,pad=0.2,rounding_size=0.5", facecolor="#FF5252"))
    ax.text(18.5, 38, "[X] Remove Indicators", color="#FFFFFF", fontsize=10.5, fontweight='bold', ha='center', va='center')
    
    ax.text(18.5, 18, "Giai phong 100% tam mat de nhin thang vao hanh dong gia.", color="#CAD4E0", fontsize=10, ha='center', wrap=True)

    # BƯỚC 2
    c2 = patches.FancyBboxPatch((35.5, 10), 29, 78, boxstyle="round,pad=1,rounding_size=1.5", facecolor="#101520", edgecolor="#00E5FF", linewidth=2)
    ax.add_patch(c2)
    ax.add_patch(patches.Circle((50, 75), 6, facecolor="#08202E", edgecolor="#00E5FF", linewidth=2))
    ax.text(50, 75, "02", color="#00E5FF", fontsize=16, fontweight='bold', ha='center', va='center')
    ax.text(50, 63, "CAI NEN TOI DARK THEME", color="#FFFFFF", fontsize=13, fontweight='bold', ha='center')
    ax.text(50, 59, "(Chong moi mat & Tang tuong phan)", color="#00E5FF", fontsize=10, ha='center')

    # Ô màu
    ax.add_patch(patches.FancyBboxPatch((38.5, 32), 23, 20, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#080C14", edgecolor="#162E44", linewidth=1))
    ax.add_patch(patches.Rectangle((40, 42), 9, 6, facecolor="#0B0E14", edgecolor="#00E5FF", linewidth=1))
    ax.text(44.5, 45, "Nen Den", color="#00E5FF", fontsize=8.5, fontweight='bold', ha='center', va='center')
    ax.add_patch(patches.Rectangle((51, 42), 9, 6, facecolor="#089981"))
    ax.text(55.5, 45, "Nen Xanh", color="#FFFFFF", fontsize=8.5, fontweight='bold', ha='center', va='center')
    ax.add_patch(patches.Rectangle((45.5, 34), 9, 6, facecolor="#F23645"))
    ax.text(50, 37, "Nen Do", color="#FFFFFF", fontsize=8.5, fontweight='bold', ha='center', va='center')

    ax.text(50, 18, "Toi uu thi giac de nhan dien ro tung bac nen va rau nen.", color="#CAD4E0", fontsize=10, ha='center')

    # BƯỚC 3
    c3 = patches.FancyBboxPatch((67, 10), 29, 78, boxstyle="round,pad=1,rounding_size=1.5", facecolor="#101520", edgecolor="#F0B90B", linewidth=2)
    ax.add_patch(c3)
    ax.add_patch(patches.Circle((81.5, 75), 6, facecolor="#281F0A", edgecolor="#F0B90B", linewidth=2))
    ax.text(81.5, 75, "03", color="#F0B90B", fontsize=16, fontweight='bold', ha='center', va='center')
    ax.text(81.5, 63, "BAT DUY NHAT VOLUME", color="#FFFFFF", fontsize=13, fontweight='bold', ha='center')
    ax.text(81.5, 59, "(Khoi Luong Khop Lenh)", color="#F0B90B", fontsize=10.5, ha='center')

    # Cột Volume
    ax.add_patch(patches.FancyBboxPatch((70, 32), 23, 20, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#080C14", edgecolor="#342810", linewidth=1))
    vols = [(73, 4, "#089981"), (76, 7, "#089981"), (79, 3, "#F23645"), (82, 11, "#00E5FF"), (86, 6, "#089981")]
    for x, vh, c in vols:
        ax.add_patch(patches.Rectangle((x, 34), 2, vh, facecolor=c))

    ax.text(81.5, 18, "Chi bao duy nhat do luong no luc tien that cua ca map.", color="#CAD4E0", fontsize=10, ha='center')

    add_watermark(ax)
    out_path = os.path.join(ASSETS_DIR, "naked_chart_setup_3_steps.png")
    plt.savefig(out_path, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Rendered: {out_path}")

# ==============================================================================
# HÌNH 1.4: BÓC TÁCH CẤU TRÚC NẾN 3D
# ==============================================================================
def render_candlestick_structure():
    fig, ax = setup_figure()
    
    # 1. Header Title
    title_box = patches.FancyBboxPatch(
        (10, 91), 80, 6.5,
        boxstyle="round,pad=0.8,rounding_size=2",
        facecolor="#141824",
        edgecolor="#2962FF",
        linewidth=1.8
    )
    ax.add_patch(title_box)
    ax.text(50, 94.2, "BOC TACH 3 BO PHAN COT LOI CUA CAY NEN TRAN", 
            color="#FFFFFF", fontsize=18, fontweight='bold', ha='center', va='center')

    # 2. KHUNG TRÁI: NẾN TĂNG MẠNH (BULLISH MOMENTUM)
    card_left = patches.FancyBboxPatch(
        (4, 10), 44, 78,
        boxstyle="round,pad=1,rounding_size=2",
        facecolor="#101520",
        edgecolor="#089981",
        linewidth=2
    )
    ax.add_patch(card_left)
    
    hdr_left = patches.FancyBboxPatch(
        (4, 81), 44, 7,
        boxstyle="round,pad=0.5,rounding_size=1",
        facecolor="#082A20",
        edgecolor="#089981",
        linewidth=1.2
    )
    ax.add_patch(hdr_left)
    ax.text(26, 84.5, "1. NEN TANG MANH (BULLISH)", 
            color="#26E7A6", fontsize=14, fontweight='bold', ha='center', va='center')

    # Vẽ Nến Tăng Xanh Ngọc
    # Râu trên
    ax.plot([16, 16], [68, 77], color="#00E5FF", linewidth=5, solid_capstyle='round')
    ax.plot([16], [77], marker='o', markersize=9, color="#F0B90B")
    
    # Thân nến xanh
    candle_bull = patches.FancyBboxPatch(
        (12, 32), 8, 36,
        boxstyle="round,pad=0.2,rounding_size=0.8",
        facecolor="#089981",
        edgecolor="#26E7A6",
        linewidth=2.5
    )
    ax.add_patch(candle_bull)
    
    # Râu dưới
    ax.plot([16, 16], [24, 32], color="#00E5FF", linewidth=5, solid_capstyle='round')
    ax.plot([16], [24], marker='o', markersize=9, color="#8E9BAE")

    # Các nhãn chỉ dẫn bên phải Nến Tăng
    ax.plot([16, 25], [77, 77], color="#F0B90B", linewidth=1.5, linestyle='--')
    ax.text(26, 77, "Gia Cao Nhat (High)", color="#F0B90B", fontsize=11.5, fontweight='bold', va='center')

    ax.plot([20, 25], [68, 68], color="#00E5FF", linewidth=2)
    close_tag = patches.FancyBboxPatch((25, 65.5), 20, 5, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#08282E", edgecolor="#00E5FF", linewidth=1.2)
    ax.add_patch(close_tag)
    ax.text(35, 68, "DONG CUA (CLOSE)", color="#00E5FF", fontsize=11, fontweight='bold', ha='center', va='center')

    ax.plot([20, 25], [50, 50], color="#26E7A6", linewidth=2)
    ax.text(26, 51.5, "THAN NEN DAI (SPREAD)", color="#26E7A6", fontsize=12, fontweight='bold', va='center')
    ax.text(26, 47.5, "= Phe Mua ap dao toan dien", color="#CAD4E0", fontsize=10.5, va='center')

    ax.plot([20, 25], [32, 32], color="#8E9BAE", linewidth=1.5, linestyle='--')
    ax.text(26, 32, "Gia Mo Cua (Open)", color="#CAD4E0", fontsize=11, va='center')

    ax.plot([16, 25], [24, 24], color="#8E9BAE", linewidth=1.5, linestyle='--')
    ax.text(26, 24, "Gia Thap Nhat (Low)", color="#8E9BAE", fontsize=11, va='center')

    # Kết luận chân thẻ trái
    ftr_left = patches.FancyBboxPatch((6, 13), 40, 6, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#082018", edgecolor="#089981", linewidth=1.2)
    ax.add_patch(ftr_left)
    ax.text(26, 16, "-> KET LUAN: DA TANG DANG RAT MANH", color="#26E7A6", fontsize=11.5, fontweight='bold', ha='center', va='center')

    # 3. KHUNG PHẢI: NẾN PIN BAR TỪ CHỐI GIÁ
    card_right = patches.FancyBboxPatch(
        (52, 10), 44, 78,
        boxstyle="round,pad=1,rounding_size=2",
        facecolor="#101520",
        edgecolor="#F23645",
        linewidth=2
    )
    ax.add_patch(card_right)
    
    hdr_right = patches.FancyBboxPatch(
        (52, 81), 44, 7,
        boxstyle="round,pad=0.5,rounding_size=1",
        facecolor="#2A0C12",
        edgecolor="#F23645",
        linewidth=1.2
    )
    ax.add_patch(hdr_right)
    ax.text(74, 84.5, "2. NEN PIN BAR TU CHOI (BEARISH)", 
            color="#FFA4AC", fontsize=14, fontweight='bold', ha='center', va='center')

    # Vẽ Nến Đỏ Pin Bar (Râu Trên Dài Ngoằng Đỏ Rực)
    ax.plot([64, 64], [44, 77], color="#FF5252", linewidth=6, solid_capstyle='round')
    ax.plot([64], [77], marker='o', markersize=10, color="#FF5252")
    
    # Thân nến đỏ nhỏ sát đáy
    candle_bear = patches.FancyBboxPatch(
        (60, 32), 8, 12,
        boxstyle="round,pad=0.2,rounding_size=0.8",
        facecolor="#F23645",
        edgecolor="#FF8A95",
        linewidth=2.5
    )
    ax.add_patch(candle_bear)
    
    # Râu dưới
    ax.plot([64, 64], [24, 32], color="#FF5252", linewidth=5, solid_capstyle='round')
    ax.plot([64], [24], marker='o', markersize=8, color="#FFA4AC")

    # Các nhãn chỉ dẫn bên phải Nến Đỏ
    ax.plot([64, 73], [60, 60], color="#FF5252", linewidth=2)
    wick_tag = patches.FancyBboxPatch((73, 54), 21, 10, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#2A0B12", edgecolor="#FF5252", linewidth=1.5)
    ax.add_patch(wick_tag)
    ax.text(83.5, 60.5, "RAU TREN DAI NGOANG", color="#FF5252", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.text(83.5, 56.5, "= Tu choi gia & Bay ca map", color="#FFA4AC", fontsize=9.5, ha='center', va='center')

    ax.plot([68, 73], [44, 44], color="#CAD4E0", linewidth=1.5, linestyle='--')
    ax.text(74, 44, "Gia Mo Cua (Open)", color="#CAD4E0", fontsize=11, va='center')

    ax.plot([68, 73], [32, 32], color="#FF5252", linewidth=2)
    close_bear_tag = patches.FancyBboxPatch((73, 29.5), 21, 5, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#2A0B12", edgecolor="#FF5252", linewidth=1.2)
    ax.add_patch(close_bear_tag)
    ax.text(83.5, 32, "DONG CUA O DAY", color="#FF707E", fontsize=11, fontweight='bold', ha='center', va='center')

    ax.plot([64, 73], [24, 24], color="#FFA4AC", linewidth=1.5, linestyle='--')
    ax.text(74, 24, "Gia Thap Nhat (Low)", color="#FFA4AC", fontsize=11, va='center')

    # Kết luận chân thẻ phải
    ftr_right = patches.FancyBboxPatch((54, 13), 40, 6, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#220A10", edgecolor="#F23645", linewidth=1.2)
    ax.add_patch(ftr_right)
    ax.text(74, 16, "-> KET LUAN: BAO HIEU DAO CHIEU GIAM", color="#FF707E", fontsize=11.5, fontweight='bold', ha='center', va='center')

    add_watermark(ax)
    out_path = os.path.join(ASSETS_DIR, "naked_candlestick_structure.png")
    plt.savefig(out_path, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Rendered: {out_path}")

# ==============================================================================
# HÌNH 1.5: MA TRẬN NỖ LỰC VS KẾT QUẢ (VSA MATRIX)
# ==============================================================================
def render_vsa_effort_result():
    fig, ax = setup_figure()
    
    # Header Title
    title_box = patches.FancyBboxPatch(
        (10, 91), 80, 6.5,
        boxstyle="round,pad=0.8,rounding_size=2",
        facecolor="#141824",
        edgecolor="#F0B90B",
        linewidth=1.8
    )
    ax.add_patch(title_box)
    ax.text(50, 94.2, "QUY LUAT NO LUC & KET QUA: NEN (KET QUA) vs VOLUME (NO LUC)", 
            color="#FFFFFF", fontsize=16, fontweight='bold', ha='center', va='center')

    # 3 CỘT SO SÁNH
    # ------------------ CỘT 1: ĐỒNG THUẬN ------------------
    c1 = patches.FancyBboxPatch((4, 10), 29, 78, boxstyle="round,pad=1,rounding_size=1.5", facecolor="#101520", edgecolor="#089981", linewidth=2)
    ax.add_patch(c1)
    
    hdr1 = patches.FancyBboxPatch((4, 81), 29, 7, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#082A20", edgecolor="#089981", linewidth=1.2)
    ax.add_patch(hdr1)
    ax.text(18.5, 84.5, "1. DONG THUAN", color="#26E7A6", fontsize=13, fontweight='bold', ha='center', va='center')

    ax.text(18.5, 76, "KET QUA: THAN DAI", color="#26E7A6", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.plot([18.5, 18.5], [52, 72], color="#00E5FF", linewidth=3)
    ax.add_patch(patches.FancyBboxPatch((15.5, 55), 6, 14, boxstyle="round,pad=0.1,rounding_size=0.5", facecolor="#089981", edgecolor="#26E7A6", linewidth=2))

    ax.plot([7, 30], [48, 48], color="#223048", linewidth=1.5, linestyle=':')

    ax.text(18.5, 43, "NO LUC: VOL CAO VOT", color="#00E5FF", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.add_patch(patches.Rectangle((15.5, 23), 6, 16, facecolor="#00E5FF", edgecolor="#26E7A6", linewidth=1.5))

    ftr1 = patches.FancyBboxPatch((6, 13), 25, 6, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#08281E", edgecolor="#26E7A6", linewidth=1.2)
    ax.add_patch(ftr1)
    ax.text(18.5, 16, "[V] TU TIN THEO TREND", color="#26E7A6", fontsize=11, fontweight='bold', ha='center', va='center')

    # ------------------ CỘT 2: BẤT THƯỜNG / HẤP THỤ ------------------
    c2 = patches.FancyBboxPatch((35.5, 10), 29, 78, boxstyle="round,pad=1,rounding_size=1.5", facecolor="#101520", edgecolor="#F23645", linewidth=2)
    ax.add_patch(c2)
    
    hdr2 = patches.FancyBboxPatch((35.5, 81), 29, 7, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#2A0C12", edgecolor="#F23645", linewidth=1.2)
    ax.add_patch(hdr2)
    ax.text(50, 84.5, "2. BAT THUONG (HAP THU)", color="#FFA4AC", fontsize=13, fontweight='bold', ha='center', va='center')

    ax.text(50, 76, "KET QUA: THAN BE TI", color="#FF707E", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.plot([50, 50], [52, 72], color="#FF5252", linewidth=3)
    ax.add_patch(patches.FancyBboxPatch((47, 58), 6, 5, boxstyle="round,pad=0.1,rounding_size=0.5", facecolor="#F23645", edgecolor="#FF8A95", linewidth=2))

    ax.plot([38.5, 61.5], [48, 48], color="#223048", linewidth=1.5, linestyle=':')

    ax.text(50, 43, "NO LUC: VOL CUC DAI", color="#FF5252", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.add_patch(patches.Rectangle((47, 23), 6, 17, facecolor="#F23645", edgecolor="#FF7A85", linewidth=1.5))

    ftr2 = patches.FancyBboxPatch((37.5, 13), 25, 6, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#2E0A12", edgecolor="#FF5252", linewidth=1.2)
    ax.add_patch(ftr2)
    ax.text(50, 16, "[!] CANH BAO DAO CHIEU!", color="#FF707E", fontsize=11, fontweight='bold', ha='center', va='center')

    # ------------------ CỘT 3: THIẾU HỤT NỖ LỰC ------------------
    c3 = patches.FancyBboxPatch((67, 10), 29, 78, boxstyle="round,pad=1,rounding_size=1.5", facecolor="#101520", edgecolor="#F0B90B", linewidth=2)
    ax.add_patch(c3)
    
    hdr3 = patches.FancyBboxPatch((67, 81), 29, 7, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#281F0A", edgecolor="#F0B90B", linewidth=1.2)
    ax.add_patch(hdr3)
    ax.text(81.5, 84.5, "3. THIEU HUT NO LUC", color="#F0B90B", fontsize=13, fontweight='bold', ha='center', va='center')

    ax.text(81.5, 76, "KET QUA: GIA TANG RUON", color="#F0B90B", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.plot([81.5, 81.5], [52, 72], color="#CAD4E0", linewidth=2)
    ax.add_patch(patches.FancyBboxPatch((78.5, 55), 6, 12, boxstyle="round,pad=0.1,rounding_size=0.5", facecolor="#089981", edgecolor="#26E7A6", linewidth=1.5))

    ax.plot([70, 93], [48, 48], color="#223048", linewidth=1.5, linestyle=':')

    ax.text(81.5, 43, "NO LUC: VOL TEO TOP", color="#8E9BAE", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.add_patch(patches.Rectangle((79.5, 23), 4, 5, facecolor="#687C94", edgecolor="#8E9BAE", linewidth=1))

    ftr3 = patches.FancyBboxPatch((69, 13), 25, 6, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#281F0A", edgecolor="#F0B90B", linewidth=1.2)
    ax.add_patch(ftr3)
    ax.text(81.5, 16, "[X] KHONG MUA DUOI", color="#F0B90B", fontsize=11, fontweight='bold', ha='center', va='center')

    add_watermark(ax)
    out_path = os.path.join(ASSETS_DIR, "naked_vsa_effort_result.png")
    plt.savefig(out_path, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Rendered: {out_path}")

# ==============================================================================
# HÌNH BÀI 2: CẤU TRÚC THỊ TRƯỜNG BOS, CHOCH & FLIP ZONE
# ==============================================================================
def render_market_structure():
    fig, ax = setup_figure()
    
    # Tiêu đề
    title_box = patches.FancyBboxPatch((10, 91), 80, 6.5, boxstyle="round,pad=0.8,rounding_size=2", facecolor="#141824", edgecolor="#00E5FF", linewidth=1.8)
    ax.add_patch(title_box)
    ax.text(50, 94.2, "BAN DO CAU TRUC THI TRUONG: BOS * CHoCH * FLIP ZONE", color="#FFFFFF", fontsize=16, fontweight='bold', ha='center', va='center')

    # Khung sơ đồ
    card = patches.FancyBboxPatch((4, 10), 92, 78, boxstyle="round,pad=1,rounding_size=2", facecolor="#101520", edgecolor="#1C2D44", linewidth=2)
    ax.add_patch(card)

    # VÙNG FLIP ZONE (CẢN ĐỔI THÀNH HỖ TRỢ)
    flip_band = patches.FancyBboxPatch((20, 48), 70, 7, boxstyle="round,pad=0.3,rounding_size=0.5", facecolor="#281F0A", edgecolor="#F0B90B", linewidth=1.5, linestyle='--')
    ax.add_patch(flip_band)
    ax.text(88, 51.5, "FLIP ZONE (CAN CHUYEN HO TRO)", color="#F0B90B", fontsize=10.5, fontweight='bold', ha='right', va='center')

    # ĐƯỜNG SÓNG ZICZAC CẤU TRÚC NGUYÊN BẢN
    # 1. Sóng tăng Uptrend (Xanh)
    ax.plot([8, 20], [30, 52], color="#089981", linewidth=4.5, solid_capstyle='round')    # Low -> High
    ax.plot([20, 28], [52, 40], color="#CAD4E0", linewidth=3.5, solid_capstyle='round')   # High -> HL1
    ax.plot([28, 44], [40, 68], color="#089981", linewidth=4.5, solid_capstyle='round')   # HL1 -> HH1 (BOS1)
    ax.plot([44, 54], [68, 52], color="#CAD4E0", linewidth=3.5, solid_capstyle='round')   # Retest Flip Zone -> HL2
    ax.plot([54, 68], [52, 82], color="#089981", linewidth=4.5, solid_capstyle='round')   # HL2 -> Peak HH2 (BOS2)

    # BOS 1 Callout
    ax.plot([20, 40], [52, 52], color="#00E5FF", linewidth=1.5, linestyle=':')
    ax.text(32, 55, "BOS 1 [V]", color="#00E5FF", fontsize=10, fontweight='bold')

    # BOS 2 Callout
    ax.plot([44, 64], [68, 68], color="#00E5FF", linewidth=1.5, linestyle=':')
    ax.text(56, 71, "BOS 2 [V]", color="#00E5FF", fontsize=10, fontweight='bold')

    # 2. Sóng gãy CHoCH (Đỏ)
    ax.plot([68, 78], [82, 42], color="#F23645", linewidth=5, solid_capstyle='round')     # Peak -> Break HL2 (CHoCH)
    
    # CHoCH Line qua HL2
    ax.plot([54, 80], [52, 52], color="#FF5252", linewidth=2, linestyle='--')
    choch_tag = patches.FancyBboxPatch((66, 44), 20, 5.5, boxstyle="round,pad=0.2,rounding_size=0.5", facecolor="#2E0A12", edgecolor="#FF5252", linewidth=1.2)
    ax.add_patch(choch_tag)
    ax.text(76, 46.8, "[!] CHoCH (GAY DAY)", color="#FF5252", fontsize=9.5, fontweight='bold', ha='center', va='center')

    # 3. Sóng Downtrend hồi về Flip Zone rồi sập
    ax.plot([78, 86], [42, 52], color="#CAD4E0", linewidth=3.5, solid_capstyle='round')   # Retest cản mới
    ax.plot([86, 94], [52, 25], color="#F23645", linewidth=5, solid_capstyle='round')     # Dump LL

    # Điểm bắn tỉa Short tại cản mới
    ax.plot([86], [52], marker='o', markersize=10, color="#F0B90B")
    ax.text(86, 57, ">> SHORT ENTRY <<", color="#F0B90B", fontsize=10, fontweight='bold', ha='center')

    # Điểm đánh dấu các mốc
    ax.plot([8], [30], marker='o', markersize=8, color="#089981")
    ax.text(8, 26, "Low", color="#089981", fontsize=11, fontweight='bold', ha='center')

    ax.plot([28], [40], marker='o', markersize=8, color="#26E7A6")
    ax.text(28, 36, "HL 1", color="#26E7A6", fontsize=11, fontweight='bold', ha='center')

    ax.plot([54], [52], marker='o', markersize=9, color="#00E5FF")
    ax.text(54, 47, "HL 2 (Moc Then Chot)", color="#00E5FF", fontsize=10.5, fontweight='bold', ha='center')

    ax.plot([68], [82], marker='o', markersize=11, color="#F0B90B")
    ax.text(68, 85.5, "** DINH CHU KY **", color="#F0B90B", fontsize=12, fontweight='bold', ha='center')

    # Tóm tắt chân thẻ
    ftr = patches.FancyBboxPatch((10, 13), 80, 8, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#081422", edgecolor="#00E5FF", linewidth=1.2)
    ax.add_patch(ftr)
    ax.text(50, 17, "Uptrend = Chuoi Dinh Cao Hon (HH) & Day Cao Hon (HL) * Dao Chieu Khi Day HL Then Chot Bi Gay (CHoCH)", 
            color="#CAD4E0", fontsize=11, fontweight='bold', ha='center', va='center')

    add_watermark(ax)
    out_path = os.path.join(ASSETS_DIR, "market_structure_bos_choch.png")
    plt.savefig(out_path, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Rendered: {out_path}")

if __name__ == '__main__':
    render_indicator_trap()
    render_clean_workspace()
    render_setup_3_steps()
    render_candlestick_structure()
    render_vsa_effort_result()
    render_market_structure()
    print("ALL PRO CHARTS RENDERED AT ULTRA HD SUCCESSFULLY!")
