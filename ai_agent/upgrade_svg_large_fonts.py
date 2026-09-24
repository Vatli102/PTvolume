# -*- coding: utf-8 -*-
"""
Script nâng cấp toàn bộ hình ảnh SVG Bài 1 với FONT CHỮ CỰC LỚN (14px - 26px),
bố cục thoáng đãng, sắc nét, tương phản tối đa, chuẩn nhận diện PTvolume.com.
"""
import os

SVG_DIR = r"d:\PHAN DUA CẤM XÓA\AI_Agent_Trading\assets\images"

# ==============================================================================
# 1. naked_chart_indicator_trap.svg
# ==============================================================================
svg_1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 820" width="100%" height="100%" style="background:#07090E; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
  <defs>
    <linearGradient id="bg-grad-trap" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#05070C"/>
      <stop offset="50%" stop-color="#0B0F19"/>
      <stop offset="100%" stop-color="#07090E"/>
    </linearGradient>

    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="glow-red" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000000" flood-opacity="0.85"/>
    </filter>

    <linearGradient id="bull-body-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#057864"/>
      <stop offset="50%" stop-color="#089981"/>
      <stop offset="100%" stop-color="#1DE9B6"/>
    </linearGradient>

    <pattern id="grid-matrix" width="35" height="35" patternUnits="userSpaceOnUse">
      <path d="M 35 0 L 0 0 0 35" fill="none" stroke="#162032" stroke-width="0.8" stroke-opacity="0.6"/>
    </pattern>
  </defs>

  <rect width="1280" height="820" fill="url(#bg-grad-trap)" rx="16"/>
  <rect width="1274" height="814" x="3" y="3" fill="none" stroke="#1A2538" stroke-width="1.5" rx="14"/>

  <!-- HEADER -->
  <g transform="translate(640, 46)" text-anchor="middle">
    <rect x="-560" y="-28" width="1120" height="56" rx="28" fill="#0C1322" stroke="#00E5FF" stroke-width="1.8" filter="url(#card-shadow)"/>
    <text y="8" font-size="21" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">
      SO SÁNH BẢN CHẤT: <tspan fill="#FF5252">MA TRẬN CHỈ BÁO ĐI CHẬM</tspan> vs <tspan fill="#00E5FF">BIỂU ĐỒ TRẦN REAL-TIME</tspan>
    </text>
  </g>

  <!-- CỘT TRÁI: MA TRẬN CHỈ BÁO -->
  <g transform="translate(35, 95)" filter="url(#card-shadow)">
    <rect width="590" height="665" rx="14" fill="#0B0E17" stroke="#F23645" stroke-width="2"/>
    
    <!-- Header -->
    <path d="M 0 14 Q 0 0 14 0 L 576 0 Q 590 0 590 14 L 590 52 L 0 52 Z" fill="#1F0D15"/>
    <line x1="0" y1="52" x2="590" y2="52" stroke="#421622" stroke-width="1.5"/>
    <circle cx="28" cy="26" r="8" fill="#FF5252" filter="url(#glow-red)"/>
    <text x="46" y="32" font-size="16" font-weight="900" fill="#FF707E">CHIẾN ĐỒ A: LẠM DỤNG CHỈ BÁO</text>
    <rect x="410" y="12" width="165" height="28" rx="14" fill="rgba(242,54,69,0.3)" stroke="#FF5252" stroke-width="1.2"/>
    <text x="492" y="31" font-size="13" font-weight="900" fill="#FFA4AC" text-anchor="middle">❌ TRỄ 7 - 10 NẾN</text>

    <!-- Chart Screen -->
    <g transform="translate(18, 68)">
      <rect width="554" height="360" rx="8" fill="#06080E"/>
      <rect width="554" height="360" rx="8" fill="url(#grid-matrix)"/>
      <rect width="554" height="360" rx="8" fill="none" stroke="#2B141C" stroke-width="1"/>

      <!-- Ticker Info -->
      <text x="16" y="28" font-size="14" font-weight="800" fill="#CAD4E0">BTC/USDT · 15M</text>
      <text x="140" y="28" font-size="13" font-weight="700" fill="#FF707E">(MA, Bollinger, RSI, MACD đá nhau)</text>

      <!-- Faint Candlesticks Behind -->
      <line x1="60" y1="260" x2="60" y2="300" stroke="#089981" stroke-width="2" opacity="0.4"/>
      <rect x="53" y="265" width="14" height="30" fill="#089981" opacity="0.4"/>

      <line x1="160" y1="180" x2="160" y2="255" stroke="#089981" stroke-width="2.5" opacity="0.5"/>
      <rect x="152" y="190" width="16" height="60" fill="#089981" opacity="0.5"/>

      <line x1="330" y1="90" x2="330" y2="150" stroke="#F23645" stroke-width="2" opacity="0.6"/>
      <rect x="322" y="100" width="16" height="40" fill="#F23645" opacity="0.6"/>

      <!-- Tangled Indicators -->
      <path d="M 10 260 Q 100 240 180 180 T 330 80 T 450 110 T 540 160" fill="none" stroke="rgba(41,98,255,0.45)" stroke-width="2.5" stroke-dasharray="4,3"/>
      <path d="M 10 310 Q 100 290 180 250 T 330 180 T 450 190 T 540 240" fill="none" stroke="rgba(41,98,255,0.45)" stroke-width="2.5" stroke-dasharray="4,3"/>
      
      <!-- MA Lines -->
      <path d="M 10 285 Q 120 280 200 240 T 330 125 T 450 135 T 540 170" fill="none" stroke="#F0B90B" stroke-width="2.8"/>
      <path d="M 10 290 Q 150 288 260 255 T 390 160 T 540 165" fill="none" stroke="#E040FB" stroke-width="2.8"/>

      <!-- TRAP CALLOUT (TO RÕ) -->
      <g transform="translate(330, 125)">
        <circle cx="0" cy="0" r="16" fill="#FF5252" filter="url(#glow-red)" opacity="0.5"/>
        <circle cx="0" cy="0" r="7" fill="#FF5252"/>
        
        <path d="M 0 0 L 25 -40 L 215 -40 L 215 35 L 0 35 Z" fill="#250910" stroke="#FF5252" stroke-width="1.8" filter="url(#card-shadow)"/>
        <text x="12" y="-18" font-size="14" font-weight="900" fill="#FF5252">❌ BẪY ĐU ĐỈNH (LATE)</text>
        <text x="12" y="3" font-size="12" font-weight="800" fill="#FFFFFF">Chỉ báo trễ 7 nến mới cắt lên!</text>
        <text x="12" y="22" font-size="11.5" font-weight="700" fill="#FFA4AC">Giá đã đỉnh, cá mập xả hàng</text>
      </g>

      <!-- Sub RSI Area -->
      <line x1="0" y1="280" x2="554" y2="280" stroke="#3A151E" stroke-width="1.2"/>
      <text x="14" y="302" font-size="12.5" font-weight="800" fill="#FF707E">RSI(14) + STOCH: TÍN HIỆU ĐÁ NHAU CHAN CHÁT</text>
      <path d="M 10 340 Q 80 335 180 320 T 330 290 T 450 325" fill="none" stroke="#FF9800" stroke-width="2.5"/>
      <path d="M 10 345 Q 80 315 180 335 T 330 285 T 450 345" fill="none" stroke="#00E5FF" stroke-width="2" stroke-dasharray="4,2"/>
    </g>

    <!-- Detailed Bullet Points (FONT TO 14px-15px) -->
    <g transform="translate(20, 445)">
      <rect width="550" height="195" rx="10" fill="#180A0F" stroke="#3E151E" stroke-width="1.5"/>
      
      <g transform="translate(18, 22)">
        <circle cx="10" cy="10" r="10" fill="#FF5252"/>
        <text x="10" y="15" font-size="13" font-weight="900" fill="#FFFFFF" text-anchor="middle">✕</text>
        <text x="30" y="16" font-size="14.5" font-weight="800" fill="#FFFFFF">Độ Trễ Toán Học Tất Yếu (Severe Lag):</text>
        <text x="30" y="36" font-size="13.5" fill="#FFA4AC">Chỉ báo cần 14-20 nến tính trung bình. Khi báo Mua thì giá đã cạn sóng.</text>
      </g>

      <g transform="translate(18, 80)">
        <circle cx="10" cy="10" r="10" fill="#FF5252"/>
        <text x="10" y="15" font-size="13" font-weight="900" fill="#FFFFFF" text-anchor="middle">✕</text>
        <text x="30" y="16" font-size="14.5" font-weight="800" fill="#FFFFFF">Đu Đỉnh &amp; Cắt Lỗ Xa Tít Tắp:</text>
        <text x="30" y="36" font-size="13.5" fill="#FFA4AC">Vào lệnh trễ tại đỉnh khiến R:R tệ hại (1:1 hoặc âm), dễ cháy tài khoản.</text>
      </g>

      <g transform="translate(18, 138)">
        <circle cx="10" cy="10" r="10" fill="#FF5252"/>
        <text x="10" y="15" font-size="13" font-weight="900" fill="#FFFFFF" text-anchor="middle">✕</text>
        <text x="30" y="16" font-size="14.5" font-weight="800" fill="#FFFFFF">Tê Liệt Phân Tích (Analysis Paralysis):</text>
        <text x="30" y="36" font-size="13.5" fill="#FFA4AC">RSI quá mua, MACD chưa cắt khiến trader bối rối, bỏ lỡ cơ hội vàng.</text>
      </g>
    </g>
  </g>

  <!-- CỘT PHẢI: BIỂU ĐỒ TRẦN -->
  <g transform="translate(655, 95)" filter="url(#card-shadow)">
    <rect width="590" height="665" rx="14" fill="#0B101A" stroke="#00E5FF" stroke-width="2"/>
    
    <!-- Header -->
    <path d="M 0 14 Q 0 0 14 0 L 576 0 Q 590 0 590 14 L 590 52 L 0 52 Z" fill="#0E1E2E"/>
    <line x1="0" y1="52" x2="590" y2="52" stroke="#183A58" stroke-width="1.5"/>
    <circle cx="28" cy="26" r="8" fill="#00E5FF" filter="url(#glow-cyan)"/>
    <text x="46" y="32" font-size="16" font-weight="900" fill="#00E5FF">CHIẾN ĐỒ B: NAKED CHART &amp; VOLUME VSA</text>
    <rect x="410" y="12" width="165" height="28" rx="14" fill="rgba(8,153,129,0.3)" stroke="#089981" stroke-width="1.2"/>
    <text x="492" y="31" font-size="13" font-weight="900" fill="#26E7A6" text-anchor="middle">✓ REAL-TIME CHÂN THỰC</text>

    <!-- Chart Screen -->
    <g transform="translate(18, 68)">
      <rect width="554" height="360" rx="8" fill="#080C14"/>
      <rect width="554" height="360" rx="8" fill="url(#grid-matrix)"/>
      <rect width="554" height="360" rx="8" fill="none" stroke="#16283C" stroke-width="1"/>

      <!-- Ticker Info -->
      <text x="16" y="28" font-size="14" font-weight="800" fill="#CAD4E0">BTC/USDT · 15M</text>
      <text x="140" y="28" font-size="13" font-weight="800" fill="#00E5FF">⚡ NAKED PRO DESK</text>
      <text x="430" y="28" font-size="14" font-weight="900" fill="#26E7A6">68,450.00 (+4.8%)</text>

      <!-- Resistance Line -->
      <line x1="0" y1="205" x2="554" y2="205" stroke="#00E5FF" stroke-width="2" stroke-dasharray="6,4"/>
      <rect x="12" y="188" width="165" height="26" rx="5" fill="#081E2C" stroke="#00E5FF" stroke-width="1.2"/>
      <text x="22" y="206" font-size="12" font-weight="800" fill="#00E5FF">VÙNG KHÁNG CỰ 65,200</text>

      <!-- Candlesticks Sequence -->
      <line x1="50" y1="260" x2="50" y2="295" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="43" y="265" width="14" height="25" fill="#089981" rx="2"/>

      <line x1="85" y1="250" x2="85" y2="290" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="78" y="258" width="14" height="26" fill="#F23645" rx="2"/>

      <line x1="120" y1="230" x2="120" y2="285" stroke="#00E5FF" stroke-width="2.5"/>
      <rect x="113" y="235" width="14" height="20" fill="#089981" rx="2"/>

      <!-- GIANT BREAKOUT CANDLE -->
      <line x1="170" y1="155" x2="170" y2="245" stroke="#26E7A6" stroke-width="3"/>
      <rect x="160" y="160" width="20" height="80" fill="url(#bull-body-grad)" stroke="#00E5FF" stroke-width="2.2" rx="2" filter="url(#glow-cyan)"/>

      <!-- SNIPER ENTRY CALLOUT (TO RÕ) -->
      <g transform="translate(170, 160)">
        <circle cx="0" cy="0" r="16" fill="#00E5FF" filter="url(#glow-cyan)" opacity="0.5"/>
        <circle cx="0" cy="0" r="7" fill="#00E5FF"/>
        
        <path d="M 0 0 L 25 -42 L 230 -42 L 230 35 L 0 35 Z" fill="#061E28" stroke="#00E5FF" stroke-width="1.8" filter="url(#card-shadow)"/>
        <text x="12" y="-20" font-size="14" font-weight="900" fill="#00E5FF">🎯 SNIPER ENTRY CHÂN SÓNG</text>
        <text x="12" y="2" font-size="12" font-weight="800" fill="#FFFFFF">Nến phá vỡ + Volume VSA bùng nổ</text>
        <text x="12" y="22" font-size="11.5" font-weight="800" fill="#26E7A6">Ăn trọn thân sóng · SL cực ngắn 0.5%</text>
      </g>

      <!-- Following candles -->
      <line x1="220" y1="125" x2="220" y2="185" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="211" y="132" width="18" height="48" fill="#089981" rx="2"/>

      <line x1="270" y1="100" x2="270" y2="160" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="261" y="108" width="18" height="45" fill="#089981" rx="2"/>

      <line x1="320" y1="75" x2="320" y2="140" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="311" y="82" width="18" height="48" fill="#089981" rx="2"/>

      <!-- Rejection Pin Bar at top -->
      <line x1="370" y1="50" x2="370" y2="130" stroke="#F0B90B" stroke-width="2.8"/>
      <rect x="361" y="100" width="18" height="20" fill="#F23645" rx="2"/>
      <rect x="395" y="60" width="145" height="26" rx="5" fill="#251608" stroke="#F0B90B" stroke-width="1.2"/>
      <text x="405" y="78" font-size="12" font-weight="900" fill="#F0B90B">💰 Chốt Lời (R:R 1:6)</text>

      <!-- Volume VSA Subwindow -->
      <line x1="0" y1="280" x2="554" y2="280" stroke="#16283C" stroke-width="1.2"/>
      <text x="14" y="302" font-size="12.5" font-weight="900" fill="#00E5FF">KHỐI LƯỢNG VSA (NỖ LỰC DÒNG TIỀN REAL-TIME)</text>
      
      <!-- Vol Surge Bar -->
      <rect x="162" y="288" width="16" height="68" fill="#00E5FF" filter="url(#glow-cyan)"/>
      <text x="170" y="284" font-size="10.5" font-weight="900" fill="#00E5FF" text-anchor="middle">VOL KHỦNG</text>
    </g>

    <!-- Detailed Bullet Points (FONT TO 14px-15px) -->
    <g transform="translate(20, 445)">
      <rect width="550" height="195" rx="10" fill="#091624" stroke="#183654" stroke-width="1.5"/>
      
      <g transform="translate(18, 22)">
        <circle cx="10" cy="10" r="10" fill="#00E5FF"/>
        <text x="10" y="15" font-size="13" font-weight="900" fill="#060910" text-anchor="middle">✓</text>
        <text x="30" y="16" font-size="14.5" font-weight="800" fill="#FFFFFF">Tốc Độ Thời Gian Thực (Zero Lag):</text>
        <text x="30" y="36" font-size="13.5" fill="#B0E5FF">Nhìn trực tiếp bước chân Smart Money ngay khi nến đang bứt phá.</text>
      </g>

      <g transform="translate(18, 80)">
        <circle cx="10" cy="10" r="10" fill="#00E5FF"/>
        <text x="10" y="15" font-size="13" font-weight="900" fill="#060910" text-anchor="middle">✓</text>
        <text x="30" y="16" font-size="14.5" font-weight="800" fill="#FFFFFF">Bắn Tỉa Chân Sóng &amp; Tối Ưu Tỷ Lệ R:R:</text>
        <text x="30" y="36" font-size="13.5" fill="#B0E5FF">Vào lệnh sát cản với Stop Loss ngắn, dễ dàng đạt tỷ lệ R:R từ 1:3 đến 1:6+.</text>
      </g>

      <g transform="translate(18, 138)">
        <circle cx="10" cy="10" r="10" fill="#00E5FF"/>
        <text x="10" y="15" font-size="13" font-weight="900" fill="#060910" text-anchor="middle">✓</text>
        <text x="30" y="16" font-size="14.5" font-weight="800" fill="#FFFFFF">Tâm Lý Sáng Suốt &amp; Kỷ Luật Vững Vàng:</text>
        <text x="30" y="36" font-size="13.5" fill="#B0E5FF">Không còn nhiễu loạn, tự tin ra quyết định theo quy luật Cung - Cầu gốc rễ.</text>
      </g>
    </g>
  </g>

  <!-- WATERMARK FOOTER -->
  <g transform="translate(640, 792)" text-anchor="middle">
    <rect x="-260" y="-18" width="520" height="36" rx="18" fill="#0B101A" stroke="#00E5FF" stroke-width="1.5"/>
    <text y="6" font-size="14" fill="#CAD4E0" font-weight="700">
      Bản quyền hình ảnh: <tspan fill="#F0B90B" font-weight="900">PT</tspan><tspan fill="#00E5FF" font-weight="900">VOLUME.COM</tspan> • Naked Price Action &amp; VSA Pro
    </text>
  </g>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_chart_indicator_trap.svg"), "w", encoding="utf-8") as f:
    f.write(svg_1)
print("1. Upgraded naked_chart_indicator_trap.svg with large fonts!")

# ==============================================================================
# 2. naked_candlestick_structure.svg
# ==============================================================================
svg_2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 820" width="100%" height="100%" style="background:#07090E; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
  <defs>
    <linearGradient id="bg-candle-canvas" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#05070C"/>
      <stop offset="50%" stop-color="#0A0F1A"/>
      <stop offset="100%" stop-color="#060910"/>
    </linearGradient>

    <linearGradient id="bull-body-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#057864"/>
      <stop offset="35%" stop-color="#089981"/>
      <stop offset="70%" stop-color="#26E7A6"/>
      <stop offset="100%" stop-color="#089981"/>
    </linearGradient>

    <linearGradient id="bear-body-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A71624"/>
      <stop offset="35%" stop-color="#F23645"/>
      <stop offset="70%" stop-color="#FF8A95"/>
      <stop offset="100%" stop-color="#F23645"/>
    </linearGradient>

    <filter id="glow-cyan-laser" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="glow-gold-laser" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="glow-red-laser" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="candle-shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000000" flood-opacity="0.85"/>
    </filter>
  </defs>

  <rect width="1280" height="820" fill="url(#bg-candle-canvas)" rx="16"/>
  <rect width="1274" height="814" x="3" y="3" fill="none" stroke="#1A2538" stroke-width="1.5" rx="14"/>

  <!-- HEADER -->
  <g transform="translate(640, 46)" text-anchor="middle">
    <rect x="-540" y="-28" width="1080" height="56" rx="28" fill="#0C1422" stroke="#00E5FF" stroke-width="1.8" filter="url(#candle-shadow)"/>
    <text y="8" font-size="20" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">
      GIẢI PHẪU HỌC NẾN TRẦN 3D: <tspan fill="#00E5FF">THÂN NẾN</tspan> • <tspan fill="#F0B90B">RÂU NẾN</tspan> • <tspan fill="#26E7A6">MỨC ĐÓNG CỬA</tspan>
    </text>
  </g>

  <!-- CỘT TRÁI: NẾN TĂNG CƯỜNG LỰC -->
  <g transform="translate(40, 95)" filter="url(#candle-shadow)">
    <rect width="585" height="665" rx="14" fill="#0A101A" stroke="#2962FF" stroke-width="2"/>
    
    <!-- Top Header -->
    <path d="M 0 14 Q 0 0 14 0 L 571 0 Q 585 0 585 14 L 585 52 L 0 52 Z" fill="#0F1B2E"/>
    <line x1="0" y1="52" x2="585" y2="52" stroke="#1C3050" stroke-width="1.5"/>
    <circle cx="28" cy="26" r="12" fill="#2962FF"/>
    <text x="28" y="31" font-size="14" font-weight="900" fill="#FFFFFF" text-anchor="middle">A</text>
    <text x="50" y="32" font-size="15.5" font-weight="900" fill="#75A5FF">NẾN TĂNG CƯỜNG LỰC (BULLISH MOMENTUM)</text>

    <!-- Candlestick Anatomy Visual -->
    <g transform="translate(40, 70)">
      <rect width="220" height="360" rx="8" fill="#060A10" stroke="#142236" stroke-width="1.2"/>
      
      <!-- Upper Wick -->
      <line x1="110" y1="20" x2="110" y2="65" stroke="#CAD4E0" stroke-width="4.5" stroke-linecap="round"/>
      <circle cx="110" cy="20" r="6" fill="#F0B90B" filter="url(#glow-gold-laser)"/>
      
      <!-- High Price Tag (TO RÕ) -->
      <g transform="translate(130, 12)">
        <rect width="160" height="26" rx="5" fill="#1C1808" stroke="#F0B90B" stroke-width="1.2"/>
        <text x="10" y="18" font-size="12.5" font-weight="900" fill="#F0B90B">Giá Cao Nhất (High)</text>
      </g>

      <!-- CANDLE BODY -->
      <rect x="70" y="65" width="80" height="220" rx="4" fill="url(#bull-body-grad)" stroke="#26E7A6" stroke-width="2.5"/>
      
      <!-- Close Price Laser Line -->
      <line x1="150" y1="65" x2="270" y2="65" stroke="#00E5FF" stroke-width="2.5" stroke-dasharray="5,4"/>
      <circle cx="150" cy="65" r="5" fill="#00E5FF" filter="url(#glow-cyan-laser)"/>
      <g transform="translate(280, 48)">
        <rect width="210" height="36" rx="6" fill="#061F22" stroke="#00E5FF" stroke-width="1.8"/>
        <text x="12" y="18" font-size="13" font-weight="900" fill="#00E5FF">GIÁ ĐÓNG CỬA (CLOSE)</text>
        <text x="12" y="30" font-size="10.5" font-weight="700" fill="#CAD4E0">Phe Mua kiểm soát hoàn toàn!</text>
      </g>

      <!-- SPREAD BRACKET (BODY HEIGHT) -->
      <g transform="translate(15, 65)">
        <path d="M 45 0 L 25 0 L 25 110 L 10 110 L 25 110 L 25 220 L 45 220" fill="none" stroke="#26E7A6" stroke-width="2.5"/>
        <text x="0" y="115" font-size="13" font-weight="900" fill="#26E7A6" text-anchor="middle" transform="rotate(-90, 0, 115)">THÂN NẾN (SPREAD)</text>
      </g>

      <!-- Open Price Laser Line -->
      <line x1="150" y1="285" x2="270" y2="285" stroke="#8E9BAE" stroke-width="2.5" stroke-dasharray="5,4"/>
      <g transform="translate(280, 272)">
        <rect width="190" height="28" rx="5" fill="#141B26" stroke="#485A72" stroke-width="1.2"/>
        <text x="12" y="19" font-size="12.5" font-weight="800" fill="#CAD4E0">Giá Mở Cửa (Open)</text>
      </g>

      <!-- Lower Wick -->
      <line x1="110" y1="285" x2="110" y2="330" stroke="#CAD4E0" stroke-width="4.5" stroke-linecap="round"/>
      <circle cx="110" cy="330" r="6" fill="#8E9BAE"/>
      
      <!-- Low Price Tag -->
      <g transform="translate(130, 320)">
        <rect width="160" height="26" rx="5" fill="#141B26" stroke="#485A72" stroke-width="1.2"/>
        <text x="10" y="18" font-size="12.5" font-weight="800" fill="#CAD4E0">Giá Thấp Nhất (Low)</text>
      </g>
    </g>

    <!-- Interpretations Card (FONT TO 14px-15px) -->
    <g transform="translate(20, 460)">
      <rect width="545" height="180" rx="10" fill="#0A1624" stroke="#163450" stroke-width="1.5"/>
      
      <g transform="translate(18, 22)">
        <text x="0" y="15" font-size="14.5" font-weight="900" fill="#26E7A6">• Thân Nến Rất Dài (Wide Spread):</text>
        <text x="0" y="36" font-size="13.5" fill="#CAD4E0">Ý chí áp đảo toàn diện của phe Mua từ đầu đến cuối phiên.</text>
      </g>

      <g transform="translate(18, 70)">
        <text x="0" y="15" font-size="14.5" font-weight="900" fill="#00E5FF">• Đóng Cửa Sát Đỉnh (High Close):</text>
        <text x="0" y="36" font-size="13.5" fill="#CAD4E0">Phe Bán hoàn toàn bất lực, không thể đẩy lùi giá.</text>
      </g>

      <!-- Bottom Action Pill -->
      <g transform="translate(14, 125)">
        <rect width="517" height="34" rx="8" fill="#09281D" stroke="#089981" stroke-width="1.2"/>
        <text x="14" y="22" font-size="13" font-weight="900" fill="#26E7A6">
          ➔ KẾT LUẬN: <tspan fill="#FFFFFF" font-weight="600">Đà tăng cực mạnh, xác suất tiếp diễn xu hướng đạt 80%+</tspan>
        </text>
      </g>
    </g>
  </g>

  <!-- CỘT PHẢI: NẾN PIN BAR TỪ CHỐI GIÁ -->
  <g transform="translate(655, 95)" filter="url(#candle-shadow)">
    <rect width="585" height="665" rx="14" fill="#140B10" stroke="#F23645" stroke-width="2"/>
    
    <!-- Top Header -->
    <path d="M 0 14 Q 0 0 14 0 L 571 0 Q 585 0 585 14 L 585 52 L 0 52 Z" fill="#260F16"/>
    <line x1="0" y1="52" x2="585" y2="52" stroke="#481B26" stroke-width="1.5"/>
    <circle cx="28" cy="26" r="12" fill="#F23645"/>
    <text x="28" y="31" font-size="14" font-weight="900" fill="#FFFFFF" text-anchor="middle">B</text>
    <text x="50" y="32" font-size="15.5" font-weight="900" fill="#FFA4AC">NẾN PIN BAR TỪ CHỐI GIÁ (BEARISH REJECTION)</text>

    <!-- Candlestick Anatomy Visual -->
    <g transform="translate(40, 70)">
      <rect width="220" height="360" rx="8" fill="#0C0608" stroke="#32141C" stroke-width="1.2"/>
      
      <!-- GIANT UPPER WICK (PRICE REJECTION) -->
      <line x1="110" y1="20" x2="110" y2="250" stroke="#FF5252" stroke-width="5.5" stroke-linecap="round" filter="url(#glow-red-laser)"/>
      <circle cx="110" cy="20" r="6" fill="#FF5252" filter="url(#glow-red-laser)"/>
      
      <!-- High Price Tag -->
      <g transform="translate(130, 12)">
        <rect width="160" height="26" rx="5" fill="#2B0A12" stroke="#FF5252" stroke-width="1.2"/>
        <text x="10" y="18" font-size="12.5" font-weight="900" fill="#FF5252">Giá Cao Nhất (High)</text>
      </g>

      <!-- REJECTION WICK BRACKET -->
      <g transform="translate(15, 20)">
        <path d="M 45 0 L 25 0 L 25 115 L 10 115 L 25 115 L 25 230 L 45 230" fill="none" stroke="#FF5252" stroke-width="2.5"/>
        <text x="0" y="120" font-size="13" font-weight="900" fill="#FF5252" text-anchor="middle" transform="rotate(-90, 0, 120)">RÂU NẾN TỪ CHỐI</text>
      </g>

      <!-- Liquidity Sweep Trap Callout (TO RÕ) -->
      <g transform="translate(260, 100)">
        <rect width="230" height="60" rx="8" fill="#220A12" stroke="#FF5252" stroke-width="1.8" filter="url(#glow-red-laser)"/>
        <text x="12" y="20" font-size="12.5" font-weight="900" fill="#FF5252">⚡ BẪY QUÉT THANH KHOẢN</text>
        <text x="12" y="36" font-size="11" font-weight="800" fill="#FFFFFF">Smart Money dụ mua (Bull Trap)</text>
        <text x="12" y="50" font-size="10.5" font-weight="600" fill="#FFA4AC">Sau đó xả hàng đè giá sập sâu</text>
      </g>

      <!-- CANDLE BODY (TINY AT BOTTOM) -->
      <rect x="70" y="250" width="80" height="42" rx="4" fill="url(#bear-body-grad)" stroke="#FF7A85" stroke-width="2"/>
      
      <!-- Open Price Line -->
      <line x1="150" y1="250" x2="260" y2="250" stroke="#8E9BAE" stroke-width="2" stroke-dasharray="4,4"/>
      <g transform="translate(270, 237)">
        <rect width="190" height="26" rx="5" fill="#1C1014" stroke="#48222A" stroke-width="1.2"/>
        <text x="10" y="18" font-size="12" font-weight="800" fill="#CAD4E0">Giá Mở Cửa (Open)</text>
      </g>

      <!-- Close Price Line -->
      <line x1="150" y1="292" x2="260" y2="292" stroke="#FF5252" stroke-width="2.5" stroke-dasharray="5,4"/>
      <circle cx="150" cy="292" r="5" fill="#FF5252" filter="url(#glow-red-laser)"/>
      <g transform="translate(270, 276)">
        <rect width="230" height="34" rx="6" fill="#2B0A12" stroke="#FF5252" stroke-width="1.8"/>
        <text x="10" y="17" font-size="12.5" font-weight="900" fill="#FF5252">GIÁ ĐÓNG CỬA (CLOSE ĐÁY)</text>
        <text x="10" y="28" font-size="10" font-weight="600" fill="#CAD4E0">Phe Bán đè bẹp hoàn toàn phe Mua!</text>
      </g>

      <!-- Lower Wick -->
      <line x1="110" y1="292" x2="110" y2="330" stroke="#CAD4E0" stroke-width="4.5" stroke-linecap="round"/>
      <circle cx="110" cy="330" r="5" fill="#8E9BAE"/>
    </g>

    <!-- Interpretations Card (FONT TO 14px-15px) -->
    <g transform="translate(20, 460)">
      <rect width="545" height="180" rx="10" fill="#1A0A10" stroke="#481822" stroke-width="1.5"/>
      
      <g transform="translate(18, 22)">
        <text x="0" y="15" font-size="14.5" font-weight="900" fill="#FF5252">• Râu Trên Dài Vượt Trội (Long Wick):</text>
        <text x="0" y="36" font-size="13.5" fill="#FFA4AC">Từ chối giá cực mạnh, phe Bán chặn trên dội xuống quyết liệt.</text>
      </g>

      <g transform="translate(18, 70)">
        <text x="0" y="15" font-size="14.5" font-weight="900" fill="#F0B90B">• Thân Nến Ép Sát Đáy (Low Close):</text>
        <text x="0" y="36" font-size="13.5" fill="#FFA4AC">Toàn bộ nỗ lực tăng giá bị dòng tiền lớn hấp thụ và dập tắt.</text>
      </g>

      <!-- Bottom Action Pill -->
      <g transform="translate(14, 125)">
        <rect width="517" height="34" rx="8" fill="#280A12" stroke="#F23645" stroke-width="1.2"/>
        <text x="14" y="22" font-size="13" font-weight="900" fill="#FF707E">
          ➔ KẾT LUẬN: <tspan fill="#FFFFFF" font-weight="600">Tín hiệu đảo chiều giảm cực nhạy (Sniper Short Setup sát vùng cản)</tspan>
        </text>
      </g>
    </g>
  </g>

  <!-- WATERMARK FOOTER -->
  <g transform="translate(640, 792)" text-anchor="middle">
    <rect x="-260" y="-18" width="520" height="36" rx="18" fill="#0B101A" stroke="#00E5FF" stroke-width="1.5"/>
    <text y="6" font-size="14" fill="#CAD4E0" font-weight="700">
      Bản quyền đồ họa: <tspan fill="#F0B90B" font-weight="900">PT</tspan><tspan fill="#00E5FF" font-weight="900">VOLUME.COM</tspan> • Naked Candlestick Anatomy
    </text>
  </g>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_candlestick_structure.svg"), "w", encoding="utf-8") as f:
    f.write(svg_2)
print("2. Upgraded naked_candlestick_structure.svg with large fonts!")

# ==============================================================================
# 3. naked_vsa_effort_result.svg
# ==============================================================================
svg_3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 840" width="100%" height="100%" style="background:#07090E; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
  <defs>
    <linearGradient id="bg-vsa-canvas" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#05070C"/>
      <stop offset="50%" stop-color="#0A0F1A"/>
      <stop offset="100%" stop-color="#060910"/>
    </linearGradient>

    <linearGradient id="card-scen-1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#081E16"/>
      <stop offset="100%" stop-color="#04100C"/>
    </linearGradient>

    <linearGradient id="card-scen-2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#240D14"/>
      <stop offset="100%" stop-color="#12060A"/>
    </linearGradient>

    <linearGradient id="card-scen-3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#201808"/>
      <stop offset="100%" stop-color="#0F0C04"/>
    </linearGradient>

    <filter id="glow-vol-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="glow-vol-red" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="vsa-shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.85"/>
    </filter>
  </defs>

  <rect width="1280" height="840" fill="url(#bg-vsa-canvas)" rx="16"/>
  <rect width="1274" height="834" x="3" y="3" fill="none" stroke="#1A2538" stroke-width="1.5" rx="14"/>

  <!-- HEADER -->
  <g transform="translate(640, 42)" text-anchor="middle">
    <rect x="-540" y="-26" width="1080" height="52" rx="26" fill="#0C1422" stroke="#F0B90B" stroke-width="1.8" filter="url(#vsa-shadow)"/>
    <text y="7" font-size="20" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">
      SỰ KẾT HỢP HOÀN HẢO: <tspan fill="#00E5FF">NẾN TRẦN (KẾT QUẢ)</tspan> &amp; <tspan fill="#F0B90B">KHỐI LƯỢNG VSA (NỖ LỰC)</tspan>
    </text>
  </g>

  <!-- Subtitle -->
  <g transform="translate(640, 86)" text-anchor="middle">
    <text font-size="14" font-weight="700" fill="#CAD4E0">
      Định luật thứ 3 của Richard Wyckoff: <tspan fill="#00E5FF" font-weight="900">"Mọi Kết quả trên thân nến phải tương xứng với Nỗ lực ở cột Volume"</tspan>
    </text>
  </g>

  <!-- KỊCH BẢN 1: ĐỒNG THUẬN HOÀN HẢO -->
  <g transform="translate(45, 112)" filter="url(#vsa-shadow)">
    <rect width="1190" height="205" rx="14" fill="url(#card-scen-1)" stroke="#089981" stroke-width="2"/>
    
    <!-- Mini Chart Box -->
    <g transform="translate(25, 20)">
      <rect width="190" height="165" rx="8" fill="#060C0A" stroke="#12382C" stroke-width="1.2"/>
      <line x1="10" y1="95" x2="180" y2="95" stroke="#102E24" stroke-width="1" stroke-dasharray="2,2"/>
      
      <!-- Bullish Wide Candle -->
      <line x1="95" y1="12" x2="95" y2="90" stroke="#00E5FF" stroke-width="2.5"/>
      <rect x="78" y="18" width="34" height="66" fill="#089981" stroke="#26E7A6" stroke-width="1.8" rx="2"/>
      <text x="95" y="54" font-size="11.5" font-weight="900" fill="#FFFFFF" text-anchor="middle">KẾT QUẢ LỚN</text>
      <text x="95" y="70" font-size="10" font-weight="800" fill="#26E7A6" text-anchor="middle">(Thân Nến Dài)</text>

      <!-- Huge Volume Bar -->
      <line x1="20" y1="125" x2="170" y2="125" stroke="#F0B90B" stroke-width="1" stroke-dasharray="2,2"/>
      <rect x="80" y="102" width="30" height="52" fill="#00E5FF" filter="url(#glow-vol-cyan)" rx="2"/>
      <text x="95" y="122" font-size="9.5" font-weight="900" fill="#060910" text-anchor="middle">NỖ LỰC LỚN</text>
      <text x="95" y="160" font-size="10" font-weight="900" fill="#26E7A6" text-anchor="middle">VOL BÙNG NỔ</text>
    </g>

    <!-- Content & Logic (FONT TO 14px-15px) -->
    <g transform="translate(240, 20)">
      <rect width="390" height="30" rx="15" fill="rgba(8,153,129,0.3)" stroke="#089981" stroke-width="1.2"/>
      <text x="20" y="20" font-size="14.5" font-weight="900" fill="#26E7A6">1. ĐỒNG THUẬN HOÀN HẢO (NỖ LỰC = KẾT QUẢ)</text>

      <g transform="translate(0, 46)">
        <text x="0" y="16" font-size="14.5" font-weight="900" fill="#FFFFFF">• Dấu hiệu nhận diện:</text>
        <text x="165" y="16" font-size="14" fill="#CAD4E0">Thân nến tăng dài dứt khoát + Volume cao vọt vượt trội trên MA20.</text>
      </g>

      <g transform="translate(0, 76)">
        <text x="0" y="16" font-size="14.5" font-weight="900" fill="#FFFFFF">• Bản chất Smart Money:</text>
        <text x="180" y="16" font-size="14" fill="#CAD4E0">Các quỹ lớn thực sự chi tiền đẩy giá. Cung và Cầu đồng lòng ủng hộ đà tăng.</text>
      </g>

      <!-- Action Pill -->
      <g transform="translate(0, 108)">
        <rect width="720" height="42" rx="8" fill="#092A1F" stroke="#26E7A6" stroke-width="1.5"/>
        <text x="18" y="26" font-size="13.5" font-weight="900" fill="#26E7A6">
          ➔ HÀNH ĐỘNG: <tspan fill="#FFFFFF" font-weight="600">Tự tin gồng lãi theo xu hướng (Trend Following). Đà tăng siêu bền bỉ!</tspan>
        </text>
      </g>
    </g>
  </g>

  <!-- KỊCH BẢN 2: BẤT THƯỜNG CỰC ĐỘ -->
  <g transform="translate(45, 335)" filter="url(#vsa-shadow)">
    <rect width="1190" height="205" rx="14" fill="url(#card-scen-2)" stroke="#F23645" stroke-width="2"/>
    
    <!-- Mini Chart Box -->
    <g transform="translate(25, 20)">
      <rect width="190" height="165" rx="8" fill="#0C0608" stroke="#3A151E" stroke-width="1.2"/>
      <line x1="10" y1="95" x2="180" y2="95" stroke="#2C0F16" stroke-width="1" stroke-dasharray="2,2"/>
      
      <!-- Doji / Narrow Candle -->
      <line x1="95" y1="12" x2="95" y2="90" stroke="#FF5252" stroke-width="2.5"/>
      <rect x="78" y="50" width="34" height="16" fill="#F23645" stroke="#FF7A85" stroke-width="1.8" rx="2"/>
      <text x="95" y="42" font-size="11" font-weight="900" fill="#FF5252" text-anchor="middle">KẾT QUẢ BÉ TÍ</text>
      <text x="95" y="80" font-size="9.5" font-weight="700" fill="#FFA4AC" text-anchor="middle">(Thân Ngắn/Râu Dài)</text>

      <!-- GIANT VOLUME BAR -->
      <line x1="20" y1="125" x2="170" y2="125" stroke="#F0B90B" stroke-width="1" stroke-dasharray="2,2"/>
      <rect x="80" y="98" width="30" height="56" fill="#F23645" filter="url(#glow-vol-red)" rx="2"/>
      <text x="95" y="118" font-size="9.5" font-weight="900" fill="#FFFFFF" text-anchor="middle">NỖ LỰC KHỦNG</text>
      <text x="95" y="160" font-size="10" font-weight="900" fill="#FF5252" text-anchor="middle">VOL CỰC ĐẠI</text>
    </g>

    <!-- Content & Logic (FONT TO 14px-15px) -->
    <g transform="translate(240, 20)">
      <rect width="450" height="30" rx="15" fill="rgba(242,54,69,0.3)" stroke="#F23645" stroke-width="1.2"/>
      <text x="20" y="20" font-size="14.5" font-weight="900" fill="#FFA4AC">2. BẤT THƯỜNG CỰC ĐỘ (NỖ LỰC KHỦNG - KẾT QUẢ NHỎ)</text>

      <g transform="translate(0, 46)">
        <text x="0" y="16" font-size="14.5" font-weight="900" fill="#FFFFFF">• Dấu hiệu nhận diện:</text>
        <text x="165" y="16" font-size="14" fill="#CAD4E0">Nến thân rất ngắn (hoặc râu dài), nhưng Volume lại cao kỷ lục đột biến.</text>
      </g>

      <g transform="translate(0, 76)">
        <text x="0" y="16" font-size="14.5" font-weight="900" fill="#FFFFFF">• Bản chất Smart Money:</text>
        <text x="180" y="16" font-size="14" fill="#FFA4AC">Đạp hết ga nhưng xe đứng yên! Đang có lượng hàng xả ngầm chặn đứng giá.</text>
      </g>

      <!-- Action Pill -->
      <g transform="translate(0, 108)">
        <rect width="720" height="42" rx="8" fill="#2A0B12" stroke="#FF5252" stroke-width="1.5"/>
        <text x="18" y="26" font-size="13.5" font-weight="900" fill="#FF707E">
          ➔ HÀNH ĐỘNG: <tspan fill="#FFFFFF" font-weight="600">CẢNH BÁO ĐẢO CHIỀU! Tuyệt đối không mua đuổi, chốt lời hoặc Short.</tspan>
        </text>
      </g>
    </g>
  </g>

  <!-- KỊCH BẢN 3: THIẾU HỤT NỖ LỰC -->
  <g transform="translate(45, 558)" filter="url(#vsa-shadow)">
    <rect width="1190" height="205" rx="14" fill="url(#card-scen-3)" stroke="#F0B90B" stroke-width="2"/>
    
    <!-- Mini Chart Box -->
    <g transform="translate(25, 20)">
      <rect width="190" height="165" rx="8" fill="#0A0804" stroke="#3A2C10" stroke-width="1.2"/>
      <line x1="10" y1="95" x2="180" y2="95" stroke="#221A0A" stroke-width="1" stroke-dasharray="2,2"/>
      
      <!-- Bullish Candle Climbing -->
      <line x1="95" y1="15" x2="95" y2="90" stroke="#CAD4E0" stroke-width="2"/>
      <rect x="80" y="24" width="30" height="58" fill="#089981" stroke="#26E7A6" stroke-width="1.5" rx="2"/>
      <text x="95" y="58" font-size="11" font-weight="900" fill="#FFFFFF" text-anchor="middle">GIÁ TĂNG RƯỚN</text>

      <!-- Low Volume Bar -->
      <line x1="20" y1="125" x2="170" y2="125" stroke="#F0B90B" stroke-width="1" stroke-dasharray="2,2"/>
      <rect x="85" y="132" width="20" height="24" fill="#687C94" opacity="0.7"/>
      <text x="95" y="120" font-size="9.5" font-weight="900" fill="#F0B90B" text-anchor="middle">NỖ LỰC YẾU</text>
      <text x="95" y="160" font-size="10" font-weight="900" fill="#CAD4E0" text-anchor="middle">VOL TEO TÓP</text>
    </g>

    <!-- Content & Logic (FONT TO 14px-15px) -->
    <g transform="translate(240, 20)">
      <rect width="420" height="30" rx="15" fill="rgba(240,185,11,0.3)" stroke="#F0B90B" stroke-width="1.2"/>
      <text x="20" y="20" font-size="14.5" font-weight="900" fill="#F0B90B">3. THIẾU HỤT NỖ LỰC (GIÁ TĂNG NHƯNG VOL MẤT HÚT)</text>

      <g transform="translate(0, 46)">
        <text x="0" y="16" font-size="14.5" font-weight="900" fill="#FFFFFF">• Dấu hiệu nhận diện:</text>
        <text x="165" y="16" font-size="14" fill="#CAD4E0">Giá cố rướn tạo đỉnh mới nhưng Volume teo tóp, nằm bẹp dí dưới MA20.</text>
      </g>

      <g transform="translate(0, 76)">
        <text x="0" y="16" font-size="14.5" font-weight="900" fill="#FFFFFF">• Bản chất Smart Money:</text>
        <text x="180" y="16" font-size="14" fill="#CAD4E0">Tay to đứng ngoài cuộc. Đà tăng chỉ do nhỏ lẻ FOMO chuyền than hồng cho nhau.</text>
      </g>

      <!-- Action Pill -->
      <g transform="translate(0, 108)">
        <rect width="720" height="42" rx="8" fill="#251C0A" stroke="#F0B90B" stroke-width="1.5"/>
        <text x="18" y="26" font-size="13.5" font-weight="900" fill="#F0B90B">
          ➔ HÀNH ĐỘNG: <tspan fill="#FFFFFF" font-weight="600">KHÔNG FOMO! Tăng ảo thiếu nỗ lực, giá sẽ gãy sập ngay khi có lực bán.</tspan>
        </text>
      </g>
    </g>
  </g>

  <!-- WATERMARK FOOTER -->
  <g transform="translate(640, 805)" text-anchor="middle">
    <rect x="-260" y="-18" width="520" height="36" rx="18" fill="#0B101A" stroke="#F0B90B" stroke-width="1.5"/>
    <text y="6" font-size="14" fill="#CAD4E0" font-weight="700">
      Bản quyền phương pháp: <tspan fill="#F0B90B" font-weight="900">PT</tspan><tspan fill="#00E5FF" font-weight="900">VOLUME.COM</tspan> • Wyckoff Effort vs Result
    </text>
  </g>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_vsa_effort_result.svg"), "w", encoding="utf-8") as f:
    f.write(svg_3)
print("3. Upgraded naked_vsa_effort_result.svg with large fonts!")

# ==============================================================================
# 4. naked_chart_setup_3_steps.svg
# ==============================================================================
svg_4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 820" width="100%" height="100%" style="background:#07090E; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
  <defs>
    <linearGradient id="bg-step-canvas" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#05070C"/>
      <stop offset="50%" stop-color="#0A0F1A"/>
      <stop offset="100%" stop-color="#060910"/>
    </linearGradient>

    <linearGradient id="card-grad-1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#200C12"/>
      <stop offset="100%" stop-color="#0E0609"/>
    </linearGradient>

    <linearGradient id="card-grad-2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E1A2C"/>
      <stop offset="100%" stop-color="#060C16"/>
    </linearGradient>

    <linearGradient id="card-grad-3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#221C0A"/>
      <stop offset="100%" stop-color="#0F0C05"/>
    </linearGradient>

    <filter id="glow-step1" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow-step2" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow-step3" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="shadow-card" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000000" flood-opacity="0.85"/>
    </filter>
  </defs>

  <rect width="1280" height="820" fill="url(#bg-step-canvas)" rx="16"/>
  <rect width="1274" height="814" x="3" y="3" fill="none" stroke="#1A2538" stroke-width="1.5" rx="14"/>

  <!-- HEADER -->
  <g transform="translate(640, 46)" text-anchor="middle">
    <rect x="-500" y="-28" width="1000" height="56" rx="28" fill="#0C1422" stroke="#2962FF" stroke-width="1.8" filter="url(#shadow-card)"/>
    <text y="8" font-size="20" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">
      3 BƯỚC THIẾT LẬP BIỂU ĐỒ TRẦN CHUẨN MỰC TRÊN <tspan fill="#00E5FF">TRADINGVIEW</tspan>
    </text>
  </g>

  <!-- Flow Direction Arrows -->
  <g stroke="#2962FF" stroke-width="3" stroke-dasharray="6,4" fill="none">
    <path d="M 430 400 L 465 400"/>
    <path d="M 845 400 L 880 400"/>
  </g>
  <polygon points="475,400 464,393 464,407" fill="#00E5FF"/>
  <polygon points="890,400 879,393 879,407" fill="#F0B90B"/>

  <!-- BƯỚC 1 -->
  <g transform="translate(45, 95)" filter="url(#shadow-card)">
    <rect width="380" height="665" rx="14" fill="url(#card-grad-1)" stroke="#FF5252" stroke-width="2"/>
    
    <path d="M 0 14 Q 0 0 14 0 L 366 0 Q 380 0 380 14 L 380 54 L 0 54 Z" fill="#280E15"/>
    <line x1="0" y1="54" x2="380" y2="54" stroke="#481822" stroke-width="1.5"/>
    <circle cx="34" cy="27" r="16" fill="#FF5252" filter="url(#glow-step1)"/>
    <text x="34" y="33" font-size="16" font-weight="900" fill="#FFFFFF" text-anchor="middle">1</text>
    <text x="62" y="33" font-size="15.5" font-weight="900" fill="#FF707E">XÓA SẠCH MỌI CHỈ BÁO</text>

    <!-- Visual -->
    <g transform="translate(18, 70)">
      <rect width="344" height="195" rx="10" fill="#060305" stroke="#3A151E" stroke-width="1.2"/>
      
      <!-- Popover Menu (TO RÕ) -->
      <rect x="25" y="30" width="294" height="135" rx="8" fill="#1C0E14" stroke="#FF5252" stroke-width="1.8" filter="url(#shadow-card)"/>
      <text x="45" y="58" font-size="13.5" font-weight="700" fill="#CAD4E0">Reset chart view</text>
      <line x1="25" y1="72" x2="319" y2="72" stroke="#3A1822" stroke-width="1.2"/>
      
      <rect x="35" y="82" width="274" height="42" rx="6" fill="#FF5252" filter="url(#glow-step1)"/>
      <text x="48" y="108" font-size="13.5" font-weight="900" fill="#FFFFFF">✕ Remove all indicators</text>
      <text x="48" y="120" font-size="10.5" font-weight="700" fill="#FFE0E3">(Xóa sạch toàn bộ chỉ báo)</text>
    </g>

    <!-- Content (FONT TO 14px-15px) -->
    <g transform="translate(20, 290)">
      <text x="0" y="18" font-size="15" font-weight="900" fill="#FFFFFF">Thao tác trên TradingView:</text>
      
      <g transform="translate(0, 36)">
        <circle cx="10" cy="8" r="9" fill="#FF5252"/>
        <text x="10" y="13" font-size="12" font-weight="900" fill="#FFFFFF" text-anchor="middle">1</text>
        <text x="28" y="13" font-size="13.5" fill="#CAD4E0">Nhấp chuột phải vào vùng trống đồ thị.</text>
      </g>

      <g transform="translate(0, 72)">
        <circle cx="10" cy="8" r="9" fill="#FF5252"/>
        <text x="10" y="13" font-size="12" font-weight="900" fill="#FFFFFF" text-anchor="middle">2</text>
        <text x="28" y="13" font-size="13.5" fill="#CAD4E0">Chọn <tspan fill="#FF707E" font-weight="800">"Remove all indicators"</tspan>.</text>
      </g>

      <g transform="translate(0, 108)">
        <circle cx="10" cy="8" r="9" fill="#FF5252"/>
        <text x="10" y="13" font-size="12" font-weight="900" fill="#FFFFFF" text-anchor="middle">3</text>
        <text x="28" y="13" font-size="13.5" fill="#CAD4E0">Tắt bỏ hoàn toàn RSI, MACD, Ichimoku.</text>
      </g>

      <g transform="translate(0, 160)">
        <rect width="340" height="175" rx="10" fill="#180A0F" stroke="#3A151E" stroke-width="1.5"/>
        <text x="16" y="28" font-size="14" font-weight="900" fill="#FF707E">💡 Lợi ích cốt lõi:</text>
        <text x="16" y="54" font-size="13.5" fill="#CAD4E0" width="310">
          Loại bỏ hoàn toàn cảm giác phụ thuộc vào chỉ báo trễ. Đôi mắt bắt đầu tập trung 100% vào sự thật đường đi của nến.
        </text>
      </g>
    </g>
  </g>

  <!-- BƯỚC 2 -->
  <g transform="translate(450, 95)" filter="url(#shadow-card)">
    <rect width="380" height="665" rx="14" fill="url(#card-grad-2)" stroke="#00E5FF" stroke-width="2"/>
    
    <path d="M 0 14 Q 0 0 14 0 L 366 0 Q 380 0 380 14 L 380 54 L 0 54 Z" fill="#0F1C2E"/>
    <line x1="0" y1="54" x2="380" y2="54" stroke="#1A3454" stroke-width="1.5"/>
    <circle cx="34" cy="27" r="16" fill="#00E5FF" filter="url(#glow-step2)"/>
    <text x="34" y="33" font-size="16" font-weight="900" fill="#060910" text-anchor="middle">2</text>
    <text x="62" y="33" font-size="15.5" font-weight="900" fill="#00E5FF">CÀI ĐẶT NỀN TỐI DARK THEME</text>

    <!-- Visual -->
    <g transform="translate(18, 70)">
      <rect width="344" height="195" rx="10" fill="#070C14" stroke="#182A40" stroke-width="1.2"/>
      
      <!-- Swatches (TO RÕ) -->
      <g transform="translate(15, 25)">
        <rect width="150" height="50" rx="8" fill="#0B0E14" stroke="#00E5FF" stroke-width="1.5"/>
        <text x="15" y="24" font-size="12" font-weight="900" fill="#FFFFFF">MÀU NỀN TỐI</text>
        <text x="15" y="40" font-size="11.5" font-family="monospace" fill="#00E5FF">#0B0E14</text>
      </g>

      <g transform="translate(180, 25)">
        <rect width="150" height="50" rx="8" fill="#141822" stroke="#2962FF" stroke-width="1.5"/>
        <text x="15" y="24" font-size="12" font-weight="900" fill="#FFFFFF">MÀU CARD</text>
        <text x="15" y="40" font-size="11.5" font-family="monospace" fill="#75A5FF">#141822</text>
      </g>

      <g transform="translate(15, 95)">
        <rect width="150" height="50" rx="8" fill="#08221B" stroke="#089981" stroke-width="1.5"/>
        <text x="15" y="24" font-size="12" font-weight="900" fill="#FFFFFF">NẾN TĂNG XANH</text>
        <text x="15" y="40" font-size="11.5" font-family="monospace" fill="#26E7A6">#089981</text>
      </g>

      <g transform="translate(180, 95)">
        <rect width="150" height="50" rx="8" fill="#250C10" stroke="#F23645" stroke-width="1.5"/>
        <text x="15" y="24" font-size="12" font-weight="900" fill="#FFFFFF">NẾN GIẢM ĐỎ</text>
        <text x="15" y="40" font-size="11.5" font-family="monospace" fill="#FFA4AC">#F23645</text>
      </g>

      <rect x="50" y="160" width="244" height="26" rx="13" fill="rgba(0,229,255,0.18)" stroke="#00E5FF" stroke-width="1"/>
      <text x="172" y="177" font-size="11" font-weight="900" fill="#00E5FF" text-anchor="middle">TỐI ƯU THỊ GIÁC CHỐNG MỎI MẮT</text>
    </g>

    <!-- Content (FONT TO 14px-15px) -->
    <g transform="translate(20, 290)">
      <text x="0" y="18" font-size="15" font-weight="900" fill="#FFFFFF">Chuẩn mực hiển thị chuyên sâu:</text>
      
      <g transform="translate(0, 36)">
        <circle cx="10" cy="8" r="9" fill="#00E5FF"/>
        <text x="10" y="13" font-size="12" font-weight="900" fill="#060910" text-anchor="middle">1</text>
        <text x="28" y="13" font-size="13.5" fill="#CAD4E0">Chuyển theme sang <tspan fill="#00E5FF" font-weight="800">Dark Mode</tspan>.</text>
      </g>

      <g transform="translate(0, 72)">
        <circle cx="10" cy="8" r="9" fill="#00E5FF"/>
        <text x="10" y="13" font-size="12" font-weight="900" fill="#060910" text-anchor="middle">2</text>
        <text x="28" y="13" font-size="13.5" fill="#CAD4E0">Chỉnh màu nến tăng xanh chuẩn, giảm đỏ.</text>
      </g>

      <g transform="translate(0, 108)">
        <circle cx="10" cy="8" r="9" fill="#00E5FF"/>
        <text x="10" y="13" font-size="12" font-weight="900" fill="#060910" text-anchor="middle">3</text>
        <text x="28" y="13" font-size="13.5" fill="#CAD4E0">Ẩn bớt các đường lưới dọc ngang gây rối.</text>
      </g>

      <g transform="translate(0, 160)">
        <rect width="340" height="175" rx="10" fill="#0A1624" stroke="#163450" stroke-width="1.5"/>
        <text x="16" y="28" font-size="14" font-weight="900" fill="#00E5FF">💡 Lợi ích cốt lõi:</text>
        <text x="16" y="54" font-size="13.5" fill="#CAD4E0" width="310">
          Nền tối giúp giảm mỏi mắt khi quan sát thị trường cả ngày, đồng thời tăng độ tương phản rõ rệt cho từng râu nến then chốt.
        </text>
      </g>
    </g>
  </g>

  <!-- BƯỚC 3 -->
  <g transform="translate(855, 95)" filter="url(#shadow-card)">
    <rect width="380" height="665" rx="14" fill="url(#card-grad-3)" stroke="#F0B90B" stroke-width="2"/>
    
    <path d="M 0 14 Q 0 0 14 0 L 366 0 Q 380 0 380 14 L 380 54 L 0 54 Z" fill="#2A220C"/>
    <line x1="0" y1="54" x2="380" y2="54" stroke="#544218" stroke-width="1.5"/>
    <circle cx="34" cy="27" r="16" fill="#F0B90B" filter="url(#glow-step3)"/>
    <text x="34" y="33" font-size="16" font-weight="900" fill="#060910" text-anchor="middle">3</text>
    <text x="62" y="33" font-size="15.5" font-weight="900" fill="#F0B90B">BẬT DUY NHẤT KHỐI LƯỢNG VSA</text>

    <!-- Visual -->
    <g transform="translate(18, 70)">
      <rect width="344" height="195" rx="10" fill="#0A0804" stroke="#3A2C10" stroke-width="1.2"/>
      
      <!-- Top Candles -->
      <rect x="50" y="45" width="12" height="30" fill="#089981" rx="2"/>
      <rect x="90" y="35" width="12" height="40" fill="#089981" rx="2"/>
      <rect x="130" y="60" width="12" height="20" fill="#F23645" rx="2"/>
      <rect x="170" y="20" width="16" height="60" fill="#00E5FF" rx="2" filter="url(#glow-step2)"/>
      <rect x="210" y="40" width="12" height="35" fill="#089981" rx="2"/>

      <!-- Volume Histogram (TO RÕ) -->
      <line x1="15" y1="135" x2="330" y2="135" stroke="#F0B90B" stroke-width="1.5" stroke-dasharray="4,3"/>
      <text x="260" y="130" font-size="11" font-weight="800" fill="#F0B90B">Vol MA20</text>

      <rect x="50" y="140" width="12" height="30" fill="#089981"/>
      <rect x="90" y="135" width="12" height="35" fill="#089981"/>
      <rect x="130" y="150" width="12" height="20" fill="#F23645"/>
      <rect x="168" y="105" width="20" height="65" fill="#F0B90B" filter="url(#glow-step3)"/>
      <rect x="210" y="137" width="12" height="33" fill="#089981"/>

      <rect x="45" y="160" width="254" height="26" rx="13" fill="rgba(240,185,11,0.25)" stroke="#F0B90B" stroke-width="1"/>
      <text x="172" y="177" font-size="11" font-weight="900" fill="#F0B90B" text-anchor="middle">NỖ LỰC DÒNG TIỀN THỰC TẾ</text>
    </g>

    <!-- Content (FONT TO 14px-15px) -->
    <g transform="translate(20, 290)">
      <text x="0" y="18" font-size="15" font-weight="900" fill="#FFFFFF">Kích hoạt &amp; Tinh chỉnh Volume:</text>
      
      <g transform="translate(0, 36)">
        <circle cx="10" cy="8" r="9" fill="#F0B90B"/>
        <text x="10" y="13" font-size="12" font-weight="900" fill="#060910" text-anchor="middle">1</text>
        <text x="28" y="13" font-size="13.5" fill="#CAD4E0">Vào Indicators ➔ Chọn <tspan fill="#F0B90B" font-weight="800">"Volume"</tspan>.</text>
      </g>

      <g transform="translate(0, 72)">
        <circle cx="10" cy="8" r="9" fill="#F0B90B"/>
        <text x="10" y="13" font-size="12" font-weight="900" fill="#060910" text-anchor="middle">2</text>
        <text x="28" y="13" font-size="13.5" fill="#CAD4E0">Bật đường trung bình Volume MA (chu kỳ 20).</text>
      </g>

      <g transform="translate(0, 108)">
        <circle cx="10" cy="8" r="9" fill="#F0B90B"/>
        <text x="10" y="13" font-size="12" font-weight="900" fill="#060910" text-anchor="middle">3</text>
        <text x="28" y="13" font-size="13.5" fill="#CAD4E0">Kéo chiều cao Volume chiếm 15-20% đáy biểu đồ.</text>
      </g>

      <g transform="translate(0, 160)">
        <rect width="340" height="175" rx="10" fill="#1A1508" stroke="#423412" stroke-width="1.5"/>
        <text x="16" y="28" font-size="14" font-weight="900" fill="#F0B90B">💡 Lợi ích cốt lõi:</text>
        <text x="16" y="54" font-size="13.5" fill="#CAD4E0" width="310">
          Khối lượng không phải chỉ báo trễ; đó là tiền thật được khớp lệnh trên sàn, giúp bạn phát hiện cú gom hàng và xả hàng ngầm của cá mập.
        </text>
      </g>
    </g>
  </g>

  <!-- WATERMARK FOOTER -->
  <g transform="translate(640, 792)" text-anchor="middle">
    <rect x="-260" y="-18" width="520" height="36" rx="18" fill="#0B101A" stroke="#2962FF" stroke-width="1.5"/>
    <text y="6" font-size="14" fill="#CAD4E0" font-weight="700">
      Bản quyền quy trình: <tspan fill="#F0B90B" font-weight="900">PT</tspan><tspan fill="#00E5FF" font-weight="900">VOLUME.COM</tspan> • Chuẩn Thiết Lập TradingView
    </text>
  </g>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_chart_setup_3_steps.svg"), "w", encoding="utf-8") as f:
    f.write(svg_4)
print("4. Upgraded naked_chart_setup_3_steps.svg with large fonts!")

# ==============================================================================
# 5. naked_chart_clean_workspace.svg
# ==============================================================================
svg_5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 820" width="100%" height="100%" style="background:#07090E; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
  <defs>
    <linearGradient id="bg-clean-canvas" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#05070C"/>
      <stop offset="50%" stop-color="#090E18"/>
      <stop offset="100%" stop-color="#060910"/>
    </linearGradient>

    <linearGradient id="supply-zone-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(242, 54, 69, 0.35)"/>
      <stop offset="100%" stop-color="rgba(242, 54, 69, 0.08)"/>
    </linearGradient>

    <linearGradient id="demand-zone-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(8, 153, 129, 0.08)"/>
      <stop offset="100%" stop-color="rgba(8, 153, 129, 0.35)"/>
    </linearGradient>

    <linearGradient id="bull-glow-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#057864"/>
      <stop offset="40%" stop-color="#089981"/>
      <stop offset="100%" stop-color="#1DE9B6"/>
    </linearGradient>

    <filter id="neon-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="neon-gold" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="terminal-shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000000" flood-opacity="0.9"/>
    </filter>

    <pattern id="clean-grid-pro" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#121C2B" stroke-width="0.8" stroke-opacity="0.6"/>
    </pattern>
  </defs>

  <rect width="1280" height="820" fill="url(#bg-clean-canvas)" rx="16"/>
  <rect width="1274" height="814" x="3" y="3" fill="none" stroke="#192438" stroke-width="1.5" rx="14"/>

  <!-- WORKSPACE CONTAINER -->
  <g transform="translate(30, 25)" filter="url(#terminal-shadow)">
    <rect width="1220" height="720" rx="14" fill="#0A0E17" stroke="#00E5FF" stroke-width="2"/>

    <!-- NAVIGATION BAR -->
    <path d="M 0 14 Q 0 0 14 0 L 1206 0 Q 1220 0 1220 14 L 1220 54 L 0 54 Z" fill="#0E1624"/>
    <line x1="0" y1="54" x2="1220" y2="54" stroke="#1C2D44" stroke-width="1.5"/>

    <circle cx="26" cy="27" r="6.5" fill="#FF5F56"/>
    <circle cx="46" cy="27" r="6.5" fill="#FFBD2E"/>
    <circle cx="66" cy="27" r="6.5" fill="#27C93F"/>

    <text x="96" y="34" font-size="16" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">XAU/USD · 4H (GOLD SPOT)</text>
    <rect x="330" y="14" width="155" height="28" rx="5" fill="rgba(41,98,255,0.3)" stroke="#2962FF" stroke-width="1.2"/>
    <text x="407" y="32" font-size="12.5" font-weight="900" fill="#00E5FF" text-anchor="middle">⚡ NAKED PRO DESK</text>

    <rect x="500" y="14" width="165" height="28" rx="5" fill="rgba(8,153,129,0.3)" stroke="#089981" stroke-width="1.2"/>
    <circle cx="515" cy="28" r="4" fill="#00E5FF" filter="url(#neon-cyan)"/>
    <text x="585" y="33" font-size="13.5" font-weight="900" fill="#26E7A6" text-anchor="middle">2,385.40 (+1.45%)</text>

    <g transform="translate(940, 13)">
      <rect width="260" height="28" rx="14" fill="rgba(0,229,255,0.18)" stroke="#00E5FF" stroke-width="1.5"/>
      <text x="130" y="19" font-size="12.5" font-weight="900" fill="#00E5FF" text-anchor="middle">✓ 0 CHỈ BÁO • 100% NGUYÊN BẢN</text>
    </g>

    <!-- LEFT TOOLBAR -->
    <g transform="translate(0, 54)">
      <rect width="50" height="605" fill="#070B12"/>
      <line x1="50" y1="0" x2="50" y2="605" stroke="#162234" stroke-width="1.2"/>
      
      <!-- Toolbar Icons -->
      <circle cx="25" cy="28" r="8" fill="none" stroke="#7E92A8" stroke-width="1.8"/>
      <line x1="25" y1="16" x2="25" y2="40" stroke="#7E92A8" stroke-width="1.8"/>
      <line x1="13" y1="28" x2="37" y2="28" stroke="#7E92A8" stroke-width="1.8"/>

      <rect x="7" y="60" width="36" height="36" rx="6" fill="#14243B" stroke="#00E5FF" stroke-width="1.2"/>
      <line x1="16" y1="88" x2="34" y2="68" stroke="#00E5FF" stroke-width="2.5"/>
    </g>

    <!-- RIGHT PRICE AXIS -->
    <g transform="translate(1125, 54)">
      <rect width="95" height="605" fill="#070B12"/>
      <line x1="0" y1="0" x2="0" y2="605" stroke="#162234" stroke-width="1.2"/>
      
      <text x="14" y="65" font-size="12" font-weight="700" fill="#7E92A8">2,420.00</text>
      <text x="14" y="135" font-size="12" font-weight="700" fill="#7E92A8">2,400.00</text>
      
      <g transform="translate(0, 175)">
        <rect width="95" height="28" rx="4" fill="#089981" filter="url(#neon-cyan)"/>
        <text x="10" y="19" font-size="12.5" font-weight="900" fill="#FFFFFF">2,385.40</text>
      </g>

      <text x="14" y="275" font-size="12" font-weight="700" fill="#7E92A8">2,360.00</text>
      <text x="14" y="365" font-size="12" font-weight="700" fill="#7E92A8">2,340.00</text>
      <text x="14" y="455" font-size="12" font-weight="700" fill="#7E92A8">2,320.00</text>
    </g>

    <!-- CHART CANVAS -->
    <g transform="translate(50, 54)">
      <rect width="1075" height="470" fill="#080C14"/>
      <rect width="1075" height="470" fill="url(#clean-grid-pro)"/>

      <!-- 1. SUPPLY ZONE (TO RÕ) -->
      <rect x="0" y="45" width="1075" height="65" fill="url(#supply-zone-grad)" stroke="#F23645" stroke-width="1.5" stroke-dasharray="5,4"/>
      <g transform="translate(20, 58)">
        <rect width="250" height="34" rx="6" fill="#200A10" stroke="#F23645" stroke-width="1.5"/>
        <text x="14" y="22" font-size="13" font-weight="900" fill="#FF707E">🔴 VÙNG CUNG CỰC ĐẠI (SUPPLY)</text>
      </g>

      <!-- 2. DEMAND ZONE (TO RÕ) -->
      <rect x="0" y="370" width="1075" height="70" fill="url(#demand-zone-grad)" stroke="#089981" stroke-width="1.5" stroke-dasharray="5,4"/>
      <g transform="translate(20, 388)">
        <rect width="240" height="34" rx="6" fill="#071E18" stroke="#089981" stroke-width="1.5"/>
        <text x="14" y="22" font-size="13" font-weight="900" fill="#26E7A6">🟢 VÙNG CẦU CHỦ ĐẠO (DEMAND)</text>
      </g>

      <!-- 3. LIQUIDITY SWEEP PIN BAR (TO RÕ) -->
      <line x1="220" y1="360" x2="220" y2="455" stroke="#00E5FF" stroke-width="3"/>
      <rect x="210" y="365" width="20" height="24" fill="url(#bull-glow-grad)" stroke="#26E7A6" stroke-width="1.8" rx="2"/>
      <g transform="translate(235, 410)">
        <rect width="230" height="36" rx="6" fill="#061B24" stroke="#00E5FF" stroke-width="1.5" filter="url(#neon-cyan)"/>
        <text x="12" y="17" font-size="12" font-weight="900" fill="#00E5FF">⚡ LIQUIDITY SWEEP (RŨ HÀNG)</text>
        <text x="12" y="30" font-size="10" font-weight="700" fill="#CAD4E0">Râu dài quét Stop Loss nhỏ lẻ</text>
      </g>

      <!-- 4. UPTREND SPRINT -->
      <!-- Massive Breakout -->
      <line x1="280" y1="260" x2="280" y2="375" stroke="#26E7A6" stroke-width="3"/>
      <rect x="269" y="268" width="22" height="100" fill="url(#bull-glow-grad)" stroke="#00E5FF" stroke-width="2.2" rx="2"/>

      <!-- Flip Zone Line -->
      <line x1="250" y1="250" x2="750" y2="250" stroke="#F0B90B" stroke-width="2" stroke-dasharray="5,4"/>
      <g transform="translate(310, 232)">
        <rect width="200" height="26" rx="5" fill="#1C1808" stroke="#F0B90B" stroke-width="1.2"/>
        <text x="10" y="18" font-size="12" font-weight="900" fill="#F0B90B">FLIP ZONE (CẢN ĐỔI THÀNH HỖ TRỢ)</text>
      </g>

      <!-- Rejection into Supply -->
      <line x1="580" y1="48" x2="580" y2="150" stroke="#FF5252" stroke-width="3"/>
      <rect x="570" y="105" width="20" height="34" fill="#F23645" stroke="#FF7A85" stroke-width="2" rx="2"/>
      <g transform="translate(605, 60)">
        <rect width="220" height="38" rx="6" fill="#220A10" stroke="#FF5252" stroke-width="1.5" filter="url(#neon-gold)"/>
        <text x="12" y="17" font-size="12" font-weight="900" fill="#FF5252">🛑 TỪ CHỐI GIÁ VÙNG CUNG</text>
        <text x="12" y="31" font-size="10" font-weight="800" fill="#F0B90B">Râu dài = Smart Money chặn xả</text>
      </g>
    </g>

    <!-- SUB-WINDOW: VOLUME VSA -->
    <g transform="translate(50, 524)">
      <rect width="1075" height="135" fill="#070A10"/>
      <line x1="0" y1="0" x2="1075" y2="0" stroke="#1C2D44" stroke-width="1.5"/>

      <text x="16" y="24" font-size="13.5" font-weight="900" fill="#00E5FF">KHỐI LƯỢNG GIAO DỊCH THỜI GIAN THỰC (VOLUME VSA PRO)</text>
      <line x1="0" y1="70" x2="1075" y2="70" stroke="#F0B90B" stroke-width="1.2" stroke-dasharray="5,4"/>
      <text x="980" y="65" font-size="11.5" font-weight="800" fill="#F0B90B">MA20 Volume</text>

      <!-- Volume Bars -->
      <rect x="272" y="15" width="16" height="110" fill="#00E5FF" filter="url(#neon-cyan)"/>
      <text x="280" y="10" font-size="11" font-weight="900" fill="#00E5FF" text-anchor="middle">VOL ĐỘT BIẾN</text>

      <rect x="572" y="20" width="16" height="105" fill="#F23645" filter="url(#neon-cyan)"/>
      <text x="580" y="14" font-size="11" font-weight="900" fill="#FF5252" text-anchor="middle">VOL XẢ HÀNG</text>
    </g>

    <!-- STATUS BAR (FONT TO 13px-14px) -->
    <g transform="translate(0, 660)">
      <rect width="1220" height="60" rx="0 0 14 14" fill="#070B12"/>
      <line x1="0" y1="0" x2="1220" y2="0" stroke="#1A2538" stroke-width="1.5"/>

      <g transform="translate(25, 14)">
        <rect width="270" height="32" rx="16" fill="#0E1E2E" stroke="#00E5FF" stroke-width="1.2"/>
        <text x="20" y="21" font-size="12.5" font-weight="900" fill="#00E5FF">1. NẾN OHLC NGUYÊN BẢN</text>
      </g>
      
      <g transform="translate(315, 14)">
        <rect width="310" height="32" rx="16" fill="#09241B" stroke="#089981" stroke-width="1.2"/>
        <text x="20" y="21" font-size="12.5" font-weight="900" fill="#26E7A6">2. VÙNG CUNG CẦU (SUPPLY/DEMAND)</text>
      </g>

      <g transform="translate(645, 14)">
        <rect width="280" height="32" rx="16" fill="#221C0A" stroke="#F0B90B" stroke-width="1.2"/>
        <text x="20" y="21" font-size="12.5" font-weight="900" fill="#F0B90B">3. CỘT KHỐI LƯỢNG VSA (VOLUME)</text>
      </g>

      <g transform="translate(945, 14)">
        <rect width="250" height="32" rx="16" fill="#0F1726" stroke="#00E5FF" stroke-width="1.5"/>
        <text x="125" y="21" font-size="12.5" font-weight="900" fill="#FFFFFF" text-anchor="middle">
          BẢN QUYỀN <tspan fill="#F0B90B">PT</tspan><tspan fill="#00E5FF">VOLUME.COM</tspan>
        </text>
      </g>
    </g>
  </g>
</svg>"""

with open(os.path.join(SVG_DIR, "naked_chart_clean_workspace.svg"), "w", encoding="utf-8") as f:
    f.write(svg_5)
print("5. Upgraded naked_chart_clean_workspace.svg with large fonts!")
