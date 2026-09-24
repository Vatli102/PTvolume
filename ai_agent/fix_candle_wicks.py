# -*- coding: utf-8 -*-
"""
Sửa lỗi râu nến ở Hình 1.4:
- Vẽ râu nến trên và dưới của cả 2 cây nến (Nến Xanh và Nến Đỏ) cực kỳ đậm nét (stroke-width: 6px).
- Nến Đỏ có Râu Trên dài đỏ rực (#FF5252) và Râu Dưới đỏ rõ ràng, có điểm High và Low to tròn.
- Mọi nhãn chú thích đều dóng ra ngoài, không đè lên nến.
"""
import os

SVG_DIR = r"d:\PHAN DUA CẤM XÓA\AI_Agent_Trading\assets\images"

svg_candle_fixed = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%" style="background:#0D111A; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
  <defs>
    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow-red" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="drop-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <!-- NỀN CANVAS -->
  <rect width="1200" height="680" fill="#0D111A" rx="16"/>
  <rect width="1192" height="672" x="4" y="4" fill="none" stroke="#1E2638" stroke-width="2" rx="14"/>

  <!-- TIÊU ĐỀ CHÍNH -->
  <text x="600" y="52" font-size="23" font-weight="900" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.5">
    GIẢI PHẪU HỌC NẾN: <tspan fill="#00E5FF">THÂN NẾN</tspan> • <tspan fill="#F0B90B">RÂU TRÊN</tspan> • <tspan fill="#FF707E">RÂU DƯỚI</tspan> • <tspan fill="#26E7A6">MỨC ĐÓNG CỬA</tspan>
  </text>

  <!-- ==================== CỘT TRÁI: NẾN TĂNG (BULLISH CANDLE) ==================== -->
  <g transform="translate(60, 80)" filter="url(#drop-shadow)">
    <rect width="510" height="540" rx="14" fill="#131824" stroke="#089981" stroke-width="2"/>
    
    <rect x="0" y="0" width="510" height="50" rx="14 14 0 0" fill="#09281E"/>
    <text x="255" y="32" font-size="17" font-weight="900" fill="#26E7A6" text-anchor="middle">1. NẾN TĂNG MẠNH (BULLISH MOMENTUM)</text>

    <!-- HỆ THỐNG NẾN XANH TO BẢN -->
    <!-- 1. Râu nến trên (xanh) -->
    <line x1="160" y1="80" x2="160" y2="150" stroke="#00E5FF" stroke-width="6" stroke-linecap="round"/>
    <circle cx="160" cy="80" r="7" fill="#F0B90B"/>

    <!-- 2. Thân nến xanh to đùng -->
    <rect x="115" y="150" width="90" height="230" rx="6" fill="#089981" stroke="#26E7A6" stroke-width="2.5" filter="url(#glow-cyan)"/>

    <!-- 3. Râu nến dưới (xanh) -->
    <line x1="160" y1="380" x2="160" y2="440" stroke="#00E5FF" stroke-width="6" stroke-linecap="round"/>
    <circle cx="160" cy="440" r="7" fill="#8E9BAE"/>

    <!-- CHỈ DẪN DÓNG RA NGOÀI BÊN PHẢI -->
    <!-- Giá cao nhất -->
    <line x1="167" y1="80" x2="250" y2="80" stroke="#F0B90B" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="260" y="86" font-size="15" font-weight="800" fill="#F0B90B">Giá Cao Nhất (High)</text>

    <!-- Giá đóng cửa -->
    <line x1="205" y1="150" x2="250" y2="150" stroke="#00E5FF" stroke-width="2.5"/>
    <rect x="255" y="130" width="225" height="38" rx="6" fill="#07242E" stroke="#00E5FF" stroke-width="1.5"/>
    <text x="267" y="155" font-size="14.5" font-weight="900" fill="#00E5FF">GIÁ ĐÓNG CỬA (CLOSE)</text>

    <!-- Thân nến -->
    <g transform="translate(260, 240)">
      <text x="0" y="0" font-size="16" font-weight="900" fill="#26E7A6">THÂN NẾN DÀI (SPREAD)</text>
      <text x="0" y="24" font-size="14" font-weight="600" fill="#CAD4E0">= Phe Mua chiếm ưu thế 100%</text>
    </g>

    <!-- Giá mở cửa -->
    <line x1="205" y1="380" x2="250" y2="380" stroke="#8E9BAE" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="260" y="386" font-size="14.5" font-weight="700" fill="#CAD4E0">Giá Mở Cửa (Open)</text>

    <!-- Giá thấp nhất -->
    <line x1="167" y1="440" x2="250" y2="440" stroke="#8E9BAE" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="260" y="446" font-size="14" font-weight="700" fill="#8E9BAE">Giá Thấp Nhất (Low)</text>

    <!-- Kết luận chân thẻ -->
    <rect x="20" y="475" width="470" height="45" rx="8" fill="#09281E" stroke="#089981" stroke-width="1.2"/>
    <text x="255" y="503" font-size="15" font-weight="900" fill="#26E7A6" text-anchor="middle">➔ KẾT LUẬN: ĐÀ TĂNG ĐANG RẤT MẠNH</text>
  </g>

  <!-- ==================== CỘT PHẢI: NẾN GIẢM / PIN BAR (BEARISH CANDLE) ==================== -->
  <g transform="translate(630, 80)" filter="url(#drop-shadow)">
    <rect width="510" height="540" rx="14" fill="#131824" stroke="#F23645" stroke-width="2"/>
    
    <rect x="0" y="0" width="510" height="50" rx="14 14 0 0" fill="#240D12"/>
    <text x="255" y="32" font-size="17" font-weight="900" fill="#FF707E" text-anchor="middle">2. NẾN PIN BAR TỪ CHỐI GIÁ (BEARISH REJECTION)</text>

    <!-- HỆ THỐNG NẾN ĐỎ TO BẢN (RÂU TRÊN VÀ RÂU DƯỚI HIỆN RÕ ĐỎ RỰC) -->
    <!-- 1. RÂU TRÊN DÀI ĐỎ RỰC (LONG UPPER WICK) -->
    <line x1="160" y1="80" x2="160" y2="300" stroke="#FF5252" stroke-width="7" stroke-linecap="round" filter="url(#glow-red)"/>
    <circle cx="160" cy="80" r="8" fill="#FF5252" filter="url(#glow-red)"/>

    <!-- 2. THÂN NẾN ĐỎ SÁT ĐÁY -->
    <rect x="115" y="300" width="90" height="70" rx="5" fill="#F23645" stroke="#FF8A95" stroke-width="2.5" filter="url(#glow-red)"/>

    <!-- 3. RÂU DƯỚI ĐỎ RÕ RÀNG (LOWER WICK) -->
    <line x1="160" y1="370" x2="160" y2="440" stroke="#FF5252" stroke-width="6" stroke-linecap="round"/>
    <circle cx="160" cy="440" r="6" fill="#FF707E"/>

    <!-- CHỈ DẪN DÓNG RA NGOÀI BÊN PHẢI -->
    <!-- Râu trên dài từ chối giá -->
    <line x1="167" y1="180" x2="250" y2="180" stroke="#FF5252" stroke-width="2.5"/>
    <g transform="translate(255, 150)">
      <rect width="225" height="58" rx="8" fill="#2A0B12" stroke="#FF5252" stroke-width="1.8"/>
      <text x="12" y="24" font-size="15" font-weight="900" fill="#FF5252">RÂU TRÊN DÀI NGOẰNG</text>
      <text x="12" y="46" font-size="13" font-weight="700" fill="#FFA4AC">= Từ chối giá &amp; Bẫy quét Stop Loss</text>
    </g>

    <!-- Giá mở cửa -->
    <line x1="205" y1="300" x2="250" y2="300" stroke="#CAD4E0" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="260" y="306" font-size="14.5" font-weight="700" fill="#CAD4E0">Giá Mở Cửa (Open)</text>

    <!-- Giá đóng cửa sát đáy -->
    <line x1="205" y1="370" x2="250" y2="370" stroke="#FF5252" stroke-width="2.5"/>
    <rect x="255" y="350" width="225" height="38" rx="6" fill="#280A10" stroke="#FF5252" stroke-width="1.5"/>
    <text x="267" y="375" font-size="14.5" font-weight="900" fill="#FF707E">ĐÓNG CỬA Ở ĐÁY (CLOSE)</text>

    <!-- Giá thấp nhất -->
    <line x1="167" y1="440" x2="250" y2="440" stroke="#FF707E" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="260" y="446" font-size="14" font-weight="700" fill="#FFA4AC">Giá Thấp Nhất (Low)</text>

    <!-- Kết luận chân thẻ -->
    <rect x="20" y="475" width="470" height="45" rx="8" fill="#220A10" stroke="#F23645" stroke-width="1.2"/>
    <text x="255" y="503" font-size="15" font-weight="900" fill="#FF707E" text-anchor="middle">➔ KẾT LUẬN: BÁO HIỆU ĐẢO CHIỀU GIẢM</text>
  </g>

  <!-- LOGO WATERMARK -->
  <text x="600" y="650" font-size="14" font-weight="800" fill="#657795" text-anchor="middle">
    PTvolume.com • Naked Price Action
  </text>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_candlestick_structure.svg"), "w", encoding="utf-8") as f:
    f.write(svg_candle_fixed)
print("Saved FIXED naked_candlestick_structure.svg with clear red wicks!")
