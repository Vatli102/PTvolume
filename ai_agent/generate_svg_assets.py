# -*- coding: utf-8 -*-
"""
Tạo lại 2 ảnh SVG cho Bài 1:
1. naked_chart_vs_indicators.svg:
   - Kích thước mở rộng: 1280 x 840 (rộng rãi, chữ to, rõ nét).
   - Tăng cỡ chữ lên 14px-18px (thay vì 10-12px cũ).
   - Chia các dòng văn bản dài thành các dòng ngắn 35-45 ký tự, đảm bảo KHÔNG BAO GIỜ bị tràn khung.
   - Minh họa trực quan: Camera trực tiếp (Live) vs Bản tin phát lại đi chậm.

2. naked_candlestick_and_vsa_mechanics.svg:
   - Kích thước mở rộng: 1280 x 840.
   - 3 thành tố nến và 3 trường hợp Nỗ lực - Kết quả (VSA).
   - Cỡ chữ to, rõ ràng, dễ đọc cho người mới (F0).
"""

import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

SVG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
os.makedirs(SVG_DIR, exist_ok=True)

# -------------------------------------------------------------
# SVG 1: NAKED CHART VS INDICATORS
# -------------------------------------------------------------
svg1_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 840" width="100%" height="100%" style="background:#0B0E14; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="bg-canvas" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0E14" />
      <stop offset="50%" stop-color="#141822" />
      <stop offset="100%" stop-color="#0E121B" />
    </linearGradient>
    <linearGradient id="card-left-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#241419" />
      <stop offset="100%" stop-color="#140C0F" />
    </linearGradient>
    <linearGradient id="card-right-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#10222D" />
      <stop offset="100%" stop-color="#0A151D" />
    </linearGradient>
    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.65"/>
    </filter>
  </defs>

  <!-- Nền Canvas -->
  <rect width="1280" height="840" fill="url(#bg-canvas)" rx="16"/>
  <rect width="1274" height="834" x="3" y="3" fill="none" stroke="#222938" stroke-width="2" rx="14"/>

  <!-- ==================== TIÊU ĐỀ CHÍNH ==================== -->
  <g transform="translate(640, 50)" text-anchor="middle">
    <rect x="-530" y="-30" width="1060" height="60" rx="30" fill="#141926" stroke="rgba(0, 229, 255, 0.5)" stroke-width="2"/>
    <text y="7" font-size="21" font-weight="800" fill="#00E5FF" letter-spacing="0.8">
      SO SÁNH THỰC TẾ: BẪY CHỈ BÁO ĐI CHẬM vs BIỂU ĐỒ TRẦN NGUYÊN BẢN
    </text>
    <text y="46" font-size="14" fill="#CAD4E0">
      Khóa Học Naked Chart, VSA &amp; Phương Pháp Wyckoff • Độc Quyền PTvolume.com
    </text>
  </g>

  <!-- ==================== CỘT TRÁI: BẪY CHỈ BÁO TRỄ ==================== -->
  <g transform="translate(45, 115)" filter="url(#card-shadow)">
    <!-- Khung Card -->
    <rect width="575" height="665" rx="16" fill="url(#card-left-grad)" stroke="#F23645" stroke-width="2"/>
    
    <!-- Tiêu Đề Cột -->
    <rect width="575" height="54" rx="16" fill="#F23645" fill-opacity="0.25"/>
    <path d="M 0 38 L 0 54 L 575 54 L 575 38 Z" fill="#F23645" fill-opacity="0.25"/>
    <circle cx="32" cy="27" r="14" fill="#F23645"/>
    <text x="32" y="32" font-size="14" font-weight="900" fill="#FFFFFF" text-anchor="middle">✕</text>
    <text x="58" y="33" font-size="16" font-weight="800" fill="#FF6B7A">BẪY CHỈ BÁO: TÍN HIỆU ĐI CHẬM &amp; GÂY RỐI MẮT</text>

    <!-- Khung mô phỏng biểu đồ bị che khuất -->
    <g transform="translate(24, 72)">
      <rect width="527" height="155" rx="10" fill="#080B10" stroke="#451B22" stroke-width="1.5"/>
      
      <!-- Cây nến bị mờ nhạt phía dưới -->
      <g opacity="0.25">
        <line x1="50" y1="50" x2="50" y2="105" stroke="#CAD4E0" stroke-width="2"/>
        <line x1="100" y1="40" x2="100" y2="95" stroke="#CAD4E0" stroke-width="2"/>
        <line x1="150" y1="65" x2="150" y2="120" stroke="#CAD4E0" stroke-width="2"/>
        <line x1="200" y1="35" x2="200" y2="90" stroke="#CAD4E0" stroke-width="2"/>
        <line x1="250" y1="50" x2="250" y2="100" stroke="#CAD4E0" stroke-width="2"/>
        <line x1="300" y1="75" x2="300" y2="125" stroke="#CAD4E0" stroke-width="2"/>
        <line x1="350" y1="55" x2="350" y2="105" stroke="#CAD4E0" stroke-width="2"/>
        <line x1="400" y1="40" x2="400" y2="85" stroke="#CAD4E0" stroke-width="2"/>
        <line x1="450" y1="60" x2="450" y2="110" stroke="#CAD4E0" stroke-width="2"/>
        <line x1="490" y1="45" x2="490" y2="95" stroke="#CAD4E0" stroke-width="2"/>
      </g>

      <!-- Các đường chỉ báo chằng chịt che mất nến -->
      <path d="M 15 35 Q 130 25 260 55 T 510 35" fill="none" stroke="#FF9800" stroke-width="2" stroke-dasharray="4,4" opacity="0.85"/>
      <path d="M 15 125 Q 130 135 260 105 T 510 130" fill="none" stroke="#FF9800" stroke-width="2" stroke-dasharray="4,4" opacity="0.85"/>
      <path d="M 15 80 Q 140 45 270 90 T 510 65" fill="none" stroke="#2962FF" stroke-width="2.5"/>
      <path d="M 15 95 Q 160 105 290 70 T 510 85" fill="none" stroke="#E91E63" stroke-width="2.5"/>
      <path d="M 15 110 Q 200 90 340 100 T 510 92" fill="none" stroke="#9C27B0" stroke-width="3"/>
      <path d="M 25 115 L 90 45 L 170 95 L 250 35 L 350 110 L 480 50" fill="none" stroke="#00E676" stroke-width="2" opacity="0.75"/>

      <!-- Nhãn cảnh báo -->
      <rect x="18" y="10" width="265" height="26" rx="5" fill="rgba(11,14,20,0.9)" stroke="#F23645" stroke-width="1"/>
      <text x="26" y="27" font-size="12" font-family="monospace" font-weight="700" fill="#FF707E">EMA20, EMA50, EMA200, BB, RSI, MACD...</text>

      <rect x="295" y="118" width="215" height="28" rx="6" fill="rgba(242,54,69,0.9)"/>
      <text x="402" y="136" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle">⚠️ KHÔNG NHÌN THẤY GIÁ THẬT!</text>
    </g>

    <!-- Danh sách các nhược điểm (Chữ to, chia dòng ngắn, KHÔNG TRÀN KHUNG) -->
    <g transform="translate(26, 248)">
      <!-- Nhược điểm 1 -->
      <g transform="translate(0, 0)">
        <circle cx="10" cy="12" r="6" fill="#F23645"/>
        <text x="26" y="17" font-size="15" font-weight="800" fill="#FFFFFF">1. Tín hiệu luôn đi chậm hơn giá thực tế:</text>
        <text x="26" y="40" font-size="14" fill="#CAD4E0">Chỉ báo lấy giá cũ tính ra. Khi chỉ báo báo Mua thì giá</text>
        <text x="26" y="60" font-size="14" fill="#CAD4E0">đã tăng lên đỉnh; chỉ báo báo Bán thì giá đã chạm đáy.</text>
      </g>

      <!-- Nhược điểm 2 -->
      <g transform="translate(0, 84)">
        <circle cx="10" cy="12" r="6" fill="#F23645"/>
        <text x="26" y="17" font-size="15" font-weight="800" fill="#FFFFFF">2. Tín hiệu mâu thuẫn, gây rối trí (Tê liệt tâm lý):</text>
        <text x="26" y="40" font-size="14" fill="#CAD4E0">Đường này khuyên Mua, đường kia lại khuyên Bán.</text>
        <text x="26" y="60" font-size="14" fill="#CAD4E0">Trader hoang mang, chần chừ và bỏ lỡ nhịp vào lệnh đẹp.</text>
      </g>

      <!-- Nhược điểm 3 -->
      <g transform="translate(0, 168)">
        <circle cx="10" cy="12" r="6" fill="#F23645"/>
        <text x="26" y="17" font-size="15" font-weight="800" fill="#FFFFFF">3. Mù tịt trước các bẫy giá của Tay To (Smart Money):</text>
        <text x="26" y="40" font-size="14" fill="#CAD4E0">Chỉ báo không thể nhìn thấy các cú quét râu nến lừa</text>
        <text x="26" y="60" font-size="14" fill="#CAD4E0">và hành vi âm thầm gom hàng của các quỹ lớn.</text>
      </g>

      <!-- Nhược điểm 4 -->
      <g transform="translate(0, 252)">
        <circle cx="10" cy="12" r="6" fill="#F23645"/>
        <text x="26" y="17" font-size="15" font-weight="800" fill="#FFFFFF">4. Mắc kẹt trong vòng xoay tìm "Chén thánh":</text>
        <text x="26" y="40" font-size="14" fill="#CAD4E0">Thua lỗ lại đi tìm chỉ báo mới, tải thêm bot và hệ thống,</text>
        <text x="26" y="60" font-size="14" fill="#CAD4E0">càng phụ thuộc công cụ thì càng mất phương hướng.</text>
      </g>
    </g>

    <!-- Lời kết chân thực góc dưới -->
    <rect x="24" y="595" width="527" height="48" rx="8" fill="rgba(242,54,69,0.15)" stroke="rgba(242,54,69,0.35)"/>
    <text x="287" y="624" font-size="13.5" font-weight="700" fill="#FF8A95" text-anchor="middle">
      Hậu quả: Vào lệnh trễ, đu đỉnh bán đáy, tâm lý mệt mỏi!
    </text>
  </g>

  <!-- ==================== CỘT PHẢI: BIỂU ĐỒ TRẦN NGUYÊN BẢN ==================== -->
  <g transform="translate(660, 115)" filter="url(#card-shadow)">
    <!-- Khung Card -->
    <rect width="575" height="665" rx="16" fill="url(#card-right-grad)" stroke="#00E5FF" stroke-width="2"/>
    
    <!-- Tiêu Đề Cột -->
    <rect width="575" height="54" rx="16" fill="#00E5FF" fill-opacity="0.2"/>
    <path d="M 0 38 L 0 54 L 575 54 L 575 38 Z" fill="#00E5FF" fill-opacity="0.2"/>
    <circle cx="32" cy="27" r="14" fill="#089981"/>
    <text x="32" y="32" font-size="14" font-weight="900" fill="#FFFFFF" text-anchor="middle">✓</text>
    <text x="58" y="33" font-size="16" font-weight="800" fill="#00E5FF">BIỂU ĐỒ TRẦN: ĐỌC GIÁ TRỰC TIẾP &amp; RÕ RÀNG</text>

    <!-- Khung mô phỏng biểu đồ sạch sẽ -->
    <g transform="translate(24, 72)">
      <rect width="527" height="155" rx="10" fill="#080B10" stroke="#183644" stroke-width="1.5"/>
      
      <!-- Vùng Cung Cản Trên -->
      <rect x="4" y="10" width="519" height="22" fill="rgba(242,54,69,0.14)" stroke="rgba(242,54,69,0.35)" stroke-dasharray="3,3"/>
      <text x="510" y="25" font-size="11" fill="#FF707E" text-anchor="end" font-weight="700">VÙNG CUNG (PHE BÁN CHỜ SẴN)</text>

      <!-- Các cây nến rõ nét -->
      <!-- Nến 1 Xanh -->
      <line x1="55" y1="85" x2="55" y2="125" stroke="#089981" stroke-width="2.5"/>
      <rect x="46" y="92" width="18" height="26" fill="#089981" rx="1.5"/>

      <!-- Nến 2 Xanh -->
      <line x1="115" y1="70" x2="115" y2="115" stroke="#089981" stroke-width="2.5"/>
      <rect x="106" y="75" width="18" height="30" fill="#089981" rx="1.5"/>

      <!-- Nến 3 Đỏ Nhỏ -->
      <line x1="175" y1="75" x2="175" y2="108" stroke="#F23645" stroke-width="2.5"/>
      <rect x="166" y="80" width="18" height="18" fill="#F23645" rx="1.5"/>

      <!-- Nến 4 Xanh Mạnh -->
      <line x1="240" y1="38" x2="240" y2="92" stroke="#089981" stroke-width="2.5"/>
      <rect x="231" y="44" width="18" height="42" fill="#089981" rx="1.5"/>

      <!-- Nến 5 Pin Bar Từ Chối Giá -->
      <line x1="310" y1="12" x2="310" y2="78" stroke="#CAD4E0" stroke-width="2.5"/>
      <rect x="301" y="54" width="18" height="16" fill="#F23645" rx="1.5"/>
      <text x="310" y="8" font-size="10" fill="#00E5FF" text-anchor="middle" font-weight="800">Pin Bar từ chối giá!</text>

      <!-- Nến 6 Đỏ Đảo Chiều -->
      <line x1="380" y1="60" x2="380" y2="120" stroke="#F23645" stroke-width="2.5"/>
      <rect x="371" y="65" width="18" height="48" fill="#F23645" rx="1.5"/>

      <!-- Nến 7 Đỏ Tiếp Tục -->
      <line x1="450" y1="80" x2="450" y2="135" stroke="#F23645" stroke-width="2.5"/>
      <rect x="441" y="90" width="18" height="38" fill="#F23645" rx="1.5"/>

      <!-- Cột Khối Lượng Dưới Đáy -->
      <line x1="10" y1="128" x2="517" y2="128" stroke="#222938" stroke-width="1.2"/>
      <rect x="49" y="136" width="12" height="12" fill="#089981" opacity="0.8"/>
      <rect x="109" y="132" width="12" height="16" fill="#089981" opacity="0.9"/>
      <rect x="169" y="142" width="12" height="6" fill="#F23645" opacity="0.6"/>
      <rect x="234" y="130" width="12" height="18" fill="#089981" opacity="0.95"/>
      <rect x="304" y="127" width="12" height="21" fill="#F0B90B"/>
      <rect x="374" y="129" width="12" height="19" fill="#F23645"/>
      <rect x="444" y="133" width="12" height="15" fill="#F23645"/>

      <text x="18" y="145" font-size="10" fill="#F0B90B" font-weight="800">VOLUME</text>
    </g>

    <!-- Danh sách các ưu điểm (Chữ to, chia dòng ngắn, KHÔNG TRÀN KHUNG) -->
    <g transform="translate(26, 248)">
      <!-- Ưu điểm 1 -->
      <g transform="translate(0, 0)">
        <circle cx="10" cy="12" r="6" fill="#00E5FF"/>
        <text x="26" y="17" font-size="15" font-weight="800" fill="#FFFFFF">1. Phản ánh thị trường theo thời gian thực (Zero Lag):</text>
        <text x="26" y="40" font-size="14" fill="#CAD4E0">Thanh nến và khối lượng phản ánh ngay tức thì</text>
        <text x="26" y="60" font-size="14" fill="#CAD4E0">cuộc chiến mua bán thực đang diễn ra ngay lúc này.</text>
      </g>

      <!-- Ưu điểm 2 -->
      <g transform="translate(0, 84)">
        <circle cx="10" cy="12" r="6" fill="#00E5FF"/>
        <text x="26" y="17" font-size="15" font-weight="800" fill="#FFFFFF">2. Nhìn thấu hành vi từ chối giá qua râu nến:</text>
        <text x="26" y="40" font-size="14" fill="#CAD4E0">Râu nến dài báo hiệu phe nào vừa nhảy vào chặn đứng</text>
        <text x="26" y="60" font-size="14" fill="#CAD4E0">đà giá, giúp bạn phát hiện điểm đảo chiều cực sớm.</text>
      </g>

      <!-- Ưu điểm 3 -->
      <g transform="translate(0, 168)">
        <circle cx="10" cy="12" r="6" fill="#00E5FF"/>
        <text x="26" y="17" font-size="15" font-weight="800" fill="#FFFFFF">3. Nhận biết dòng tiền lớn qua Khối lượng (VSA):</text>
        <text x="26" y="40" font-size="14" fill="#CAD4E0">Thân nến kết hợp cột Volume giúp bóc trần những cây nến</text>
        <text x="26" y="60" font-size="14" fill="#CAD4E0">lừa gạt, biết chính xác khi nào Tay To đang âm thầm gom.</text>
      </g>

      <!-- Ưu điểm 4 -->
      <g transform="translate(0, 252)">
        <circle cx="10" cy="12" r="6" fill="#00E5FF"/>
        <text x="26" y="17" font-size="15" font-weight="800" fill="#FFFFFF">4. Điểm vào lệnh chuẩn xác, Cắt lỗ cực ngắn:</text>
        <text x="26" y="40" font-size="14" fill="#CAD4E0">Vào lệnh sát các ngưỡng cản then chốt giúp bạn có</text>
        <text x="26" y="60" font-size="14" fill="#CAD4E0">mức dừng lỗ rất nhỏ, tỷ lệ Lời/Lỗ (R:R) từ 1:3 trở lên.</text>
      </g>
    </g>

    <!-- Lời kết chân thực góc dưới -->
    <rect x="24" y="595" width="527" height="48" rx="8" fill="rgba(0,229,255,0.12)" stroke="rgba(0,229,255,0.35)"/>
    <text x="287" y="624" font-size="13.5" font-weight="700" fill="#00E5FF" text-anchor="middle">
      Lợi thế: Nhìn rõ sự thật, vào lệnh tự tin, tâm lý thoải mái!
    </text>
  </g>

  <!-- ==================== CHÂN TRANG WATERMARK BẢN QUYỀN ==================== -->
  <g transform="translate(640, 810)" text-anchor="middle">
    <text font-size="13.5" fill="#CAD4E0" font-weight="600">
      Đóng dấu bản quyền: <tspan fill="#00E5FF" font-weight="800">PTvolume.com</tspan> • Chuyên Trang Naked Chart, Volume Spread Analysis &amp; Wyckoff
    </text>
  </g>
</svg>
"""

with open(os.path.join(SVG_DIR, "naked_chart_vs_indicators.svg"), "w", encoding="utf-8") as f:
    f.write(svg1_content.strip())
print("Saved naked_chart_vs_indicators.svg successfully.")


# -------------------------------------------------------------
# SVG 2: NAKED CANDLESTICK & VSA MECHANICS
# -------------------------------------------------------------
svg2_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 840" width="100%" height="100%" style="background:#0B0E14; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="bg-canvas-2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0E14" />
      <stop offset="50%" stop-color="#141822" />
      <stop offset="100%" stop-color="#0E121B" />
    </linearGradient>
    <linearGradient id="card-grad-a" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#122033" />
      <stop offset="100%" stop-color="#0B1522" />
    </linearGradient>
    <linearGradient id="card-grad-b" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#242013" />
      <stop offset="100%" stop-color="#14120B" />
    </linearGradient>
    <filter id="card-shadow-2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.65"/>
    </filter>
  </defs>

  <!-- Nền Canvas -->
  <rect width="1280" height="840" fill="url(#bg-canvas-2)" rx="16"/>
  <rect width="1274" height="834" x="3" y="3" fill="none" stroke="#222938" stroke-width="2" rx="14"/>

  <!-- ==================== TIÊU ĐỀ CHÍNH ==================== -->
  <g transform="translate(640, 50)" text-anchor="middle">
    <rect x="-530" y="-30" width="1060" height="60" rx="30" fill="#141926" stroke="rgba(240, 185, 11, 0.5)" stroke-width="2"/>
    <text y="7" font-size="21" font-weight="800" fill="#F0B90B" letter-spacing="0.8">
      GIẢI PHẪU NẾN TRẦN &amp; NGUYÊN LÝ NỖ LỰC - KẾT QUẢ DỄ HIỂU NHẤT
    </text>
    <text y="46" font-size="14" fill="#CAD4E0">
      Cách Đọc Vị Nến Nhật Cùng Khối Lượng VSA Chuẩn PTvolume.com Cho Người Mới
    </text>
  </g>

  <!-- ==================== CỘT TRÁI: 3 BỘ PHẬN CỐT LÕI CỦA NẾN ==================== -->
  <g transform="translate(45, 115)" filter="url(#card-shadow-2)">
    <rect width="575" height="665" rx="16" fill="url(#card-grad-a)" stroke="#2962FF" stroke-width="2"/>
    
    <!-- Tiêu đề Cột Trái -->
    <rect width="575" height="54" rx="16" fill="#2962FF" fill-opacity="0.25"/>
    <path d="M 0 38 L 0 54 L 575 54 L 575 38 Z" fill="#2962FF" fill-opacity="0.25"/>
    <circle cx="32" cy="27" r="14" fill="#2962FF"/>
    <text x="32" y="32" font-size="14" font-weight="900" fill="#FFFFFF" text-anchor="middle">1</text>
    <text x="58" y="33" font-size="16" font-weight="800" fill="#75A5FF">3 BỘ PHẬN CỐT LÕI CỦA MỘT CÂY NẾN TRẦN</text>

    <!-- Hình vẽ Cây Nến Minh Họa To Rõ -->
    <g transform="translate(45, 80)">
      <!-- Râu trên -->
      <line x1="95" y1="15" x2="95" y2="75" stroke="#CAD4E0" stroke-width="3.5"/>
      <!-- Thân nến -->
      <rect x="73" y="75" width="44" height="130" fill="#089981" rx="2" stroke="#26E7A6" stroke-width="2"/>
      <!-- Râu dưới -->
      <line x1="95" y1="205" x2="95" y2="280" stroke="#CAD4E0" stroke-width="3.5"/>

      <!-- Vạch đóng cửa -->
      <line x1="70" y1="75" x2="165" y2="75" stroke="#00E5FF" stroke-width="2.5" stroke-dasharray="4,4"/>
      <circle cx="165" cy="75" r="4.5" fill="#00E5FF"/>

      <!-- Chú thích Râu Trên -->
      <path d="M 105 38 L 175 38" fill="none" stroke="#F0B90B" stroke-width="2"/>
      <circle cx="175" cy="38" r="3.5" fill="#F0B90B"/>
      <text x="188" y="35" font-size="14" font-weight="800" fill="#F0B90B">Bóng nến trên (Râu trên)</text>
      <text x="188" y="55" font-size="13" fill="#CAD4E0">Vùng giá bị phe Bán từ chối và đẩy lùi xuống.</text>

      <!-- Chú thích Mức Đóng Cửa -->
      <text x="188" y="80" font-size="14" font-weight="800" fill="#00E5FF">Mức giá đóng cửa (Close)</text>
      <text x="188" y="100" font-size="13" fill="#CAD4E0">Kết quả cuối cùng: Phe nào thắng thế khi kết phiên?</text>

      <!-- Chú thích Thân Nến -->
      <path d="M 55 75 L 35 75 L 35 205 L 55 205" fill="none" stroke="#26E7A6" stroke-width="2"/>
      <text x="22" y="135" font-size="14" font-weight="900" fill="#26E7A6" text-anchor="end">THÂN NẾN</text>
      <text x="22" y="155" font-size="12.5" fill="#CAD4E0" text-anchor="end">(Biên độ giá)</text>

      <!-- Chú thích Râu Dưới -->
      <path d="M 105 245 L 175 245" fill="none" stroke="#F0B90B" stroke-width="2"/>
      <circle cx="175" cy="245" r="3.5" fill="#F0B90B"/>
      <text x="188" y="242" font-size="14" font-weight="800" fill="#F0B90B">Bóng nến dưới (Râu dưới)</text>
      <text x="188" y="262" font-size="13" fill="#CAD4E0">Vùng phe Mua nhảy vào bắt đáy đỡ giá mạnh.</text>
    </g>

    <!-- 3 Thẻ tóm tắt ý nghĩa thực chiến (Chữ to, thoáng, KHÔNG TRÀN) -->
    <g transform="translate(24, 385)">
      <!-- Thẻ 1 -->
      <rect width="527" height="78" rx="8" fill="#0F1826" stroke="#22334D" stroke-width="1.2"/>
      <text x="18" y="28" font-size="14.5" font-weight="800" fill="#FFFFFF">• Thân Nến Dài (Biên độ rộng):</text>
      <text x="18" y="52" font-size="13.5" fill="#26E7A6">Chứng tỏ một bên đang hoàn toàn kiểm soát và áp đảo thế trận.</text>

      <!-- Thẻ 2 -->
      <rect y="90" width="527" height="78" rx="8" fill="#0F1826" stroke="#22334D" stroke-width="1.2"/>
      <text x="18" y="118" font-size="14.5" font-weight="800" fill="#FFFFFF">• Râu Nến Dài Vượt Trội:</text>
      <text x="18" y="142" font-size="13.5" fill="#F0B90B">Cho thấy có lực đối kháng khổng lồ vừa đảo ngược cục diện phiên giao dịch.</text>

      <!-- Thẻ 3 -->
      <rect y="180" width="527" height="78" rx="8" fill="#0F1826" stroke="#22334D" stroke-width="1.2"/>
      <text x="18" y="208" font-size="14.5" font-weight="800" fill="#FFFFFF">• Giá Đóng Cửa Sát Đỉnh / Đáy:</text>
      <text x="18" y="232" font-size="13.5" fill="#00E5FF">Dấu hiệu khẳng định đà tăng hoặc đà giảm sẽ còn tiếp diễn mạnh mẽ.</text>
    </g>
  </g>

  <!-- ==================== CỘT PHẢI: QUY LUẬT NỖ LỰC VS KẾT QUẢ ==================== -->
  <g transform="translate(660, 115)" filter="url(#card-shadow-2)">
    <rect width="575" height="665" rx="16" fill="url(#card-grad-b)" stroke="#F0B90B" stroke-width="2"/>
    
    <!-- Tiêu đề Cột Phải -->
    <rect width="575" height="54" rx="16" fill="#F0B90B" fill-opacity="0.25"/>
    <path d="M 0 38 L 0 54 L 575 54 L 575 38 Z" fill="#F0B90B" fill-opacity="0.25"/>
    <circle cx="32" cy="27" r="14" fill="#F0B90B"/>
    <text x="32" y="32" font-size="14" font-weight="900" fill="#0B0E14" text-anchor="middle">2</text>
    <text x="58" y="33" font-size="16" font-weight="800" fill="#F0B90B">QUY LUẬT NỖ LỰC vs KẾT QUẢ (NẾN + VOLUME)</text>

    <!-- 3 Trường hợp so sánh VSA -->
    <g transform="translate(24, 72)">
      <!-- Trường hợp 1: Đồng thuận -->
      <rect width="527" height="180" rx="10" fill="#0D1D18" stroke="rgba(8, 153, 129, 0.45)" stroke-width="1.5"/>
      <g transform="translate(20, 18)">
        <!-- Nến và Volume minh họa -->
        <line x1="22" y1="5" x2="22" y2="85" stroke="#089981" stroke-width="2.5"/>
        <rect x="12" y="14" width="20" height="60" fill="#089981" rx="1.5"/>
        <rect x="14" y="98" width="16" height="34" fill="#089981"/>
        <text x="22" y="146" font-size="10" fill="#089981" font-weight="800" text-anchor="middle">VOL LỚN</text>

        <!-- Nội dung giải thích -->
        <text x="58" y="24" font-size="15" font-weight="800" fill="#26E7A6">1. ĐỒNG THUẬN: NỖ LỰC LỚN = KẾT QUẢ LỚN</text>
        <text x="58" y="50" font-size="13.5" fill="#CAD4E0">• Biểu hiện: Thân nến dài đi kèm Cột khối lượng tăng vọt.</text>
        <text x="58" y="74" font-size="13.5" fill="#CAD4E0">• Ý nghĩa: Dòng tiền lớn đẩy giá thực chất, thị trường đồng lòng.</text>
        <text x="58" y="100" font-size="13.5" fill="#00E5FF" font-weight="700">→ Hành động: Tự tin giữ lệnh, đi theo xu hướng (Thuận buồm xuôi gió).</text>
        <text x="58" y="124" font-size="12.5" fill="#8E9BAE">Ví dụ: Đột phá cản thành công với lực mua áp đảo.</text>
      </g>

      <!-- Trường hợp 2: Bất thường -->
      <rect y="196" width="527" height="186" rx="10" fill="#261418" stroke="rgba(242, 54, 69, 0.45)" stroke-width="1.5"/>
      <g transform="translate(20, 212)">
        <!-- Nến và Volume minh họa -->
        <line x1="22" y1="5" x2="22" y2="85" stroke="#CAD4E0" stroke-width="2.5"/>
        <rect x="12" y="38" width="20" height="18" fill="#F23645" rx="1.5"/>
        <rect x="14" y="98" width="16" height="38" fill="#F0B90B"/>
        <text x="22" y="148" font-size="10" fill="#F0B90B" font-weight="800" text-anchor="middle">VOL KHỦNG</text>

        <!-- Nội dung giải thích -->
        <text x="58" y="24" font-size="15" font-weight="800" fill="#FF707E">2. BẤT THƯỜNG: NỖ LỰC CỰC LỚN NHƯNG KẾT QUẢ NHỎ</text>
        <text x="58" y="50" font-size="13.5" fill="#CAD4E0">• Biểu hiện: Nến thân bé tí nhưng Khối lượng lại to đột biến.</text>
        <text x="58" y="74" font-size="13.5" fill="#CAD4E0">• Ý nghĩa: Có lực cản ngầm khổng lồ đang âm thầm hấp thụ hết lực mua.</text>
        <text x="58" y="100" font-size="13.5" fill="#F0B90B" font-weight="700">→ Cảnh báo: Nguy cơ đảo chiều sắp tới, cẩn thận bẫy giá Tay To!</text>
        <text x="58" y="124" font-size="12.5" fill="#8E9BAE">Ví dụ: Mua ráng sức nhưng không tăng nổi vì bên bán xả ồ ạt.</text>
      </g>

      <!-- Trường hợp 3: Thiếu nỗ lực -->
      <rect y="398" width="527" height="180" rx="10" fill="#141926" stroke="rgba(0, 229, 255, 0.35)" stroke-width="1.5"/>
      <g transform="translate(20, 414)">
        <!-- Nến và Volume minh họa -->
        <line x1="22" y1="5" x2="22" y2="85" stroke="#CAD4E0" stroke-width="2.5"/>
        <rect x="12" y="24" width="20" height="42" fill="#089981" opacity="0.65" rx="1.5"/>
        <rect x="14" y="118" width="16" height="14" fill="#8E9BAE" opacity="0.5"/>
        <text x="22" y="146" font-size="10" fill="#8E9BAE" font-weight="800" text-anchor="middle">VOL TÈO</text>

        <!-- Nội dung giải thích -->
        <text x="58" y="24" font-size="15" font-weight="800" fill="#00E5FF">3. THIẾU NỖ LỰC: GIÁ CHẠY NHƯNG KHỐI LƯỢNG TỤT DỐC</text>
        <text x="58" y="50" font-size="13.5" fill="#CAD4E0">• Biểu hiện: Giá vẫn cố rướn tăng nhưng Khối lượng cạn kiệt dần.</text>
        <text x="58" y="74" font-size="13.5" fill="#CAD4E0">• Ý nghĩa: Tay To không tham gia; chỉ là vài nhà đầu tư nhỏ lẻ mua đuổi.</text>
        <text x="58" y="100" font-size="13.5" fill="#FF707E" font-weight="700">→ Cấm kỵ: Tuyệt đối không FOMO mua đuổi, cú tăng này rất dễ sập!</text>
        <text x="58" y="124" font-size="12.5" fill="#8E9BAE">Ví dụ: Tăng giá trong nghi ngờ nhưng không có tiền thật bảo chứng.</text>
      </g>
    </g>
  </g>

  <!-- ==================== CHÂN TRANG WATERMARK BẢN QUYỀN ==================== -->
  <g transform="translate(640, 810)" text-anchor="middle">
    <text font-size="13.5" fill="#CAD4E0" font-weight="600">
      Đóng dấu bản quyền: <tspan fill="#00E5FF" font-weight="800">PTvolume.com</tspan> • Khóa Học Naked Chart, VSA &amp; Phương Pháp Wyckoff
    </text>
  </g>
</svg>
"""

with open(os.path.join(SVG_DIR, "naked_candlestick_and_vsa_mechanics.svg"), "w", encoding="utf-8") as f:
    f.write(svg2_content.strip())
print("Saved naked_candlestick_and_vsa_mechanics.svg successfully.")
