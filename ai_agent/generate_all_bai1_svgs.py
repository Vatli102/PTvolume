# -*- coding: utf-8 -*-
"""
Tạo bộ 5 ảnh SVG chuyên sâu cho Bài 1 của PTvolume.com:
1. naked_chart_indicator_trap.svg (Mục 1: Bẫy chỉ báo đi chậm & nhiễu loạn)
2. naked_chart_clean_workspace.svg (Mục 2: Không gian biểu đồ trần nguyên bản & vùng Cung Cầu)
3. naked_chart_setup_3_steps.svg (Mục 3: 3 Bước thiết lập biểu đồ trần chuẩn TradingView)
4. naked_candlestick_structure.svg (Mục 4: Bóc tách 3 bộ phận cốt lõi của nến trần)
5. naked_vsa_effort_result.svg (Mục 5: 3 Kịch bản đối chiếu Nỗ lực vs Kết quả VSA)
Tất cả hình đều có kích thước lớn 1280px, chữ to rõ (14px-20px), KHÔNG TRÀN KHUNG, có Watermark PTvolume.com.
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

SVG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
os.makedirs(SVG_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. HÌNH MỤC 1: BẪY CHỈ BÁO ĐI CHẬM
# -------------------------------------------------------------
svg1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="100%" height="100%" style="background:#0B0E14; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="bg-canvas-1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0E14" />
      <stop offset="50%" stop-color="#141822" />
      <stop offset="100%" stop-color="#0E121B" />
    </linearGradient>
    <linearGradient id="box-warn" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#261418" />
      <stop offset="100%" stop-color="#140C0F" />
    </linearGradient>
    <filter id="shadow-1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1280" height="720" fill="url(#bg-canvas-1)" rx="16"/>
  <rect width="1274" height="714" x="3" y="3" fill="none" stroke="#222938" stroke-width="2" rx="14"/>

  <!-- Tiêu đề -->
  <g transform="translate(640, 45)" text-anchor="middle">
    <rect x="-480" y="-25" width="960" height="50" rx="25" fill="#141926" stroke="rgba(242, 54, 69, 0.4)" stroke-width="1.8"/>
    <text y="7" font-size="19" font-weight="800" fill="#FF707E" letter-spacing="0.5">
      BẪY CHỈ BÁO: TÍN HIỆU ĐI CHẬM HƠN GIÁ THỰC TẾ &amp; HẬU QUẢ VỚI F0
    </text>
  </g>

  <!-- So sánh 2 bên: Camera Trực Tiếp vs Bản Tin Phát Lại -->
  <!-- Bên Trái: Nến Thực Tế (Live Camera) -->
  <g transform="translate(50, 95)" filter="url(#shadow-1)">
    <rect width="560" height="555" rx="14" fill="#0D1E26" stroke="#00E5FF" stroke-width="2"/>
    <rect width="560" height="48" rx="14" fill="#00E5FF" fill-opacity="0.2"/>
    <path d="M 0 34 L 0 48 L 560 48 L 560 34 Z" fill="#00E5FF" fill-opacity="0.2"/>
    <circle cx="28" cy="24" r="12" fill="#089981"/>
    <text x="28" y="28" font-size="13" font-weight="900" fill="#FFFFFF" text-anchor="middle">✓</text>
    <text x="50" y="29" font-size="15.5" font-weight="800" fill="#00E5FF">GIÁ NGUYÊN BẢN: CAMERA TRỰC TIẾP (LIVE STREAM)</text>

    <!-- Biểu đồ nến thật -->
    <g transform="translate(20, 65)">
      <rect width="520" height="150" rx="8" fill="#080B10" stroke="#16303D" stroke-width="1.2"/>
      
      <!-- Cây nến đang chạy tăng -->
      <line x1="60" y1="90" x2="60" y2="130" stroke="#089981" stroke-width="2.5"/>
      <rect x="51" y="95" width="18" height="28" fill="#089981" rx="1.5"/>

      <line x1="120" y1="75" x2="120" y2="120" stroke="#089981" stroke-width="2.5"/>
      <rect x="111" y="80" width="18" height="32" fill="#089981" rx="1.5"/>

      <line x1="180" y1="50" x2="180" y2="105" stroke="#089981" stroke-width="2.5"/>
      <rect x="171" y="55" width="18" height="42" fill="#089981" rx="1.5"/>

      <!-- Nến bứt phá mạnh ngay lúc này -->
      <line x1="240" y1="20" x2="240" y2="85" stroke="#089981" stroke-width="3"/>
      <rect x="230" y="25" width="20" height="52" fill="#089981" rx="1.5"/>

      <circle cx="240" cy="22" r="5" fill="#00E5FF"/>
      <text x="252" y="26" font-size="12" fill="#00E5FF" font-weight="700">Giá đang chạy NGAY TẠI GIÂY NÀY!</text>

      <!-- Volume tương ứng -->
      <line x1="10" y1="125" x2="510" y2="125" stroke="#1c2436"/>
      <rect x="54" y="132" width="12" height="14" fill="#089981"/>
      <rect x="114" y="130" width="12" height="16" fill="#089981"/>
      <rect x="174" y="126" width="12" height="20" fill="#089981"/>
      <rect x="234" y="120" width="12" height="26" fill="#00E5FF"/>
      <text x="18" y="142" font-size="9.5" fill="#00E5FF" font-weight="800">VOLUME</text>
    </g>

    <!-- Điểm mạnh cốt lõi -->
    <g transform="translate(24, 235)">
      <rect width="512" height="65" rx="8" fill="#0B161F" stroke="#183648"/>
      <text x="16" y="25" font-size="14" font-weight="800" fill="#FFFFFF">• Phản ánh ngay lập tức (Không trễ nhịp):</text>
      <text x="16" y="48" font-size="13.5" fill="#26E7A6">Từng lệnh mua bán khớp tại thời điểm thực đều hiện lên nến.</text>

      <rect y="76" width="512" height="65" rx="8" fill="#0B161F" stroke="#183648"/>
      <text x="16" y="101" font-size="14" font-weight="800" fill="#FFFFFF">• Thấy rõ điểm bắt đầu bứt phá (Early Entry):</text>
      <text x="16" y="124" font-size="13.5" fill="#00E5FF">Vào lệnh sớm ngay chân sóng, điểm dừng lỗ (Stop Loss) siêu ngắn.</text>

      <rect y="152" width="512" height="65" rx="8" fill="#0B161F" stroke="#183648"/>
      <text x="16" y="177" font-size="14" font-weight="800" fill="#FFFFFF">• Nhận diện áp lực mua/bán thực chất:</text>
      <text x="16" y="200" font-size="13.5" fill="#CAD4E0">Khối lượng đi cùng nến xác nhận dòng tiền thật của cá mập.</text>

      <rect y="228" width="512" height="65" rx="8" fill="#0B161F" stroke="#183648"/>
      <text x="16" y="253" font-size="14" font-weight="800" fill="#FFFFFF">• Không bị nhiễu sóng và không phân tâm:</text>
      <text x="16" y="276" font-size="13.5" fill="#F0B90B">Tâm lý sáng suốt, không bị các tín hiệu giả đánh lừa.</text>
    </g>
  </g>

  <!-- Bên Phải: Chỉ Báo Trễ (Delayed Broadcast) -->
  <g transform="translate(670, 95)" filter="url(#shadow-1)">
    <rect width="560" height="555" rx="14" fill="url(#box-warn)" stroke="#F23645" stroke-width="2"/>
    <rect width="560" height="48" rx="14" fill="#F23645" fill-opacity="0.25"/>
    <path d="M 0 34 L 0 48 L 560 48 L 560 34 Z" fill="#F23645" fill-opacity="0.25"/>
    <circle cx="28" cy="24" r="12" fill="#F23645"/>
    <text x="28" y="28" font-size="13" font-weight="900" fill="#FFFFFF" text-anchor="middle">✕</text>
    <text x="50" y="29" font-size="15.5" font-weight="800" fill="#FF707E">CHỈ BÁO KỸ THUẬT: BẢN TIN PHÁT LẠI ĐI CHẬM</text>

    <!-- Biểu đồ chỉ báo trễ -->
    <g transform="translate(20, 65)">
      <rect width="520" height="150" rx="8" fill="#080B10" stroke="#48181E" stroke-width="1.2"/>
      
      <!-- Nến đã bay lên đỉnh -->
      <g opacity="0.3">
        <line x1="60" y1="90" x2="60" y2="130" stroke="#8E9BAE" stroke-width="2"/>
        <line x1="120" y1="75" x2="120" y2="120" stroke="#8E9BAE" stroke-width="2"/>
        <line x1="180" y1="50" x2="180" y2="105" stroke="#8E9BAE" stroke-width="2"/>
        <line x1="240" y1="20" x2="240" y2="85" stroke="#8E9BAE" stroke-width="2"/>
      </g>
      <!-- Nến chạm đỉnh rồi đảo chiều đỏ -->
      <line x1="300" y1="15" x2="300" y2="60" stroke="#F23645" stroke-width="2.5"/>
      <rect x="291" y="22" width="18" height="24" fill="#F23645" rx="1.5"/>

      <!-- Đường chỉ báo uốn cong lết theo sau -->
      <path d="M 30 115 Q 120 110 200 95 T 300 50" fill="none" stroke="#2962FF" stroke-width="3"/>
      <path d="M 30 120 Q 120 120 200 108 T 300 65" fill="none" stroke="#FF9800" stroke-width="2.5" stroke-dasharray="3,3"/>
      
      <!-- Tín hiệu Mua xuất hiện khi giá ĐÃ Ở ĐỈNH -->
      <circle cx="300" cy="50" r="6" fill="#F23645"/>
      <rect x="315" y="38" width="190" height="28" rx="4" fill="rgba(242,54,69,0.9)"/>
      <text x="410" y="56" font-size="12" font-weight="800" fill="#FFFFFF" text-anchor="middle">⚠️ MỚI BÁO MUA THÌ ĐÃ ĐỈNH!</text>
    </g>

    <!-- Hậu quả thực tế -->
    <g transform="translate(24, 235)">
      <rect width="512" height="65" rx="8" fill="#1C0E12" stroke="#3D181D"/>
      <text x="16" y="25" font-size="14" font-weight="800" fill="#FFFFFF">• Tín hiệu luôn có độ trễ 3 đến 10 nến:</text>
      <text x="16" y="48" font-size="13.5" fill="#FF707E">Phải chờ giá chạy xong mới tính toán, luôn đi sau thị trường.</text>

      <rect y="76" width="512" height="65" rx="8" fill="#1C0E12" stroke="#3D181D"/>
      <text x="16" y="101" font-size="14" font-weight="800" fill="#FFFFFF">• Đu đỉnh và cắt lỗ đúng đáy:</text>
      <text x="16" y="124" font-size="13.5" fill="#FF707E">Chỉ báo hô "Mua" thì giá kịch trần; hô "Bán" thì giá chạm đáy.</text>

      <rect y="152" width="512" height="65" rx="8" fill="#1C0E12" stroke="#3D181D"/>
      <text x="16" y="177" font-size="14" font-weight="800" fill="#FFFFFF">• Các chỉ báo đá nhau chan chát:</text>
      <text x="16" y="200" font-size="13.5" fill="#CAD4E0">Đường này báo tăng, đường kia báo giảm khiến trader rối trí.</text>

      <rect y="228" width="512" height="65" rx="8" fill="#1C0E12" stroke="#3D181D"/>
      <text x="16" y="253" font-size="14" font-weight="800" fill="#FFFFFF">• Mù tịt trước bẫy quét thanh khoản:</text>
      <text x="16" y="276" font-size="13.5" fill="#CAD4E0">Không thấy được các cú giật râu nến gom hàng của cá mập.</text>
    </g>
  </g>

  <!-- Watermark -->
  <g transform="translate(640, 690)" text-anchor="middle">
    <text font-size="13" fill="#CAD4E0" font-weight="600">
      Đóng dấu bản quyền: <tspan fill="#00E5FF" font-weight="800">PTvolume.com</tspan> • Chuyên Trang Naked Chart &amp; VSA Wyckoff
    </text>
  </g>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_chart_indicator_trap.svg"), "w", encoding="utf-8") as f:
    f.write(svg1.strip())
print("Created naked_chart_indicator_trap.svg")


# -------------------------------------------------------------
# 2. HÌNH MỤC 2: KHÔNG GIAN BIỂU ĐỒ TRẦN NGUYÊN BẢN
# -------------------------------------------------------------
svg2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="100%" height="100%" style="background:#0B0E14; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="bg-canvas-2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0E14" />
      <stop offset="50%" stop-color="#141822" />
      <stop offset="100%" stop-color="#0E121B" />
    </linearGradient>
    <filter id="shadow-2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1280" height="720" fill="url(#bg-canvas-2)" rx="16"/>
  <rect width="1274" height="714" x="3" y="3" fill="none" stroke="#222938" stroke-width="2" rx="14"/>

  <!-- Tiêu đề -->
  <g transform="translate(640, 45)" text-anchor="middle">
    <rect x="-480" y="-25" width="960" height="50" rx="25" fill="#141926" stroke="rgba(0, 229, 255, 0.4)" stroke-width="1.8"/>
    <text y="7" font-size="19" font-weight="800" fill="#00E5FF" letter-spacing="0.5">
      KHÔNG GIAN BIỂU ĐỒ TRẦN (THE NAKED CHART): 3 YẾU TỐ CỐT LÕI DUY NHẤT
    </text>
  </g>

  <!-- Giao diện Biểu Đồ Trần Minh Họa Lớn -->
  <g transform="translate(50, 95)" filter="url(#shadow-2)">
    <rect width="1180" height="555" rx="14" fill="#0D141F" stroke="#223348" stroke-width="1.8"/>

    <!-- Vùng Cung Cản Trên (Supply Zone) -->
    <rect x="25" y="45" width="1130" height="42" rx="6" fill="rgba(242,54,69,0.12)" stroke="rgba(242,54,69,0.35)" stroke-dasharray="4,4"/>
    <text x="1140" y="71" font-size="13" font-weight="800" fill="#FF707E" text-anchor="end">
      [1] VÙNG CUNG / KHÁNG CỰ THEN CHỐT (SUPPLY ZONE) &ndash; Phe Bán Chờ Sẵn
    </text>

    <!-- Biểu đồ nến sạch sẽ -->
    <!-- Nhịp 1: Tăng -->
    <line x1="120" y1="260" x2="120" y2="330" stroke="#089981" stroke-width="2.5"/>
    <rect x="110" y="270" width="20" height="45" fill="#089981" rx="1.5"/>

    <line x1="200" y1="210" x2="200" y2="280" stroke="#089981" stroke-width="2.5"/>
    <rect x="190" y="220" width="20" height="50" fill="#089981" rx="1.5"/>

    <line x1="280" y1="160" x2="280" y2="240" stroke="#089981" stroke-width="2.5"/>
    <rect x="270" y="170" width="20" height="60" fill="#089981" rx="1.5"/>

    <!-- Nhịp 2: Chạm cản & Từ chối giá -->
    <line x1="360" y1="50" x2="360" y2="180" stroke="#CAD4E0" stroke-width="3"/>
    <rect x="350" y="125" width="20" height="35" fill="#F23645" rx="1.5"/>
    <circle cx="360" cy="50" r="5" fill="#F0B90B"/>
    <text x="360" y="38" font-size="12" font-weight="800" fill="#F0B90B" text-anchor="middle">PIN BAR TỪ CHỐI GIÁ CỰC MẠNH</text>

    <!-- Nhịp 3: Giảm về vùng cầu -->
    <line x1="440" y1="150" x2="440" y2="230" stroke="#F23645" stroke-width="2.5"/>
    <rect x="430" y="160" width="20" height="55" fill="#F23645" rx="1.5"/>

    <line x1="520" y1="200" x2="520" y2="290" stroke="#F23645" stroke-width="2.5"/>
    <rect x="510" y="210" width="20" height="65" fill="#F23645" rx="1.5"/>

    <line x1="600" y1="260" x2="600" y2="350" stroke="#F23645" stroke-width="2.5"/>
    <rect x="590" y="270" width="20" height="60" fill="#F23645" rx="1.5"/>

    <!-- Vùng Cầu Đáy Dưới (Demand Zone) -->
    <rect x="25" y="340" width="1130" height="42" rx="6" fill="rgba(8,153,129,0.12)" stroke="rgba(8,153,129,0.35)" stroke-dasharray="4,4"/>
    <text x="1140" y="366" font-size="13" font-weight="800" fill="#26E7A6" text-anchor="end">
      [2] VÙNG CẦU / HỖ TRỢ KIÊN CỐ (DEMAND ZONE) &ndash; Phe Mua Đỡ Giá
    </text>

    <!-- Nhịp 4: Phản ứng tại vùng cầu -->
    <line x1="680" y1="310" x2="680" y2="375" stroke="#CAD4E0" stroke-width="3"/>
    <rect x="670" y="315" width="20" height="30" fill="#089981" rx="1.5"/>
    <circle cx="680" cy="375" r="5" fill="#26E7A6"/>
    <text x="680" y="400" font-size="12" font-weight="800" fill="#26E7A6" text-anchor="middle">RÂU DƯỚI ĐỠ GIÁ BẬT TĂNG</text>

    <line x1="760" y1="250" x2="760" y2="320" stroke="#089981" stroke-width="2.5"/>
    <rect x="750" y="260" width="20" height="50" fill="#089981" rx="1.5"/>

    <!-- Khối Lượng Dưới Đáy (Volume) -->
    <line x1="25" y1="415" x2="1155" y2="415" stroke="#223348" stroke-width="1.5"/>
    <text x="35" y="438" font-size="13" font-weight="900" fill="#F0B90B">[3] CỘT KHỐI LƯỢNG VSA (VOLUME)</text>

    <rect x="114" y="450" width="12" height="40" fill="#089981"/>
    <rect x="194" y="440" width="12" height="50" fill="#089981"/>
    <rect x="274" y="430" width="12" height="60" fill="#089981"/>
    <rect x="354" y="420" width="12" height="70" fill="#F0B90B"/>
    <rect x="434" y="445" width="12" height="45" fill="#F23645"/>
    <rect x="514" y="435" width="12" height="55" fill="#F23645"/>
    <rect x="594" y="440" width="12" height="50" fill="#F23645"/>
    <rect x="674" y="425" width="12" height="65" fill="#26E7A6"/>
    <rect x="754" y="445" width="12" height="45" fill="#089981"/>

    <!-- 3 Hộp Tóm Tắt Ý Nghĩa -->
    <g transform="translate(25, 495)">
      <rect width="365" height="46" rx="6" fill="#141C28" stroke="#223348"/>
      <text x="14" y="28" font-size="13" font-weight="700" fill="#FFFFFF">1. Nến Nhật (OHLC): Thấy rõ phe kiểm soát</text>

      <rect x="382" width="365" height="46" rx="6" fill="#141C28" stroke="#223348"/>
      <text x="396" y="28" font-size="13" font-weight="700" fill="#00E5FF">2. Vùng Cung Cầu: Thấy rõ chiến địa ra quyết định</text>

      <rect x="764" width="365" height="46" rx="6" fill="#141C28" stroke="#223348"/>
      <text x="778" y="28" font-size="13" font-weight="700" fill="#F0B90B">3. Volume VSA: Thấy rõ nỗ lực dòng tiền lớn</text>
    </g>
  </g>

  <!-- Watermark -->
  <g transform="translate(640, 690)" text-anchor="middle">
    <text font-size="13" fill="#CAD4E0" font-weight="600">
      Đóng dấu bản quyền: <tspan fill="#00E5FF" font-weight="800">PTvolume.com</tspan> • Chuyên Trang Naked Chart &amp; VSA Wyckoff
    </text>
  </g>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_chart_clean_workspace.svg"), "w", encoding="utf-8") as f:
    f.write(svg2.strip())
print("Created naked_chart_clean_workspace.svg")


# -------------------------------------------------------------
# 3. HÌNH MỤC 3: 3 BƯỚC CẤU HÌNH BIỂU ĐỒ TRẦN
# -------------------------------------------------------------
svg3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="100%" height="100%" style="background:#0B0E14; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="bg-canvas-3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0E14" />
      <stop offset="50%" stop-color="#141822" />
      <stop offset="100%" stop-color="#0E121B" />
    </linearGradient>
    <filter id="shadow-3" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1280" height="720" fill="url(#bg-canvas-3)" rx="16"/>
  <rect width="1274" height="714" x="3" y="3" fill="none" stroke="#222938" stroke-width="2" rx="14"/>

  <!-- Tiêu đề -->
  <g transform="translate(640, 45)" text-anchor="middle">
    <rect x="-480" y="-25" width="960" height="50" rx="25" fill="#141926" stroke="rgba(240, 185, 11, 0.4)" stroke-width="1.8"/>
    <text y="7" font-size="19" font-weight="800" fill="#F0B90B" letter-spacing="0.5">
      3 BƯỚC THIẾT LẬP BIỂU ĐỒ TRẦN CHUẨN MỰC CHO NGƯỜI MỚI (TRADINGVIEW)
    </text>
  </g>

  <!-- 3 Cột Bước 1, Bước 2, Bước 3 -->
  <!-- Bước 1 -->
  <g transform="translate(50, 95)" filter="url(#shadow-3)">
    <rect width="370" height="555" rx="14" fill="#18131B" stroke="#F23645" stroke-width="1.8"/>
    <rect width="370" height="52" rx="14" fill="#F23645" fill-opacity="0.25"/>
    <path d="M 0 36 L 0 52 L 370 52 L 370 36 Z" fill="#F23645" fill-opacity="0.25"/>
    <circle cx="28" cy="26" r="14" fill="#F23645"/>
    <text x="28" y="31" font-size="15" font-weight="900" fill="#FFFFFF" text-anchor="middle">1</text>
    <text x="52" y="32" font-size="16" font-weight="800" fill="#FF707E">BƯỚC 1: XÓA HẾT CHỈ BÁO</text>

    <!-- Minh họa icon thùng rác & chỉ báo gạch chéo -->
    <g transform="translate(20, 75)">
      <rect width="330" height="150" rx="8" fill="#080B10" stroke="#38181F"/>
      
      <circle cx="165" cy="65" r="40" fill="rgba(242,54,69,0.15)" stroke="#F23645" stroke-width="2"/>
      <path d="M 148 55 L 182 75 M 182 55 L 148 75" stroke="#F23645" stroke-width="4" stroke-linecap="round"/>

      <text x="165" y="130" font-size="12" fill="#FF8A95" font-weight="700" text-anchor="middle">Xóa sạch: RSI, MACD, BB, MA, Ichimoku...</text>
    </g>

    <g transform="translate(20, 245)">
      <text x="0" y="20" font-size="14.5" font-weight="800" fill="#FFFFFF">• Thao tác thực hiện:</text>
      <text x="0" y="45" font-size="13.5" fill="#CAD4E0">Chuột phải vào đồ thị $\rightarrow$ chọn</text>
      <text x="0" y="68" font-size="13.5" fill="#F0B90B" font-weight="700">"Remove all indicators" (Xóa toàn bộ).</text>

      <text x="0" y="110" font-size="14.5" font-weight="800" fill="#FFFFFF">• Mục tiêu cốt lõi:</text>
      <text x="0" y="135" font-size="13.5" fill="#CAD4E0">Giải phóng 100% không gian màn hình,</text>
      <text x="0" y="158" font-size="13.5" fill="#CAD4E0">trả lại sự tập trung cao nhất vào giá.</text>

      <rect y="195" width="330" height="85" rx="6" fill="#201014" stroke="#481820"/>
      <text x="12" y="222" font-size="13" font-weight="700" fill="#FF8A95">Lời khuyên tâm lý:</text>
      <text x="12" y="244" font-size="12.5" fill="#CAD4E0">Đừng sợ cảm giác trống trải; đó là</text>
      <text x="12" y="264" font-size="12.5" fill="#CAD4E0">bước đầu tiên để mắt nhìn thấy giá thật!</text>
    </g>
  </g>

  <!-- Bước 2 -->
  <g transform="translate(455, 95)" filter="url(#shadow-3)">
    <rect width="370" height="555" rx="14" fill="#0F1824" stroke="#00E5FF" stroke-width="1.8"/>
    <rect width="370" height="52" rx="14" fill="#00E5FF" fill-opacity="0.2"/>
    <path d="M 0 36 L 0 52 L 370 52 L 370 36 Z" fill="#00E5FF" fill-opacity="0.2"/>
    <circle cx="28" cy="26" r="14" fill="#00E5FF"/>
    <text x="28" y="31" font-size="15" font-weight="900" fill="#0B0E14" text-anchor="middle">2</text>
    <text x="52" y="32" font-size="16" font-weight="800" fill="#00E5FF">BƯỚC 2: CÀI ĐẶT NỀN TỐI</text>

    <!-- Minh họa Dark Theme Palette -->
    <g transform="translate(20, 75)">
      <rect width="330" height="150" rx="8" fill="#080B10" stroke="#163040"/>
      
      <!-- Palette circles -->
      <rect x="25" y="35" width="80" height="50" rx="6" fill="#0B0E14" stroke="#00E5FF" stroke-width="1.5"/>
      <text x="65" y="65" font-size="11" fill="#00E5FF" font-weight="700" text-anchor="middle">#0B0E14</text>

      <rect x="125" y="35" width="80" height="50" rx="6" fill="#141822" stroke="#2962FF" stroke-width="1.5"/>
      <text x="165" y="65" font-size="11" fill="#6095FF" font-weight="700" text-anchor="middle">#141822</text>

      <rect x="225" y="35" width="80" height="50" rx="6" fill="#089981"/>
      <text x="265" y="65" font-size="11" fill="#FFFFFF" font-weight="700" text-anchor="middle">Nến Xanh</text>

      <text x="165" y="125" font-size="12" fill="#00E5FF" font-weight="700" text-anchor="middle">Tương phản cao &amp; Giảm mỏi mắt</text>
    </g>

    <g transform="translate(20, 245)">
      <text x="0" y="20" font-size="14.5" font-weight="800" fill="#FFFFFF">• Màu nền khuyến nghị:</text>
      <text x="0" y="45" font-size="13.5" fill="#CAD4E0">Sử dụng tone Dark Theme chuẩn mực</text>
      <text x="0" y="68" font-size="13.5" fill="#00E5FF" font-weight="700">Mã màu: #0B0E14 hoặc #141822.</text>

      <text x="0" y="110" font-size="14.5" font-weight="800" fill="#FFFFFF">• Lợi ích sinh học:</text>
      <text x="0" y="135" font-size="13.5" fill="#CAD4E0">Giảm điều tiết mắt khi theo dõi biểu đồ,</text>
      <text x="0" y="158" font-size="13.5" fill="#CAD4E0">nhìn rõ râu nến và độ co giãn thân nến.</text>

      <rect y="195" width="330" height="85" rx="6" fill="#0E1E2C" stroke="#1C3850"/>
      <text x="12" y="222" font-size="13" font-weight="700" fill="#00E5FF">Cài đặt nến:</text>
      <text x="12" y="244" font-size="12.5" fill="#CAD4E0">Nến tăng: Xanh (#089981)</text>
      <text x="12" y="264" font-size="12.5" fill="#CAD4E0">Nến giảm: Đỏ (#F23645) chuẩn quốc tế.</text>
    </g>
  </g>

  <!-- Bước 3 -->
  <g transform="translate(860, 95)" filter="url(#shadow-3)">
    <rect width="370" height="555" rx="14" fill="#1C180E" stroke="#F0B90B" stroke-width="1.8"/>
    <rect width="370" height="52" rx="14" fill="#F0B90B" fill-opacity="0.25"/>
    <path d="M 0 36 L 0 52 L 370 52 L 370 36 Z" fill="#F0B90B" fill-opacity="0.25"/>
    <circle cx="28" cy="26" r="14" fill="#F0B90B"/>
    <text x="28" y="31" font-size="15" font-weight="900" fill="#0B0E14" text-anchor="middle">3</text>
    <text x="52" y="32" font-size="16" font-weight="800" fill="#F0B90B">BƯỚC 3: CỐ ĐỊNH VOLUME</text>

    <!-- Minh họa Cột Volume ở 1/5 đáy -->
    <g transform="translate(20, 75)">
      <rect width="330" height="150" rx="8" fill="#080B10" stroke="#3E3416"/>
      
      <!-- Mini Chart -->
      <line x1="20" y1="95" x2="310" y2="95" stroke="#222938" stroke-width="1.5"/>
      <text x="30" y="85" font-size="11" fill="#8E9BAE">Vùng Giá Nến (Chiếm 80% trên)</text>

      <!-- Mini Volume bars -->
      <rect x="50" y="105" width="10" height="35" fill="#089981"/>
      <rect x="90" y="115" width="10" height="25" fill="#089981"/>
      <rect x="130" y="100" width="10" height="40" fill="#F0B90B"/>
      <rect x="170" y="120" width="10" height="20" fill="#F23645"/>
      <rect x="210" y="110" width="10" height="30" fill="#F23645"/>
      <rect x="250" y="102" width="10" height="38" fill="#089981"/>

      <text x="165" y="138" font-size="11" fill="#F0B90B" font-weight="800" text-anchor="middle">Khối Lượng VSA ở 1/5 đáy</text>
    </g>

    <g transform="translate(20, 245)">
      <text x="0" y="20" font-size="14.5" font-weight="800" fill="#FFFFFF">• Thao tác cài đặt:</text>
      <text x="0" y="45" font-size="13.5" fill="#CAD4E0">Vào Indicators $\rightarrow$ tìm gõ</text>
      <text x="0" y="68" font-size="13.5" fill="#F0B90B" font-weight="700">"Volume" (Khối lượng khớp lệnh thuần).</text>

      <text x="0" y="110" font-size="14.5" font-weight="800" fill="#FFFFFF">• Vị trí chuẩn:</text>
      <text x="0" y="135" font-size="13.5" fill="#CAD4E0">Thu nhỏ chiều cao cột Volume, chỉ chiếm</text>
      <text x="0" y="158" font-size="13.5" fill="#CAD4E0">khoảng 15% - 20% cạnh dưới màn hình.</text>

      <rect y="195" width="330" height="85" rx="6" fill="#241E10" stroke="#504218"/>
      <text x="12" y="222" font-size="13" font-weight="700" fill="#F0B90B">Nguyên lý cốt tử:</text>
      <text x="12" y="244" font-size="12.5" fill="#CAD4E0">Khối lượng là số liệu thực của sàn,</text>
      <text x="12" y="264" font-size="12.5" fill="#CAD4E0">không phải công thức toán học trễ!</text>
    </g>
  </g>

  <!-- Watermark -->
  <g transform="translate(640, 690)" text-anchor="middle">
    <text font-size="13" fill="#CAD4E0" font-weight="600">
      Đóng dấu bản quyền: <tspan fill="#00E5FF" font-weight="800">PTvolume.com</tspan> • Chuyên Trang Naked Chart &amp; VSA Wyckoff
    </text>
  </g>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_chart_setup_3_steps.svg"), "w", encoding="utf-8") as f:
    f.write(svg3.strip())
print("Created naked_chart_setup_3_steps.svg")


# -------------------------------------------------------------
# 4. HÌNH MỤC 4: BÓC TÁCH 3 BỘ PHẬN CỐT LÕI CỦA NẾN TRẦN
# -------------------------------------------------------------
svg4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="100%" height="100%" style="background:#0B0E14; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="bg-canvas-4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0E14" />
      <stop offset="50%" stop-color="#141822" />
      <stop offset="100%" stop-color="#0E121B" />
    </linearGradient>
    <filter id="shadow-4" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1280" height="720" fill="url(#bg-canvas-4)" rx="16"/>
  <rect width="1274" height="714" x="3" y="3" fill="none" stroke="#222938" stroke-width="2" rx="14"/>

  <!-- Tiêu đề -->
  <g transform="translate(640, 45)" text-anchor="middle">
    <rect x="-480" y="-25" width="960" height="50" rx="25" fill="#141926" stroke="rgba(41, 98, 255, 0.4)" stroke-width="1.8"/>
    <text y="7" font-size="19" font-weight="800" fill="#6095FF" letter-spacing="0.5">
      BÓC TÁCH 3 BỘ PHẬN CỐT LÕI CỦA NẾN TRẦN: ĐỌC VỊ HÀNH ĐỘNG GIÁ
    </text>
  </g>

  <!-- Cột Trái: Hình vẽ cây nến to rõ ràng -->
  <g transform="translate(50, 95)" filter="url(#shadow-4)">
    <rect width="530" height="555" rx="14" fill="#0E1624" stroke="#2962FF" stroke-width="1.8"/>
    <rect width="530" height="48" rx="14" fill="#2962FF" fill-opacity="0.25"/>
    <path d="M 0 34 L 0 48 L 530 48 L 530 34 Z" fill="#2962FF" fill-opacity="0.25"/>
    <circle cx="28" cy="24" r="12" fill="#2962FF"/>
    <text x="28" y="28" font-size="13" font-weight="900" fill="#FFFFFF" text-anchor="middle">A</text>
    <text x="50" y="29" font-size="15.5" font-weight="800" fill="#75A5FF">MÔ HÌNH NẾN NHẬT &amp; CÁC MỐC GIÁ QUAN TRỌNG</text>

    <!-- Cây Nến Trực Quan -->
    <g transform="translate(55, 75)">
      <!-- Râu trên -->
      <line x1="90" y1="15" x2="90" y2="80" stroke="#CAD4E0" stroke-width="4"/>
      <circle cx="90" cy="15" r="4" fill="#F0B90B"/>
      <text x="105" y="18" font-size="13" fill="#F0B90B" font-weight="700">Giá Cao Nhất (High)</text>

      <!-- Thân nến -->
      <rect x="66" y="80" width="48" height="150" fill="#089981" rx="3" stroke="#26E7A6" stroke-width="2"/>

      <!-- Mức đóng cửa -->
      <line x1="60" y1="80" x2="160" y2="80" stroke="#00E5FF" stroke-width="3" stroke-dasharray="4,4"/>
      <circle cx="160" cy="80" r="5" fill="#00E5FF"/>
      <text x="175" y="84" font-size="14" fill="#00E5FF" font-weight="800">GIÁ ĐÓNG CỬA (CLOSE)</text>
      <text x="175" y="104" font-size="12" fill="#CAD4E0">Phán quyết chung cuộc của phiên</text>

      <!-- Mức mở cửa -->
      <line x1="60" y1="230" x2="160" y2="230" stroke="#8E9BAE" stroke-width="2" stroke-dasharray="4,4"/>
      <text x="175" y="234" font-size="13" fill="#8E9BAE" font-weight="700">Giá Mở Cửa (Open)</text>

      <!-- Râu dưới -->
      <line x1="90" y1="230" x2="90" y2="310" stroke="#CAD4E0" stroke-width="4"/>
      <circle cx="90" cy="310" r="4" fill="#F0B90B"/>
      <text x="105" y="314" font-size="13" fill="#F0B90B" font-weight="700">Giá Thấp Nhất (Low)</text>

      <!-- Thân nến thước đo -->
      <path d="M 45 80 L 25 80 L 25 230 L 45 230" fill="none" stroke="#26E7A6" stroke-width="2"/>
      <text x="15" y="150" font-size="14" font-weight="900" fill="#26E7A6" text-anchor="end">THÂN NẾN</text>
      <text x="15" y="170" font-size="12" fill="#CAD4E0" text-anchor="end">(SPREAD)</text>
    </g>

    <!-- Lưu ý chân nến -->
    <rect x="25" y="465" width="480" height="65" rx="8" fill="#141E30" stroke="#223652"/>
    <text x="40" y="493" font-size="13.5" font-weight="700" fill="#00E5FF">Quy tắc vàng của Pro Trader:</text>
    <text x="40" y="515" font-size="13" fill="#CAD4E0">Màu nến chỉ là hình thức, vị trí đóng cửa và râu nến mới là bản chất!</text>
  </g>

  <!-- Cột Phải: Ý Nghĩa Thực Chiến Của 3 Bộ Phận -->
  <g transform="translate(610, 95)" filter="url(#shadow-4)">
    <rect width="620" height="555" rx="14" fill="#101824" stroke="#00E5FF" stroke-width="1.8"/>
    <rect width="620" height="48" rx="14" fill="#00E5FF" fill-opacity="0.2"/>
    <path d="M 0 34 L 0 48 L 620 48 L 620 34 Z" fill="#00E5FF" fill-opacity="0.2"/>
    <circle cx="28" cy="24" r="12" fill="#089981"/>
    <text x="28" y="28" font-size="13" font-weight="900" fill="#FFFFFF" text-anchor="middle">B</text>
    <text x="50" y="29" font-size="15.5" font-weight="800" fill="#00E5FF">Ý NGHĨA CHIẾN LƯỢC CỦA 3 THÀNH PHẦN</text>

    <!-- Bộ phận 1: Thân nến -->
    <g transform="translate(25, 68)">
      <rect width="570" height="135" rx="8" fill="#141E2C" stroke="#20344C"/>
      <circle cx="20" cy="24" r="7" fill="#26E7A6"/>
      <text x="36" y="28" font-size="15" font-weight="800" fill="#26E7A6">1. THÂN NẾN (SPREAD): THƯỚC ĐO Ý CHÍ KIỂM SOÁT</text>
      <text x="36" y="55" font-size="13.5" fill="#CAD4E0">• Thân nến dài dứt khoát: Một phe áp đảo hoàn toàn đối phương.</text>
      <text x="36" y="78" font-size="13.5" fill="#CAD4E0">• Thân nến ngắn cũn: Hai bên đang giằng co, lưỡng lự hoặc chững lại.</text>
      <text x="36" y="105" font-size="13" fill="#00E5FF" font-weight="700">→ Giúp bạn xác định bên nào đang nắm quyền kiểm soát thị trường.</text>
    </g>

    <!-- Bộ phận 2: Râu nến -->
    <g transform="translate(25, 218)">
      <rect width="570" height="145" rx="8" fill="#141E2C" stroke="#20344C"/>
      <circle cx="20" cy="24" r="7" fill="#F0B90B"/>
      <text x="36" y="28" font-size="15" font-weight="800" fill="#F0B90B">2. RÂU NẾN (WICKS): VẾT TÍCH CỦA SỰ TỪ CHỐI GIÁ</text>
      <text x="36" y="55" font-size="13.5" fill="#CAD4E0">• Râu trên dài: Phe Bán chặn đứng lực tăng và đập giá rơi xuống.</text>
      <text x="36" y="78" font-size="13.5" fill="#CAD4E0">• Râu dưới dài: Phe Mua nhảy vào bắt đáy, hấp thụ toàn bộ lực bán.</text>
      <text x="36" y="105" font-size="13.5" fill="#FF707E">• Cảnh báo bẫy: Thường là cú quét lệnh dừng lỗ (Stop Hunt) của cá mập.</text>
    </g>

    <!-- Bộ phận 3: Giá đóng cửa -->
    <g transform="translate(25, 378)">
      <rect width="570" height="145" rx="8" fill="#141E2C" stroke="#20344C"/>
      <circle cx="20" cy="24" r="7" fill="#00E5FF"/>
      <text x="36" y="28" font-size="15" font-weight="800" fill="#00E5FF">3. GIÁ ĐÓNG CỬA (CLOSE): PHÁN QUYẾT CHUNG CUỘC</text>
      <text x="36" y="55" font-size="13.5" fill="#CAD4E0">• Đóng cửa sát đỉnh: Phe Mua thắng tuyệt đối, đà tăng sẽ tiếp diễn.</text>
      <text x="36" y="78" font-size="13.5" fill="#CAD4E0">• Đóng cửa sát đáy: Phe Bán làm chủ cuộc chơi, đà giảm tiếp tục.</text>
      <text x="36" y="105" font-size="13.5" fill="#26E7A6" font-weight="700">→ Phán quyết xem phe nào thực sự chiến thắng khi hết phiên.</text>
    </g>
  </g>

  <!-- Watermark -->
  <g transform="translate(640, 690)" text-anchor="middle">
    <text font-size="13" fill="#CAD4E0" font-weight="600">
      Đóng dấu bản quyền: <tspan fill="#00E5FF" font-weight="800">PTvolume.com</tspan> • Chuyên Trang Naked Chart &amp; VSA Wyckoff
    </text>
  </g>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_candlestick_structure.svg"), "w", encoding="utf-8") as f:
    f.write(svg4.strip())
print("Created naked_candlestick_structure.svg")


# -------------------------------------------------------------
# 5. HÌNH MỤC 5: 3 KỊCH BẢN NỖ LỰC VS KẾT QUẢ VSA
# -------------------------------------------------------------
svg5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="100%" height="100%" style="background:#0B0E14; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="bg-canvas-5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0E14" />
      <stop offset="50%" stop-color="#141822" />
      <stop offset="100%" stop-color="#0E121B" />
    </linearGradient>
    <filter id="shadow-5" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1280" height="720" fill="url(#bg-canvas-5)" rx="16"/>
  <rect width="1274" height="714" x="3" y="3" fill="none" stroke="#222938" stroke-width="2" rx="14"/>

  <!-- Tiêu đề -->
  <g transform="translate(640, 45)" text-anchor="middle">
    <rect x="-480" y="-25" width="960" height="50" rx="25" fill="#141926" stroke="rgba(240, 185, 11, 0.4)" stroke-width="1.8"/>
    <text y="7" font-size="19" font-weight="800" fill="#F0B90B" letter-spacing="0.5">
      SỰ KẾT HỢP HOÀN HẢO: NẾN TRẦN &amp; KHỐI LƯỢNG VSA (NỖ LỰC vs KẾT QUẢ)
    </text>
  </g>

  <!-- 3 Hộp Kịch Bản Nằm Ngang Rộng Rãi -->
  <!-- Kịch bản 1 -->
  <g transform="translate(50, 95)" filter="url(#shadow-5)">
    <rect width="1180" height="165" rx="12" fill="#0E1A17" stroke="#089981" stroke-width="1.8"/>
    <g transform="translate(30, 20)">
      <!-- Mini Candle & Volume -->
      <line x1="25" y1="10" x2="25" y2="75" stroke="#089981" stroke-width="2.5"/>
      <rect x="15" y="18" width="20" height="48" fill="#089981" rx="1.5"/>
      <rect x="17" y="85" width="16" height="32" fill="#089981"/>
      <text x="25" y="128" font-size="10" fill="#089981" font-weight="800" text-anchor="middle">VOL LỚN</text>

      <!-- Nội dung -->
      <text x="65" y="24" font-size="16" font-weight="800" fill="#26E7A6">1. ĐỒNG THUẬN HOÀN HẢO: NỖ LỰC LỚN = KẾT QUẢ LỚN</text>
      <text x="65" y="52" font-size="14" fill="#CAD4E0">• Dấu hiệu: Thân nến dài dứt khoát đi kèm Cột khối lượng tăng vọt cao vượt trội.</text>
      <text x="65" y="78" font-size="14" fill="#CAD4E0">• Bản chất: Dòng tiền cá mập giải ngân thực chất để đẩy xu hướng đi xa. Cung - Cầu đồng lòng.</text>
      <text x="65" y="104" font-size="14" fill="#00E5FF" font-weight="700">→ Hành động: Tự tin giữ lệnh, đi thuận theo xu hướng (Trend Following).</text>
    </g>
  </g>

  <!-- Kịch bản 2 -->
  <g transform="translate(50, 280)" filter="url(#shadow-5)">
    <rect width="1180" height="175" rx="12" fill="#221216" stroke="#F23645" stroke-width="1.8"/>
    <g transform="translate(30, 20)">
      <!-- Mini Candle & Volume -->
      <line x1="25" y1="8" x2="25" y2="75" stroke="#CAD4E0" stroke-width="2.5"/>
      <rect x="15" y="32" width="20" height="18" fill="#F23645" rx="1.5"/>
      <rect x="17" y="85" width="16" height="38" fill="#F0B90B"/>
      <text x="25" y="132" font-size="10" fill="#F0B90B" font-weight="800" text-anchor="middle">VOL KHỦNG</text>

      <!-- Nội dung -->
      <text x="65" y="24" font-size="16" font-weight="800" fill="#FF707E">2. BẤT THƯỜNG CỰC ĐỘ: NỖ LỰC CỰC LỚN NHƯNG KẾT QUẢ NHỎ</text>
      <text x="65" y="52" font-size="14" fill="#CAD4E0">• Dấu hiệu: Nến thân rất bé (hoặc râu nến dài ngoằng) nhưng Cột khối lượng to đột biến.</text>
      <text x="65" y="78" font-size="14" fill="#CAD4E0">• Bản chất: Lực cản đối ứng ngầm khổng lồ đang âm thầm hấp thụ hết lực đẩy (Xả hàng hoặc Hứng hàng).</text>
      <text x="65" y="104" font-size="14" fill="#F0B90B" font-weight="700">→ Cảnh báo: Dấu hiệu đảo chiều hoặc bẫy giá nguy hiểm. Tuyệt đối KHÔNG mua đuổi!</text>
    </g>
  </g>

  <!-- Kịch bản 3 -->
  <g transform="translate(50, 475)" filter="url(#shadow-5)">
    <rect width="1180" height="165" rx="12" fill="#121824" stroke="#00E5FF" stroke-width="1.8"/>
    <g transform="translate(30, 20)">
      <!-- Mini Candle & Volume -->
      <line x1="25" y1="10" x2="25" y2="75" stroke="#CAD4E0" stroke-width="2.5"/>
      <rect x="15" y="22" width="20" height="38" fill="#089981" opacity="0.65" rx="1.5"/>
      <rect x="17" y="100" width="16" height="15" fill="#8E9BAE" opacity="0.5"/>
      <text x="25" y="128" font-size="10" fill="#8E9BAE" font-weight="800" text-anchor="middle">VOL TÈO</text>

      <!-- Nội dung -->
      <text x="65" y="24" font-size="16" font-weight="800" fill="#00E5FF">3. THIẾU HỤT NỖ LỰC: GIÁ TĂNG RƯỚN NHƯNG KHỐI LƯỢNG TỤT DỐC</text>
      <text x="65" y="52" font-size="14" fill="#CAD4E0">• Dấu hiệu: Giá vẫn cố rướn lên cao nhưng Cột khối lượng teo tóp và cạn kiệt dần.</text>
      <text x="65" y="78" font-size="14" fill="#CAD4E0">• Bản chất: Cá mập đứng ngoài cuộc; chỉ có vài nhà đầu tư nhỏ lẻ mua đuổi trong nghi ngờ.</text>
      <text x="65" y="104" font-size="14" fill="#FF707E" font-weight="700">→ Cấm kỵ: Tuyệt đối không FOMO! Cú tăng giá không có tiền thật bảo chứng này sẽ dễ sập.</text>
    </g>
  </g>

  <!-- Watermark -->
  <g transform="translate(640, 690)" text-anchor="middle">
    <text font-size="13" fill="#CAD4E0" font-weight="600">
      Đóng dấu bản quyền: <tspan fill="#00E5FF" font-weight="800">PTvolume.com</tspan> • Chuyên Trang Naked Chart &amp; VSA Wyckoff
    </text>
  </g>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_vsa_effort_result.svg"), "w", encoding="utf-8") as f:
    f.write(svg5.strip())
print("Created naked_vsa_effort_result.svg")
