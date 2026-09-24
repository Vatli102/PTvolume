# -*- coding: utf-8 -*-
"""
TÁI THIẾT KẾ TOÀN BỘ HÌNH ẢNH THEO PHONG CÁCH MINIMALIST VIDEO EXPLAINER:
- Siêu tối giản, cực kỳ sáng sủa, trực quan 100%.
- Không nhồi nhét văn bản dài.
- Nến và Volume to bản, màu sắc nổi bật, mũi tên và nhãn to đùng.
- Nhìn 2 giây hiểu ngay bản chất VSA & Naked Price Action.
"""
import os

SVG_DIR = r"d:\PHAN DUA CẤM XÓA\AI_Agent_Trading\assets\images"

# ==============================================================================
# 1. naked_candlestick_structure.svg (Bóc tách nến: 2 cây nến to khổng lồ)
# ==============================================================================
svg_candle = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%" style="background:#0D111A; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
  <defs>
    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow-red" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="drop-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <!-- NỀN TỐI SÁNG SỦA -->
  <rect width="1200" height="680" fill="#0D111A" rx="16"/>
  <rect width="1192" height="672" x="4" y="4" fill="none" stroke="#1E2638" stroke-width="2" rx="14"/>

  <!-- TIÊU ĐỀ CHÍNH TO RÕ -->
  <text x="600" y="55" font-size="24" font-weight="900" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.5">
    3 BỘ PHẬN CỐT LÕI CỦA CÂY NẾN: <tspan fill="#00E5FF">THÂN</tspan> • <tspan fill="#F0B90B">RÂU</tspan> • <tspan fill="#26E7A6">ĐÓNG CỬA</tspan>
  </text>

  <!-- ==================== CỘT TRÁI: NẾN TĂNG MẠNH ==================== -->
  <g transform="translate(60, 90)" filter="url(#drop-shadow)">
    <rect width="510" height="520" rx="14" fill="#131824" stroke="#223048" stroke-width="1.5"/>
    
    <!-- Tiêu đề thẻ -->
    <rect x="0" y="0" width="510" height="50" rx="14 14 0 0" fill="#182030"/>
    <text x="255" y="32" font-size="18" font-weight="900" fill="#089981" text-anchor="middle">1. NẾN TĂNG MẠNH (BULLISH)</text>

    <!-- BÓNG VÀ THÂN NẾN KHỔNG LỒ -->
    <!-- Râu trên -->
    <line x1="180" y1="90" x2="180" y2="140" stroke="#CAD4E0" stroke-width="6" stroke-linecap="round"/>
    <!-- Thân nến xanh to bản -->
    <rect x="135" y="140" width="90" height="260" rx="6" fill="#089981" stroke="#26E7A6" stroke-width="3" filter="url(#glow-cyan)"/>
    <!-- Râu dưới -->
    <line x1="180" y1="400" x2="180" y2="440" stroke="#CAD4E0" stroke-width="6" stroke-linecap="round"/>

    <!-- CHỈ DẪN MŨI TÊN TO RÕ -->
    <!-- Giá cao nhất -->
    <line x1="180" y1="90" x2="270" y2="90" stroke="#F0B90B" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="280" y="96" font-size="16" font-weight="800" fill="#F0B90B">Giá Cao Nhất (High)</text>

    <!-- Mức đóng cửa -->
    <line x1="225" y1="140" x2="270" y2="140" stroke="#00E5FF" stroke-width="3"/>
    <g transform="translate(280, 120)">
      <rect width="200" height="42" rx="6" fill="#092524" stroke="#00E5FF" stroke-width="1.5"/>
      <text x="12" y="26" font-size="15" font-weight="900" fill="#00E5FF">ĐÓNG CỬA (CLOSE)</text>
    </g>

    <!-- Thân nến -->
    <g transform="translate(280, 245)">
      <text x="0" y="0" font-size="18" font-weight="900" fill="#26E7A6">THÂN NẾN DÀI</text>
      <text x="0" y="24" font-size="15" font-weight="600" fill="#CAD4E0">= Phe Mua làm chủ 100%</text>
    </g>

    <!-- Giá mở cửa -->
    <line x1="225" y1="400" x2="270" y2="400" stroke="#8E9BAE" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="280" y="406" font-size="15" font-weight="700" fill="#8E9BAE">Giá Mở Cửa (Open)</text>

    <!-- Tóm tắt chân thẻ -->
    <rect x="25" y="455" width="460" height="45" rx="8" fill="#09281E" stroke="#089981" stroke-width="1.2"/>
    <text x="255" y="483" font-size="16" font-weight="800" fill="#26E7A6" text-anchor="middle">➔ KẾT LUẬN: ĐÀ TĂNG RẤT MẠNH</text>
  </g>

  <!-- ==================== CỘT PHẢI: NẾN PIN BAR TỪ CHỐI GIÁ ==================== -->
  <g transform="translate(630, 90)" filter="url(#drop-shadow)">
    <rect width="510" height="520" rx="14" fill="#131824" stroke="#223048" stroke-width="1.5"/>
    
    <!-- Tiêu đề thẻ -->
    <rect x="0" y="0" width="510" height="50" rx="14 14 0 0" fill="#1F1518"/>
    <text x="255" y="32" font-size="18" font-weight="900" fill="#F23645" text-anchor="middle">2. NẾN TỪ CHỐI GIÁ (PIN BAR)</text>

    <!-- RÂU NẾN DÀI NGOẰNG VÀ THÂN NHỎ -->
    <!-- Râu trên dài bất thường -->
    <line x1="180" y1="90" x2="180" y2="340" stroke="#FF5252" stroke-width="7" stroke-linecap="round" filter="url(#glow-red)"/>
    <!-- Thân nến nhỏ sát đáy -->
    <rect x="135" y="340" width="90" height="60" rx="6" fill="#F23645" stroke="#FF8A95" stroke-width="2.5"/>
    <!-- Râu dưới ngắn -->
    <line x1="180" y1="400" x2="180" y2="430" stroke="#CAD4E0" stroke-width="5" stroke-linecap="round"/>

    <!-- CHỈ DẪN MŨI TÊN TO RÕ -->
    <!-- Râu nến dài -->
    <g transform="translate(280, 190)">
      <rect width="200" height="65" rx="8" fill="#280D12" stroke="#FF5252" stroke-width="1.8"/>
      <text x="12" y="26" font-size="16" font-weight="900" fill="#FF5252">RÂU NẾN DÀI</text>
      <text x="12" y="48" font-size="14" font-weight="700" fill="#FFA4AC">= Từ chối giá &amp; Bẫy cá mập</text>
    </g>

    <!-- Mức đóng cửa bị ép xuống đáy -->
    <line x1="225" y1="400" x2="270" y2="400" stroke="#FF5252" stroke-width="3"/>
    <g transform="translate(280, 380)">
      <text x="0" y="0" font-size="16" font-weight="900" fill="#FF5252">ĐÓNG CỬA Ở ĐÁY</text>
      <text x="0" y="22" font-size="14" font-weight="600" fill="#CAD4E0">= Phe Bán đè bẹp phe Mua</text>
    </g>

    <!-- Tóm tắt chân thẻ -->
    <rect x="25" y="455" width="460" height="45" rx="8" fill="#280A10" stroke="#F23645" stroke-width="1.2"/>
    <text x="255" y="483" font-size="16" font-weight="800" fill="#FF707E" text-anchor="middle">➔ KẾT LUẬN: BÁO HIỆU ĐẢO CHIỀU GIẢM</text>
  </g>

  <!-- LOGO WATERMARK -->
  <text x="600" y="645" font-size="14" font-weight="800" fill="#657795" text-anchor="middle">
    PTvolume.com • Naked Price Action
  </text>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_candlestick_structure.svg"), "w", encoding="utf-8") as f:
    f.write(svg_candle)
print("Saved clean naked_candlestick_structure.svg")


# ==============================================================================
# 2. naked_vsa_effort_result.svg (Nỗ lực vs Kết quả: 3 kịch bản cực ngắn gọn)
# ==============================================================================
svg_vsa = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%" style="background:#0D111A; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
  <defs>
    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow-red" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="drop-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1200" height="680" fill="#0D111A" rx="16"/>
  <rect width="1192" height="672" x="4" y="4" fill="none" stroke="#1E2638" stroke-width="2" rx="14"/>

  <!-- TIÊU ĐỀ CHÍNH -->
  <text x="600" y="55" font-size="24" font-weight="900" fill="#FFFFFF" text-anchor="middle">
    QUY LUẬT NỖ LỰC &amp; KẾT QUẢ: <tspan fill="#00E5FF">NẾN (KẾT QUẢ)</tspan> vs <tspan fill="#F0B90B">VOLUME (NỖ LỰC)</tspan>
  </text>

  <!-- ==================== CỘT 1: ĐỒNG THUẬN ==================== -->
  <g transform="translate(50, 90)" filter="url(#drop-shadow)">
    <rect width="340" height="520" rx="14" fill="#131824" stroke="#089981" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="50" rx="14 14 0 0" fill="#09281E"/>
    <text x="170" y="32" font-size="16" font-weight="900" fill="#26E7A6" text-anchor="middle">1. ĐỒNG THUẬN (BÌNH THƯỜNG)</text>

    <!-- Nến dài -->
    <line x1="170" y1="80" x2="170" y2="240" stroke="#00E5FF" stroke-width="4"/>
    <rect x="135" y="95" width="70" height="130" rx="4" fill="#089981" stroke="#26E7A6" stroke-width="2" filter="url(#glow-cyan)"/>
    <text x="170" y="165" font-size="14" font-weight="900" fill="#FFFFFF" text-anchor="middle">THÂN DÀI</text>

    <!-- Đường ngăn cách -->
    <line x1="20" y1="270" x2="320" y2="270" stroke="#223048" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- Cột Volume cao vọt -->
    <rect x="135" y="300" width="70" height="120" rx="4" fill="#00E5FF" filter="url(#glow-cyan)"/>
    <text x="170" y="365" font-size="15" font-weight="900" fill="#07090E" text-anchor="middle">VOL LỚN</text>

    <!-- Nhãn hành động -->
    <rect x="20" y="450" width="300" height="48" rx="8" fill="#0A2D22" stroke="#26E7A6" stroke-width="1.5"/>
    <text x="170" y="480" font-size="15" font-weight="900" fill="#26E7A6" text-anchor="middle">✓ TỰ TIN THEO XU HƯỚNG</text>
  </g>

  <!-- ==================== CỘT 2: BẤT THƯỜNG ==================== -->
  <g transform="translate(430, 90)" filter="url(#drop-shadow)">
    <rect width="340" height="520" rx="14" fill="#131824" stroke="#F23645" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="50" rx="14 14 0 0" fill="#280A10"/>
    <text x="170" y="32" font-size="16" font-weight="900" fill="#FF707E" text-anchor="middle">2. BẤT THƯỜNG (HẤP THỤ)</text>

    <!-- Nến ngắn râu dài -->
    <line x1="170" y1="80" x2="170" y2="240" stroke="#FF5252" stroke-width="4"/>
    <rect x="135" y="150" width="70" height="35" rx="4" fill="#F23645" stroke="#FF8A95" stroke-width="2" filter="url(#glow-red)"/>
    <text x="170" y="173" font-size="13" font-weight="900" fill="#FFFFFF" text-anchor="middle">THÂN NGẮN</text>

    <!-- Đường ngăn cách -->
    <line x1="20" y1="270" x2="320" y2="270" stroke="#223048" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- Cột Volume CỰC ĐẠI -->
    <rect x="135" y="290" width="70" height="130" rx="4" fill="#F23645" filter="url(#glow-red)"/>
    <text x="170" y="360" font-size="14" font-weight="900" fill="#FFFFFF" text-anchor="middle">VOL CỰC KHỦNG</text>

    <!-- Nhãn hành động -->
    <rect x="20" y="450" width="300" height="48" rx="8" fill="#2E0A12" stroke="#FF5252" stroke-width="1.5"/>
    <text x="170" y="480" font-size="15" font-weight="900" fill="#FF707E" text-anchor="middle">⚠️ CẢNH BÁO ĐẢO CHIỀU!</text>
  </g>

  <!-- ==================== CỘT 3: THIẾU NỖ LỰC ==================== -->
  <g transform="translate(810, 90)" filter="url(#drop-shadow)">
    <rect width="340" height="520" rx="14" fill="#131824" stroke="#F0B90B" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="50" rx="14 14 0 0" fill="#251C08"/>
    <text x="170" y="32" font-size="16" font-weight="900" fill="#F0B90B" text-anchor="middle">3. THIẾU HỤT NỖ LỰC</text>

    <!-- Nến tăng rướn -->
    <line x1="170" y1="80" x2="170" y2="240" stroke="#CAD4E0" stroke-width="3"/>
    <rect x="135" y="100" width="70" height="110" rx="4" fill="#089981" stroke="#26E7A6" stroke-width="1.5"/>
    <text x="170" y="160" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle">TĂNG RƯỚN</text>

    <!-- Đường ngăn cách -->
    <line x1="20" y1="270" x2="320" y2="270" stroke="#223048" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- Cột Volume thấp lè tè -->
    <rect x="145" y="375" width="50" height="45" rx="3" fill="#687C94"/>
    <text x="170" y="402" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle">VOL BÉ TÍ</text>

    <!-- Nhãn hành động -->
    <rect x="20" y="450" width="300" height="48" rx="8" fill="#281F0A" stroke="#F0B90B" stroke-width="1.5"/>
    <text x="170" y="480" font-size="15" font-weight="900" fill="#F0B90B" text-anchor="middle">❌ KHÔNG FOMO MUA ĐUỔI</text>
  </g>

  <!-- LOGO WATERMARK -->
  <text x="600" y="645" font-size="14" font-weight="800" fill="#657795" text-anchor="middle">
    PTvolume.com • Wyckoff Effort vs Result
  </text>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_vsa_effort_result.svg"), "w", encoding="utf-8") as f:
    f.write(svg_vsa)
print("Saved clean naked_vsa_effort_result.svg")


# ==============================================================================
# 3. naked_chart_indicator_trap.svg (Bẫy chỉ báo vs Biểu đồ trần: Siêu trực quan)
# ==============================================================================
svg_trap = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%" style="background:#0D111A; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
  <defs>
    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow-red" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="drop-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1200" height="680" fill="#0D111A" rx="16"/>
  <rect width="1192" height="672" x="4" y="4" fill="none" stroke="#1E2638" stroke-width="2" rx="14"/>

  <!-- TIÊU ĐỀ CHÍNH -->
  <text x="600" y="55" font-size="24" font-weight="900" fill="#FFFFFF" text-anchor="middle">
    BẢN CHẤT: <tspan fill="#FF5252">MA TRẬN CHỈ BÁO TRỄ</tspan> vs <tspan fill="#00E5FF">BIỂU ĐỒ TRẦN REAL-TIME</tspan>
  </text>

  <!-- ==================== CỘT TRÁI: MA TRẬN CHỈ BÁO ==================== -->
  <g transform="translate(50, 90)" filter="url(#drop-shadow)">
    <rect width="525" height="520" rx="14" fill="#131824" stroke="#F23645" stroke-width="2"/>
    <rect x="0" y="0" width="525" height="50" rx="14 14 0 0" fill="#220D12"/>
    <text x="262" y="32" font-size="17" font-weight="900" fill="#FF707E" text-anchor="middle">❌ LẠM DỤNG CHỈ BÁO (BỊ TRỄ)</text>

    <!-- Khu vực đồ thị rối rắm -->
    <g transform="translate(20, 70)">
      <rect width="485" height="340" rx="8" fill="#080C14" stroke="#32141C" stroke-width="1"/>

      <!-- Nến chạy trước -->
      <path d="M 30 250 L 150 180 L 250 200 L 380 60 L 450 100" fill="none" stroke="#485A72" stroke-width="3" opacity="0.4"/>
      
      <!-- Đống đường chỉ báo chằng chịt -->
      <path d="M 20 280 Q 120 270 240 220 T 380 110 T 460 140" fill="none" stroke="#F0B90B" stroke-width="3"/>
      <path d="M 20 290 Q 160 280 270 240 T 410 130 T 460 150" fill="none" stroke="#E040FB" stroke-width="3"/>
      <path d="M 20 300 Q 200 290 350 260 T 460 180" fill="none" stroke="#00E5FF" stroke-width="3"/>

      <!-- BẪY ĐU ĐỈNH CALLOUT (TO RÕ) -->
      <g transform="translate(380, 110)">
        <circle cx="0" cy="0" r="14" fill="#FF5252" filter="url(#glow-red)"/>
        <g transform="translate(-160, -80)">
          <rect width="210" height="55" rx="8" fill="#2E0A12" stroke="#FF5252" stroke-width="1.8"/>
          <text x="105" y="24" font-size="14" font-weight="900" fill="#FF5252" text-anchor="middle">❌ CHỈ BÁO BÁO MUA</text>
          <text x="105" y="44" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle">GIÁ ĐÃ ĐỈNH ➔ ĐU ĐỈNH!</text>
        </g>
      </g>
    </g>

    <!-- Kết luận -->
    <rect x="20" y="435" width="485" height="65" rx="8" fill="#200A10" stroke="#F23645" stroke-width="1.2"/>
    <text x="262" y="462" font-size="15" font-weight="800" fill="#FFA4AC" text-anchor="middle">Chỉ báo đi sau giá từ 5 - 15 cây nến.</text>
    <text x="262" y="486" font-size="15" font-weight="900" fill="#FF5252" text-anchor="middle">Khi chỉ báo báo Mua thì giá đã hết sóng!</text>
  </g>

  <!-- ==================== CỘT PHẢI: BIỂU ĐỒ TRẦN ==================== -->
  <g transform="translate(625, 90)" filter="url(#drop-shadow)">
    <rect width="525" height="520" rx="14" fill="#131824" stroke="#00E5FF" stroke-width="2"/>
    <rect x="0" y="0" width="525" height="50" rx="14 14 0 0" fill="#09202E"/>
    <text x="262" y="32" font-size="17" font-weight="900" fill="#00E5FF" text-anchor="middle">✓ BIỂU ĐỒ TRẦN (THỜI GIAN THỰC)</text>

    <!-- Khu vực đồ thị sáng sủa -->
    <g transform="translate(20, 70)">
      <rect width="485" height="340" rx="8" fill="#080C14" stroke="#162E44" stroke-width="1"/>

      <!-- Vùng kháng cự nét đứt -->
      <line x1="20" y1="180" x2="465" y2="180" stroke="#00E5FF" stroke-width="2" stroke-dasharray="6,4"/>
      <text x="35" y="170" font-size="13" font-weight="800" fill="#00E5FF">CẢN KHÁNG CỰ</text>

      <!-- Chuỗi nến rõ ràng -->
      <rect x="60" y="210" width="16" height="40" fill="#089981" rx="2"/>
      <rect x="110" y="195" width="16" height="50" fill="#F23645" rx="2"/>
      
      <!-- NẾN BREAKOUT BỨT PHÁ + SNIPER ENTRY -->
      <rect x="170" y="120" width="22" height="95" fill="#089981" stroke="#26E7A6" stroke-width="2" rx="2" filter="url(#glow-cyan)"/>
      <g transform="translate(180, 110)">
        <circle cx="0" cy="0" r="12" fill="#00E5FF" filter="url(#glow-cyan)"/>
        <g transform="translate(25, -45)">
          <rect width="210" height="55" rx="8" fill="#07202B" stroke="#00E5FF" stroke-width="1.8"/>
          <text x="105" y="24" font-size="14" font-weight="900" fill="#00E5FF" text-anchor="middle">🎯 MUA NGAY CHÂN SÓNG</text>
          <text x="105" y="44" font-size="13" font-weight="800" fill="#26E7A6" text-anchor="middle">Nến bứt phá + Vol bùng nổ</text>
        </g>
      </g>

      <rect x="230" y="90" width="18" height="50" fill="#089981" rx="2"/>
      <rect x="280" y="60" width="18" height="55" fill="#089981" rx="2"/>
      <rect x="340" y="40" width="18" height="40" fill="#089981" rx="2"/>

      <!-- Volume phía dưới -->
      <line x1="20" y1="260" x2="465" y2="260" stroke="#1C2D44" stroke-width="1"/>
      <rect x="62" y="295" width="12" height="35" fill="#089981"/>
      <rect x="112" y="305" width="12" height="25" fill="#F23645"/>
      <rect x="172" y="270" width="18" height="60" fill="#00E5FF" filter="url(#glow-cyan)"/>
    </g>

    <!-- Kết luận -->
    <rect x="20" y="435" width="485" height="65" rx="8" fill="#0A241C" stroke="#26E7A6" stroke-width="1.2"/>
    <text x="262" y="462" font-size="15" font-weight="800" fill="#26E7A6" text-anchor="middle">Bắt trọn 100% thân sóng ngay khi nến vượt cản.</text>
    <text x="262" y="486" font-size="15" font-weight="900" fill="#00E5FF" text-anchor="middle">Cắt lỗ siêu ngắn (0.5%) • Tỷ lệ R:R đỉnh cao 1:4+</text>
  </g>

  <!-- LOGO WATERMARK -->
  <text x="600" y="645" font-size="14" font-weight="800" fill="#657795" text-anchor="middle">
    PTvolume.com • Naked Price Action
  </text>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_chart_indicator_trap.svg"), "w", encoding="utf-8") as f:
    f.write(svg_trap)
print("Saved clean naked_chart_indicator_trap.svg")


# ==============================================================================
# 4. naked_chart_clean_workspace.svg (Không gian làm việc 3 thành phần siêu sáng)
# ==============================================================================
svg_work = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%" style="background:#0D111A; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
  <defs>
    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="drop-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1200" height="680" fill="#0D111A" rx="16"/>
  <rect width="1192" height="672" x="4" y="4" fill="none" stroke="#1E2638" stroke-width="2" rx="14"/>

  <!-- TIÊU ĐỀ -->
  <text x="600" y="55" font-size="24" font-weight="900" fill="#FFFFFF" text-anchor="middle">
    3 THÀNH PHẦN DUY NHẤT TRÊN BIỂU ĐỒ TRẦN THỰC CHIẾN
  </text>

  <!-- KHUNG TERMINAL CHÍNH -->
  <g transform="translate(60, 85)" filter="url(#drop-shadow)">
    <rect width="1080" height="490" rx="14" fill="#131824" stroke="#00E5FF" stroke-width="2"/>

    <!-- VÙNG CUNG (SUPPLY ZONE) TRÊN ĐỈNH -->
    <rect x="30" y="30" width="1020" height="60" rx="6" fill="rgba(242,54,69,0.2)" stroke="#F23645" stroke-width="1.5" stroke-dasharray="5,4"/>
    <text x="50" y="65" font-size="16" font-weight="900" fill="#FF707E">🔴 VÙNG CUNG (SUPPLY ZONE) &ndash; Nơi cá mập xả hàng</text>

    <!-- NẾN CHẠY SẮC NÉT Ở GIỮA -->
    <g transform="translate(0, 10)">
      <rect x="150" y="280" width="22" height="50" fill="#089981" rx="3"/>
      <rect x="240" y="220" width="22" height="70" fill="#089981" rx="3"/>
      <rect x="330" y="170" width="22" height="65" fill="#089981" rx="3"/>
      
      <!-- Nến bứt phá -->
      <rect x="440" y="110" width="28" height="100" fill="#089981" stroke="#26E7A6" stroke-width="2" rx="3" filter="url(#glow-cyan)"/>
      <text x="454" y="85" font-size="14" font-weight="900" fill="#00E5FF" text-anchor="middle">NẾN GIÁ OHLC</text>

      <rect x="560" y="60" width="22" height="60" fill="#089981" rx="3"/>
      
      <!-- Nến chạm cản quay đầu -->
      <line x1="680" y1="20" x2="680" y2="120" stroke="#FF5252" stroke-width="4"/>
      <rect x="669" y="80" width="22" height="35" fill="#F23645" rx="3"/>
      <text x="680" y="150" font-size="14" font-weight="900" fill="#FF707E" text-anchor="middle">Từ Chối Vùng Cung</text>

      <rect x="780" y="110" width="22" height="65" fill="#F23645" rx="3"/>
      <rect x="880" y="170" width="22" height="75" fill="#F23645" rx="3"/>
    </g>

    <!-- VÙNG CẦU (DEMAND ZONE) DƯỚI ĐÁY -->
    <rect x="30" y="320" width="1020" height="60" rx="6" fill="rgba(8,153,129,0.2)" stroke="#089981" stroke-width="1.5" stroke-dasharray="5,4"/>
    <text x="50" y="355" font-size="16" font-weight="900" fill="#26E7A6">🟢 VÙNG CẦU (DEMAND ZONE) &ndash; Nơi cá mập gom hàng</text>

    <!-- CỘT KHỐI LƯỢNG VSA DƯỚI ĐÁY -->
    <line x1="30" y1="400" x2="1050" y2="400" stroke="#223048" stroke-width="1.5"/>
    <text x="50" y="425" font-size="14" font-weight="900" fill="#F0B90B">📊 KHỐI LƯỢNG GIAO DỊCH (VOLUME VSA)</text>
    
    <rect x="150" y="435" width="20" height="40" fill="#089981"/>
    <rect x="240" y="425" width="20" height="50" fill="#089981"/>
    <rect x="330" y="430" width="20" height="45" fill="#089981"/>
    <rect x="442" y="405" width="24" height="70" fill="#00E5FF" filter="url(#glow-cyan)"/>
    <rect x="560" y="420" width="20" height="55" fill="#089981"/>
    <rect x="670" y="408" width="20" height="67" fill="#F23645"/>
    <rect x="780" y="425" width="20" height="50" fill="#F23645"/>
    <rect x="880" y="430" width="20" height="45" fill="#F23645"/>
  </g>

  <!-- 3 NHÃN CỐT LÕI DƯỚI CÙNG -->
  <g transform="translate(60, 600)">
    <rect x="0" y="0" width="340" height="42" rx="21" fill="#08202E" stroke="#00E5FF" stroke-width="1.5"/>
    <text x="170" y="26" font-size="15" font-weight="900" fill="#00E5FF" text-anchor="middle">1. NẾN GIÁ NGUYÊN BẢN</text>

    <rect x="370" y="0" width="340" height="42" rx="21" fill="#09281E" stroke="#089981" stroke-width="1.5"/>
    <text x="540" y="26" font-size="15" font-weight="900" fill="#26E7A6" text-anchor="middle">2. VÙNG CUNG CẦU NGANG</text>

    <rect x="740" y="0" width="340" height="42" rx="21" fill="#281F0A" stroke="#F0B90B" stroke-width="1.5"/>
    <text x="910" y="26" font-size="15" font-weight="900" fill="#F0B90B" text-anchor="middle">3. CỘT KHỐI LƯỢNG VSA</text>
  </g>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_chart_clean_workspace.svg"), "w", encoding="utf-8") as f:
    f.write(svg_work)
print("Saved clean naked_chart_clean_workspace.svg")


# ==============================================================================
# 5. naked_chart_setup_3_steps.svg (3 Bước thiết lập: 3 Card to, biểu tượng lớn)
# ==============================================================================
svg_steps = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%" style="background:#0D111A; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
  <defs>
    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="drop-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1200" height="680" fill="#0D111A" rx="16"/>
  <rect width="1192" height="672" x="4" y="4" fill="none" stroke="#1E2638" stroke-width="2" rx="14"/>

  <!-- TIÊU ĐỀ -->
  <text x="600" y="55" font-size="24" font-weight="900" fill="#FFFFFF" text-anchor="middle">
    3 BƯỚC THIẾT LẬP BÀN LÀM VIỆC NAKED CHART TRÊN TRADINGVIEW
  </text>

  <!-- BƯỚC 1 -->
  <g transform="translate(50, 95)" filter="url(#drop-shadow)">
    <rect width="340" height="500" rx="14" fill="#131824" stroke="#FF5252" stroke-width="2"/>
    
    <!-- Số 01 To đùng -->
    <circle cx="170" cy="80" r="42" fill="#280A10" stroke="#FF5252" stroke-width="3"/>
    <text x="170" y="93" font-size="34" font-weight="900" fill="#FF5252" text-anchor="middle">01</text>

    <text x="170" y="165" font-size="18" font-weight="900" fill="#FFFFFF" text-anchor="middle">XÓA SẠCH CHỈ BÁO</text>
    <text x="170" y="195" font-size="14" font-weight="700" fill="#FF707E" text-anchor="middle">(Remove All Indicators)</text>

    <!-- Hộp mô phỏng thao tác -->
    <rect x="25" y="235" width="290" height="150" rx="10" fill="#080C14" stroke="#32141C" stroke-width="1.5"/>
    <text x="170" y="275" font-size="15" font-weight="800" fill="#CAD4E0" text-anchor="middle">Nhấp chuột phải vào biểu đồ</text>
    <line x1="45" y1="295" x2="295" y2="295" stroke="#22151B" stroke-width="1"/>
    
    <rect x="40" y="315" width="260" height="45" rx="8" fill="#FF5252"/>
    <text x="170" y="343" font-size="15" font-weight="900" fill="#FFFFFF" text-anchor="middle">✕ Remove Indicators</text>

    <text x="170" y="440" font-size="15" font-weight="700" fill="#FFA4AC" text-anchor="middle">Giải phóng 100% tầm mắt</text>
  </g>

  <!-- BƯỚC 2 -->
  <g transform="translate(430, 95)" filter="url(#drop-shadow)">
    <rect width="340" height="500" rx="14" fill="#131824" stroke="#00E5FF" stroke-width="2"/>
    
    <!-- Số 02 To đùng -->
    <circle cx="170" cy="80" r="42" fill="#08202E" stroke="#00E5FF" stroke-width="3"/>
    <text x="170" y="93" font-size="34" font-weight="900" fill="#00E5FF" text-anchor="middle">02</text>

    <text x="170" y="165" font-size="18" font-weight="900" fill="#FFFFFF" text-anchor="middle">CÀI NỀN TỐI DARK THEME</text>
    <text x="170" y="195" font-size="14" font-weight="700" fill="#00E5FF" text-anchor="middle">(Bảo vệ mắt &amp; Tăng tương phản)</text>

    <!-- Ô màu -->
    <rect x="25" y="235" width="290" height="150" rx="10" fill="#080C14" stroke="#162E44" stroke-width="1.5"/>
    <g transform="translate(45, 260)">
      <rect x="0" y="0" width="110" height="45" rx="6" fill="#0B0E14" stroke="#00E5FF" stroke-width="1.5"/>
      <text x="55" y="28" font-size="13" font-weight="900" fill="#00E5FF" text-anchor="middle">NỀN ĐEN</text>

      <rect x="130" y="0" width="110" height="45" rx="6" fill="#089981"/>
      <text x="185" y="28" font-size="13" font-weight="900" fill="#FFFFFF" text-anchor="middle">NẾN XANH</text>

      <rect x="65" y="55" width="110" height="45" rx="6" fill="#F23645"/>
      <text x="120" y="83" font-size="13" font-weight="900" fill="#FFFFFF" text-anchor="middle">NẾN ĐỎ</text>
    </g>

    <text x="170" y="440" font-size="15" font-weight="700" fill="#CAD4E0" text-anchor="middle">Nhìn rõ từng râu nến then chốt</text>
  </g>

  <!-- BƯỚC 3 -->
  <g transform="translate(810, 95)" filter="url(#drop-shadow)">
    <rect width="340" height="500" rx="14" fill="#131824" stroke="#F0B90B" stroke-width="2"/>
    
    <!-- Số 03 To đùng -->
    <circle cx="170" cy="80" r="42" fill="#281F0A" stroke="#F0B90B" stroke-width="3"/>
    <text x="170" y="93" font-size="34" font-weight="900" fill="#F0B90B" text-anchor="middle">03</text>

    <text x="170" y="165" font-size="18" font-weight="900" fill="#FFFFFF" text-anchor="middle">BẬT DUY NHẤT VOLUME</text>
    <text x="170" y="195" font-size="14" font-weight="700" fill="#F0B90B" text-anchor="middle">(Volume Spread Analysis)</text>

    <!-- Cột Volume -->
    <rect x="25" y="235" width="290" height="150" rx="10" fill="#080C14" stroke="#342810" stroke-width="1.5"/>
    <g transform="translate(50, 270)">
      <rect x="20" y="40" width="25" height="50" fill="#089981"/>
      <rect x="60" y="20" width="25" height="70" fill="#089981"/>
      <rect x="100" y="50" width="25" height="40" fill="#F23645"/>
      <rect x="140" y="0" width="30" height="90" fill="#00E5FF" filter="url(#glow-cyan)"/>
      <text x="155" y="-10" font-size="12" font-weight="900" fill="#00E5FF" text-anchor="middle">VOL KHỦNG</text>
    </g>

    <text x="170" y="440" font-size="15" font-weight="700" fill="#F0B90B" text-anchor="middle">Đo lường nỗ lực tiền thật</text>
  </g>

  <!-- LOGO WATERMARK -->
  <text x="600" y="645" font-size="14" font-weight="800" fill="#657795" text-anchor="middle">
    PTvolume.com • 3 Steps Setup
  </text>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_chart_setup_3_steps.svg"), "w", encoding="utf-8") as f:
    f.write(svg_steps)
print("Saved clean naked_chart_setup_3_steps.svg")
