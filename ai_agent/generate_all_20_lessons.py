# -*- coding: utf-8 -*-
"""
Trình khởi tạo 20 bài học toàn diện cho khóa học:
LÀM CHỦ BIỂU ĐỒ TRẦN, VSA & PHƯƠNG PHÁP WYCKOFF THỰC CHIẾN
Chạy hoàn toàn cục bộ, TUYỆT ĐỐI KHÔNG PUSH LÊN WEB PTVOLUME.COM.
"""
import os
import sys

# Thiết lập UTF-8 cho console Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from template_engine import generate_lesson_html
from course_data import LESSONS as LESSONS_PART1

LESSONS_REMAINING = [
    # BÀI 5
    {
        "id": "5",
        "slug": "khoa-hoc-vsa-wyckoff-bai-5-vsa-can-ban-spread-va-khoi-luong",
        "title": "Bài 5: VSA Căn Bản &ndash; Mối Tương Quan Giữa Spread Thân Nến Và Cột Khối Lượng",
        "badge": "Học Phần 2 • Volume Spread Analysis • Bài 5",
        "desc": "Nhập môn VSA: Định nghĩa Spread chuẩn xác, phân loại 4 mức Volume và nguyên lý phát hiện Bất thường (Anomaly) giữa Nỗ lực và Kết quả.",
        "read_time": "16 Phút Đọc",
        "views": "2,310 Lượt Xem",
        "date": "12/09/2026",
        "image": "../assets/images/naked_candlestick_and_vsa_mechanics.svg",
        "image_caption": "Hình 5.1: Mối tương quan giữa độ mở thân nến (Spread) và cột Khối lượng VSA.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-4-nghe-thuat-phan-tich-da-khung-thoi-gian",
        "prev_title": "Bài 4: Nghệ Thuật Phân Tích Đa Khung Thời Gian",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-6-doc-vi-nen-no-demand-va-upthrust",
        "next_title": "Bài 6: Đọc Vị Nến No Demand & Upthrust",
        "takeaways": [
            ("Spread Là Gì Trong VSA?", "Spread là khoảng cách từ giá Cao nhất đến Thấp nhất của thanh giá (hoặc thân nến Open - Close). Nó đo lường kết quả di chuyển thực tế."),
            ("Khối Lượng Là Nỗ Lực:", "Volume thể hiện năng lượng và số tiền thực tế mà thị trường đã bỏ ra để tạo nên độ dài Spread đó."),
            ("Sự Bất Thường (Anomaly):", "Bất kỳ khi nào có sự khập khiễng giữa Nỗ lực (Volume) và Kết quả (Spread), đó là dấu vết Smart Money đang giăng bẫy."),
            ("4 Cấp Độ Volume:", "Thấp (Below Average), Trung bình (Average), Cao (High), Siêu cao đột biến (Ultra-High Volume).")
        ],
        "quote": "Bảng giá và biểu đồ nến có thể đánh lừa bạn bằng những cú quét râu giả tạo, nhưng khối lượng giao dịch là thứ duy nhất nhà tạo lập không thể giấu giếm được. Khối lượng chính là ADN của dòng tiền.",
        "quote_author": "Tom Williams (Master the Markets)",
        "html_content": """
            <h2><i class="fa-solid fa-calculator"></i> 1. Spread Là Gì Dưới Lăng Kính VSA?</h2>
            <p>
                Khác với định nghĩa Spread trong Forex (chênh lệch giữa giá Bid và Ask), trong <strong>Volume Spread Analysis (VSA)</strong>, <strong>Spread chính là biên độ di chuyển của giá</strong> trong một khung thời gian xác định.
            </p>
            <ul>
                <li><strong>Wide Spread (Biên độ rộng):</strong> Giá biến động mạnh mẽ, khoảng cách từ đỉnh đến đáy rất lớn. Thể hiện một bên đang áp đảo toàn diện.</li>
                <li><strong>Narrow Spread (Biên độ hẹp):</strong> Giá biến động rất nhỏ, nến bị nén chặt. Thể hiện sự do dự hoặc thị trường đang bị bóp nghẹt thanh khoản.</li>
                <li><strong>Average Spread (Biên độ trung bình):</strong> Di chuyển bình thường theo nhịp tự nhiên của thị trường.</li>
            </ul>

            <h2><i class="fa-solid fa-chart-column"></i> 2. Phân Loại 4 Cấp Độ Khối Lượng (Volume Benchmark)</h2>
            <p>
                Để đọc được VSA, bạn cần gắn đường Trung bình Khối lượng 20 kỳ (Volume SMA 20) vào cửa sổ Volume để làm thước đo tham chiếu khách quan:
            </p>
            <div class="step-card">
                <h4>1. Khối lượng thấp (Low Volume): Cột Volume nằm dưới 50% đường SMA 20</h4>
                <p>Ý nghĩa: Thị trường thiếu vắng sự tham gia của các tay to; thanh khoản chỉ do nhỏ lẻ trao tay.</p>
            </div>
            <div class="step-card">
                <h4>2. Khối lượng trung bình (Average Volume): Cột Volume xấp xỉ đường SMA 20</h4>
                <p>Ý nghĩa: Hoạt động thị trường bình thường, không có dấu chân đột biến của dòng tiền lớn.</p>
            </div>
            <div class="step-card">
                <h4>3. Khối lượng cao (High Volume): Cột Volume cao gấp 1.5 - 2 lần SMA 20</h4>
                <p>Ý nghĩa: Bắt đầu có sự can thiệp tích cực của các quỹ đầu tư thể chế.</p>
            </div>
            <div class="step-card">
                <h4>4. Khối lượng siêu cao đột biến (Ultra-High Volume): Cao gấp 3 - 5 lần bình thường</h4>
                <p>Ý nghĩa: BÁO ĐỘNG ĐỎ! Đây là lúc diễn ra các trận đại chiến thanh khoản: Cao trào mua (Buying Climax), Cao trào bán (Selling Climax) hoặc bẫy xả hàng quy mô lớn.</p>
            </div>
        """,
        "comments": [
            ("Lê Tuấn", "12/09/2026 21:10:00", "Khái niệm Spread trong VSA trước mình hay nhầm với chênh lệch Bid-Ask của sàn. Bài viết giải thích rất chuẩn xác."),
            ("Phương Nam", "12/09/2026 21:45:30", "Gắn SMA 20 vào Volume nhìn trực quan hẳn. Biết ngay khi nào là Ultra-High Volume để cảnh giác!"),
            ("Việt Dũng", "12/09/2026 22:15:00", "Tom Williams giải thích bản chất khối lượng quả là bậc thầy. Hóng bài tiếp theo về No Demand.")
        ]
    },

    # BÀI 6
    {
        "id": "6",
        "slug": "khoa-hoc-vsa-wyckoff-bai-6-doc-vi-nen-no-demand-va-upthrust",
        "title": "Bài 6: Đọc Vị Nến Cạn Cầu (No Demand Bar) &amp; Nến Thử Cầu (Upthrust)",
        "badge": "Học Phần 2 • Volume Spread Analysis • Bài 6",
        "desc": "Nhận diện dấu hiệu dòng tiền lớn từ chối mua đẩy giá lên cao; kỹ thuật bắt đỉnh sóng tăng giả tạo tại ngưỡng kháng cự bằng No Demand và Upthrust.",
        "read_time": "15 Phút Đọc",
        "views": "2,180 Lượt Xem",
        "date": "12/09/2026",
        "image": "../assets/images/candlesticks/shooting_star_chart.jpg",
        "image_caption": "Hình 6.1: Nến Upthrust quét cản kháng cự với râu nến dài từ chối giá quyết liệt.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-5-vsa-can-ban-spread-va-khoi-luong",
        "prev_title": "Bài 5: VSA Căn Bản - Spread & Khối Lượng",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-7-doc-vi-nen-no-supply-va-stopping-volume",
        "next_title": "Bài 7: Đọc Vị Nến No Supply & Stopping Volume",
        "takeaways": [
            ("Nến No Demand Bar:", "Nến tăng giá có thân hẹp (Narrow Spread), giá đóng cửa ở giữa hoặc nửa dưới, và Khối lượng THẤP HƠN cả 2 nến trước đó."),
            ("Bản Chất Của No Demand:", "Dòng tiền lớn KHÔNG THAM GIA mua ở mức giá cao này. Không có lực mua của tay to, thị trường bắt buộc phải sụp đổ."),
            ("Nến Upthrust (Cú Thử Cầu):", "Nến đâm thủng kháng cự nhưng bị đạp đóng cửa về đáy với Volume cực cao; đây là bẫy lừa F0 đu đỉnh kinh điển."),
            ("Kỹ Thuật Vào Lệnh Short:", "Đặt lệnh Sell Stop dưới đáy của nến No Demand hoặc Upthrust sau khi xuất hiện nến xác nhận giảm tiếp theo.")
        ],
        "quote": "Một thị trường không thể tiếp tục tăng nếu những kẻ nắm giữ hàng triệu USD từ chối đặt lệnh mua ở mức giá cao hơn. Thiếu vắng nhu cầu mua (No Demand) là lời tuyên án tử cho mọi xu hướng tăng.",
        "quote_author": "PTvolume VSA Trading Desk",
        "html_content": """
            <h2><i class="fa-solid fa-hand-holding-dollar"></i> 1. Nến No Demand Bar &ndash; Khi Dòng Tiền Lớn Nói 'KHÔNG'</h2>
            <p>
                Hãy tưởng tượng bạn đang chứng kiến một buổi đấu giá tranh nghệ thuật. Người điều hành phiên đấu giá hét giá 10 triệu USD, nhưng cả khán phòng im phăng phắc, không một cánh tay nào giơ lên. Đó chính là <strong>No Demand Bar (Thanh Nến Không Có Lực Cầu)</strong> trên đồ thị giá!
            </p>
            <p>
                <strong>Đặc điểm nhận dạng chuẩn VSA:</strong>
            </p>
            <ul>
                <li>Là một thanh nến TĂNG (hoặc nến Doji xanh nhẹ).</li>
                <li>Thân nến hẹp hoặc trung bình (Narrow Spread).</li>
                <li>Khối lượng (Volume) <strong>thấp hơn hẳn so với khối lượng của 2 thanh nến liền trước</strong>.</li>
                <li>Vị trí xuất hiện: Thường xuất hiện trong nhịp hồi phục nhẹ (Pullback) sau một xu hướng giảm, hoặc ngay tại ngưỡng kháng cự then chốt.</li>
            </ul>

            <h2><i class="fa-solid fa-bolt-lightning"></i> 2. Nến Upthrust &ndash; Cú Quét Bẫy Thanh Khoản Kinh Hoàng</h2>
            <p>
                Upthrust là một trong những thanh nến đảo chiều giảm uy lực nhất trong toàn bộ phương pháp VSA. Nó diễn ra như sau:
            </p>
            <p>
                Vào đầu phiên, giá được đẩy tăng vọt vượt qua mức đỉnh cũ của ngày hôm trước. Nhìn thấy điều này, hàng ngàn trader nhỏ lẻ hưng phấn nhảy vào Buy đuổi vì nghĩ rằng giá đã Breakout. Nhưng ngay lập tức, Smart Money tung hàng triệu cổ phiếu/hợp đồng ra bán tháo vào đầu phe mua nhỏ lẻ, đạp giá đóng cửa tụt về tận đáy thấp nhất phiên.
            </p>
            <p>
                Cây nến kết thúc với một <strong>chiếc râu nến trên dài ngoằng</strong> và Volume cao chót vót. Toàn bộ phe Mua Breakout bị kẹp chặt trong chiếc bẫy Upthrust và chỉ chờ bị thanh lý!
            </p>
        """,
        "comments": [
            ("Minh Khang", "12/09/2026 22:30:10", "No Demand bar đúng là chỉ báo sớm tuyệt vời. Nhìn volume tụt đáy là biết tay to không mua rồi."),
            ("Hoàng Yến", "12/09/2026 23:05:00", "Trước đây hay bị dính đòn nến Upthrust này lắm. Giờ thấy volume cao mà râu trên dài ngoằng là chỉ canh Short."),
            ("Quang Huy", "12/09/2026 23:40:20", "Bài học rất trực quan, ví dụ phòng đấu giá cực kỳ dễ hiểu cho người mới!")
        ]
    },

    # BÀI 7
    {
        "id": "7",
        "slug": "khoa-hoc-vsa-wyckoff-bai-7-doc-vi-nen-no-supply-va-stopping-volume",
        "title": "Bài 7: Đọc Vị Nến Cạn Cung (No Supply Bar) &amp; Nến Dừng Giá (Stopping Volume)",
        "badge": "Học Phần 2 • Volume Spread Analysis • Bài 7",
        "desc": "Nhận diện dấu hiệu cạn kiệt lực bán; phát hiện dòng tiền lớn ra tay hấp thụ lệnh bán tháo hoảng loạn của F0 để tạo đáy qua Stopping Volume.",
        "read_time": "16 Phút Đọc",
        "views": "2,420 Lượt Xem",
        "date": "12/09/2026",
        "image": "../assets/images/candlesticks/hammer_candle.jpg",
        "image_caption": "Hình 7.1: Nến Stopping Volume xuất hiện tại đáy hỗ trợ chặn đứng đà lao dốc của thị trường.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-6-doc-vi-nen-no-demand-va-upthrust",
        "prev_title": "Bài 6: Đọc Vị Nến No Demand & Upthrust",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-8-hap-thu-cung-absorption-va-phan-phoi-am-tham",
        "next_title": "Bài 8: Hấp Thụ Cung & Phân Phối Âm Thầm",
        "takeaways": [
            ("No Supply Bar (Cạn Cung):", "Nến giảm thân hẹp có Volume thấp hơn 2 nến trước; chứng minh không còn ai muốn bán tháo ở mức giá rẻ này nữa."),
            ("Stopping Volume (Khối Lượng Dừng Giá):", "Nến giảm có biên độ co hẹp dần nhưng Volume cực đại; dấu hiệu Smart Money đặt hàng loạt lệnh mua giới hạn (Buy Limit) để hấp thụ toàn bộ lực xả."),
            ("Quy Tắc Quả Bóng Rơi:", "Stopping Volume giống như một chiếc lưới an toàn giăng ra dưới đáy vực; khi quả bóng rơi vào lưới, đà rơi sẽ bị triệt tiêu hoàn toàn."),
            ("Điểm Vào Lệnh Buy:", "Kiên nhẫn chờ một thanh nến No Supply xuất hiện sau Stopping Volume để kích hoạt lệnh Buy với xác suất thắng trên 80%.")
        ],
        "quote": "Đáy thị trường không bao giờ được tạo ra vì mọi người đều lạc quan, mà được tạo ra khi kẻ cuối cùng muốn bán tháo đã bán xong. Khi nguồn cung cạn kiệt, con đường ít lực cản nhất sẽ tự động quay đầu hướng lên.",
        "quote_author": "Jesse Livermore",
        "html_content": """
            <h2><i class="fa-solid fa-battery-empty"></i> 1. No Supply Bar &ndash; Khi Nguồn Cung Bị Rút Cạn Khô</h2>
            <p>
                Sau một đợt giảm giá kéo dài, nếu thị trường muốn tăng trở lại, điều kiện tiên quyết là <strong>nguồn cung (áp lực bán) phải được dọn sạch</strong>. Nếu vẫn còn nhiều người muốn bán tháo, Smart Money sẽ không dại gì đẩy giá lên để cho người khác chốt lời vào đầu mình.
            </p>
            <p>
                <strong>Dấu hiệu của No Supply Bar:</strong>
            </p>
            <ul>
                <li>Là một thanh nến GIẢM có thân hẹp (Narrow Spread).</li>
                <li>Giá đóng cửa nằm ở nửa trên hoặc giữa thanh nến.</li>
                <li>Volume <strong>thấp hơn rõ rệt so với 2 thanh nến trước đó</strong>.</li>
                <li>Ý nghĩa: Không còn ai muốn bán ra ở vùng giá này nữa. Phe Bán đã kiệt sức!</li>
            </ul>

            <h2><i class="fa-solid fa-shield"></i> 2. Stopping Volume &ndash; Tấm Khiên Hấp Thụ Khổng Lồ</h2>
            <p>
                Trong các đợt sụp đổ hoảng loạn (Market Crash / Panic Selling), F0 ồ ạt bấm nút Market Sell để cắt lỗ bằng mọi giá. Nhưng thay vì giá rơi tự do không phanh, bạn đột ngột thấy xuất hiện một cây nến có râu dưới dài và Volume to khổng lồ.
            </p>
            <p>
                Ai là người đã mua hết toàn bộ số lượng lệnh bán tháo điên cuồng đó? <strong>Chính là Smart Money!</strong> Họ đã kê sẵn hàng triệu lệnh Buy Limit để gom sạch hàng giá rẻ. Cú chạm đó được gọi là <strong>Stopping Volume (Khối lượng dừng xu hướng)</strong>, báo hiệu đáy chu kỳ đã được thiết lập.
            </p>
        """,
        "comments": [
            ("Trần Kiên", "13/09/2026 08:15:20", "Stopping volume trên cặp Vàng khung H4 chuẩn không cần chỉnh! Cứ thấy volume khổng lồ mà nến rút râu dưới là chuẩn bị gom hàng."),
            ("Thanh Sơn", "13/09/2026 09:00:10", "No Supply Bar kết hợp với Hỗ trợ Flip Zone là setup có winrate cao nhất của mình."),
            ("Hoài An", "13/09/2026 09:45:00", "Ví dụ về tấm lưới hấp thụ lực rơi rất hình tượng và trực quan, giúp người mới nắm bắt ngay bản chất nến Stopping Volume.")
        ]
    },

    # BÀI 8
    {
        "id": "8",
        "slug": "khoa-hoc-vsa-wyckoff-bai-8-hap-thu-cung-absorption-va-phan-phoi-am-tham",
        "title": "Bài 8: Hiện Tượng Hấp Thụ Cung (Absorption) &amp; Phân Phối Âm Thầm (Churning)",
        "badge": "Học Phần 2 • Volume Spread Analysis • Bài 8",
        "desc": "Giải mã hiện tượng nến thân nhỏ nhưng Volume kỷ lục: Bẫy thanh khoản kinh điển của tạo lập thị trường trước khi bẻ gãy xu hướng.",
        "read_time": "15 Phút Đọc",
        "views": "2,050 Lượt Xem",
        "date": "13/09/2026",
        "image": "../assets/images/candlesticks/doji_chart.jpg",
        "image_caption": "Hình 8.1: Hiện tượng Churning - Nỗ lực khối lượng lớn bị kẹt lại không tạo ra kết quả di chuyển giá.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-7-doc-vi-nen-no-supply-va-stopping-volume",
        "prev_title": "Bài 7: Đọc Vị Nến No Supply & Stopping Volume",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-9-ba-quy-luat-song-con-cua-richard-wyckoff",
        "next_title": "Bài 9: 3 Quy Luật Sống Còn Của Richard Wyckoff",
        "takeaways": [
            ("Hiện Tượng Churning Là Gì?", "Thị trường giao dịch sôi động với Volume siêu cao nhưng thân nến hầu như không di chuyển (Narrow Spread)."),
            ("Bản Chất Của Sự Khập Khiễng:", "Nỗ lực cực đại (Ultra-High Volume) nhưng kết quả bằng không (No Progress) chứng minh có một lực cản đối ứng khổng lồ đang âm thầm hấp thụ."),
            ("Absorption Tại Kháng Cự:", "Smart Money chủ động hấp thụ toàn bộ lệnh bán để chuẩn bị cho cú bứt phá nhảy qua lạch (Jumping Across the Creek)."),
            ("Churning Tại Đỉnh (Phân Phối):", "Smart Money âm thầm xả hàng sang tay F0 trong khi giá vẫn được giữ ở mức cao để dụ dỗ người mua.")
        ],
        "quote": "Khi bạn thấy một chiếc xe hơi nhấn hết chân ga, động cơ gầm rú với vòng tua máy cực đại (Khối lượng lớn) nhưng chiếc xe vẫn đứng yên tại chỗ (Spread nhỏ) &ndash; bạn biết rằng chiếc xe đó đang húc vào một bức tường bê tông cốt thép.",
        "quote_author": "David Weis (Trades About to Happen)",
        "html_content": """
            <h2><i class="fa-solid fa-gears"></i> 1. Churning &ndash; Nghịch Lý Động Cơ Gầm Rú Nhưng Xe Không Chạy</h2>
            <p>
                Quy luật nỗ lực và kết quả của Wyckoff quy định: Nỗ lực (Volume) phải tương xứng với Kết quả (Độ dài nến). Khi bạn thấy một cây nến có Volume cao kỷ lục (Ultra-High Volume), bạn kỳ vọng nó phải là một cây nến Marubozu dài ngoằng.
            </p>
            <p>
                Thế nhưng trên biểu đồ lại xuất hiện một cây nến thân tí hon, giá đóng cửa dậm chân tại chỗ. Hiện tượng này trong VSA gọi là <strong>Churning (Khuấy đảo thanh khoản)</strong>.
            </p>

            <h2><i class="fa-solid fa-arrows-split-up-and-left"></i> 2. Phân Biệt Absorption (Tích Lũy) vs Churning (Phân Phối)</h2>
            <ul>
                <li><strong>Hấp Thụ Cung (Absorption - Tích Cực):</strong> Diễn ra ngay dưới ngưỡng kháng cự mạnh. Smart Money chấp nhận chi tiền mua lại toàn bộ cổ phiếu mà các nhà đầu tư muốn chốt lời bán ra. Khi nguồn bán cạn sạch, giá sẽ bùng nổ xuyên cản.</li>
                <li><strong>Phân Phối Âm Thầm (Churning - Tiêu Cực):</strong> Diễn ra sau một chu kỳ tăng giá dài. Smart Money liên tục sang tay bán chốt lời cho F0 đang say men chiến thắng. Nến không thể tăng thêm được nữa vì cứ có ai mua là tay to lập tức dội hàng ra bán.</li>
            </ul>
        """,
        "comments": [
            ("Lâm Vũ", "13/09/2026 10:15:00", "Ví dụ về chiếc xe rồ ga húc tường bê tông quá đắt giá! Đọc xong là hiểu ngay hiện tượng Churning."),
            ("Mai Chi", "13/09/2026 11:00:20", "Bài học rất logic. Nỗ lực lớn mà không tạo ra kết quả là dấu hiệu bất thường rõ ràng nhất."),
            ("Thế Hưng", "13/09/2026 11:40:00", "VSA giải thích được những điều mà mọi chỉ báo RSI hay MACD hoàn toàn bó tay.")
        ]
    },

    # BÀI 9
    {
        "id": "9",
        "slug": "khoa-hoc-vsa-wyckoff-bai-9-ba-quy-luat-song-con-cua-richard-wyckoff",
        "title": "Bài 9: Ba Quy Luật Sống Còn Của Richard Wyckoff (Cung Cầu, Nguyên Nhân &amp; Nỗ Lực)",
        "badge": "Học Phần 3 • Phương Pháp Wyckoff • Bài 9",
        "desc": "Khám phá 3 quy luật vĩnh cửu điều khiển thị trường tài chính của Richard D. Wyckoff: Cung - Cầu, Nguyên nhân - Kết quả và Nỗ lực - Kết quả.",
        "read_time": "16 Phút Đọc",
        "views": "2,560 Lượt Xem",
        "date": "13/09/2026",
        "image": "../assets/images/ticker_tape_board.jpg",
        "image_caption": "Hình 9.1: Ba quy luật vĩnh cửu của Richard Wyckoff - Kim chỉ nam của mọi chu kỳ tài chính.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-8-hap-thu-cung-absorption-va-phan-phoi-am-tham",
        "prev_title": "Bài 8: Hấp Thụ Cung & Phân Phối Âm Thầm",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-10-boc-tach-5-pha-tich-luy-wyckoff-va-cu-ru-bo-spring",
        "next_title": "Bài 10: 5 Pha Tích Lũy Wyckoff & Tuyệt Kỹ Spring",
        "takeaways": [
            ("1. Quy Luật Cung &amp; Cầu:", "Khi Cầu > Cung $\rightarrow$ Giá Tăng; Khi Cung > Cầu $\rightarrow$ Giá Giảm; Khi Cung = Cầu $\rightarrow$ Thị trường đi ngang tích lũy."),
            ("2. Quy Luật Nguyên Nhân &amp; Kết Quả:", "Không có xu hướng lớn nào tự nhiên sinh ra. Vùng tích lũy đi ngang càng dài (Nguyên nhân lớn), con sóng tăng sau đó càng bùng nổ dữ dội (Kết quả lớn)."),
            ("3. Quy Luật Nỗ Lực &amp; Kết Quả:", "Khối lượng (Nỗ lực) phải phản ánh tương xứng với độ dịch chuyển của Nến (Kết quả). Bất thường là nơi xuất hiện cơ hội giao dịch."),
            ("Nhà Tạo Lập (Composite Man):", "Wyckoff dạy chúng ta xem toàn bộ thị trường như được vận hành bởi một thực thể duy nhất: Ngài Tạo Lập Thị Trường.")
        ],
        "quote": "Thị trường tài chính không vận hành ngẫu nhiên. Nó vận hành dựa trên các quy luật kinh tế và tâm lý vĩnh cửu mà con người không bao giờ thay đổi được trong hàng trăm năm qua.",
        "quote_author": "Richard D. Wyckoff",
        "html_content": """
            <h2><i class="fa-solid fa-landmark"></i> 1. Richard Wyckoff &amp; Khái Niệm 'Composite Man'</h2>
            <p>
                Richard Demille Wyckoff (1873 &ndash; 1934) là một trong những tượng đài bất tử của Phố Wall. Ông là người tiên phong đưa ra khái niệm <strong>The Composite Man (Nhà Tạo Lập / Người Tổng Hợp)</strong>.
            </p>
            <p>
                Wyckoff khuyên các nhà đầu tư: Hãy xem toàn bộ biến động trên thị trường như được điều khiển bởi một cá nhân khổng lồ ngồi sau hậu trường. Người đàn ông này chuẩn bị hàng tháng trời để gom hàng bí mật (Tích lũy), sau đó đẩy giá lên cao (Đẩy sóng), bán trao tay cho công chúng ở đỉnh (Phân phối), và đạp giá rơi xuống để bắt đầu chu kỳ mới.
            </p>

            <h2><i class="fa-solid fa-scale-balanced"></i> 2. Chi Tiết 3 Quy Luật Wyckoff Cốt Lõi</h2>
            <div class="step-card">
                <h4>Quy luật 1: Cung và Cầu (Law of Supply and Demand)</h4>
                <p>Quyết định phương hướng di chuyển của giá. Nếu người mua sẵn sàng trả giá cao hơn để sở hữu hàng hóa vì nguồn cung khan hiếm $\rightarrow$ Giá buộc phải tăng. Ngược lại, nếu nguồn cung tràn ngập thị trường mà không ai muốn mua $\rightarrow$ Giá buộc phải hạ.</p>
            </div>
            <div class="step-card">
                <h4>Quy luật 2: Nguyên Nhân và Kết Quả (Law of Cause and Effect)</h4>
                <p>Nguyên nhân được đo lường bằng độ dài thời gian và khối lượng tích lũy trong vùng Trading Range (TR). Kết quả là độ dài biên độ của con sóng theo sau. Bạn không thể đòi hỏi một con sóng tăng 500% nếu thị trường mới chỉ tích lũy trong 2 ngày!</p>
            </div>
            <div class="step-card">
                <h4>Quy luật 3: Nỗ Lực và Kết Quả (Law of Effort vs Result)</h4>
                <p>Nỗ lực thể hiện qua Volume; Kết quả thể hiện qua Spread của nến. Nếu nỗ lực và kết quả đồng thuận $\rightarrow$ Xu hướng vững chắc. Nếu nỗ lực và kết quả bất hòa $\rightarrow$ Đảo chiều đang đến gần.</p>
            </div>
        """,
        "comments": [
            ("Hoàng Long", "13/09/2026 12:30:00", "Triết lý Composite Man của Wyckoff giúp mình thay đổi hoàn toàn tư duy. Không còn cay cú thị trường mà học cách bơi cùng cá mập."),
            ("Thành Đạt", "13/09/2026 13:15:20", "Quy luật Cause & Effect rất chuẩn, tích lũy càng lâu nén càng chặt thì sóng sau bùng nổ càng xa."),
            ("Bích Phương", "13/09/2026 14:00:10", "Bài học kinh điển của mọi trader. Bài viết hành văn rất cuốn hút và gãy gọn!")
        ]
    },

    # BÀI 10
    {
        "id": "10",
        "slug": "khoa-hoc-vsa-wyckoff-bai-10-boc-tach-5-pha-tich-luy-wyckoff-va-cu-ru-bo-spring",
        "title": "Bài 10: Bóc Tách 5 Pha Tích Lũy Wyckoff &amp; Tuyệt Kỹ Bắt Cú Rũ Bỏ Spring (Pha C)",
        "badge": "Học Phần 3 • Phương Pháp Wyckoff • Bài 10",
        "desc": "Giải mã chi tiết 5 pha tích lũy Wyckoff (Phase A - E): Selling Climax, Automatic Rally, và tuyệt kỹ vào lệnh đón đầu chân sóng lớn tại cú rũ bỏ Spring.",
        "read_time": "18 Phút Đọc",
        "views": "2,890 Lượt Xem",
        "date": "13/09/2026",
        "image": "../assets/images/wyckoff_accumulation_schematic.svg",
        "image_caption": "Hình 10.1: Sơ đồ 5 pha tích lũy Wyckoff chuẩn mực và vị trí cú rũ bỏ Spring (Pha C).",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-9-ba-quy-luat-song-con-cua-richard-wyckoff",
        "prev_title": "Bài 9: 3 Quy Luật Sống Còn Của Richard Wyckoff",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-11-boc-tach-5-pha-phan-phoi-wyckoff-va-bay-utad",
        "next_title": "Bài 11: 5 Pha Phân Phối Wyckoff & Bẫy Mua Đỉnh UTAD",
        "takeaways": [
            ("Pha A - Dừng Xu Hướng Giảm:", "Bao gồm PS, SC (Selling Climax cao trào bán), AR (Hồi tự động tạo trần TR) và ST (Thử nghiệm thứ cấp)."),
            ("Pha B - Xây Dựng Nguyên Nhân:", "Giai đoạn dòng tiền lớn âm thầm gom nhặt cổ phiếu/hợp đồng ở vùng giá sàn."),
            ("Pha C - Cú Rũ Bỏ Spring:", "ĐIỂM VÀO LỆNH VÀNG! Giá cố tình đâm thủng hỗ trợ để quét sạch Stop Loss rồi giật ngược trở lại biên độ."),
            ("Pha D &amp; E - Bứt Phá &amp; Tăng Tốc:", "Xuất hiện các tín hiệu SOS (Sign of Strength), điểm mua gia tăng LPS và bước vào sóng tăng tốc Markup.")
        ],
        "quote": "Cú rũ bỏ Spring trong Pha C của Wyckoff là món quà tuyệt vời nhất mà nhà tạo lập ban tặng cho trader kiên nhẫn. Đó là nơi bạn mua được giá rẻ nhất với rủi ro thấp nhất ngay trước khi con sóng thần xuất hiện.",
        "quote_author": "Ruben Villahermosa (The Wyckoff Methodology)",
        "html_content": """
            <h2><i class="fa-solid fa-diagram-project"></i> 1. Bóc Tách 5 Pha Tích Lũy Wyckoff Chuẩn</h2>
            <p>
                Sơ đồ tích lũy của Wyckoff là một kiệt tác giải phẫu tâm lý đám đông:
            </p>
            <ul>
                <li><strong>PHA A (Dừng xu hướng giảm trước đó):</strong> Giá lao dốc tạo cú bán tháo hoảng loạn <em>Selling Climax (SC)</em> với Volume khổng lồ. Lực mua chặn đáy của Smart Money kích hoạt cú nảy <em>Automatic Rally (AR)</em> định hình biên độ Trading Range.</li>
                <li><strong>PHA B (Hấp thụ nguồn cung ngầm):</strong> Thời gian dài nhất trong chu kỳ. Giá dao động dập dờn giữa hỗ trợ và kháng cự để thử lòng kiên nhẫn của F0, khiến họ chán nản bỏ cuộc và bán rẻ tài sản.</li>
                <li><strong>PHA C (Thử nghiệm nguồn cung &ndash; SPRING):</strong> Đỉnh cao chiến thuật của Smart Money! Giá đột ngột đạp thủng hỗ trợ cứng. Toàn bộ trader đặt SL dưới hỗ trợ đều bị quét sạch. Nhưng ngay sau đó, giá đóng cửa kéo ngược trở lại vào trong hộp tích lũy.</li>
                <li><strong>PHA D (Bứt phá khỏi Trading Range):</strong> Xuất hiện các cây nến tăng mạnh mẽ với Volume cao <em>(Sign of Strength - SOS)</em>, theo sau là nhịp kiểm định cạn cung <em>(Last Point of Support - LPS)</em>.</li>
                <li><strong>PHA E (Thị trường mở sóng tăng tốc Markup):</strong> Giá hoàn toàn thoát khỏi vùng tích lũy và phi thẳng lên các tầm cao mới.</li>
            </ul>

            <h2><i class="fa-solid fa-bullseye"></i> 2. Tuyệt Kỹ Bắt Lệnh Tại Spring (Pha C)</h2>
            <p>
                Có 2 cách vào lệnh với Spring:
            </p>
            <ol>
                <li><strong>Vào lệnh mạo hiểm (Aggressive Entry):</strong> Khi nến Spring đâm thủng hỗ trợ rồi rút râu đóng cửa ngược vào trong TR $\rightarrow$ Mua ngay tại giá đóng cửa của nến Spring, Stop Loss dưới đáy râu nến.</li>
                <li><strong>Vào lệnh an toàn (Conservative Entry):</strong> Chờ cây nến tiếp theo kiểm định lại đáy nến Spring với Volume thấp (Test of Spring) $\rightarrow$ Mua khi nến Test đóng cửa xanh. Tỷ lệ Risk:Reward ở đây thường đạt từ 1:4 đến 1:7!</li>
            </ol>
        """,
        "comments": [
            ("Đăng Khoa", "13/09/2026 14:40:00", "Sơ đồ SVG 5 pha tích lũy vẽ quá đỉnh! Nhìn một phát là định vị được ngay Spring nằm ở đâu."),
            ("Quỳnh Như", "13/09/2026 15:15:30", "Bắt được Spring ở khung H4 vàng đúng là cảm giác ăn trọn con sóng lớn vô cùng phấn khích."),
            ("Bảo Long", "13/09/2026 16:00:00", "Giải thích chi tiết từ SC đến AR rồi LPS rất tường minh. Cảm ơn admin!")
        ]
    },

    # BÀI 11
    {
        "id": "11",
        "slug": "khoa-hoc-vsa-wyckoff-bai-11-boc-tach-5-pha-phan-phoi-wyckoff-va-bay-utad",
        "title": "Bài 11: Bóc Tách 5 Pha Phân Phối Wyckoff &amp; Bẫy Mua Đỉnh UTAD (Pha C)",
        "badge": "Học Phần 3 • Phương Pháp Wyckoff • Bài 11",
        "desc": "Nhận diện bẫy phân phối đỉnh tinh vi của Smart Money: Cao trào mua Buying Climax, cú lừa mua đỉnh UTAD và điểm vào lệnh Short đón đầu sụp đổ Markdown.",
        "read_time": "17 Phút Đọc",
        "views": "2,480 Lượt Xem",
        "date": "13/09/2026",
        "image": "../assets/images/wyckoff_distribution_schematic.svg",
        "image_caption": "Hình 11.1: Sơ đồ 5 pha phân phối Wyckoff và bẫy lừa người mua đỉnh UTAD (Pha C).",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-10-boc-tach-5-pha-tich-luy-wyckoff-va-cu-ru-bo-spring",
        "prev_title": "Bài 10: 5 Pha Tích Lũy Wyckoff & Tuyệt Kỹ Spring",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-12-bay-thanh-khoan-liquidity-hunt-va-stop-hunt",
        "next_title": "Bài 12: Bẫy Thanh Khoản & Stop Hunt Của Smart Money",
        "takeaways": [
            ("Buying Climax (BC - Cao Trào Mua):", "Khối lượng cực đại xuất hiện khi tin tức tốt nhất tràn ngập mặt báo; F0 hưng phấn đu đỉnh và Smart Money bắt đầu xả hàng đợt 1."),
            ("Pha C Phân Phối &ndash; Bẫy UTAD:", "Upthrust After Distribution: Cú rướn giả vượt đỉnh cũ để tạo cảm giác giá sắp bay lên mặt trăng, thực chất là cái bẫy để gom nốt thanh khoản bán khống."),
            ("Dấu Hiệu Yếu Ớt (Sign of Weakness - SOW):", "Giá rơi thẳng đứng xuyên thủng hỗ trợ với các nến đỏ thân dài."),
            ("Điểm Bán Khống Đẹp Nhất (LPSY):", "Last Point of Supply: Nhịp hồi yếu ớt cạn kiệt Volume lên kiểm định lại hỗ trợ vừa bị thủng $\rightarrow$ Kích hoạt lệnh Short tổng lực.")
        ],
        "quote": "Tại đỉnh của thị trường, tin tức luôn luôn tuyệt vời nhất, sự lạc quan luôn ở mức cao nhất, và đó chính là lúc nhà tạo lập thị trường trao lại chiếc cúp than hồng cho những kẻ ngây thơ.",
        "quote_author": "Richard D. Wyckoff",
        "html_content": """
            <h2><i class="fa-solid fa-mountain"></i> 1. Cơ Chế Phân Phối Của Smart Money</h2>
            <p>
                Sau một chu kỳ tăng giá thần tốc, Smart Money nắm giữ hàng triệu cổ phiếu/hợp đồng mua từ vùng đáy. Làm thế nào để họ bán ra số lượng khổng lồ đó mà giá không bị sập ngay lập tức?
            </p>
            <p>
                Họ bắt buộc phải tạo ra một vùng đi ngang tích tắc được gọi là <strong>Trading Range Phân Phối (Distribution)</strong>, nơi họ liên tục bơm các tin tức lạc quan, kích thích lòng tham của đám đông F0 nhảy vào mua, để họ ung dung xả hàng dần dần.
            </p>

            <h2><i class="fa-solid fa-skull-crossbones"></i> 2. Giải Mã Cú Lừa Kinh Điển UTAD (Pha C)</h2>
            <p>
                <strong>UTAD (Upthrust After Distribution)</strong> là đối trọng của Spring, nhưng xuất hiện tại đỉnh:
            </p>
            <p>
                Khi mọi người nghĩ rằng thị trường đã sẵn sàng bứt phá lên đỉnh cao mới, giá phóng vụt qua ngưỡng kháng cự cao nhất của TR. Nhóm breakout trader hò reo nhảy vào mua đuổi. Nhưng hỡi ôi, ngay sau đó nến quay đầu cắm thẳng xuống đóng cửa dưới cản, tạo thành một thanh nến Upthrust khổng lồ.
            </p>
            <p>
                Toàn bộ những người mua tại UTAD lập tức bị kẹt hàng và trở thành nguồn thanh khoản bị bức tử trong pha lao dốc Markdown theo sau!
            </p>
        """,
        "comments": [
            ("Hoàng Nam", "13/09/2026 16:30:00", "UTAD chính là bài học xương máu của mình năm 2024. Đu đỉnh vì tin tức quá tốt rồi ăn trọn cây thông Noel."),
            ("Văn Toàn", "13/09/2026 17:05:10", "Sơ đồ phân phối chi tiết và sắc sảo lắm admin. Điểm LPSY bán cực kỳ an toàn."),
            ("Hải Đăng", "13/09/2026 17:40:00", "Đọc xong bài 10 và 11 là nắm trọn vẹn vòng đời tích lũy - đẩy giá - phân phối - đè giá.")
        ]
    },

    # BÀI 12
    {
        "id": "12",
        "slug": "khoa-hoc-vsa-wyckoff-bai-12-bay-thanh-khoan-liquidity-hunt-va-stop-hunt",
        "title": "Bài 12: Bẫy Thanh Khoản (Liquidity Hunts) &amp; Stop Hunt Của Smart Money",
        "badge": "Học Phần 3 • Phương Pháp Wyckoff • Bài 12",
        "desc": "Hiểu rõ cơ chế săn thanh khoản: Nơi đám đông đặt Stop Loss chính là mỏ vàng của Smart Money. Nghệ thuật tránh bẫy và bơi theo dấu chân cá mập.",
        "read_time": "16 Phút Đọc",
        "views": "2,610 Lượt Xem",
        "date": "13/09/2026",
        "image": "../assets/images/dao_warren_buffett_framework.svg",
        "image_caption": "Hình 12.1: Bản đồ thanh khoản và các vùng bẫy săn Stop Loss của nhà tạo lập.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-11-boc-tach-5-pha-phan-phoi-wyckoff-va-bay-utad",
        "prev_title": "Bài 11: 5 Pha Phân Phối Wyckoff & Bẫy Mua Đỉnh UTAD",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-13-setup-1-ban-tia-dao-chieu-cung-cau-vsa",
        "next_title": "Bài 13: Setup 1 - Bắn Tỉa Đảo Chiều Cung Cầu",
        "takeaways": [
            ("Thanh Khoản Là Gì?", "Thanh khoản là xăng dầu để bộ máy thị trường vận hành. Smart Money cần hàng triệu đơn vị lệnh đối ứng để khớp vị thế."),
            ("Mỏ Vàng Stop Loss:", "Đám đông nhỏ lẻ luôn đặt SL ngay sát dưới đáy cũ hoặc ngay trên đỉnh cũ $\rightarrow$ Đây chính là nơi tập trung thanh khoản dày đặc nhất."),
            ("Cơ Chế Stop Hunt:", "Smart Money cố tình đẩy giá giật qua các mốc đó để kích hoạt hàng loạt lệnh cắt lỗ tự động, tạo thanh khoản cho chính họ gom hàng."),
            ("Tư Duy Săn Cá Mập:", "Thay vì đặt SL như đám đông và trở thành nạn nhân, hãy kiên nhẫn chờ cú Stop Hunt diễn ra xong rồi mới vào lệnh cùng hướng với cá mập.")
        ],
        "quote": "Nếu bạn ngồi vào bàn poker trong 30 phút mà không biết ai là kẻ ngốc bị vặt lông, thì người đó chính là bạn. Trên thị trường, nếu bạn không biết thanh khoản nằm ở đâu, thì chính tài khoản của bạn là thanh khoản cho kẻ khác.",
        "quote_author": "Phố Wall Ngạn Ngữ",
        "html_content": """
            <h2><i class="fa-solid fa-water"></i> 1. Vì Sao Smart Money Buộc Phải Săn Thanh Khoản?</h2>
            <p>
                Một nhà đầu tư nhỏ lẻ có thể mua 1 lot Vàng hoặc 1.000 cổ phiếu bằng một cú click chuột mà không làm dịch chuyển thị trường. Nhưng một quỹ đầu tư nắm giữ <strong>500 triệu USD</strong> muốn mua vào thì sao?
            </p>
            <p>
                Nếu họ bấm lệnh Market Buy, thị trường sẽ lập tức trượt giá (Slippage) bay vút lên đỉnh và họ phải mua với giá cắt cổ. Do đó, cách duy nhất để họ khớp được 500 triệu USD là <strong>phải tìm thấy một lượng lệnh BÁN đối ứng khổng lồ tương đương</strong>.
            </p>
            <p>
                Lượng lệnh Bán đó nằm ở đâu? Nằm ở chính các lệnh <em>Stop Loss (Lệnh dừng lỗ bán)</em> của hàng ngàn trader nhỏ lẻ đang đặt ngay dưới các đáy hỗ trợ rõ như ban ngày!
            </p>

            <h2><i class="fa-solid fa-magnifying-glass-dollar"></i> 2. Bản Đồ Nhận Diện Bẫy Stop Hunt</h2>
            <div class="step-card">
                <h4>Vùng 1: Equal Highs / Equal Lows (Đáy/Đỉnh Bằng Nhau)</h4>
                <p>Khi biểu đồ tạo 2 hoặc 3 đáy bằng nhau (Mô hình 2 đáy / 3 đáy trong sách giáo khoa), F0 coi đó là hỗ trợ thép và đặt SL ngay dưới đó. Smart Money chỉ cần một cú quét nến nhẹ xuyên thủng qua là nuốt trọn toàn bộ SL.</p>
            </div>
            <div class="step-card">
                <h4>Vùng 2: Ngưỡng Hỗ Trợ / Kháng Cự Quá Rõ Ràng</h4>
                <p>Càng nhiều người nhìn thấy một ngưỡng cản, thanh khoản tập trung tại đó càng lớn, và xác suất bị Smart Money săn Stop Hunt càng cao.</p>
            </div>
        """,
        "comments": [
            ("Gia Huy", "13/09/2026 18:10:00", "Thấm thía từng chữ! Hồi trước cứ đặt SL dưới đáy cũ là bị quét xong giá mới chạy đúng hướng. Giờ hiểu ra cơ chế thanh khoản."),
            ("Bảo Trâm", "13/09/2026 18:50:20", "Trích dẫn câu chuyện poker quá chuẩn. Học cách chờ cá mập quét xong mới vào lệnh nhẹ cả đầu."),
            ("Đức Anh", "13/09/2026 19:25:00", "Chuyển sang Học phần 4 học các setup bắn tỉa thực chiến thôi admin ơi!")
        ]
    },

    # BÀI 13
    {
        "id": "13",
        "slug": "khoa-hoc-vsa-wyckoff-bai-13-setup-1-ban-tia-dao-chieu-cung-cau-vsa",
        "title": "Bài 13: Setup 1 &ndash; Bắn Tỉa Đảo Chiều Tại Vùng Cung Cầu (Reversal at Key Zone)",
        "badge": "Học Phần 4 • Hệ Thống Setup Thực Chiến • Bài 13",
        "desc": "Công thức bắt đỉnh đáy xác suất thắng cao: Kết hợp nến Pin Bar (Kangaroo Tail) từ chối giá quyết liệt tại Vùng Cung Cầu với sự xác nhận bất thường của Khối lượng VSA.",
        "read_time": "16 Phút Đọc",
        "views": "2,740 Lượt Xem",
        "date": "13/09/2026",
        "image": "../assets/images/naked_vsa_trading_setups.svg",
        "image_caption": "Hình 13.1: Chi tiết Setup 1 - Bắn tỉa đảo chiều tại Vùng Cung Cầu với tỷ lệ R:R tối thiểu 1:3.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-12-bay-thanh-khoan-liquidity-hunt-va-stop-hunt",
        "prev_title": "Bài 12: Bẫy Thanh Khoản & Stop Hunt",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-14-setup-2-thuan-xu-huong-pullback-flip-zone",
        "next_title": "Bài 14: Setup 2 - Thuận Xu Hướng Pullback Flip Zone",
        "takeaways": [
            ("Điều Kiện 1 - Vị Trí Chiến Lược:", "Giá phải chạm vào Vùng Cung (Supply) hoặc Vùng Cầu (Demand) quan trọng trên khung thời gian H4 hoặc Daily."),
            ("Điều Kiện 2 - Tín Hiệu Nến:", "Xuất hiện cây nến Pin Bar từ chối giá (Kangaroo Tail) hoặc cụm Engulfing đảo chiều rõ nét."),
            ("Điều Kiện 3 - Xác Nhận VSA:", "Volume tại nến đảo chiều phải cao đột biến (Stopping Volume) chứng minh có dòng tiền tổ chức tham chiến."),
            ("Kế Hoạch Khớp Lệnh:", "Entry: Dưới đáy nến Pin Bar; Stop Loss: Phía trên đỉnh râu nến + 2 pips; Take Profit: Vùng Cầu đối diện với R:R &ge; 1:3.")
        ],
        "quote": "Bắn tỉa không phải là bắn liên tục. Bắn tỉa là nằm im hàng giờ trong bụi rậm, chờ mục tiêu đi đúng vào hồng tâm và chỉ siết cò một phát duy nhất.",
        "quote_author": "PTvolume Sniper Desk",
        "html_content": """
            <h2><i class="fa-solid fa-crosshairs"></i> 1. Quy Trình 4 Bước Triển Khai Setup 1</h2>
            <div class="step-card">
                <h4>Bước 1: Lọc Bối Cảnh Trên Khung Lớn (H4 / Daily)</h4>
                <p>Xác định xem giá có đang nằm ở vùng cực trị không: Kháng cự tuần, Vùng Cung chưa được kiểm định (Fresh Supply Zone) hoặc Đỉnh chu kỳ phân phối.</p>
            </div>
            <div class="step-card">
                <h4>Bước 2: Chờ Đợi Nến Từ Chối Giá Xuất Hiện</h4>
                <p>Khi giá đâm vào Key Zone, không được vội vàng Limit Sell ngay. Hãy chờ nến H1 hoặc M15 đóng cửa tạo thành cây nến Pin Bar có râu nhô hẳn ra ngoài cản.</p>
            </div>
            <div class="step-card">
                <h4>Bước 3: Kiểm Tra Cột Khối Lượng VSA</h4>
                <p>Khối lượng của cây nến từ chối giá phải cao vượt trội so với mức trung bình 20 kỳ. Điều này chứng minh phe Bán đã ra tay thực chất.</p>
            </div>
            <div class="step-card">
                <h4>Bước 4: Đặt Lệnh Bắn Tỉa (Execution)</h4>
                <p>Đặt lệnh Sell Stop cách đáy nến Pin Bar 1 pip. Đặt Stop Loss cách đỉnh râu nến 2 pips. Đo lường khoảng cách SL, nếu khoảng cách tới Vùng Cầu tiếp theo đạt tỷ lệ R:R &ge; 1:3 thì kích hoạt lệnh.</p>
            </div>
        """,
        "comments": [
            ("Tuấn Hưng", "13/09/2026 20:00:00", "Setup 1 này đánh trên khung H1 Vàng cực kỳ thơm! Cứ đúng 4 bước là vào lệnh, tâm lý vững như bàn thạch."),
            ("Minh Trang", "13/09/2026 20:40:15", "Quy tắc R:R &ge; 1:3 loại bỏ được rất nhiều lệnh rác. Cảm ơn admin!"),
            ("Văn Nam", "13/09/2026 21:15:00", "Hình minh họa các setup rất trực quan và dễ áp dụng.")
        ]
    },

    # BÀI 14
    {
        "id": "14",
        "slug": "khoa-hoc-vsa-wyckoff-bai-14-setup-2-thuan-xu-huong-pullback-flip-zone",
        "title": "Bài 14: Setup 2 &ndash; Thuận Xu Hướng Sau Cú Test Cạn Kiệt (Pullback to Flip Zone)",
        "badge": "Học Phần 4 • Hệ Thống Setup Thực Chiến • Bài 14",
        "desc": "Chiến lược giao dịch bám đuôi xu hướng có độ an toàn cao nhất: Chờ nhịp hồi quy về Vùng Chuyển Đổi (Flip Zone) kết hợp nến No Supply/No Demand để vào lệnh.",
        "read_time": "15 Phút Đọc",
        "views": "2,350 Lượt Xem",
        "date": "13/09/2026",
        "image": "../assets/images/candlesticks/marubozu_candle.jpg",
        "image_caption": "Hình 14.1: Điểm vào lệnh thuận xu hướng khi giá hồi về Flip Zone kiểm định cạn cung.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-13-setup-1-ban-tia-dao-chieu-cung-cau-vsa",
        "prev_title": "Bài 13: Setup 1 - Bắn Tỉa Đảo Chiều Cung Cầu",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-15-setup-3-bat-diem-but-pha-vung-nen-build-up",
        "next_title": "Bài 15: Setup 3 - Bắt Điểm Bứt Phá Vùng Nén",
        "takeaways": [
            ("Bản Chất Của Setup 2:", "Xu hướng là bạn (Trend is your friend). Tuyệt đối không chống lại xu hướng chính của khung lớn."),
            ("Flip Zone Là Trạm Thu Phí:", "Kháng cự cũ bị phá vỡ biến thành hỗ trợ mới. Giá luôn có xu hướng quay lại kiểm định trạm thu phí này."),
            ("Tín Hiệu No Supply / No Demand:", "Nhịp hồi về Flip Zone phải có khối lượng cạn kiệt (Volume teo tóp), chứng minh không có lực bán tháo theo hướng ngược lại."),
            ("Ưu Điểm Vượt Trội:", "Tỷ lệ thắng (Winrate) của Setup này thường đạt trên 60% vì đi thuận dòng tiền lớn.")
        ],
        "quote": "Đừng bao giờ cố gắng chặn đầu một đoàn tàu đang lao dốc, cũng đừng bao giờ nhảy bổ vào một chiếc xe đang chạy với tốc độ tối đa. Hãy đợi nó dừng lại đón khách ở trạm ga (Flip Zone) rồi đàng hoàng bước lên tàu.",
        "quote_author": "Phố Wall Châm Ngôn",
        "html_content": """
            <h2><i class="fa-solid fa-train"></i> 1. Triết Lý Của Setup Bám Theo Xu Hướng</h2>
            <p>
                Nếu Setup 1 là nghệ thuật bắt đỉnh/đáy đảo chiều (đòi hỏi kỹ năng cao), thì <strong>Setup 2 chính là 'cần câu cơm' đều đặn và an toàn nhất</strong> cho mọi trader.
            </p>
            <p>
                Khi một xu hướng tăng mạnh đã được thiết lập (tạo các đỉnh cao hơn HH và đáy cao hơn HL), chúng ta không bao giờ nhảy vào mua đuổi ở đỉnh. Chúng ta kiên nhẫn như một thợ săn ngồi chờ giá hồi quy (Pullback) về vùng kháng cự cũ vừa bị phá vỡ (nay đã hóa thành Hỗ trợ - Flip Zone).
            </p>

            <h2><i class="fa-solid fa-clipboard-check"></i> 2. Tiêu Chí Kích Hoạt Lệnh Mua Chuẩn VSA</h2>
            <ol>
                <li>Giá tạo BOS bứt phá qua đỉnh cũ với Volume lớn.</li>
                <li>Giá thoái lui (Pullback) về Flip Zone với các cây nến nhỏ, chậm rãi và <strong>Khối lượng giảm dần đều</strong>.</li>
                <li>Ngay tại Flip Zone, xuất hiện một thanh nến <strong>No Supply Bar</strong> (nến giảm thân hẹp, Volume siêu thấp dưới SMA 20).</li>
                <li>Thanh nến tiếp theo đóng cửa xanh xác nhận $\rightarrow$ Đặt lệnh <strong>Buy Stop</strong> ngay trên đỉnh nến xác nhận, SL đặt dưới đáy Flip Zone.</li>
            </ol>
        """,
        "comments": [
            ("Thành Trung", "13/09/2026 21:40:00", "Setup 2 này chuẩn sách giáo khoa luôn! Đánh theo sóng hồi Flip Zone cực kỳ an tâm."),
            ("Bích Loan", "13/09/2026 22:10:20", "Nhịp hồi volume cạn kiệt là chìa khóa vàng. Trước đây mình cứ thấy giá hồi là sợ, giờ nhìn volume biết ngay là cơ hội."),
            ("Quốc Việt", "13/09/2026 22:45:00", "Ví dụ về đoàn tàu đón khách ở trạm ga rất hay và ý nghĩa!")
        ]
    },

    # BÀI 15
    {
        "id": "15",
        "slug": "khoa-hoc-vsa-wyckoff-bai-15-setup-3-bat-diem-but-pha-vung-nen-build-up",
        "title": "Bài 15: Setup 3 &ndash; Bắt Điểm Bứt Phá Vùng Nén (Breakout from Build-Up)",
        "badge": "Học Phần 4 • Hệ Thống Setup Thực Chiến • Bài 15",
        "desc": "Bắt trọn con sóng tăng tốc (Momentum Ignition) khi giá phá vỡ vùng tích lũy nén chặt (Build-up) trước ngưỡng cản với mức Stop Loss siêu ngắn.",
        "read_time": "15 Phút Đọc",
        "views": "2,290 Lượt Xem",
        "date": "13/09/2026",
        "image": "../assets/images/candlesticks/engulfing_chart.jpg",
        "image_caption": "Hình 15.1: Cú bứt phá dũng mãnh thoát khỏi vùng nén Build-up kích hoạt chu kỳ tăng tốc.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-14-setup-2-thuan-xu-huong-pullback-flip-zone",
        "prev_title": "Bài 14: Setup 2 - Thuận Xu Hướng Pullback Flip Zone",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-16-structural-stop-loss-cat-lo-theo-cau-truc",
        "next_title": "Bài 16: Structural Stop Loss - Cắt Lỗ Cấu Trúc",
        "takeaways": [
            ("Cơ Chế Nén Giá:", "Các cây nến xếp hàng ngang ép sát cản, biên độ nến co hẹp dần thể hiện sự hấp thụ cung triệt để."),
            ("Volume Trong Vùng Nén:", "Volume cạn kiệt dần trong vùng nén, sau đó bùng nổ vượt trội (Volume Expansion) tại cây nến bứt phá."),
            ("Điểm Vào Lệnh Trước Cú Nổ:", "Đặt lệnh Buy Stop ngay trên đỉnh vùng nén để đón đầu con sóng tăng tốc mà không bị trượt giá."),
            ("Stop Loss Siêu Chặt Chẽ:", "Đặt SL ngay dưới đáy vùng nén (thường chỉ 10 - 15 pips trên Vàng), mở ra tỷ lệ R:R từ 1:4 đến 1:6.")
        ],
        "quote": "Một chiếc lò xo càng bị nén chặt bao nhiêu, khi buông tay nó sẽ bật nhảy xa bấy nhiêu. Vùng nén Build-up chính là chiếc lò xo chứa đựng năng lượng bùng nổ của thị trường.",
        "quote_author": "Bob Volman",
        "html_content": """
            <h2><i class="fa-solid fa-bolt"></i> 1. Vì Sao Setup 3 Mang Lại Tỷ Lệ R:R Cao Nhất?</h2>
            <p>
                Điểm yếu của phần lớn các trader giao dịch bứt phá (Breakout) là họ phải đặt mức Stop Loss rất xa (ở tận đáy của con sóng trước). Điều này làm tỷ lệ Risk:Reward bị bóp nghẹt xuống chỉ còn 1:1 hoặc 1:1.5.
            </p>
            <p>
                <strong>Setup 3 giải quyết triệt để bài toán này bằng Vùng Nén (Build-up):</strong>
            </p>
            <p>
                Vì giá đã nén chặt lại thành một khối bê tông ngay sát cản, toàn bộ năng lượng đã được tích tụ. Nếu cú bứt phá thành công, giá sẽ phóng đi như tên lửa mà không bao giờ quay lại vùng nén đó nữa. Do đó, chúng ta có thể tự tin đặt Stop Loss <strong>ngay phía sau vùng nén nhỏ bé này</strong>, tạo nên một tỷ lệ R:R không tưởng từ 1:4 đến 1:8!
            </p>

            <h2><i class="fa-solid fa-list-check"></i> 2. Check-list Kiểm Tra Trước Khi Bấm Nút</h2>
            <ul>
                <li>Có ít nhất 4 đến 6 cây nến nén sát nhau dưới cản không? $\rightarrow$ Có.</li>
                <li>Volume trong các cây nến nén có giảm dần không? $\rightarrow$ Có.</li>
                <li>Đáy của các cây nến nén có xu hướng nâng cao dần (Higher Lows ép sát cản) không? $\rightarrow$ Có.</li>
                <li>$\rightarrow$ <strong>HÀNH ĐỘNG:</strong> Đặt lệnh Buy Stop trên đỉnh cản, SL dưới đáy vùng nén và chuẩn bị đón nhận con sóng tăng tốc!</li>
            </ul>
        """,
        "comments": [
            ("Khánh Toàn", "13/09/2026 23:10:00", "Setup Build-up này gồng lời phê nhất trong 3 setup. SL siêu ngắn nên đánh lot vừa phải mà ăn đậm đà."),
            ("Ngọc Ánh", "13/09/2026 23:45:10", "Khái niệm chiếc lò xo bị nén rất chính xác. Càng nén chặt bay càng mạnh!"),
            ("Văn Hùng", "14/09/2026 00:20:00", "Trọn bộ 3 setup đã xong, sẵn sàng qua Học phần 5 về Quản trị rủi ro và Tâm lý!")
        ]
    },

    # BÀI 16
    {
        "id": "16",
        "slug": "khoa-hoc-vsa-wyckoff-bai-16-structural-stop-loss-cat-lo-theo-cau-truc",
        "title": "Bài 16: Structural Stop Loss &ndash; Nghệ Thuật Cắt Lỗ Dựa Trên Cấu Trúc Nến &amp; Vùng Thanh Khoản",
        "badge": "Học Phần 5 • Quản Trị Rủi Ro & Tâm Lý • Bài 16",
        "desc": "Tạm biệt thói quen đặt Stop Loss cảm tính theo số pips cố định. Hướng dẫn thiết lập điểm cắt lỗ an toàn tuyệt đối phía sau các bức tường bảo vệ cấu trúc.",
        "read_time": "15 Phút Đọc",
        "views": "2,190 Lượt Xem",
        "date": "14/09/2026",
        "image": "../assets/images/minervini_trading_math_matrix.svg",
        "image_caption": "Hình 16.1: Ma trận toán học giao dịch và nguyên tắc thiết lập Structural Stop Loss bảo vệ vốn gốc.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-15-setup-3-bat-diem-but-pha-vung-nen-build-up",
        "prev_title": "Bài 15: Setup 3 - Bắt Điểm Bứt Phá Vùng Nén",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-17-nghe-thuat-gong-loi-trailing-stop-toi-uu-rr",
        "next_title": "Bài 17: Nghệ Thuật Gồng Lời Trailing Stop",
        "takeaways": [
            ("Sai Lầm Chí Mạng:", "Đặt SL theo số pips cố định (như 20 pips, 30 pips) hoặc theo số tiền đô la chấp nhận mất. Thị trường không quan tâm bạn muốn mất bao nhiêu tiền!"),
            ("Structural Stop Loss:", "Mức cắt lỗ phải được đặt tại nơi mà nếu giá chạm tới, LUẬN ĐIỂM VÀO LỆNH CỦA BẠN CHÍNH THỨC BỊ CHỨNG MINH LÀ SAI."),
            ("Bức Tường Bảo Vệ:", "Đặt SL phía sau đỉnh/đáy của nến Pin Bar thể chế, hoặc phía sau vùng Flip Zone đã được quét sạch thanh khoản."),
            ("Khoảng Đệm Hơi Thở (Buffer):", "Luôn cộng thêm 2-3 pips (hoặc spread của sàn) vào ngoài mức cản để tránh bị các cú quét nến liếm trúng SL.")
        ],
        "quote": "Cắt lỗ không phải là thất bại. Cắt lỗ là chi phí kinh doanh bắt buộc để mua lấy cơ hội thắng lớn. Một trader chuyên nghiệp tự hào vì họ cắt lỗ chuẩn xác, không phải vì họ không bao giờ thua.",
        "quote_author": "Mark Douglas (Trading in the Zone)",
        "html_content": """
            <h2><i class="fa-solid fa-shield-halved"></i> 1. Vì Sao 90% Trader Đặt Stop Loss Sai Cách?</h2>
            <p>
                Rất nhiều F0 hỏi: <em>"Em nên đặt SL 20 pips hay 30 pips thì an toàn?"</em>
            </p>
            <p>
                Đây là câu hỏi hoàn toàn sai lầm! Thị trường tài chính không hoạt động theo con số 20 hay 30 pips. Thị trường chỉ nhận biết các <strong>Vùng Cấu Trúc (Structures)</strong> và <strong>Vùng Thanh Khoản (Liquidity Pools)</strong>.
            </p>
            <p>
                Nếu bạn đặt SL 20 pips nhưng mốc đó nằm lơ lửng ngay trước một đáy Swing Low quan trọng, cá mập sẽ quét qua mốc 20 pips của bạn để liếm thanh khoản rồi mới bay lên. Bạn bị mất tiền oan ức dù phân tích đúng hướng!
            </p>

            <h2><i class="fa-solid fa-person-shelter"></i> 2. Ba Vị Trí Đặt Structural Stop Loss Chuẩn Mực</h2>
            <div class="step-card">
                <h4>Vị trí 1: Phía sau Đuôi Chuột Túi (Kangaroo Tail / Pin Bar)</h4>
                <p>Đặt SL cách đỉnh/đáy râu nến Pin Bar từ 2 đến 3 pips. Nếu giá quay lại phá vỡ râu nến này, điều đó chứng minh cú từ chối giá đã thất bại $\rightarrow$ Bạn phải thoát lệnh ngay lập tức.</p>
            </div>
            <div class="step-card">
                <h4>Vị trí 2: Phía sau Vùng Nén Tích Lũy (Build-Up Base)</h4>
                <p>Đặt SL ngay dưới đáy của khối nến nén Build-up. Đây là vùng có chi phí rủi ro thấp nhất.</p>
            </div>
            <div class="step-card">
                <h4>Vị trí 3: Phía sau Đáy Higher Low (HL) Then Chốt</h4>
                <p>Trong lệnh Buy thuận xu hướng, đặt SL dưới đáy HL gần nhất. Khi đáy này bị thủng, cấu trúc xu hướng tăng đã bị phá vỡ (CHoCH), lệnh mua không còn lý do để tồn tại.</p>
            </div>
        """,
        "comments": [
            ("Quang Minh", "14/09/2026 01:00:00", "Khái niệm Structural SL mở mang tầm mắt! Bỏ hẳn thói quen cài 20 pips cố định."),
            ("Thanh Trúc", "14/09/2026 01:30:20", "Khoảng đệm Buffer 2-3 pips cứu mình không biết bao nhiêu bàn thua trông thấy."),
            ("Việt Hùng", "14/09/2026 02:00:00", "Bài học quản trị rủi ro quá giá trị, đáng giá từng câu chữ.")
        ]
    },

    # BÀI 17
    {
        "id": "17",
        "slug": "khoa-hoc-vsa-wyckoff-bai-17-nghe-thuat-gong-loi-trailing-stop-toi-uu-rr",
        "title": "Bài 17: Nghệ Thuật Gồng Lời (Trailing Stop) Theo Swing Points Để Đạt R:R &ge; 1:3",
        "badge": "Học Phần 5 • Quản Trị Rủi Ro & Tâm Lý • Bài 17",
        "desc": "Kỹ thuật dời Stop Loss bám theo cấu trúc đỉnh đáy để ăn trọn con sóng lớn; xóa bỏ nỗi sợ hãi chốt non và tối ưu hóa tỷ lệ lợi nhuận bền vững.",
        "read_time": "15 Phút Đọc",
        "views": "2,240 Lượt Xem",
        "date": "14/09/2026",
        "image": "../assets/images/minervini_progressive_exposure.svg",
        "image_caption": "Hình 17.1: Chiến lược dời Stop Loss bám theo cấu trúc sóng để bảo toàn lợi nhuận và gồng lãi cực đại.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-16-structural-stop-loss-cat-lo-theo-cau-truc",
        "prev_title": "Bài 16: Structural Stop Loss - Cắt Lỗ Cấu Trúc",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-18-toan-hoc-xac-suat-va-quan-tri-vi-the-position-sizing",
        "next_title": "Bài 18: Toán Học Xác Suất & Position Sizing",
        "takeaways": [
            ("Bi Kịch Chốt Non:", "Lỗ thì gồng hàng trăm pips, nhưng vừa lãi được vài pips là tim đập chân run vội vàng chốt non $\rightarrow$ Công thức dẫn đến cháy tài khoản."),
            ("Quy Tắc Trailing Theo Swing Points:", "Chỉ dời Stop Loss lên đáy Higher Low mới khi giá đã tạo đỉnh Higher High mới (BOS)."),
            ("Khóa Hòa Vốn (Break-Even):", "Dời SL về hòa vốn khi giá đã đi được quãng đường bằng 1R rủi ro ban đầu."),
            ("Chốt Lời Từng Phần (Partial TP):", "Chốt 50% vị thế tại mốc R:R 1:2 để an tâm tâm lý, 50% còn lại dùng Trailing Stop để gồng đến tận cùng xu hướng.")
        ],
        "quote": "Kẻ nghiệp dư tập trung vào việc kiếm được bao nhiêu tiền từ mỗi lệnh thắng; người chuyên nghiệp tập trung vào việc họ để cho con sóng chạy xa đến đâu trước khi thị trường đảo chiều.",
        "quote_author": "Jesse Livermore",
        "html_content": """
            <h2><i class="fa-solid fa-arrow-trend-up"></i> 1. Nghịch Lý Tâm Lý: 'Sợ Mất Lãi' Khiến Bạn Mãi Nghèo</h2>
            <p>
                Bộ não con người có xu hướng ghét mất mát (Loss Aversion). Khi thấy tài khoản xanh 50 USD, bạn bắt đầu lo sợ số tiền đó sẽ biến mất nếu giá quay đầu, thế là bạn vội vã bấm nút đóng lệnh. Kết quả: Sau khi bạn vừa chốt non, giá phi một mạch thêm 500 pips!
            </p>
            <p>
                Để trở thành một Pro Trader, bạn phải học cách <strong>để cho lợi nhuận tự sinh sôi (Let your winners run)</strong> bằng phương pháp <em>Trailing Stop theo cấu trúc</em>.
            </p>

            <h2><i class="fa-solid fa-route"></i> 2. Kỹ Thuật Trailing Stop Từng Bước Chuẩn Cấu Trúc</h2>
            <ol>
                <li><strong>Giai đoạn 1 (Khởi động):</strong> Vào lệnh Buy tại Flip Zone với SL đặt dưới đáy sóng. Giữ nguyên lệnh cho đến khi giá đi được biên độ 1:1 R:R.</li>
                <li><strong>Giai đoạn 2 (Bảo vệ vốn):</strong> Khi giá bứt phá tạo BOS đỉnh cũ, lập tức dời SL về điểm vào lệnh (Break-Even) + phí giao dịch. Lúc này bạn đã có một "Lệnh giao dịch miễn phí rủi ro" (Risk-Free Trade).</li>
                <li><strong>Giai đoạn 3 (Bám đuôi Swing Low):</strong> Khi giá hồi lại tạo đáy Higher Low (HL) mới rồi bật tăng tiếp, dời SL từ hòa vốn lên đặt ngay dưới đáy HL mới này.</li>
                <li><strong>Giai đoạn 4 (Chốt hạ):</strong> Lặp lại quy trình cho đến khi giá chính thức gãy cấu trúc (CHoCH) liếm vào SL của bạn. Bạn rời khỏi cuộc chơi với một khoản lợi nhuận khổng lồ đạt tỷ lệ R:R 1:4 hoặc 1:6!</li>
            </ol>
        """,
        "comments": [
            ("Trường Giang", "14/09/2026 02:40:00", "Phương pháp Trailing theo Swing Low giúp mình ăn trọn con sóng vàng 70 giá tuần trước. Quá vi diệu!"),
            ("Hải Yến", "14/09/2026 03:15:10", "Chốt 50% ở 1:2 rồi gồng 50% còn lại giải tỏa tâm lý cực kỳ tốt."),
            ("Đăng Khoa", "14/09/2026 03:50:00", "Học được cách để lợi nhuận tự chạy là bước ngoặt của cuộc đời trading.")
        ]
    },

    # BÀI 18
    {
        "id": "18",
        "slug": "khoa-hoc-vsa-wyckoff-bai-18-toan-hoc-xac-suat-va-quan-tri-vi-the-position-sizing",
        "title": "Bài 18: Toán Học Xác Suất &ndash; Vì Sao Thắng 40% Vẫn Kiếm Lợi Nhuận Khủng?",
        "badge": "Học Phần 5 • Quản Trị Rủi Ro & Tâm Lý • Bài 18",
        "desc": "Bóc trần ảo tưởng về tỷ lệ thắng (Winrate). Khám phá công thức tính quy mô vị thế (Position Sizing) chuẩn xác và bí mật Kỳ vọng toán học dương (Positive Expectancy).",
        "read_time": "16 Phút Đọc",
        "views": "2,410 Lượt Xem",
        "date": "14/09/2026",
        "image": "../assets/images/minervini_trading_math_matrix.svg",
        "image_caption": "Hình 18.1: Bảng ma trận toán học tỷ lệ thắng Winrate vs Tỷ lệ Risk:Reward (R:R).",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-17-nghe-thuat-gong-loi-trailing-stop-toi-uu-rr",
        "prev_title": "Bài 17: Nghệ Thuật Gồng Lời Trailing Stop",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-19-tam-ly-trading-in-the-zone-cai-nghien-fomo",
        "next_title": "Bài 19: Tâm Lý Trading In The Zone",
        "takeaways": [
            ("Ảo Tưởng Tỷ Lệ Thắng (Winrate):", "Hệ thống thắng 90% vẫn có thể cháy tài khoản nếu 1 lần thua mất sạch (R:R âm). Hệ thống thắng 40% vẫn làm giàu bền vững nếu R:R đạt 1:3."),
            ("Kỳ Vọng Toán Học (Expectancy):", "Công thức sinh tử: E = (Winrate x Win Size) - (Lossrate x Loss Size). Nếu E > 0, bạn là một cỗ máy in tiền hợp pháp."),
            ("Quy Tắc 1% - 2% Vốn:", "Tuyệt đối không bao giờ mạo hiểm quá 1% đến 2% tổng tài khoản cho một lệnh giao dịch duy nhất."),
            ("Công Thức Position Sizing:", "Khối lượng Lot = (Số tiền chấp nhận rủi ro) / (Khoảng cách Stop Loss x Giá trị 1 pip).")
        ],
        "quote": "Trong giao dịch tài chính, việc bạn đúng hay sai không quan trọng bằng việc: Khi bạn đúng bạn kiếm được bao nhiêu tiền, và khi bạn sai bạn mất bao nhiêu tiền.",
        "quote_author": "George Soros",
        "html_content": """
            <h2><i class="fa-solid fa-square-root-variable"></i> 1. Bài Toán Kỳ Diệu Của Tỷ Lệ R:R 1:3</h2>
            <p>
                Hãy làm một phép tính thực tế trên chuỗi <strong>100 lệnh giao dịch</strong> với tỷ lệ thắng chỉ vẻn vẹn <strong>40%</strong> (tức là bạn đoán sai tới 60 lần!):
            </p>
            <ul>
                <li>Bạn mạo hiểm <strong>100 USD (1R)</strong> cho mỗi lệnh thua.</li>
                <li>Với mỗi lệnh thắng, bạn kiên quyết kiếm <strong>300 USD (3R)</strong>.</li>
            </ul>
            <p>
                <strong>Kết quả chung cuộc sau 100 lệnh:</strong>
            </p>
            <ul>
                <li>Tổng 60 lệnh thua: $60 \\times (-100\\text{ USD}) = -6.000\\text{ USD}$.</li>
                <li>Tổng 40 lệnh thắng: $40 \\times (+300\\text{ USD}) = +12.000\\text{ USD}$.</li>
                <li><strong>Lợi nhuận ròng thực nhận:</strong> $+12.000 - 6.000 = \\mathbf{+6.000\\text{ USD}}$!</li>
            </ul>
            <p>
                Bạn thấy không? <strong>Bạn sai nhiều hơn đúng</strong> (thua 60 trận, chỉ thắng 40 trận), nhưng tài khoản của bạn vẫn bỏ túi 6.000 USD tiền lời! Đó chính là sức mạnh tối thượng của Toán học giao dịch trong trường phái Naked Chart &amp; VSA.
            </p>

            <h2><i class="fa-solid fa-calculator"></i> 2. Công Thức Tính Quy Mô Lô Vị Thế (Position Sizing)</h2>
            <p>
                Đừng bao giờ vào lệnh với số lot cố định (như lệnh nào cũng phang 0.5 lot hay 1 lot). Mỗi lệnh có khoảng cách Stop Loss cấu trúc khác nhau, do đó số lot phải thay đổi linh hoạt:
            </p>
            <div class="highlight-box">
                <h3>Công Thức Tính Lot Chuẩn Quốc Tế:</h3>
                <p style="font-family:var(--font-mono); font-size:1.1rem; color:#00E5FF; text-align:center; margin:16px 0;">
                    Số Lot = (Vốn x % Rủi ro) / (Khoảng cách SL theo Pips x Giá trị 1 Pip)
                </p>
                <p>Ví dụ: Tài khoản 10.000 USD, rủi ro 1% = 100 USD. Khoảng cách SL là 25 pips trên Vàng ($1 pip = 10 USD/lot). Số lot = 100 / (25 x 10) = <strong>0.4 lot</strong>.</p>
            </div>
        """,
        "comments": [
            ("Tuấn Kiệt", "14/09/2026 04:20:00", "Bài toán 100 lệnh mở mắt cho mình hoàn toàn! Trước cứ đi tìm chén thánh winrate 90% mà tài khoản vẫn âm."),
            ("Lan Hương", "14/09/2026 05:00:10", "Công thức tính lot chuẩn này giúp mình kiểm soát Drawdown cực kỳ mượt mà."),
            ("Minh Trí", "14/09/2026 05:45:00", "George Soros nói câu nào là thấm câu đó. Đỉnh cao của quản trị rủi ro!")
        ]
    },

    # BÀI 19
    {
        "id": "19",
        "slug": "khoa-hoc-vsa-wyckoff-bai-19-tam-ly-trading-in-the-zone-cai-nghien-fomo",
        "title": "Bài 19: Tâm Lý 'Trading In The Zone' &ndash; Cai Nghiện FOMO &amp; Chấp Nhận Rủi Ro Xác Suất",
        "badge": "Học Phần 5 • Quản Trị Rủi Ro & Tâm Lý • Bài 19",
        "desc": "Làm chủ tâm lý giao dịch theo trường phái Mark Douglas: Rèn luyện tính kiên nhẫn như báo hoa mai săn mồi, loại bỏ cảm xúc sợ hãi, tham lam và cay cú trả thù thị trường.",
        "read_time": "15 Phút Đọc",
        "views": "2,380 Lượt Xem",
        "date": "14/09/2026",
        "image": "../assets/images/psychology_diagram.jpg",
        "image_caption": "Hình 19.1: Vòng tròn tâm lý giao dịch và trạng thái tâm trí vô vi (Trading in the Zone).",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-18-toan-hoc-xac-suat-va-quan-tri-vi-the-position-sizing",
        "prev_title": "Bài 18: Toán Học Xác Suất & Position Sizing",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-20-mindmap-toan-thu-va-10-case-study-thuc-te",
        "next_title": "Bài 20: Mindmap Toàn Thư & 10 Case Study",
        "takeaways": [
            ("Bản Chất Của Xác Suất:", "Bất kỳ lệnh nào bạn vào cũng có thể thua, bất kể setup đẹp đến đâu. Hãy chấp nhận rủi ro 100% trước khi bấm nút."),
            ("Cai Nghiện FOMO (Sợ Bỏ Lỡ):", "Thị trường tài chính mở cửa mỗi ngày và cơ hội là vô tận. Bỏ lỡ một con sóng không làm bạn nghèo đi, nhưng nhảy vào đu đỉnh sẽ làm bạn cháy tài khoản."),
            ("Tâm Lý Báo Hoa Mai:", "Báo hoa mai chỉ săn những con mồi yếu nhất và ở cự ly gần nhất. Trader giỏi chỉ ra đòn khi Setup chuẩn mực xuất hiện."),
            ("Không Trả Thù Thị Trường (Revenge Trading):", "Sau một lệnh thua, hãy đứng dậy rời khỏi màn hình 30 phút để thiết lập lại trạng thái tâm trí cân bằng.")
        ],
        "quote": "Những nhà giao dịch vĩ đại nhất không cố gắng dự đoán thị trường sẽ làm gì tiếp theo; họ học cách chấp nhận rằng bất cứ điều gì cũng có thể xảy ra, và họ có một kế hoạch hành động dứt khoát cho mọi kịch bản.",
        "quote_author": "Mark Douglas (Trading in the Zone)",
        "html_content": """
            <h2><i class="fa-solid fa-brain"></i> 1. 5 Sự Thật Cơ Bản Về Thị Trường Của Mark Douglas</h2>
            <p>
                Trong cuốn sách kinh điển <em>Trading in the Zone</em>, Mark Douglas đã đúc kết 5 chân lý bất biến:
            </p>
            <ol>
                <li>Bất cứ điều gì cũng có thể xảy ra trên thị trường.</li>
                <li>Bạn không cần phải biết điều gì sẽ xảy ra tiếp theo để có thể kiếm được tiền.</li>
                <li>Có sự phân bổ ngẫu nhiên giữa các lệnh thắng và lệnh thua cho bất kỳ tập hợp quy tắc nào.</li>
                <li>Một lợi thế cạnh tranh (Edge) chỉ đơn giản là một chỉ dấu cho thấy khả năng điều này xảy ra cao hơn điều khác.</li>
                <li>Mỗi khoảnh khắc trên thị trường là hoàn toàn độc nhất vô nhị.</li>
            </ol>

            <h2><i class="fa-solid fa-peace"></i> 2. Nghệ Thuật Ngồi Im (The Art of Sitting Tight)</h2>
            <p>
                Huyền thoại Jesse Livermore từng khẳng định: <em>"Tiền bạc không được tạo ra từ việc bạn bấm nút mua bán liên tục mỗi ngày, mà tiền bạc được tạo ra trong sự kiên nhẫn ngồi im chờ đợi."</em>
            </p>
            <p>
                Khi bạn mở biểu đồ trần lên và không thấy bất kỳ setup hợp lệ nào theo tiêu chuẩn (không có Pin Bar tại Key Zone, không có Build-up, không có tín hiệu cạn kiệt VSA) $\rightarrow$ <strong>HÀNH ĐỘNG THÔNG MINH NHẤT LÀ KHÔNG LÀM GÌ CẢ!</strong>
            </p>
            <p>
                Giữ được tiền và bảo toàn sức mua cũng chính là một chiến thắng vĩ đại trên thị trường tài chính khốc liệt này.
            </p>
        """,
        "comments": [
            ("Minh Châu", "14/09/2026 06:15:00", "Trading in the Zone là cuốn sách gối đầu giường của mình. Bài tóm lược rất súc tích và đánh trúng tim đen."),
            ("Quốc Tuấn", "14/09/2026 06:45:20", "Bài học về Báo hoa mai săn mồi quá thấm! Ngồi im kiên nhẫn chính là cảnh giới cao nhất."),
            ("Bảo Ngọc", "14/09/2026 07:15:00", "Rời khỏi màn hình sau lệnh thua là bí quyết giúp mình không bao giờ bị cháy tài khoản nữa.")
        ]
    },

    # BÀI 20
    {
        "id": "20",
        "slug": "khoa-hoc-vsa-wyckoff-bai-20-mindmap-toan-thu-va-10-case-study-thuc-te",
        "title": "Bài 20: Bản Đồ Tư Duy (Mindmap) Toàn Thư Naked Chart &amp; VSA Wyckoff + 10 Case Study Thực Tế",
        "badge": "Học Phần 5 • Tổng Kết & Thực Hành • Bài 20",
        "desc": "Đúc kết trọn vẹn 20 bài học thành 1 bản đồ tư duy Mindmap trực quan. Bộ 10 bài tập tình huống (Case Studies) thực chiến trên Vàng, Dầu, Ngô và Forex.",
        "read_time": "20 Phút Đọc",
        "views": "3,450 Lượt Xem",
        "date": "14/09/2026",
        "image": "../assets/images/dao_warren_buffett_framework.svg",
        "image_caption": "Hình 20.1: Bản đồ tư duy toàn thư - Hệ thống giao dịch Naked Chart, VSA & Wyckoff Mastery.",
        "prev_slug": "khoa-hoc-vsa-wyckoff-bai-19-tam-ly-trading-in-the-zone-cai-nghien-fomo",
        "prev_title": "Bài 19: Tâm Lý Trading In The Zone",
        "next_slug": "khoa-hoc-vsa-wyckoff-bai-1-bieu-do-tran-the-naked-chart-phan-1",
        "next_title": "Về Lại Bài 1 (Phần 1): Khởi Đầu Khóa Học",
        "takeaways": [
            ("Tổng Kết Hệ Thống:", "Toàn bộ 20 bài học được kết nối thành một dòng chảy liên tục: Từ bỏ chỉ báo $\rightarrow$ Đọc cấu trúc $\rightarrow$ Giải mã VSA $\rightarrow$ Nhận diện chu kỳ Wyckoff $\rightarrow$ Bắn tỉa Setup $\rightarrow$ Quản trị rủi ro."),
            ("10 Case Study Thực Chiến:", "Phân tích chi tiết từng thanh nến và cột volume trên các thương vụ kinh điển của Vàng (XAU/USD), Dầu WTI, Hàng hóa CBOT và Ngoại hối."),
            ("Bộ Quy Tắc 10 Điểm Bất Di Bất Dịch:", "Check-list 10 điều bắt buộc phải tích đủ trước khi bấm nút vào bất kỳ lệnh giao dịch nào."),
            ("Tự Do Tài Chính Đích Thực:", "Trở thành một nhà giao dịch độc lập, tự tin nhìn thấu bản chất thị trường mà không cần phụ thuộc vào bất kỳ hội nhóm hay 'chuyên gia' phím lệnh nào.")
        ],
        "quote": "Đỉnh cao của sự phức tạp chính là sự giản đơn. Khi bạn đã thấu suốt toàn bộ cấu trúc thị trường, nến và khối lượng, biểu đồ của bạn sẽ trở lại trong veo và tâm trí bạn sẽ hoàn toàn tĩnh lặng.",
        "quote_author": "PTvolume Master Academy",
        "html_content": """
            <h2><i class="fa-solid fa-map"></i> 1. Bản Đồ Tư Duy Hệ Thống Naked Chart &amp; VSA Wyckoff</h2>
            <p>
                Xin chúc mừng bạn đã hoàn thành trọn vẹn <strong>20 bài học tinh hoa</strong> của khóa học. Toàn bộ hệ thống giờ đây được tóm lược trong 4 trụ cột cốt lõi:
            </p>
            <div class="step-card">
                <h4>Trụ Cột 1: Không Gian Làm Việc Trong Veo (The Canvas)</h4>
                <p>Loại bỏ 100% chỉ báo trễ. Chỉ giữ lại Nến Nhật nguyên bản (OHLC) và Khối lượng giao dịch (Volume).</p>
            </div>
            <div class="step-card">
                <h4>Trụ Cột 2: Bản Đồ Cấu Trúc Đa Khung (Market Structure)</h4>
                <p>Khung Daily/H4 xác định xu hướng lớn và Key Zones; nhận diện BOS tiếp diễn và CHoCH đảo chiều; tìm kiếm Flip Zone đón đầu.</p>
            </div>
            <div class="step-card">
                <h4>Trụ Cột 3: Giải Mã Dòng Tiền Lớn (VSA & Wyckoff)</h4>
                <p>Quy luật Nỗ lực vs Kết quả; đọc vị No Demand, No Supply, Stopping Volume; bắt cú rũ bỏ Spring (Pha C) và tránh bẫy mua đỉnh UTAD.</p>
            </div>
            <div class="step-card">
                <h4>Trụ Cột 4: Bắn Tỉa Thực Thi & Quản Trị Rủi Ro (Execution & Math)</h4>
                <p>Áp dụng 3 Setup chuẩn mực; Structural Stop Loss chặt chẽ; Trailing Stop theo Swing Points; tỷ lệ R:R tối thiểu 1:3; rủi ro tối đa 1-2% vốn.</p>
            </div>

            <h2><i class="fa-solid fa-graduation-cap"></i> 2. Check-list 10 Bước Bất Di Bất Dịch Trước Khi Vào Lệnh</h2>
            <ol>
                <li>Khung lớn (H4/Daily) đang có xu hướng Tăng, Giảm hay Tích lũy?</li>
                <li>Giá hiện tại có đang nằm tại Vùng Cung/Cầu then chốt hoặc Flip Zone không?</li>
                <li>Có tín hiệu nến từ chối giá (Pin Bar / Engulfing) hoặc vùng nén Build-up không?</li>
                <li>Khối lượng VSA có xác nhận bất thường hoặc cạn kiệt không?</li>
                <li>Đã diễn ra cú quét bẫy thanh khoản (Liquidity Hunt / Spring / UTAD) chưa?</li>
                <li>Điểm Stop Loss cấu trúc nằm ở đâu? Có an toàn phía sau bức tường bảo vệ không?</li>
                <li>Khoảng cách tới mục tiêu chốt lời (TP) có đạt tỷ lệ Risk:Reward &ge; 1:3 không?</li>
                <li>Quy mô khối lượng Lot đã được tính toán chuẩn xác theo công thức 1% vốn chưa?</li>
                <li>Tâm lý bản thân có đang hoàn toàn bình tĩnh, không bị FOMO hay cay cú trả thù không?</li>
                <li>Nếu lệnh này bị cắt lỗ, bạn có hoàn toàn vui vẻ chấp nhận xác suất của thị trường không?</li>
            </ol>
        """,
        "comments": [
            ("Tuấn Hưng", "14/09/2026 08:00:00", "Khóa học thực sự quá chất lượng và tâm huyết! Hệ thống hóa từ biểu đồ trần, VSA đến Wyckoff rất logic và bài bản."),
            ("Hồng Nhung", "14/09/2026 08:45:20", "Check-list 10 bước này em đã in ra dán ngay cạnh màn hình máy tính để luôn nhắc nhở bản thân kỷ luật."),
            ("Đức Thịnh", "14/09/2026 09:30:00", "Trọn bộ các bài học quá đồ sộ và chi tiết. Rèn luyện theo đúng kỷ luật và quản trị vốn này thì tự tin hơn rất nhiều khi đối mặt thị trường.")
        ]
    }
]

def main():
    target_dir = r"D:\PHAN DUA CẤM XÓA\AI_Agent_Trading\hoc-tap"
    all_lessons = LESSONS_PART1 + LESSONS_REMAINING
    
    print(f"Bắt đầu khởi tạo {len(all_lessons)} bài học HTML vào thư mục: {target_dir}")
    print("CHÚ Ý: Chỉ tạo file cục bộ, TUYỆT ĐỐI KHÔNG CHẠY GIT PUSH THEO LỆNH CỦA BẠN!")
    
    count = 0
    for lesson in all_lessons:
        file_path = os.path.join(target_dir, f"{lesson['slug']}.html")
        html_code = generate_lesson_html(lesson)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_code)
        count += 1
        print(f"[{count:02d}/20] Đã tạo thành công: {lesson['slug']}.html")
        
    print("=" * 70)
    print(f"HOÀN TẤT! Đã sinh toàn bộ {count} bài học HTML chuẩn Investopedia trong hoc-tap/")
    print("Tất cả bài học đều có giao diện Dark Theme, Song ngữ, Watermark, Bình luận và Liên kết điều hướng.")

if __name__ == "__main__":
    main()
