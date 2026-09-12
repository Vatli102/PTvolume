# -*- coding: utf-8 -*-
"""
Dữ liệu nội dung chuyên sâu cho 20 bài học Khóa học:
LÀM CHỦ BIỂU ĐỒ TRẦN, VSA & PHƯƠNG PHÁP WYCKOFF THỰC CHIẾN
Chuẩn phong cách Investopedia Financial - PTvolume.com
"""

LESSONS = [
    # BÀI 1 PHẦN 2
    {
        "id": "1b",
        "slug": "khoa-hoc-vsa-wyckoff-bai-1-cau-truc-thi-truong-va-vung-cung-cau-phan-2",
        "title": "Bài 1 (Phần 2): Cấu Trúc Thị Trường (Market Structure) &ndash; Đỉnh/Đáy Xoay Chiều &amp; Vùng Cung Cầu",
        "badge": "Học Phần 1 • Naked Price Action • Bài 1 (Phần 2)",
        "desc": "Làm chủ cấu trúc thị trường nguyên bản: Phân biệt Đỉnh/Đáy Swing High/Low, sự phá vỡ cấu trúc BOS, đổi tính chất CHoCH, và cách vẽ vùng Cung - Cầu then chốt.",
        "read_time": "16 Phút Đọc",
        "views": "2,150 Lượt Xem",
        "date": "12/09/2026",
        "image": "../assets/images/market_structure_bos_choch.svg",
        "image_caption": "Hình 1.3: Bản đồ cấu trúc thị trường thời gian thực - Xác định BOS, CHoCH và điểm bắn tỉa tại Flip Zone.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-1-bieu-do-tran-the-naked-chart-phan-1",
        "prev_title": "Bài 1: Biểu Đồ Trần - Khám Phá Bản Năng Của Giá",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-2-ngon-ngu-nen-don-va-cum-nen-dao-chieu-sat-thu",
        "next_title": "Bài 2: Ngôn Ngữ Nến Đơn & Cụm Nến Đảo Chiều Sát Thủ",
        "takeaways": [
            ("Bản Đồ Cấu Trúc Là Kim Chỉ Nam:", "Một cây nến đơn lẻ không có ý nghĩa nếu không được đặt vào bối cảnh cấu trúc thị trường (Market Structure). Đỉnh/Đáy xoay chiều (Swing Points) là nơi phán quyết xu hướng."),
            ("Phá Vỡ Cấu Trúc (BOS) vs Đổi Tính Chất (CHoCH):", "BOS (Break of Structure) xác nhận xu hướng tiếp diễn; CHoCH (Change of Character) là hồi chuông cảnh báo xu hướng đảo chiều đầu tiên khi đáy/đỉnh then chốt bị xuyên thủng."),
            ("Vùng Chuyển Đổi (Flip Zones):", "Ngưỡng kháng cự bị phá vỡ biến thành hỗ trợ kiên cố (và ngược lại). Đây là chiến địa săn lệnh có xác suất thắng cao nhất."),
            ("Nguyên Tắc Bắn Tỉa (Sniper Entry):", "Không bao giờ mua đuổi khi giá đang bay xa khỏi cấu trúc; kiên nhẫn chờ giá hồi quy (Retest) về Flip Zone hoặc Vùng Cầu được bảo vệ.")
        ],
        "quote": "Giao dịch mà không nắm rõ cấu trúc thị trường cũng giống như một vị tướng xua quân vào trận địa mà không có bản đồ địa hình. Mọi chỉ báo đều vô dụng nếu cấu trúc nói rằng xu hướng đã cạn kiệt.",
        "quote_author": "PTvolume Market Structure Desk",
        "html_content": """
            <h2><i class="fa-solid fa-sitemap"></i> 1. Đỉnh/Đáy Xoay Chiều (Swing High &amp; Swing Low) Là Gì?</h2>
            <p>
                Rất nhiều F0 lầm tưởng rằng mọi chỗ nến nhô lên đều là đỉnh, và mọi chỗ nến thò xuống đều là đáy. Điều này dẫn đến việc vẽ biểu đồ rối như tơ vò và liên tục bị nhiễu sóng (Market Noise).
            </p>
            <p>
                Trong trường phái <strong>Naked Price Action thực chiến</strong>, một Đỉnh/Đáy chỉ được công nhận là một <em>Điểm xoay chiều cấu trúc (Swing Point)</em> khi nó thỏa mãn cấu trúc nến tối thiểu 3 thanh hoặc 5 thanh:
            </p>
            <ul>
                <li><strong>Đỉnh Xoay Chiều (Swing High):</strong> Là thanh nến có đỉnh cao nhất (High) được kẹp giữa ít nhất 1 hoặc 2 thanh nến có đỉnh thấp hơn ở cả bên trái và bên phải. Đây là nơi phe Mua đã dốc toàn lực nhưng bị phe Bán chặn đứng và đẩy lùi.</li>
                <li><strong>Đáy Xoay Chiều (Swing Low):</strong> Là thanh nến có đáy thấp nhất (Low) được kẹp giữa các thanh nến có đáy cao hơn ở hai bên. Đây là cứ điểm phòng thủ vững chắc nơi phe Bán cạn lực và phe Mua lao vào giải cứu.</li>
            </ul>

            <h2><i class="fa-solid fa-chart-line"></i> 2. Giải Mã 3 Trạng Thái Của Cấu Trúc Thị Trường</h2>
            <p>
                Thị trường chỉ vận động trong 3 trạng thái cấu trúc duy nhất:
            </p>
            <div class="step-card">
                <h4><i class="fa-solid fa-arrow-trend-up" style="color:var(--bullish);"></i> 1. Cấu Trúc Xu Hướng Tăng (Bullish Market Structure)</h4>
                <p>
                    Được định nghĩa bởi chuỗi liên tục tạo ra <strong>Đỉnh cao hơn (Higher Highs - HH)</strong> và <strong>Đáy cao hơn (Higher Lows - HL)</strong>. Quy tắc sống còn: Một xu hướng tăng chỉ thực sự bị đe dọa khi đáy Higher Low gần nhất bị phá vỡ.
                </p>
            </div>
            <div class="step-card">
                <h4><i class="fa-solid fa-arrow-trend-down" style="color:var(--bearish);"></i> 2. Cấu Trúc Xu Hướng Giảm (Bearish Market Structure)</h4>
                <p>
                    Được định nghĩa bởi chuỗi liên tục tạo ra <strong>Đỉnh thấp hơn (Lower Highs - LH)</strong> và <strong>Đáy thấp hơn (Lower Lows - LL)</strong>. Phe Bán hoàn toàn kiểm soát cuộc chơi; mỗi nhịp hồi lên chỉ là cơ hội để phe Bán tích lũy thêm vị thế Short giá hời.
                </p>
            </div>
            <div class="step-card">
                <h4><i class="fa-solid fa-arrows-left-right" style="color:var(--accent-gold);"></i> 3. Cấu Trúc Tích Lũy / Đi Ngang (Trading Range / Consolidation)</h4>
                <p>
                    Giá dao động giằng co giữa một biên độ trần Kháng cự (Ceiling) và biên độ sàn Hỗ trợ (Floor). Cung và Cầu đang tạm thời cân bằng. Naked Chart trader sẽ kiên nhẫn chờ cú bứt phá hoặc đánh chặn ở hai biên.
                </p>
            </div>

            <h2><i class="fa-solid fa-crosshairs"></i> 3. BOS (Break of Structure) và CHoCH (Change of Character)</h2>
            <p>
                Hai khái niệm tối thượng mà bất kỳ trader hiện đại nào cũng phải nằm lòng:
            </p>
            <ul>
                <li><strong>BOS (Break of Structure - Phá Vỡ Cấu Trúc Tiếp Diễn):</strong> Xảy ra khi giá phá vỡ đỉnh cũ HH trong xu hướng tăng hoặc phá đáy cũ LL trong xu hướng giảm. BOS chứng minh động lượng (Momentum) đang cực kỳ mạnh mẽ và xu hướng tiếp tục được duy trì.</li>
                <li><strong>CHoCH (Change of Character - Thay Đổi Tính Chất / Tín Hiệu Đảo Chiều Sớm):</strong> Xảy ra khi giá đang tăng nhưng đột ngột lao dốc đâm thủng đáy Higher Low (HL) then chốt gần nhất. Đây là tiếng chuông báo tử cho phe Bò, báo hiệu dòng tiền thông minh đã bắt đầu xả hàng và xu hướng chuẩn bị xoay trục sang giảm.</li>
            </ul>

            <h2><i class="fa-solid fa-shield-halved"></i> 4. Vùng Chuyển Đổi (Flip Zones) &ndash; Thánh Địa Bắn Tỉa</h2>
            <p>
                Khi một ngưỡng cản kháng cự bị phá vỡ, các trader đã từng Bán khống tại đó bị kẹt lệnh (Trapped Shorts). Khi giá quay trở lại kiểm định (Pullback), họ sẽ vội vã đóng lệnh hòa vốn (Buy to Cover), đồng thời những trader chờ mua bứt phá sẽ nhảy vào. Sự cộng hưởng này biến ngưỡng Kháng cự cũ trở thành <strong>Hỗ Trợ Mới cực kỳ kiên cố (Flip Zone)</strong>.
            </p>
            <p>
                Đây chính là nơi bạn tìm kiếm các cây nến Pin Bar hoặc nến cạn kiệt khối lượng (No Supply) để bắn tỉa điểm vào lệnh với mức Stop Loss siêu ngắn và tỷ lệ R:R tối thiểu 1:3.
            </p>
        """,
        "comments": [
            ("Tuấn Anh (Pro PA)", "12/09/2026 14:30:15", "Giải thích về CHoCH và HL then chốt rất sáng tỏ! Trước đây mình cứ thấy phá đáy nhỏ ở khung M5 là tưởng đảo chiều, hóa ra khung H4 vẫn là HL vững chắc nên bị dính bẫy quét thanh khoản liên tục."),
            ("Ngọc Mai (Trader Forex)", "12/09/2026 15:05:22", "Sơ đồ BOS và CHoCH vẽ rất đẹp và dễ nhớ. Flip Zone quả thực là vùng mình thích nhất vì tỷ lệ R:R ở đây luôn cực kỳ cao."),
            ("Đức Thịnh (CBOT Trader)", "12/09/2026 15:40:00", "Kiến thức bài bản không thua kém gì giáo trình Phố Wall. Đang hóng Bài 2 về các cụm nến đảo chiều sát thủ!")
        ]
    },

    # BÀI 2
    {
        "id": "2",
        "slug": "khoa-hoc-vsa-wyckoff-bai-2-ngon-ngu-nen-don-va-cum-nen-dao-chieu-sat-thu",
        "title": "Bài 2: Ngôn Ngữ Nến Đơn &amp; Cụm Nến Đảo Chiều Sát Thủ (Pin Bar, Engulfing &amp; Fakey)",
        "badge": "Học Phần 1 • Naked Price Action • Bài 2",
        "desc": "Bóc tách các mô hình nến đảo chiều có xác suất thắng cao nhất trong Naked Chart: Tuyệt chiêu Pin Bar (Đuôi Kangaroo), Nến Nhấn Chìm (Engulfing) và Bẫy giá Fakey Inside Bar.",
        "read_time": "15 Phút Đọc",
        "views": "1,980 Lượt Xem",
        "date": "12/09/2026",
        "image": "../assets/images/candlesticks/engulfing_patterns.jpg",
        "image_caption": "Hình 2.1: Các mẫu nến Naked Price Action đảo chiều kinh điển kích hoạt điểm vào lệnh chuẩn mực.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-1-cau-truc-thi-truong-va-vung-cung-cau-phan-2",
        "prev_title": "Bài 1 (Phần 2): Cấu Trúc Thị Trường & Vùng Cung Cầu",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-3-vung-nen-tich-luy-build-up-va-true-breakout",
        "next_title": "Bài 3: Vùng Nén Tích Lũy (Build-Up) & True Breakout",
        "takeaways": [
            ("Pin Bar (Đuôi Kangaroo):", "Râu nến phải chiếm tối thiểu 2/3 tổng chiều dài cây nến và nhô hẳn ra ngoài cấu trúc giá xung quanh để chứng minh sự từ chối giá thực thụ."),
            ("Nến Nhấn Chìm (Engulfing):", "Thân nến sau nuốt trọn hoàn toàn thân nến trước; khối lượng bùng nổ chứng minh phe đối lập đã áp đảo hoàn toàn."),
            ("Tuyệt Chiêu Fakey (Inside Bar False Breakout):", "Cú lừa ngoạn mục nhất của Smart Money: Giả vờ phá vỡ nến mẹ để dụ F0 vào lệnh rồi quay xe quét sạch Stop Loss."),
            ("Nguyên Tắc Vị Trí:", "Mô hình nến chỉ có giá trị khi nó xuất hiện tại Key Level (Vùng Cung/Cầu then chốt hoặc Flip Zone), nến xuất hiện lơ lửng giữa đường hoàn toàn vô nghĩa.")
        ],
        "quote": "Đừng bao giờ giao dịch một mô hình nến chỉ vì nó đẹp như sách giáo khoa. Hãy tự hỏi: Ai đang bị mắc bẫy ở cây nến này? Nơi nào họ buộc phải cắt lỗ? Đó mới là nơi dòng tiền lớn kiếm ăn.",
        "quote_author": "Alex Nekritin & Walter Peters (Naked Forex)",
        "html_content": """
            <h2><i class="fa-solid fa-wand-magic-sparkles"></i> 1. Pin Bar (The Kangaroo Tail) &ndash; Tuyệt Chiêu Từ Chối Giá</h2>
            <p>
                Trong cuốn sách kinh điển <em>Naked Forex</em>, tiến sĩ Alex Nekritin gọi cây nến Pin Bar chuẩn mực là <strong>The Kangaroo Tail (Chiếc đuôi chuột túi)</strong>. Một cây nến Kangaroo Tail sát thủ phải hội tụ đủ 3 điều kiện khắt khe:
            </p>
            <ol>
                <li><strong>Chiếc đuôi nhô hẳn ra ngoài:</strong> Râu nến dài phải đâm thấu qua ngưỡng cản và nhô vượt hẳn lên trên/dưới tất cả các thanh nến lân cận.</li>
                <li><strong>Thân nến rất nhỏ:</strong> Thân nến co cụm lại ở 1/3 đầu đối diện và nằm gọn trong biên độ của cây nến trước.</li>
                <li><strong>Vị trí đóng cửa:</strong> Nến Pin Bar tăng phải đóng cửa ở nửa trên; nến Pin Bar giảm phải đóng cửa ở nửa dưới.</li>
            </ol>

            <h2><i class="fa-solid fa-fire"></i> 2. Nến Nhấn Chìm (Engulfing) &ndash; Cú Nuốt Chửng Của Phe Kiểm Soát</h2>
            <p>
                Engulfing không đơn thuần là một mô hình 2 nến, nó là hiện tượng <strong>chuyển giao quyền lực tuyệt đối</strong> trong tích tắc:
            </p>
            <ul>
                <li><strong>Bullish Engulfing:</strong> Sau một chuỗi nến giảm, xuất hiện một cây nến xanh khổng lồ mở cửa ngang hoặc thấp hơn đáy nến trước nhưng đóng cửa vọt qua đỉnh nến trước. Toàn bộ phe Bán ngắn hạn bị chôn vùi trong thua lỗ.</li>
                <li><strong>Bearish Engulfing:</strong> Cây nến đỏ đồ sộ nuốt trọn nến xanh trước đó tại vùng kháng cự. Dấu hiệu cho thấy Smart Money đã tung toàn bộ nguồn cung để đè bẹp lực mua yếu ớt.</li>
            </ul>

            <h2><i class="fa-solid fa-mask"></i> 3. Bẫy Giá Fakey (Inside Bar False Breakout)</h2>
            <p>
                Nếu Inside Bar tượng trưng cho sự nén giá (Consolidation) bên trong thân của cây nến mẹ (Mother Bar), thì <strong>Fakey chính là chiếc bẫy tinh vi nhất</strong>:
            </p>
            <p>
                Giá ban đầu phá vỡ nhẹ ra khỏi nến mẹ (khiến các breakout trader nhảy vào Buy/Sell theo quán tính), nhưng ngay trong phiên hoặc phiên tiếp theo, giá quay đầu 180 độ giật ngược vào trong, tạo thành một thanh nến có râu dài quét sạch SL của nhóm breakout. Giao dịch theo hướng quay đầu của Fakey mang lại tỷ lệ thắng cực kỳ cao vì bạn đang đi cùng hướng với Smart Money sau khi họ đã quét sạch thanh khoản.
            </p>
        """,
        "comments": [
            ("Hoàng Nam", "12/09/2026 16:10:00", "Đuôi Kangaroo Tail trên khung Daily Vàng đánh cực kỳ uy tín! Râu nến đâm qua cản rồi thụt lại là vào lệnh với SL cực ngắn."),
            ("Quốc Bảo", "12/09/2026 16:45:12", "Fakey là setup ruột của mình. Cứ thấy nến thò ra khỏi Inside Bar rồi thụt lại là vào lệnh ngược hướng ngay!"),
            ("Hương Giang", "12/09/2026 17:15:30", "Bài viết đã chỉ rất rõ nến phải xuất hiện tại Key Level mới có giá trị. Trước mình đánh nến lơ lửng giữa chừng bị quét SL suốt.")
        ]
    },

    # BÀI 3
    {
        "id": "3",
        "slug": "khoa-hoc-vsa-wyckoff-bai-3-vung-nen-tich-luy-build-up-va-true-breakout",
        "title": "Bài 3: Vùng Nén Tích Lũy (Build-Up) &amp; Kỹ Thuật Phân Biệt True Breakout vs Fakeout",
        "badge": "Học Phần 1 • Naked Price Action • Bài 3",
        "desc": "Giải mã bí kíp đỉnh cao của Bob Volman: Nhận diện hiện tượng nén giá (Build-up) trước ngưỡng cản then chốt để phân biệt bứt phá thật (True Breakout) và bẫy giả (Fakeout).",
        "read_time": "15 Phút Đọc",
        "views": "1,820 Lượt Xem",
        "date": "12/09/2026",
        "image": "../assets/images/candlesticks/marubozu_trend.jpg",
        "image_caption": "Hình 3.1: Vùng nén giá Build-up trước ngưỡng cản then chốt tạo lực đẩy bứt phá ngoạn mục.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-2-ngon-ngu-nen-don-va-cum-nen-dao-chieu-sat-thu",
        "prev_title": "Bài 2: Ngôn Ngữ Nến Đơn & Cụm Nến Đảo Chiều",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-4-nghe-thuat-phan-tich-da-khung-thoi-gian",
        "next_title": "Bài 4: Nghệ Thuật Phân Tích Đa Khung Thời Gian",
        "takeaways": [
            ("Bản Chất Của Vùng Nén (Build-Up):", "Giá không bị cản dội ngược lại mà bám chặt sát ngưỡng cản, tạo các nến thân nhỏ dần. Điều này chứng minh phe Bán không còn đủ lực đẩy lùi phe Mua."),
            ("Phân Biệt True Breakout vs Fakeout:", "Breakout không có Build-up 80% là Fakeout; Breakout có Build-up vững chắc 80% là bứt phá thật."),
            ("Stop Loss Cực Kỳ Chặt Chẽ:", "Nhờ có vùng nén Build-up, trader có thể đặt Stop Loss ngay phía sau vùng nén thay vì phải đặt tít xa ở đáy cũ."),
            ("Quy Tắc Nam Châm (Magnet Effect):", "Khi một ngưỡng cản bị ép liên tục (Squeeze), thanh khoản bán cạn kiệt và giá sẽ bùng nổ xuyên cản như mũi tên bắn khỏi cung.")
        ],
        "quote": "Bứt phá mà không có tích lũy nén giá (Build-up) giống như một vận động viên nhảy cao mà không lấy đà: Cú nhảy sẽ sớm kiệt sức và rơi tự do.",
        "quote_author": "Bob Volman (Understanding Price Action)",
        "html_content": """
            <h2><i class="fa-solid fa-compress"></i> 1. Khái Niệm Vùng Nén Giá (Build-Up) Của Bob Volman</h2>
            <p>
                Hầu hết F0 thường mắc bẫy khi giao dịch bứt phá (Breakout Trading) vì họ nhảy vào Buy ngay khi thấy một cây nến xanh lớn lao qua đỉnh cũ. Nhưng chỉ vài phút sau, cây nến đó rút râu biến thành nến bẫy (Bull Trap) và cắm đầu giảm sâu.
            </p>
            <p>
                Bậc thầy Price Action Bob Volman đã chỉ ra bí mật sống còn: <strong>Cần phải có VÙNG NÉN TÍCH LŨY (BUILD-UP) ngay sát ngưỡng cản trước khi bứt phá.</strong>
            </p>
            <p>
                Build-up là hiện tượng từ 3 đến 8 cây nến có biên độ co hẹp dần, xếp hàng san sát nhau ngay dưới mức kháng cự (hoặc ngay trên mức hỗ trợ).
            </p>

            <h2><i class="fa-solid fa-scale-unbalanced"></i> 2. Vì Sao Build-Up Lại Bảo Chứng Cho True Breakout?</h2>
            <p>
                Hãy tư duy theo góc độ Cung &ndash; Cầu thời gian thực:
            </p>
            <ul>
                <li>Nếu tại ngưỡng kháng cự có nhiều phe Bán mạnh, giá lẽ ra phải bị đạp rơi thẳng cánh ngay khi vừa chạm cản.</li>
                <li>Nhưng nếu giá chạm cản mà <strong>KHÔNG CHỊU RƠI</strong>, trái lại vẫn lì lợm neo ở sát mép cản &ndash; điều đó chứng minh phe Mua sẵn sàng hấp thụ sạch sành sanh mọi lệnh bán ở mức giá cao này!</li>
                <li>Khi lượng hàng bán ra bị nuốt trọn, nguồn cung cạn kiệt hoàn toàn. Lúc này chỉ cần một lực mua nhỏ kích hoạt, giá sẽ bay vút qua cản tạo nên cú <strong>True Breakout thần sầu</strong>.</li>
            </ul>

            <h2><i class="fa-solid fa-crosshairs"></i> 3. Kỹ Thuật Vào Lệnh Chuẩn Xác Với Vùng Nén</h2>
            <p>
                Cách thức thực thi:
            </p>
            <ol>
                <li>Xác định ngưỡng cản mạnh trên khung H1 hoặc H4.</li>
                <li>Quan sát hành vi giá khi tiếp cận cản: Nếu giá phóng một mạch từ xa tới cản $\rightarrow$ <strong>TUYỆT ĐỐI KHÔNG MUA</strong> vì giá đã kiệt sức.</li>
                <li>Nếu giá từ từ tiến tới và hình thành vùng nén nến nhỏ (Build-up) trong 30 &ndash; 60 phút $\rightarrow$ Đặt lệnh <strong>Buy Stop</strong> ngay trên đỉnh vùng nén, Stop Loss đặt ngay dưới đáy vùng nén.</li>
            </ol>
        """,
        "comments": [
            ("Thanh Tùng", "12/09/2026 18:00:15", "Khái niệm Build-up của Bob Volman thật sự đã cứu tài khoản của mình. Bỏ hẳn thói quen mua đuổi breakout vu vơ."),
            ("Văn Hùng", "12/09/2026 18:40:20", "SL đặt sau Build-up cực kỳ chặt chẽ, nếu ăn được sóng R:R toàn 1:4 đến 1:6."),
            ("Lan Anh", "12/09/2026 19:10:00", "Hình dung về vận động viên nhảy cao không lấy đà quá trực quan và thấm thía!")
        ]
    },

    # BÀI 4
    {
        "id": "4",
        "slug": "khoa-hoc-vsa-wyckoff-bai-4-nghe-thuat-phan-tich-da-khung-thoi-gian",
        "title": "Bài 4: Nghệ Thuật Phân Tích Đa Khung Thời Gian (Multi-Timeframe Top-Down Analysis)",
        "badge": "Học Phần 1 • Naked Price Action • Bài 4",
        "desc": "Quy tắc 3 khung thời gian trong Naked Chart: Sử dụng HTF (Daily/H4) để định vị bản đồ tác chiến và LTF (M15/M5) để bắn tỉa điểm vào lệnh với mức Stop Loss nhỏ nhất.",
        "read_time": "15 Phút Đọc",
        "views": "1,940 Lượt Xem",
        "date": "12/09/2026",
        "image": "../assets/images/macro_intermarket_flow.jpg",
        "image_caption": "Hình 4.1: Bản đồ tác chiến liên khung thời gian - Phân tích từ trên xuống (Top-Down Analysis).",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-3-vung-nen-tich-luy-build-up-va-true-breakout",
        "prev_title": "Bài 3: Vùng Nén Tích Lũy (Build-Up) & True Breakout",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-5-vsa-can-ban-spread-va-khoi-luong",
        "next_title": "Bài 5: VSA Căn Bản - Spread & Khối Lượng",
        "takeaways": [
            ("Top-Down Analysis:", "Luôn bắt đầu từ khung lớn nhìn xuống khung nhỏ, không bao giờ làm ngược lại."),
            ("Bộ 3 Khung Thời Gian Chuẩn Mực:", "Khung Lớn (Daily/H4) xác định xu hướng & Key Zone; Khung Trung (H1) định vị cấu trúc sóng; Khung Nhỏ (M15/M5) bắn tỉa điểm vào lệnh."),
            ("Giải Quyết Nghịch Lý Mâu Thuẫn Khung:", "Khi M15 báo Bán nhưng Daily là Vùng Hỗ Trợ Tăng $\rightarrow$ Ưu tiên tuyệt đối phe Daily, canh M15 đảo chiều tăng để Mua."),
            ("Tối Ưu R:R Thần Kỳ:", "Phân tích theo khung lớn để ăn biên độ sóng dài, nhưng vào lệnh theo khung nhỏ để Stop Loss nhỏ nhất có thể.")
        ],
        "quote": "Giao dịch ở khung thời gian nhỏ mà không nhìn khung lớn cũng giống như bạn lạc vào giữa một khu rừng rậm mà chỉ nhìn thấy những tán lá trước mặt mà không biết cả khu rừng đang bốc cháy.",
        "quote_author": "Alexander Elder (Trading for a Living)",
        "html_content": """
            <h2><i class="fa-solid fa-layer-group"></i> 1. Vì Sao Phải Phân Tích Đa Khung Thời Gian (Top-Down)?</h2>
            <p>
                Một trong những lý do lớn nhất khiến các day trader thua lỗ là họ chỉ "dán mắt" vào khung M1, M5 hoặc M15. Tại các khung thời gian siêu nhỏ này, 80% tín hiệu nến chỉ là tạp âm (Noise) do các thuật toán HFT giao dịch ngắn hạn tạo ra.
            </p>
            <p>
                Dòng tiền lớn (Smart Money, quỹ phòng hộ, ngân hàng trung ương) <strong>KHÔNG BAO GIỜ</strong> ra quyết định trên khung M5. Họ tích lũy và giải ngân trên khung Daily và H4. Do đó, muốn bơi cùng cá mập, bạn phải nhìn thế giới qua lăng kính khung lớn trước!
            </p>

            <h2><i class="fa-solid fa-cubes-stacked"></i> 2. Bộ 3 Khung Thời Gian Chuẩn Mực Cho Naked Trader</h2>
            <div class="step-card">
                <h4>1. Khung Thời Gian Lớn (HTF - Daily / H4): "Bản Đồ Tác Chiến"</h4>
                <p>Nhiệm vụ: Xác định xu hướng vĩ mô (Uptrend hay Downtrend) và đánh dấu các vùng Cung/Cầu kiên cố nhất. Tại khung này, bạn trả lời câu hỏi: <em>Tôi chỉ nên canh BUY hay chỉ nên canh SELL?</em></p>
            </div>
            <div class="step-card">
                <h4>2. Khung Thời Gian Trung Gian (MTF - H1): "Định Hướng Chiến Thuật"</h4>
                <p>Nhiệm vụ: Quan sát cấu trúc sóng hồi (Pullback) đang tiến về Key Zone của khung lớn. Nhận diện các vùng Flip Zone trung hạn.</p>
            </div>
            <div class="step-card">
                <h4>3. Khung Thời Gian Nhỏ (LTF - M15 / M5): "Ống Ngắm Bắn Tỉa (Sniper)"</h4>
                <p>Nhiệm vụ: Khi giá đã chạm vào Key Zone của H4, phóng to vào M15 để tìm kiếm nến Pin Bar từ chối giá, nến Engulfing hoặc mô hình CHoCH gãy cấu trúc nhỏ để bấm nút vào lệnh với mức Stop Loss chỉ vài pips!</p>
            </div>
        """,
        "comments": [
            ("Minh Hoàng", "12/09/2026 19:40:00", "Công thức HTF H4 - LTF M15 này làm tỷ lệ R:R của mình tăng vọt từ 1:1.5 lên đều đặn 1:4!"),
            ("Huy Cường", "12/09/2026 20:15:10", "Trước giờ toàn bị mâu thuẫn khung, giờ hiểu phải tuân thủ tuyệt đối khung Daily/H4."),
            ("Khánh Ly", "12/09/2026 20:50:00", "Bài học rất chi tiết và giải tỏa được nỗi băn khoăn bấy lâu nay của mình.")
        ]
    }
]

print(f"Loaded {len(LESSONS)} sample lessons in course_data.py")
