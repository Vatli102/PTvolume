# -*- coding: utf-8 -*-
"""
Bộ công cụ tạo hình ảnh đồ họa tài chính chất lượng cao (Pro Financial Graphics Engine)
Sử dụng Matplotlib + Pillow để tạo hình ảnh Full HD siêu trực quan, sắc nét, cuốn hút,
chuẩn nhận diện thương hiệu PTvolume.com.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = r"d:\PHAN DUA CẤM XÓA\AI_Agent_Trading\assets\images"
os.makedirs(ASSETS_DIR, exist_ok=True)

def setup_figure(w=16, h=9, bg_color="#0B0E14"):
    """Tạo canvas chuẩn 16:9 chất lượng cao"""
    fig, ax = plt.subplots(figsize=(w, h), dpi=120)
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    return fig, ax

def add_watermark(ax):
    """Đóng dấu nhận diện thương hiệu PTvolume.com"""
    # Watermark badge
    badge = patches.FancyBboxPatch(
        (35, 2), 30, 4,
        boxstyle="round,pad=0.5,rounding_size=1.5",
        facecolor="#141822",
        edgecolor="#00E5FF",
        linewidth=1.2,
        alpha=0.9
    )
    ax.add_patch(badge)
    ax.text(50, 4, "PTvolume.com • Naked Price Action & VSA Pro", 
            color="#CAD4E0", fontsize=11, fontweight='bold', ha='center', va='center')

# ==============================================================================
# HÌNH 1.4: BÓC TÁCH CẤU TRÚC NẾN 3D (CỰC KỲ TRỰC QUAN & CUỐN HÚT)
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
    ax.text(50, 94.2, "BÓC TÁCH 3 BỘ PHẬN CỐT LÕI CỦA CÂY NẾN TRẦN", 
            color="#FFFFFF", fontsize=18, fontweight='black', ha='center', va='center')

    # 2. KHUNG TRÁI: NẾN TĂNG MẠNH (BULLISH MOMENTUM)
    card_left = patches.FancyBboxPatch(
        (4, 10), 44, 78,
        boxstyle="round,pad=1,rounding_size=2",
        facecolor="#101520",
        edgecolor="#089981",
        linewidth=2
    )
    ax.add_patch(card_left)
    
    # Header Card Trái
    hdr_left = patches.FancyBboxPatch(
        (4, 81), 44, 7,
        boxstyle="round,pad=0.5,rounding_size=1",
        facecolor="#082A20",
        edgecolor="#089981",
        linewidth=1.2
    )
    ax.add_patch(hdr_left)
    ax.text(26, 84.5, "1. NẾN TĂNG MẠNH (BULLISH)", 
            color="#26E7A6", fontsize=14, fontweight='bold', ha='center', va='center')

    # Vẽ Nến Tăng Xanh Ngọc (Khổng Lồ, Sắc Nét)
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
    # Giá cao nhất
    ax.plot([16, 25], [77, 77], color="#F0B90B", linewidth=1.5, linestyle='--')
    ax.text(26, 77, "Giá Cao Nhất (High)", color="#F0B90B", fontsize=11.5, fontweight='bold', va='center')

    # Giá đóng cửa
    ax.plot([20, 25], [68, 68], color="#00E5FF", linewidth=2)
    close_tag = patches.FancyBboxPatch((25, 65.5), 20, 5, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#08282E", edgecolor="#00E5FF", linewidth=1.2)
    ax.add_patch(close_tag)
    ax.text(35, 68, "ĐÓNG CỬA (CLOSE)", color="#00E5FF", fontsize=11, fontweight='black', ha='center', va='center')

    # Thân nến (Spread)
    ax.plot([20, 25], [50, 50], color="#26E7A6", linewidth=2)
    ax.text(26, 51.5, "THÂN NẾN DÀI (SPREAD)", color="#26E7A6", fontsize=12, fontweight='black', va='center')
    ax.text(26, 47.5, "= Phe Mua áp đảo toàn diện", color="#CAD4E0", fontsize=10.5, va='center')

    # Giá mở cửa
    ax.plot([20, 25], [32, 32], color="#8E9BAE", linewidth=1.5, linestyle='--')
    ax.text(26, 32, "Giá Mở Cửa (Open)", color="#CAD4E0", fontsize=11, va='center')

    # Giá thấp nhất
    ax.plot([16, 25], [24, 24], color="#8E9BAE", linewidth=1.5, linestyle='--')
    ax.text(26, 24, "Giá Thấp Nhất (Low)", color="#8E9BAE", fontsize=11, va='center')

    # Kết luận chân thẻ trái
    ftr_left = patches.FancyBboxPatch((6, 13), 40, 6, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#082018", edgecolor="#089981", linewidth=1.2)
    ax.add_patch(ftr_left)
    ax.text(26, 16, "➔ KẾT LUẬN: ĐÀ TĂNG ĐANG RẤT MẠNH", color="#26E7A6", fontsize=11.5, fontweight='bold', ha='center', va='center')


    # 3. KHUNG PHẢI: NẾN PIN BAR TỪ CHỐI GIÁ (BEARISH REJECTION)
    card_right = patches.FancyBboxPatch(
        (52, 10), 44, 78,
        boxstyle="round,pad=1,rounding_size=2",
        facecolor="#101520",
        edgecolor="#F23645",
        linewidth=2
    )
    ax.add_patch(card_right)
    
    # Header Card Phải
    hdr_right = patches.FancyBboxPatch(
        (52, 81), 44, 7,
        boxstyle="round,pad=0.5,rounding_size=1",
        facecolor="#2A0C12",
        edgecolor="#F23645",
        linewidth=1.2
    )
    ax.add_patch(hdr_right)
    ax.text(74, 84.5, "2. NẾN PIN BAR TỪ CHỐI (BEARISH)", 
            color="#FFA4AC", fontsize=14, fontweight='bold', ha='center', va='center')

    # Vẽ Nến Đỏ Pin Bar (Râu Trên Dài Ngoằng Đỏ Rực)
    # Râu trên dài (70% chiều dài)
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
    # Râu trên dài
    ax.plot([64, 73], [60, 60], color="#FF5252", linewidth=2)
    wick_tag = patches.FancyBboxPatch((73, 54), 21, 10, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#2A0B12", edgecolor="#FF5252", linewidth=1.5)
    ax.add_patch(wick_tag)
    ax.text(83.5, 60.5, "RÂU TRÊN DÀI NGOẰNG", color="#FF5252", fontsize=11, fontweight='black', ha='center', va='center')
    ax.text(83.5, 56.5, "= Từ chối giá & Bẫy cá mập", color="#FFA4AC", fontsize=9.5, ha='center', va='center')

    # Giá mở cửa
    ax.plot([68, 73], [44, 44], color="#CAD4E0", linewidth=1.5, linestyle='--')
    ax.text(74, 44, "Giá Mở Cửa (Open)", color="#CAD4E0", fontsize=11, va='center')

    # Giá đóng cửa sát đáy
    ax.plot([68, 73], [32, 32], color="#FF5252", linewidth=2)
    close_bear_tag = patches.FancyBboxPatch((73, 29.5), 21, 5, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#2A0B12", edgecolor="#FF5252", linewidth=1.2)
    ax.add_patch(close_bear_tag)
    ax.text(83.5, 32, "ĐÓNG CỬA Ở ĐÁY", color="#FF707E", fontsize=11, fontweight='black', ha='center', va='center')

    # Giá thấp nhất
    ax.plot([64, 73], [24, 24], color="#FFA4AC", linewidth=1.5, linestyle='--')
    ax.text(74, 24, "Giá Thấp Nhất (Low)", color="#FFA4AC", fontsize=11, va='center')

    # Kết luận chân thẻ phải
    ftr_right = patches.FancyBboxPatch((54, 13), 40, 6, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#220A10", edgecolor="#F23645", linewidth=1.2)
    ax.add_patch(ftr_right)
    ax.text(74, 16, "➔ KẾT LUẬN: BÁO HIỆU ĐẢO CHIỀU GIẢM", color="#FF707E", fontsize=11.5, fontweight='bold', ha='center', va='center')

    add_watermark(ax)
    
    out_path = os.path.join(ASSETS_DIR, "naked_candlestick_structure.png")
    plt.savefig(out_path, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Rendered: {out_path}")

# ==============================================================================
# HÌNH 1.5: MA TRẬN NỖ LỰC VS KẾT QUẢ (VSA MATRIX - CỰC KỲ SÁNG SỦA)
# ==============================================================================
def render_vsa_effort_result():
    fig, ax = setup_figure()
    
    # 1. Header Title
    title_box = patches.FancyBboxPatch(
        (10, 91), 80, 6.5,
        boxstyle="round,pad=0.8,rounding_size=2",
        facecolor="#141824",
        edgecolor="#F0B90B",
        linewidth=1.8
    )
    ax.add_patch(title_box)
    ax.text(50, 94.2, "QUY LUẬT NỖ LỰC & KẾT QUẢ: NẾN (KẾT QUẢ) vs VOLUME (NỖ LỰC)", 
            color="#FFFFFF", fontsize=16, fontweight='black', ha='center', va='center')

    # 3 CỘT SO SÁNH
    # ------------------ CỘT 1: ĐỒNG THUẬN ------------------
    c1 = patches.FancyBboxPatch((4, 10), 29, 78, boxstyle="round,pad=1,rounding_size=1.5", facecolor="#101520", edgecolor="#089981", linewidth=2)
    ax.add_patch(c1)
    
    hdr1 = patches.FancyBboxPatch((4, 81), 29, 7, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#082A20", edgecolor="#089981", linewidth=1.2)
    ax.add_patch(hdr1)
    ax.text(18.5, 84.5, "1. ĐỒNG THUẬN", color="#26E7A6", fontsize=13, fontweight='black', ha='center', va='center')

    # Nến xanh dài ở trên
    ax.text(18.5, 76, "KẾT QUẢ: THÂN DÀI", color="#26E7A6", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.plot([18.5, 18.5], [52, 72], color="#00E5FF", linewidth=3)
    ax.add_patch(patches.FancyBboxPatch((15.5, 55), 6, 14, boxstyle="round,pad=0.1,rounding_size=0.5", facecolor="#089981", edgecolor="#26E7A6", linewidth=2))

    # Đường ngăn cách
    ax.plot([7, 30], [48, 48], color="#223048", linewidth=1.5, linestyle=':')

    # Cột Volume cao vọt ở dưới
    ax.text(18.5, 43, "NỖ LỰC: VOL CAO VỌT", color="#00E5FF", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.add_patch(patches.Rectangle((15.5, 23), 6, 16, facecolor="#00E5FF", edgecolor="#26E7A6", linewidth=1.5))

    # Kết luận cột 1
    ftr1 = patches.FancyBboxPatch((6, 13), 25, 6, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#08281E", edgecolor="#26E7A6", linewidth=1.2)
    ax.add_patch(ftr1)
    ax.text(18.5, 16, "✓ TỰ TIN THEO TREND", color="#26E7A6", fontsize=11, fontweight='black', ha='center', va='center')


    # ------------------ CỘT 2: BẤT THƯỜNG / HẤP THỤ ------------------
    c2 = patches.FancyBboxPatch((35.5, 10), 29, 78, boxstyle="round,pad=1,rounding_size=1.5", facecolor="#101520", edgecolor="#F23645", linewidth=2)
    ax.add_patch(c2)
    
    hdr2 = patches.FancyBboxPatch((35.5, 81), 29, 7, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#2A0C12", edgecolor="#F23645", linewidth=1.2)
    ax.add_patch(hdr2)
    ax.text(50, 84.5, "2. BẤT THƯỜNG (HẤP THỤ)", color="#FFA4AC", fontsize=13, fontweight='black', ha='center', va='center')

    # Nến đỏ ngắn râu dài ở trên
    ax.text(50, 76, "KẾT QUẢ: THÂN BÉ TÍ", color="#FF707E", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.plot([50, 50], [52, 72], color="#FF5252", linewidth=3)
    ax.add_patch(patches.FancyBboxPatch((47, 58), 6, 5, boxstyle="round,pad=0.1,rounding_size=0.5", facecolor="#F23645", edgecolor="#FF8A95", linewidth=2))

    # Đường ngăn cách
    ax.plot([38.5, 61.5], [48, 48], color="#223048", linewidth=1.5, linestyle=':')

    # Cột Volume cực đại ở dưới
    ax.text(50, 43, "NỖ LỰC: VOL CỰC ĐẠI", color="#FF5252", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.add_patch(patches.Rectangle((47, 23), 6, 17, facecolor="#F23645", edgecolor="#FF7A85", linewidth=1.5))

    # Kết luận cột 2
    ftr2 = patches.FancyBboxPatch((37.5, 13), 25, 6, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#2E0A12", edgecolor="#FF5252", linewidth=1.2)
    ax.add_patch(ftr2)
    ax.text(50, 16, "⚠️ CẢNH BÁO ĐẢO CHIỀU!", color="#FF707E", fontsize=11, fontweight='black', ha='center', va='center')


    # ------------------ CỘT 3: THIẾU HỤT NỖ LỰC ------------------
    c3 = patches.FancyBboxPatch((67, 10), 29, 78, boxstyle="round,pad=1,rounding_size=1.5", facecolor="#101520", edgecolor="#F0B90B", linewidth=2)
    ax.add_patch(c3)
    
    hdr3 = patches.FancyBboxPatch((67, 81), 29, 7, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#281F0A", edgecolor="#F0B90B", linewidth=1.2)
    ax.add_patch(hdr3)
    ax.text(81.5, 84.5, "3. THIẾU HỤT NỖ LỰC", color="#F0B90B", fontsize=13, fontweight='black', ha='center', va='center')

    # Nến tăng rướn ở trên
    ax.text(81.5, 76, "KẾT QUẢ: GIÁ TĂNG RƯỚN", color="#F0B90B", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.plot([81.5, 81.5], [52, 72], color="#CAD4E0", linewidth=2)
    ax.add_patch(patches.FancyBboxPatch((78.5, 55), 6, 12, boxstyle="round,pad=0.1,rounding_size=0.5", facecolor="#089981", edgecolor="#26E7A6", linewidth=1.5))

    # Đường ngăn cách
    ax.plot([70, 93], [48, 48], color="#223048", linewidth=1.5, linestyle=':')

    # Cột Volume teo tóp ở dưới
    ax.text(81.5, 43, "NỖ LỰC: VOL TEO TÓP", color="#8E9BAE", fontsize=11, fontweight='bold', ha='center', va='center')
    ax.add_patch(patches.Rectangle((79.5, 23), 4, 5, facecolor="#687C94", edgecolor="#8E9BAE", linewidth=1))

    # Kết luận cột 3
    ftr3 = patches.FancyBboxPatch((69, 13), 25, 6, boxstyle="round,pad=0.3,rounding_size=0.8", facecolor="#281F0A", edgecolor="#F0B90B", linewidth=1.2)
    ax.add_patch(ftr3)
    ax.text(81.5, 16, "❌ KHÔNG MUA ĐUỔI", color="#F0B90B", fontsize=11, fontweight='black', ha='center', va='center')

    add_watermark(ax)
    
    out_path = os.path.join(ASSETS_DIR, "naked_vsa_effort_result.png")
    plt.savefig(out_path, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Rendered: {out_path}")

if __name__ == '__main__':
    render_candlestick_structure()
    render_vsa_effort_result()
