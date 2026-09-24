# -*- coding: utf-8 -*-
"""
Khắc phục triệt để lỗi chữ đè hình và hình đè chữ:
- Nến và Cột Volume đứng độc lập, sạch sẽ 100%.
- Không có bất kỳ chữ nào ghi đè vào thân nến hoặc cột Volume.
- Mọi nhãn chú thích được tách sang bên cạnh với đường dóng rõ ràng.
- Hộp thoại callout nằm ở vùng trống phía trên hoặc dưới, không che mất nến.
"""
import os

SVG_DIR = r"d:\PHAN DUA CẤM XÓA\AI_Agent_Trading\assets\images"

# ==============================================================================
# 1. naked_chart_indicator_trap.svg (Hình 1.1)
# ==============================================================================
svg_trap_fixed = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%" style="background:#0D111A; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
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

  <rect width="1200" height="680" fill="#0D111A" rx="16"/>
  <rect width="1192" height="672" x="4" y="4" fill="none" stroke="#1E2638" stroke-width="2" rx="14"/>

  <!-- TIÊU ĐỀ CHÍNH -->
  <text x="600" y="52" font-size="23" font-weight="900" fill="#FFFFFF" text-anchor="middle">
    BẢN CHẤT: <tspan fill="#FF5252">MA TRẬN CHỈ BÁO TRỄ</tspan> vs <tspan fill="#00E5FF">BIỂU ĐỒ TRẦN REAL-TIME</tspan>
  </text>

  <!-- ==================== CỘT TRÁI: MA TRẬN CHỈ BÁO ==================== -->
  <g transform="translate(45, 80)" filter="url(#drop-shadow)">
    <rect width="535" height="540" rx="14" fill="#131824" stroke="#F23645" stroke-width="2"/>
    <rect x="0" y="0" width="535" height="50" rx="14 14 0 0" fill="#240D12"/>
    <text x="267" y="32" font-size="17" font-weight="900" fill="#FF707E" text-anchor="middle">❌ LẠM DỤNG CHỈ BÁO (BỊ TRỄ)</text>

    <!-- Hộp cảnh báo bẫy đu đỉnh (NẰM TÁCH BIỆT PHÍA TRÊN ĐỒ THỊ) -->
    <g transform="translate(20, 65)">
      <rect width="495" height="45" rx="8" fill="#2E0A12" stroke="#FF5252" stroke-width="1.5"/>
      <circle cx="25" cy="22" r="8" fill="#FF5252" filter="url(#glow-red)"/>
      <text x="45" y="28" font-size="15" font-weight="900" fill="#FF5252">BẪY ĐU ĐỈNH:</text>
      <text x="160" y="28" font-size="14" font-weight="700" fill="#FFFFFF">Chỉ báo trễ 10 nến mới cắt lên báo Mua!</text>
    </g>

    <!-- Khung đồ thị trực quan (NẾN VÀ ĐƯỜNG VẼ TỰ DO, KHÔNG BỊ CHỮ ĐÈ) -->
    <g transform="translate(20, 125)">
      <rect width="495" height="310" rx="8" fill="#080C14" stroke="#32141C" stroke-width="1.2"/>

      <!-- Nến thực tế đã chạy trước -->
      <!-- Sóng tăng -->
      <line x1="50" y1="260" x2="50" y2="290" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="42" y="265" width="16" height="25" fill="#089981" rx="2" opacity="0.4"/>

      <line x1="100" y1="220" x2="100" y2="260" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="92" y="230" width="16" height="25" fill="#089981" rx="2" opacity="0.4"/>

      <line x1="160" y1="160" x2="160" y2="225" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="152" y="170" width="16" height="45" fill="#089981" rx="2" opacity="0.4"/>

      <!-- Đỉnh sóng -->
      <line x1="230" y1="90" x2="230" y2="160" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="222" y="100" width="16" height="45" fill="#089981" rx="2" opacity="0.5"/>

      <!-- Nến đảo chiều giảm sau đỉnh -->
      <line x1="310" y1="75" x2="310" y2="135" stroke="#FF5252" stroke-width="2"/>
      <rect x="302" y="85" width="16" height="30" fill="#F23645" rx="2"/>

      <line x1="380" y1="110" x2="380" y2="185" stroke="#FF5252" stroke-width="2"/>
      <rect x="372" y="125" width="16" height="50" fill="#F23645" rx="2"/>

      <line x1="450" y1="170" x2="450" y2="250" stroke="#FF5252" stroke-width="2"/>
      <rect x="442" y="185" width="16" height="55" fill="#F23645" rx="2"/>

      <!-- Các đường chỉ báo trễ uốn lượn phía sau -->
      <!-- MA20 Vàng -->
      <path d="M 30 280 Q 150 270 250 210 T 360 115 T 470 170" fill="none" stroke="#F0B90B" stroke-width="3"/>
      <!-- MA50 Tím -->
      <path d="M 30 290 Q 180 285 290 240 T 420 145 T 470 185" fill="none" stroke="#E040FB" stroke-width="3"/>
      <!-- MA200 Xanh Cyan (Trễ hoàn toàn) -->
      <path d="M 30 295 Q 220 290 350 265 T 470 215" fill="none" stroke="#00E5FF" stroke-width="3"/>

      <!-- Điểm cắt trễ ngay tại đỉnh -->
      <circle cx="360" cy="115" r="10" fill="#FF5252" stroke="#FFFFFF" stroke-width="2" filter="url(#glow-red)"/>
      <line x1="360" y1="115" x2="360" y2="60" stroke="#FF5252" stroke-width="2" stroke-dasharray="3,3"/>
      <text x="360" y="50" font-size="13" font-weight="900" fill="#FF707E" text-anchor="middle">Điểm MA Cắt Lên (Báo Mua Trễ)</text>
    </g>

    <!-- Kết luận dưới đáy -->
    <rect x="20" y="450" width="495" height="70" rx="8" fill="#1F0A10" stroke="#F23645" stroke-width="1.2"/>
    <text x="267" y="478" font-size="15" font-weight="800" fill="#FFA4AC" text-anchor="middle">Chỉ báo đi sau giá từ 5 - 15 cây nến.</text>
    <text x="267" y="502" font-size="15" font-weight="900" fill="#FF5252" text-anchor="middle">Khi chỉ báo báo Mua thì giá đã bắt đầu sập!</text>
  </g>

  <!-- ==================== CỘT PHẢI: BIỂU ĐỒ TRẦN ==================== -->
  <g transform="translate(620, 80)" filter="url(#drop-shadow)">
    <rect width="535" height="540" rx="14" fill="#131824" stroke="#00E5FF" stroke-width="2"/>
    <rect x="0" y="0" width="535" height="50" rx="14 14 0 0" fill="#09202E"/>
    <text x="267" y="32" font-size="17" font-weight="900" fill="#00E5FF" text-anchor="middle">✓ BIỂU ĐỒ TRẦN (THỜI GIAN THỰC)</text>

    <!-- Hộp tín hiệu bắn tỉa (NẰM TÁCH BIỆT PHÍA TRÊN ĐỒ THỊ) -->
    <g transform="translate(20, 65)">
      <rect width="495" height="45" rx="8" fill="#07242E" stroke="#00E5FF" stroke-width="1.5"/>
      <circle cx="25" cy="22" r="8" fill="#00E5FF" filter="url(#glow-cyan)"/>
      <text x="45" y="28" font-size="15" font-weight="900" fill="#00E5FF">SNIPER ENTRY:</text>
      <text x="170" y="28" font-size="14" font-weight="700" fill="#26E7A6">Bắt trọn 100% sóng ngay khi nến vượt cản!</text>
    </g>

    <!-- Khung đồ thị trực quan (NẾN SẠCH SẼ, KHÔNG CÓ CHỮ ĐÈ) -->
    <g transform="translate(20, 125)">
      <rect width="495" height="310" rx="8" fill="#080C14" stroke="#162E44" stroke-width="1.2"/>

      <!-- Đường cản ngang nét đứt -->
      <line x1="20" y1="160" x2="475" y2="160" stroke="#00E5FF" stroke-width="2" stroke-dasharray="6,4"/>
      <text x="35" y="150" font-size="13" font-weight="800" fill="#00E5FF">CẢN KHÁNG CỰ (65,200)</text>

      <!-- Chuỗi nến tích lũy -->
      <line x1="60" y1="180" x2="60" y2="230" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="52" y="190" width="16" height="35" fill="#089981" rx="2"/>

      <line x1="110" y1="170" x2="110" y2="225" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="102" y="180" width="16" height="38" fill="#F23645" rx="2"/>

      <!-- NẾN BỨT PHÁ (MOMENTUM CANDLE) -->
      <line x1="170" y1="90" x2="170" y2="200" stroke="#26E7A6" stroke-width="3"/>
      <rect x="160" y="100" width="20" height="90" fill="#089981" stroke="#26E7A6" stroke-width="2" rx="2" filter="url(#glow-cyan)"/>
      
      <!-- Mũi tên chỉ điểm mua (ĐỨNG Ở NGOÀI, KHÔNG ĐÈ NẾN) -->
      <circle cx="170" cy="90" r="7" fill="#00E5FF" filter="url(#glow-cyan)"/>
      <line x1="170" y1="90" x2="170" y2="40" stroke="#00E5FF" stroke-width="2"/>
      <rect x="105" y="15" width="130" height="25" rx="4" fill="#07202B" stroke="#00E5FF" stroke-width="1"/>
      <text x="170" y="32" font-size="12" font-weight="900" fill="#00E5FF" text-anchor="middle">MUA TẠI ĐÂY</text>

      <!-- Nến chạy tiếp diễn xu hướng -->
      <line x1="230" y1="70" x2="230" y2="130" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="222" y="75" width="16" height="45" fill="#089981" rx="2"/>

      <line x1="290" y1="45" x2="290" y2="105" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="282" y="50" width="16" height="45" fill="#089981" rx="2"/>

      <line x1="350" y1="25" x2="350" y2="85" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="342" y="30" width="16" height="45" fill="#089981" rx="2"/>

      <!-- Nến đảo chiều chốt lời đỉnh -->
      <line x1="420" y1="15" x2="420" y2="80" stroke="#F0B90B" stroke-width="2.5"/>
      <rect x="412" y="45" width="16" height="20" fill="#F23645" rx="2"/>
      <text x="420" y="98" font-size="12" font-weight="800" fill="#F0B90B" text-anchor="middle">Chốt Lời</text>

      <!-- Cột Volume phía dưới -->
      <line x1="20" y1="245" x2="475" y2="245" stroke="#1C2D44" stroke-width="1"/>
      <text x="35" y="260" font-size="11" font-weight="800" fill="#8E9BAE">KHỐI LƯỢNG VSA:</text>

      <rect x="54" y="275" width="12" height="25" fill="#089981"/>
      <rect x="104" y="280" width="12" height="20" fill="#F23645"/>
      <!-- Cột Vol bùng nổ -->
      <rect x="162" y="250" width="16" height="50" fill="#00E5FF" filter="url(#glow-cyan)"/>
      <text x="170" y="308" font-size="10" font-weight="900" fill="#00E5FF" text-anchor="middle">VOL LỚN</text>

      <rect x="224" y="270" width="12" height="30" fill="#089981"/>
      <rect x="284" y="275" width="12" height="25" fill="#089981"/>
      <rect x="344" y="280" width="12" height="20" fill="#089981"/>
      <rect x="414" y="265" width="12" height="35" fill="#F23645"/>
    </g>

    <!-- Kết luận dưới đáy -->
    <rect x="20" y="450" width="495" height="70" rx="8" fill="#0A241C" stroke="#26E7A6" stroke-width="1.2"/>
    <text x="267" y="478" font-size="15" font-weight="800" fill="#26E7A6" text-anchor="middle">Nhận diện điểm phá vỡ ngay khi nến hình thành.</text>
    <text x="267" y="502" font-size="15" font-weight="900" fill="#00E5FF" text-anchor="middle">Cắt lỗ siêu ngắn (0.5%) • Tỷ lệ R:R đỉnh cao 1:4+</text>
  </g>

  <!-- LOGO WATERMARK -->
  <text x="600" y="650" font-size="14" font-weight="800" fill="#657795" text-anchor="middle">
    PTvolume.com • Naked Price Action
  </text>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_chart_indicator_trap.svg"), "w", encoding="utf-8") as f:
    f.write(svg_trap_fixed)
print("Saved FIXED naked_chart_indicator_trap.svg")


# ==============================================================================
# 2. naked_vsa_effort_result.svg (Hình 1.5 - KHÔNG CÓ CHỮ ĐÈ TRONG NẾN & VOLUME)
# ==============================================================================
svg_vsa_fixed = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%" style="background:#0D111A; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
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

  <rect width="1200" height="680" fill="#0D111A" rx="16"/>
  <rect width="1192" height="672" x="4" y="4" fill="none" stroke="#1E2638" stroke-width="2" rx="14"/>

  <!-- TIÊU ĐỀ CHÍNH -->
  <text x="600" y="52" font-size="23" font-weight="900" fill="#FFFFFF" text-anchor="middle">
    QUY LUẬT NỖ LỰC &amp; KẾT QUẢ: <tspan fill="#00E5FF">NẾN (KẾT QUẢ)</tspan> vs <tspan fill="#F0B90B">VOLUME (NỖ LỰC)</tspan>
  </text>

  <!-- ==================== CỘT 1: ĐỒNG THUẬN ==================== -->
  <g transform="translate(45, 80)" filter="url(#drop-shadow)">
    <rect width="350" height="540" rx="14" fill="#131824" stroke="#089981" stroke-width="2"/>
    <rect x="0" y="0" width="350" height="50" rx="14 14 0 0" fill="#09281E"/>
    <text x="175" y="32" font-size="16" font-weight="900" fill="#26E7A6" text-anchor="middle">1. ĐỒNG THUẬN (BÌNH THƯỜNG)</text>

    <!-- KHU VỰC NẾN: NẾN ĐỨNG ĐỘC LẬP -->
    <g transform="translate(0, 65)">
      <!-- Nhãn ở trên -->
      <text x="175" y="20" font-size="14" font-weight="800" fill="#26E7A6" text-anchor="middle">KẾT QUẢ: THÂN NẾN DÀI</text>

      <!-- Cây nến xanh dài sạch sẽ -->
      <line x1="175" y1="35" x2="175" y2="195" stroke="#00E5FF" stroke-width="4"/>
      <rect x="145" y="45" width="60" height="135" rx="4" fill="#089981" stroke="#26E7A6" stroke-width="2" filter="url(#glow-cyan)"/>
    </g>

    <!-- Đường phân cách -->
    <line x1="25" y1="285" x2="325" y2="285" stroke="#223048" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- KHU VỰC VOLUME: VOLUME ĐỨNG ĐỘC LẬP -->
    <g transform="translate(0, 300)">
      <!-- Nhãn ở trên volume -->
      <text x="175" y="15" font-size="14" font-weight="800" fill="#00E5FF" text-anchor="middle">NỖ LỰC: CỘT VOLUME CAO VỌT</text>

      <!-- Cột Volume xanh cyan sạch sẽ -->
      <rect x="145" y="30" width="60" height="110" rx="4" fill="#00E5FF" filter="url(#glow-cyan)"/>
    </g>

    <!-- Khung hành động chân thẻ -->
    <rect x="20" y="465" width="310" height="55" rx="8" fill="#0A2D22" stroke="#26E7A6" stroke-width="1.5"/>
    <text x="175" y="492" font-size="15" font-weight="900" fill="#26E7A6" text-anchor="middle">✓ TỰ TIN GIỮ LỆNH</text>
    <text x="175" y="510" font-size="13" font-weight="700" fill="#CAD4E0" text-anchor="middle">Xu hướng tăng rất bền vững</text>
  </g>

  <!-- ==================== CỘT 2: BẤT THƯỜNG / HẤP THỤ ==================== -->
  <g transform="translate(425, 80)" filter="url(#drop-shadow)">
    <rect width="350" height="540" rx="14" fill="#131824" stroke="#F23645" stroke-width="2"/>
    <rect x="0" y="0" width="350" height="50" rx="14 14 0 0" fill="#280A10"/>
    <text x="175" y="32" font-size="16" font-weight="900" fill="#FF707E" text-anchor="middle">2. BẤT THƯỜNG (HẤP THỤ)</text>

    <!-- KHU VỰC NẾN: NẾN ĐỨNG ĐỘC LẬP -->
    <g transform="translate(0, 65)">
      <!-- Nhãn ở trên -->
      <text x="175" y="20" font-size="14" font-weight="800" fill="#FF707E" text-anchor="middle">KẾT QUẢ: THÂN NẾN BÉ TÍ</text>

      <!-- Cây nến ngắn râu dài sạch sẽ -->
      <line x1="175" y1="35" x2="175" y2="195" stroke="#FF5252" stroke-width="4"/>
      <rect x="145" y="105" width="60" height="30" rx="3" fill="#F23645" stroke="#FF8A95" stroke-width="2" filter="url(#glow-red)"/>
    </g>

    <!-- Đường phân cách -->
    <line x1="25" y1="285" x2="325" y2="285" stroke="#223048" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- KHU VỰC VOLUME: VOLUME ĐỨNG ĐỘC LẬP -->
    <g transform="translate(0, 300)">
      <!-- Nhãn ở trên volume -->
      <text x="175" y="15" font-size="14" font-weight="800" fill="#FF5252" text-anchor="middle">NỖ LỰC: CỘT VOLUME CỰC ĐẠI</text>

      <!-- Cột Volume đỏ khổng lồ sạch sẽ -->
      <rect x="145" y="25" width="60" height="115" rx="4" fill="#F23645" filter="url(#glow-red)"/>
    </g>

    <!-- Khung hành động chân thẻ -->
    <rect x="20" y="465" width="310" height="55" rx="8" fill="#2E0A12" stroke="#FF5252" stroke-width="1.5"/>
    <text x="175" y="492" font-size="15" font-weight="900" fill="#FF707E" text-anchor="middle">⚠️ CẢNH BÁO ĐẢO CHIỀU!</text>
    <text x="175" y="510" font-size="13" font-weight="700" fill="#FFA4AC" text-anchor="middle">Có lực cản xả hàng khổng lồ</text>
  </g>

  <!-- ==================== CỘT 3: THIẾU HỤT NỖ LỰC ==================== -->
  <g transform="translate(805, 80)" filter="url(#drop-shadow)">
    <rect width="350" height="540" rx="14" fill="#131824" stroke="#F0B90B" stroke-width="2"/>
    <rect x="0" y="0" width="350" height="50" rx="14 14 0 0" fill="#251C08"/>
    <text x="175" y="32" font-size="16" font-weight="900" fill="#F0B90B" text-anchor="middle">3. THIẾU HỤT NỖ LỰC</text>

    <!-- KHU VỰC NẾN: NẾN ĐỨNG ĐỘC LẬP -->
    <g transform="translate(0, 65)">
      <!-- Nhãn ở trên -->
      <text x="175" y="20" font-size="14" font-weight="800" fill="#F0B90B" text-anchor="middle">KẾT QUẢ: GIÁ TĂNG RƯỚN</text>

      <!-- Cây nến tăng rướn sạch sẽ -->
      <line x1="175" y1="35" x2="175" y2="195" stroke="#CAD4E0" stroke-width="3"/>
      <rect x="145" y="55" width="60" height="110" rx="4" fill="#089981" stroke="#26E7A6" stroke-width="1.5"/>
    </g>

    <!-- Đường phân cách -->
    <line x1="25" y1="285" x2="325" y2="285" stroke="#223048" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- KHU VỰC VOLUME: VOLUME ĐỨNG ĐỘC LẬP -->
    <g transform="translate(0, 300)">
      <!-- Nhãn ở trên volume -->
      <text x="175" y="15" font-size="14" font-weight="800" fill="#8E9BAE" text-anchor="middle">NỖ LỰC: CỘT VOLUME TEO TÓP</text>

      <!-- Cột Volume thấp lè tè sạch sẽ -->
      <rect x="155" y="100" width="40" height="40" rx="3" fill="#687C94"/>
    </g>

    <!-- Khung hành động chân thẻ -->
    <rect x="20" y="465" width="310" height="55" rx="8" fill="#281F0A" stroke="#F0B90B" stroke-width="1.5"/>
    <text x="175" y="492" font-size="15" font-weight="900" fill="#F0B90B" text-anchor="middle">❌ KHÔNG FOMO MUA ĐUỔI</text>
    <text x="175" y="510" font-size="13" font-weight="700" fill="#CAD4E0" text-anchor="middle">Tăng ảo, cá mập không vào tiền</text>
  </g>

  <!-- LOGO WATERMARK -->
  <text x="600" y="650" font-size="14" font-weight="800" fill="#657795" text-anchor="middle">
    PTvolume.com • Wyckoff Effort vs Result
  </text>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_vsa_effort_result.svg"), "w", encoding="utf-8") as f:
    f.write(svg_vsa_fixed)
print("Saved FIXED naked_vsa_effort_result.svg")
