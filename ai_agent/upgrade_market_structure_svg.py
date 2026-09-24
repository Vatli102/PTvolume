# -*- coding: utf-8 -*-
import os

SVG_DIR = r"d:\PHAN DUA CẤM XÓA\AI_Agent_Trading\assets\images"

svg_ms = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 820" width="100%" height="100%" style="background:#07090E; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;">
  <defs>
    <linearGradient id="bg-ms-canvas" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#05070C"/>
      <stop offset="50%" stop-color="#0A0F1A"/>
      <stop offset="100%" stop-color="#060910"/>
    </linearGradient>

    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="glow-red" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="glow-gold" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000000" flood-opacity="0.85"/>
    </filter>
  </defs>

  <rect width="1280" height="820" fill="url(#bg-ms-canvas)" rx="16"/>
  <rect width="1274" height="814" x="3" y="3" fill="none" stroke="#1A2538" stroke-width="1.5" rx="14"/>

  <!-- HEADER -->
  <g transform="translate(640, 46)" text-anchor="middle">
    <rect x="-540" y="-28" width="1080" height="56" rx="28" fill="#0C1422" stroke="#00E5FF" stroke-width="1.8" filter="url(#card-shadow)"/>
    <text y="8" font-size="20" font-weight="900" fill="#FFFFFF" letter-spacing="0.5">
      BẢN ĐỒ CẤU TRÚC THỊ TRƯỜNG NGUYÊN BẢN: <tspan fill="#26E7A6">BOS</tspan> • <tspan fill="#FF5252">CHoCH</tspan> • <tspan fill="#F0B90B">FLIP ZONE</tspan>
    </text>
  </g>

  <!-- DIAGRAM CANVAS (TO RÕ RÀNG) -->
  <g transform="translate(45, 95)" filter="url(#card-shadow)">
    <rect width="1190" height="665" rx="14" fill="#090E18" stroke="#1C2D44" stroke-width="1.8"/>

    <!-- Grid lines -->
    <line x1="40" y1="120" x2="1150" y2="120" stroke="#141E30" stroke-width="1.2" stroke-dasharray="6,4"/>
    <line x1="40" y1="260" x2="1150" y2="260" stroke="#141E30" stroke-width="1.2" stroke-dasharray="6,4"/>
    <line x1="40" y1="400" x2="1150" y2="400" stroke="#141E30" stroke-width="1.2" stroke-dasharray="6,4"/>

    <!-- FLIP ZONE BAND (TO RÕ) -->
    <rect x="250" y="240" width="880" height="48" fill="rgba(240, 185, 11, 0.12)" stroke="#F0B90B" stroke-width="1.5" stroke-dasharray="6,4" rx="6"/>
    <g transform="translate(1110, 264)" text-anchor="end">
      <rect x="-420" y="-16" width="430" height="32" rx="16" fill="#1C1608" stroke="#F0B90B" stroke-width="1.2"/>
      <text x="-15" y="6" font-size="13.5" font-weight="900" fill="#F0B90B">⚡ VÙNG CHUYỂN ĐỔI (FLIP ZONE: CẢN ĐỔI THÀNH HỖ TRỢ)</text>
    </g>

    <!-- UPTREND PHASE (GREEN ARROWS & LINES) -->
    <!-- Low 1 -> High 1 -->
    <line x1="80" y1="440" x2="200" y2="260" stroke="#089981" stroke-width="5" stroke-linecap="round"/>
    <!-- High 1 -> HL 1 -->
    <line x1="200" y1="260" x2="280" y2="360" stroke="#CAD4E0" stroke-width="4" stroke-linecap="round"/>
    <!-- HL 1 -> HH 1 (BOS 1) -->
    <line x1="280" y1="360" x2="440" y2="150" stroke="#089981" stroke-width="5" stroke-linecap="round"/>
    <!-- HH 1 -> HL 2 (Pullback Retest Flip Zone) -->
    <line x1="440" y1="150" x2="540" y2="260" stroke="#CAD4E0" stroke-width="4" stroke-linecap="round"/>
    <!-- HL 2 -> Peak HH 2 (BOS 2) -->
    <line x1="540" y1="260" x2="700" y2="80" stroke="#089981" stroke-width="5" stroke-linecap="round"/>

    <!-- BOS 1 CALLOUT BOX (TO RÕ) -->
    <line x1="200" y1="260" x2="400" y2="260" stroke="#00E5FF" stroke-width="2" stroke-dasharray="5,3"/>
    <g transform="translate(290, 220)">
      <rect width="95" height="30" rx="6" fill="#081E2C" stroke="#00E5FF" stroke-width="1.5" filter="url(#glow-cyan)"/>
      <text x="47" y="20" font-size="13" font-weight="900" fill="#00E5FF" text-anchor="middle">BOS 1 ✓</text>
    </g>

    <!-- BOS 2 CALLOUT BOX (TO RÕ) -->
    <line x1="440" y1="150" x2="640" y2="150" stroke="#00E5FF" stroke-width="2" stroke-dasharray="5,3"/>
    <g transform="translate(530, 110)">
      <rect width="95" height="30" rx="6" fill="#081E2C" stroke="#00E5FF" stroke-width="1.5" filter="url(#glow-cyan)"/>
      <text x="47" y="20" font-size="13" font-weight="900" fill="#00E5FF" text-anchor="middle">BOS 2 ✓</text>
    </g>

    <!-- CHoCH PHASE (REVERSAL SIGNAL) -->
    <!-- Peak -> Deep Drop (Breaks HL2) -->
    <line x1="700" y1="80" x2="820" y2="330" stroke="#F23645" stroke-width="5.5" stroke-linecap="round" filter="url(#glow-red)"/>
    
    <!-- CHoCH Breakout Line across HL2 -->
    <line x1="540" y1="260" x2="830" y2="260" stroke="#F23645" stroke-width="2.5" stroke-dasharray="5,3"/>
    <g transform="translate(680, 275)">
      <rect width="210" height="40" rx="8" fill="#250910" stroke="#FF5252" stroke-width="1.8" filter="url(#glow-red)"/>
      <text x="105" y="25" font-size="13.5" font-weight="900" fill="#FF5252" text-anchor="middle">⚠️ CHoCH (GÃY CẤU TRÚC)</text>
    </g>

    <!-- DOWNTREND PHASE -->
    <!-- Pullback Retest Flip Zone as Resistance -->
    <line x1="820" y1="330" x2="920" y2="260" stroke="#CAD4E0" stroke-width="4" stroke-linecap="round"/>
    <!-- Dump to Lower Low -->
    <line x1="920" y1="260" x2="1080" y2="470" stroke="#F23645" stroke-width="5.5" stroke-linecap="round"/>

    <!-- SNIPER SHORT ENTRY CALLOUT AT FLIP ZONE -->
    <g transform="translate(920, 260)">
      <circle cx="0" cy="0" r="14" fill="#F0B90B" filter="url(#glow-gold)" opacity="0.5"/>
      <circle cx="0" cy="0" r="7" fill="#F0B90B"/>
      <g transform="translate(15, -45)">
        <rect width="220" height="42" rx="6" fill="#221808" stroke="#F0B90B" stroke-width="1.5"/>
        <text x="12" y="18" font-size="12.5" font-weight="900" fill="#F0B90B">🎯 SNIPER SHORT ENTRY</text>
        <text x="12" y="32" font-size="11" font-weight="700" fill="#FFFFFF">Retest cản mới + Vol giảm</text>
      </g>
    </g>

    <!-- POINT MARKERS (FONT TO 14px-15px) -->
    <!-- Low 1 -->
    <circle cx="80" cy="440" r="9" fill="#089981"/>
    <text x="80" y="475" font-size="14" font-weight="800" fill="#089981" text-anchor="middle">Low (Đáy gốc)</text>

    <!-- High 1 -->
    <circle cx="200" cy="260" r="9" fill="#089981"/>
    <text x="200" y="240" font-size="14" font-weight="800" fill="#089981" text-anchor="middle">High (Đỉnh 1)</text>

    <!-- HL 1 -->
    <circle cx="280" cy="360" r="9" fill="#26E7A6"/>
    <text x="280" y="395" font-size="14" font-weight="900" fill="#26E7A6" text-anchor="middle">HL 1 (Đáy cao hơn)</text>

    <!-- HH 1 -->
    <circle cx="440" cy="150" r="9" fill="#26E7A6"/>
    <text x="440" y="130" font-size="14" font-weight="900" fill="#26E7A6" text-anchor="middle">HH 1 (Đỉnh cao hơn)</text>

    <!-- HL 2 (Key Point) -->
    <circle cx="540" cy="260" r="11" fill="#00E5FF" filter="url(#glow-cyan)"/>
    <text x="540" y="235" font-size="14.5" font-weight="900" fill="#00E5FF" text-anchor="middle">HL 2 (MỐC THEN CHỐT)</text>

    <!-- Peak HH 2 -->
    <circle cx="700" cy="80" r="11" fill="#F0B90B" filter="url(#glow-gold)"/>
    <text x="700" y="55" font-size="15" font-weight="900" fill="#F0B90B" text-anchor="middle">👑 ĐỈNH CHU KỲ (PEAK)</text>

    <!-- Lower High -->
    <circle cx="920" cy="260" r="9" fill="#FF5252"/>
    <text x="920" y="300" font-size="14" font-weight="900" fill="#FFA4AC" text-anchor="middle">LH (Đỉnh thấp hơn)</text>

    <!-- Lower Low -->
    <circle cx="1080" cy="470" r="9" fill="#FF5252"/>
    <text x="1080" y="505" font-size="14" font-weight="900" fill="#FF5252" text-anchor="middle">LL (Đáy thấp hơn)</text>

    <!-- SUMMARY EXPLANATION BAR AT BOTTOM (FONT TO 14px) -->
    <g transform="translate(30, 560)">
      <rect width="1130" height="85" rx="10" fill="#0B1322" stroke="#1A2D48" stroke-width="1.2"/>
      
      <g transform="translate(25, 25)">
        <text x="0" y="15" font-size="14" font-weight="900" fill="#26E7A6">1. XU HƯỚNG TĂNG (BULLISH):</text>
        <text x="245" y="15" font-size="13.5" fill="#CAD4E0">Tạo chuỗi Đỉnh cao hơn (HH) &amp; Đáy cao hơn (HL). Cứ mỗi lần phá đỉnh gọi là <tspan fill="#00E5FF" font-weight="800">BOS</tspan>.</text>
      </g>

      <g transform="translate(25, 52)">
        <text x="0" y="15" font-size="14" font-weight="900" fill="#FF5252">2. ĐẢO CHIỀU SANG GIẢM (CHoCH):</text>
        <text x="280" y="15" font-size="13.5" fill="#CAD4E0">Khi đáy then chốt HL2 bị đâm thủng ➔ Xuất hiện tín hiệu <tspan fill="#FF707E" font-weight="800">CHoCH</tspan>. Chờ hồi về Flip Zone để Short!</text>
      </g>
    </g>
  </g>

  <!-- WATERMARK FOOTER -->
  <g transform="translate(640, 792)" text-anchor="middle">
    <rect x="-260" y="-18" width="520" height="36" rx="18" fill="#0B101A" stroke="#00E5FF" stroke-width="1.5"/>
    <text y="6" font-size="14" fill="#CAD4E0" font-weight="700">
      Bản quyền đồ họa: <tspan fill="#F0B90B" font-weight="900">PT</tspan><tspan fill="#00E5FF" font-weight="900">VOLUME.COM</tspan> • Market Structure Mastery
    </text>
  </g>
</svg>"""

with open(os.path.join(SVG_DIR, "market_structure_bos_choch.svg"), "w", encoding="utf-8") as f:
    f.write(svg_ms)
print("Upgraded market_structure_bos_choch.svg with large fonts!")
