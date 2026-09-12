# -*- coding: utf-8 -*-
"""
Tự động đổi tên và đánh lại số thứ tự từ Bài 1 đến Bài 21:
- Bài 1 (P1) -> Bài 1
- Bài 1 (P2) -> Bài 2
- Bài 2 -> Bài 3
...
- Bài 20 -> Bài 21
Đồng bộ toàn bộ nội dung, liên kết điều hướng Next/Prev, index.html và sitemap.xml
TUYỆT ĐỐI KHÔNG CHẠY GIT PUSH THEO CHỈ THỊ CỦA BẠN.
"""
import os
import sys
import glob

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from template_engine import generate_lesson_html
from course_data import LESSONS as P1_LESSONS
from generate_all_20_lessons import LESSONS_REMAINING

# Tổng hợp 21 bài học
# Bài 1 cũ (gốc trong P1)
# Bài 1 (Phần 2) -> Bài 2
# Bài 2 cũ -> Bài 3
# ...
# Bài 20 cũ -> Bài 21

LESSON_1_CONTENT = {
    "id": 1,
    "slug": "khoa-hoc-vsa-wyckoff-bai-1-bieu-do-tran-the-naked-chart",
    "title": "Bài 1: BIỂU ĐỒ TRẦN (The Naked Chart) &ndash; Khám Phá Bản Năng Của Giá",
    "badge": "Học Phần 1 • Naked Price Action • Bài 1",
    "desc": "Khóa học Naked Chart, VSA & Wyckoff Bài 1: Giải mã bản chất Biểu đồ trần (The Naked Chart), lột trần bẫy tín hiệu đi chậm của chỉ báo, bóc tách 3 thành phần nến nguyên bản và sự kết hợp hoàn hảo cùng Khối lượng VSA.",
    "read_time": "16 Phút Đọc",
    "views": "2,450 Lượt Xem",
    "date": "12/09/2026",
    "image": "../assets/images/naked_chart_indicator_trap.svg",
    "image_caption": "Hình 1.1: Phân kỳ thực tế giữa Giá nguyên bản (Camera trực tiếp) và Chỉ báo kỹ thuật (Bản tin phát lại đi chậm).",
    "takeaways": [
        ("Bản Chất Của Biểu Đồ Trần (The Naked Chart):", "Dọn sạch mọi chỉ báo kỹ thuật phụ trợ để tập trung 100% vào 2 yếu tố gốc rễ quyết định thị trường: Hành động giá thực tế (Price Action) và Khối lượng giao dịch (Volume)."),
        ("Bẫy Tín Hiệu Đi Chậm Hơn Giá:", "Mọi chỉ báo (MA, RSI, MACD...) đều tính từ dữ liệu quá khứ, giống như nhìn gương chiếu hậu để lái xe. Khi chỉ báo báo Mua thì giá đã ở đỉnh; khi báo Bán thì giá đã ở đáy."),
        ("Bóc Tách 3 Bộ Phận Cốt Lõi Của Nến Trần:", "Thân nến (Spread) đo lường ý chí áp đảo; Râu nến (Wicks) hé lộ sự từ chối giá và các bẫy quét thanh khoản của cá mập; Mức đóng cửa (Close) là phán quyết cuối cùng bên nào thắng thế."),
        ("Sự Kết Hợp Hoàn Hảo Giữa Nến & Khối Lượng VSA:", "Nến là kết quả hiển thị bên ngoài, Khối lượng là nỗ lực thực tế bỏ ra. Thân nến dài kèm khối lượng lớn là đồng thuận; nến ngắn mà khối lượng cực lớn là có bất thường ngầm; giá tăng nhưng khối lượng teo tóp là tăng ảo.")
    ],
    "quote": "Thị trường tài chính không di chuyển vì một đường chỉ báo RSI cắt lên hay cắt xuống. Giá di chuyển duy nhất bởi lực mua và lực bán thực tế của dòng tiền trên thị trường. Muốn thấy sự thật, hãy học cách nhìn thẳng vào nến và khối lượng nguyên bản.",
    "quote_author": "PTvolume Institutional Desk",
    "html_content": """
            <!-- ==================== PHẦN 1 ==================== -->
            <h2><i class="fa-solid fa-triangle-exclamation"></i> 1. Bẫy Tín Hiệu Đi Chậm &ndash; Tại Sao Lạm Dụng Chỉ Báo Lại Dễ Khiến Người Mới Thua Lỗ?</h2>
            <p>
                Trên thị trường tài chính, hầu hết người mới tham gia thường bắt đầu bằng cách cài đặt hàng loạt công cụ chỉ báo kỹ thuật: từ các đường trung bình động (MA), dải băng Bollinger Bands, mây Ichimoku, cho đến RSI, MACD hay Stochastic. Tâm lý chung của người mới là tin rằng: <em>càng gắn nhiều công cụ phân tích hiện đại thì việc dự đoán đường đi của giá sẽ càng chuẩn xác</em>. Màn hình giao dịch nhanh chóng biến thành một "ma trận" xanh đỏ chằng chịt, khiến bản thân cây nến &ndash; thứ quan trọng nhất phản ánh tiền bạc thực tế &ndash; bị che khuất gần như hoàn toàn.
            </p>
            <p>
                Thế nhưng sau một thời gian giao dịch, kết quả quen thuộc của hơn 90% người mới vẫn là: tài khoản hao hụt, tâm lý luôn trong trạng thái hoang mang và mệt mỏi. Nguyên nhân gốc rễ không phải vì thị trường quá khó lường, mà vì người mới đang tự làm khó mình khi đặt trọn niềm tin vào các công cụ vốn dĩ <strong>luôn đi chậm hơn thực tế</strong>.
            </p>

            <div class="step-card">
                <h4><i class="fa-solid fa-video" style="color:var(--accent-cyan);"></i> Camera Trực Tiếp (Live Stream) vs Bản Tin Tóm Tắt Phát Lại</h4>
                <p>
                    Để hiểu vì sao các chỉ báo lại phản bội bạn vào những thời khắc then chốt, hãy hình dung một sự so sánh rất bình dân và thực tế:
                </p>
                <ul>
                    <li><strong>Nến và Cột Khối Lượng là Camera Trực Tiếp (Live Stream):</strong> Từng lệnh Mua và Bán của các quỹ đầu tư lớn lẫn nhà đầu tư cá nhân diễn ra ngay tại giây phút này đều được ghi nhận trực tiếp lên thanh nến và cột khối lượng. Đó là sự thật đang xảy ra ngay trước mắt bạn.</li>
                    <li><strong>Chỉ Báo Kỹ Thuật chỉ là Bản Tin Tóm Tắt Phát Lại:</strong> Mọi đường chỉ báo như MA20, RSI14 hay MACD đều phải đợi các cây nến đóng cửa xong, lấy dữ liệu giá quá khứ của 14 hay 20 cây nến trước rồi mới đưa vào công thức tính toán. Nghĩa là giá thực tế phải chạy xong một quãng đường dài rồi, đường chỉ báo mới từ từ uốn lượn lết theo sau!</li>
                </ul>
                <p>
                    Việc cố gắng dự đoán hướng đi tiếp theo của thị trường bằng một đống chỉ báo đi chậm chẳng khác nào bạn đang <strong>lái một chiếc xe chạy với vận tốc 100 km/h trên đường cao tốc, nhưng lại dán kín kính chắn gió phía trước và chỉ ngoái nhìn gương chiếu hậu xem đoạn đường mình vừa đi qua để quyết định đánh lái</strong>!
                </p>
            </div>

            <p>
                Chính độ trễ tự nhiên này đã tạo ra 3 bi kịch kinh điển mà bất kỳ người mới nào cũng từng nếm trải:
            </p>
            <ol>
                <li><strong>Bẫy Đu Đỉnh và Bán Đúng Đáy:</strong> Khi đường chỉ báo kỹ thuật vừa kịp uốn cong lên và phát tín hiệu "Nên Mua", thì trên thực tế giá đã tăng một đoạn dài kịch trần. Người mới vội vã nhảy vào mua là vừa vặn đu ngay đỉnh. Ngược lại, khi chỉ báo cắt xuống báo "Bán tháo khẩn cấp", thì giá đã rơi chạm đáy và chuẩn bị bật tăng, khiến người mới cắt lỗ đúng ngay đáy!</li>
                <li><strong>Tín Hiệu Đá Nhau Chan Chát (Tê Liệt Tâm Lý):</strong> Cùng một thời điểm, chỉ báo A báo nên Mua, nhưng chỉ báo B lại báo Quá Mua nên Bán; dải Bollinger Bands báo chạm biên trên nhưng MACD lại chưa cho tín hiệu. Trader đứng hình ở giữa, hoang mang không biết bấm nút nào, dẫn đến việc lỡ mất cơ hội đẹp hoặc vào lệnh lung tung theo cảm xúc.</li>
                <li><strong>Mù Tịt Trước Đòn Gài Bẫy Của Cá Mập (Smart Money):</strong> Chỉ báo chỉ là các đường trung bình toán học vô hồn, chúng hoàn toàn không thể nhìn thấy những cây nến giật râu lừa gạt (Liquidity Sweep) hay những đợt âm thầm gom hàng của dòng tiền lớn.</li>
            </ol>

            <!-- HÌNH MINH HỌA MỤC 1 -->
            <div class="watermark-box">
                <img src="../assets/images/naked_chart_indicator_trap.svg" alt="Bẫy Chỉ Báo Kỹ Thuật: Tín Hiệu Đi Chậm Và Gây Rối Mắt">
                <div class="watermark-stamp"><i class="fa-solid fa-shield-halved"></i> PTvolume.com</div>
                <div class="watermark-caption">Hình 1.1: Phân kỳ thực tế giữa Giá nguyên bản (Camera trực tiếp) và Chỉ báo kỹ thuật (Bản tin phát lại đi chậm).</div>
            </div>

            <!-- ==================== PHẦN 2 ==================== -->
            <h2><i class="fa-solid fa-eye"></i> 2. Biểu Đồ Trần (The Naked Chart) Là Gì? Triết Lý Của Các Huyền Thoại Đầu Tư</h2>
            <p>
                <strong>Biểu đồ trần (The Naked Chart)</strong>, đúng như tên gọi mộc mạc của nó, là một biểu đồ giá được <strong>dọn dẹp sạch sẽ 100% mọi chỉ báo kỹ thuật phụ trợ</strong>. Trên không gian làm việc của một Naked Chart Trader thực thụ, bạn chỉ giữ lại duy nhất 3 thành phần cốt lõi:
            </p>
            <div class="step-card">
                <h4><i class="fa-solid fa-chart-column" style="color:var(--bullish);"></i> 3 Thành Phần Duy Nhất Trên Biểu Đồ Trần</h4>
                <ul>
                    <li><strong>Hành Động Giá Nguyên Bản (Raw Price Action):</strong> Thể hiện qua các thanh Nến Nhật (Candlesticks) hoặc Thanh giá (Bar Chart) ghi nhận 4 mốc giá cốt lõi: <em>Mở cửa (Open), Cao nhất (High), Thấp nhất (Low), và Đóng cửa (Close) &ndash; OHLC</em>.</li>
                    <li><strong>Khối Lượng Giao Dịch Thực Tế (Volume):</strong> Cột đo lường số lượng cổ phiếu, hợp đồng hoặc khối lượng tiền thật được trao tay tại mỗi cây nến.</li>
                    <li><strong>Các Vùng Giá Then Chốt (Key Horizontal Zones):</strong> Các mốc Cung &ndash; Cầu (Supply / Demand), Kháng cự &ndash; Hỗ trợ then chốt do chính hành vi giá trong quá khứ kiến tạo.</li>
                </ul>
            </div>

            <p>
                Phương pháp biểu đồ trần không hề mới lạ. Nó chính là cội nguồn của mọi trường phái giao dịch thành công nhất trong lịch sử tài chính:
            </p>
            <ul>
                <li><strong>Jesse Livermore (Đầu thế kỷ 20):</strong> Ông kiếm được 100 triệu USD trong cuộc đại suy thoái 1929 hoàn toàn bằng nghệ thuật <em>Đọc băng giá (Tape Reading)</em> &ndash; chỉ nhìn vào biến động giá từng giây và khối lượng khớp lệnh thực tế trên dải băng giấy.</li>
                <li><strong>Richard D. Wyckoff:</strong> Cha đẻ của phương pháp Wyckoff chỉ sử dụng biểu đồ giá thanh (Bar Chart) và cột khối lượng giao dịch để bóc tách 3 quy luật cung cầu chi phối toàn thị trường.</li>
                <li><strong>Bob Volman &amp; Al Brooks:</strong> Những bậc thầy Price Action hiện đại đã chứng minh rằng một biểu đồ trần sạch sẽ mang lại tỷ lệ Risk:Reward (R:R) và độ nhạy bén vượt xa bất kỳ thuật toán máy tính phức tạp nào.</li>
            </ul>

            <!-- BẢNG SO SÁNH TRỰC QUAN -->
            <div class="data-table-wrapper">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th style="width: 25%;">Tiêu Chí So Sánh</th>
                            <th style="width: 37.5%;">Hệ Thống Phụ Thuộc Chỉ Báo (Indicators)</th>
                            <th style="width: 37.5%;">Hệ Thống Biểu Đồ Trần (Naked Chart &amp; VSA)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Tốc độ dữ liệu</strong></td>
                            <td>Trễ từ 3 &ndash; 10 chu kỳ nến do phải qua công thức toán học trung bình.</td>
                            <td>Thời gian thực (Real-time): Nhận diện hành vi ngay khi nến đang hình thành.</td>
                        </tr>
                        <tr>
                            <td><strong>Góc nhìn thị trường</strong></td>
                            <td>Bị che khuất bởi đường vẽ, nhìn cây mà không thấy rừng.</td>
                            <td>Thông thoáng tuyệt đối, thấy rõ cấu trúc thị trường (Market Structure) Đỉnh &ndash; Đáy.</td>
                        </tr>
                        <tr>
                            <td><strong>Điểm vào lệnh (Entry)</strong></td>
                            <td>Vào lệnh muộn khi xu hướng đã đi được 50% &ndash; 70% quãng đường.</td>
                            <td>Bắn tỉa sát vùng cản (Sniper Entry) ngay tại điểm xuất hiện tín hiệu từ chối giá.</td>
                        </tr>
                        <tr>
                            <td><strong>Tỷ lệ Rủi ro / Lợi nhuận (R:R)</strong></td>
                            <td>Kém (thường chỉ đạt 1:1 hoặc 1:1.5 vì mức Stop Loss phải đặt rất xa).</td>
                            <td>Tối ưu vượt trội (Dễ dàng đạt tỷ lệ R:R từ 1:3 đến 1:5+ với Stop Loss chặt chẽ).</td>
                        </tr>
                        <tr>
                            <td><strong>Khả năng thích ứng</strong></td>
                            <td>Dễ bị gãy hệ thống khi thị trường chuyển trạng thái từ Sideway sang Trend.</td>
                            <td>Vận hành bền bỉ trên mọi chu kỳ, mọi khung thời gian và mọi loại tài sản.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- HÌNH MINH HỌA MỤC 2 -->
            <div class="watermark-box">
                <img src="../assets/images/naked_chart_clean_workspace.svg" alt="Không Gian Biểu Đồ Trần Nguyên Bản Với 3 Yếu Tố Cốt Lõi">
                <div class="watermark-stamp"><i class="fa-solid fa-shield-halved"></i> PTvolume.com</div>
                <div class="watermark-caption">Hình 1.2: Không gian biểu đồ trần nguyên bản (Clean Chart) &ndash; Giữ lại 3 yếu tố cốt lõi: Nến OHLC, Vùng Cung Cầu và Khối lượng VSA.</div>
            </div>

            <!-- ==================== PHẦN 3 ==================== -->
            <h2><i class="fa-solid fa-sliders"></i> 3. Hướng Dẫn Thiết Lập Biểu Đồ Trần Chuẩn Mực Cho Người Mới</h2>
            <p>
                Để bắt đầu luyện tập quan sát thị trường không chỉ báo, bạn cần thiết lập một <strong>môi trường làm việc tối giản và chuẩn mực</strong> (Clean Workspace) trên nền tảng biểu đồ của mình (như TradingView, MT4 hoặc MT5) qua 3 bước đơn giản:
            </p>

            <div class="step-card">
                <h4><i class="fa-solid fa-trash-can" style="color:var(--bearish);"></i> Bước 1: Xóa Bỏ Toàn Bộ Chỉ Báo Phụ Trợ (Remove All Indicators)</h4>
                <p>
                    Nhấp chuột phải vào màn hình đồ thị và chọn <em>"Remove all indicators" (Xóa toàn bộ chỉ báo)</em>. Hãy dũng cảm tắt toàn bộ RSI, MACD, Stoch, Bollinger Bands. Ban đầu bạn có thể cảm thấy hơi "trống trải", nhưng đây là bước dọn dẹp bắt buộc để giải phóng đôi mắt và tâm trí.
                </p>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-palette" style="color:var(--accent-cyan);"></i> Bước 2: Cài Đặt Giao Diện Nền Tối (Dark Theme)</h4>
                <p>
                    Cài đặt màu nền đen chuyên nghiệp (Mã màu khuyến nghị: <code>#0B0E14</code> hoặc <code>#141822</code>). Màu nền tối giúp giảm mỏi mắt khi theo dõi biểu đồ trong các phiên giao dịch kéo dài, đồng thời làm nổi bật độ tương phản của thân nến và các râu nến then chốt. Nến tăng chọn màu Xanh chuẩn (<code>#089981</code>) và nến giảm chọn màu Đỏ (<code>#F23645</code>).
                </p>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-chart-column" style="color:var(--accent-gold);"></i> Bước 3: Giữ Lại Duy Nhất Cột Khối Lượng Giao Dịch (Volume)</h4>
                <p>
                    Chỉ báo duy nhất được phép tồn tại trên biểu đồ nến trần thực chiến là <strong>Khối Lượng Giao Dịch (Volume)</strong> nằm gọn gàng ở 15% - 20% cạnh dưới màn hình. Khối lượng không phải là chỉ báo toán học trễ; Khối lượng là <strong>số lượng giao dịch thực tế</strong> do sàn giao dịch cung cấp trực tiếp.
                </p>
            </div>

            <!-- HÌNH MINH HỌA MỤC 3 -->
            <div class="watermark-box">
                <img src="../assets/images/naked_chart_setup_3_steps.svg" alt="3 Bước Cấu Hình Biểu Đồ Trần Chuẩn TradingView Cho Người Mới">
                <div class="watermark-stamp"><i class="fa-solid fa-shield-halved"></i> PTvolume.com</div>
                <div class="watermark-caption">Hình 1.3: Sơ đồ 3 bước thiết lập không gian biểu đồ trần chuyên nghiệp trên nền tảng TradingView.</div>
            </div>

            <!-- ==================== PHẦN 4 ==================== -->
            <h2><i class="fa-solid fa-shapes"></i> 4. Bóc Tách 3 Thành Phần Cốt Lõi Của Nến Trần (Đọc Vị Hành Động Giá)</h2>
            <p>
                Nhiều người mới nhìn vào cây nến chỉ biết nó là màu Xanh (tăng) hay màu Đỏ (giảm). Nhưng với một nhà giao dịch biểu đồ trần chuyên nghiệp, mỗi cây nến là một chiến trường thu nhỏ phản ánh cuộc chiến giữa phe Mua và phe Bán. Bạn chỉ cần <strong>bóc tách đúng 3 thành phần cốt lõi</strong> sau đây &ndash; ai cũng có thể nắm bắt chỉ trong 30 giây:
            </p>

            <div class="step-card">
                <h4><i class="fa-solid fa-arrows-up-down" style="color:var(--accent-cyan);"></i> 4.1 Thân Nến (Spread) &ndash; Bên Nào Đang Nắm Quyền Kiểm Soát?</h4>
                <p>
                    Thân nến là khoảng cách giữa giá Mở cửa và giá Đóng cửa. Độ dài của thân nến thể hiện biên độ di chuyển thực tế và ý chí của phe đang chiếm ưu thế:
                </p>
                <ul>
                    <li><strong>Thân nến dài vượt trội (Wide Spread):</strong> Thể hiện sự quyết đoán và áp đảo hoàn toàn của một bên. Nến xanh thân dài là phe Mua đang làm chủ thế trận; nến đỏ thân dài là phe Bán đang dốc toàn lực đè bẹp đối phương.</li>
                    <li><strong>Thân nến bé tí (Narrow Spread):</strong> Thể hiện sự do dự, chững lại hoặc cuộc giằng co quyết liệt giữa hai phe mà chưa bên nào chịu nhượng bộ.</li>
                </ul>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-arrow-turn-up" style="color:var(--accent-gold);"></i> 4.2 Râu Nến (Bóng Nến / Wicks) &ndash; Vùng Bị Từ Chối &amp; Bẫy Săn Thanh Khoản</h4>
                <p>
                    Râu nến chính là "vết sẹo" ghi lại hành vi từ chối giá (Price Rejection) trong phiên giao dịch:
                </p>
                <ul>
                    <li><strong>Râu nến trên dài:</strong> Giá từng có lúc rướn lên rất cao, nhưng ngay sau đó bị một lực Bán cực mạnh dội ngược xuống, ép giá phải đóng cửa thấp hơn nhiều so với đỉnh. Đây là dấu hiệu phe Bán đang chặn trên quyết liệt.</li>
                    <li><strong>Râu nến dưới dài:</strong> Giá từng bị phe Bán đạp xuống rất sâu, nhưng lực Cầu mua bắt đáy của phe Mua đã nhảy vào hấp thụ toàn bộ và đẩy bật giá trở lại. Đây là dấu hiệu có lực đỡ ngầm rất mạnh.</li>
                    <li><strong>Cảnh báo bẫy cá mập:</strong> Râu nến dài nhô qua một ngưỡng hỗ trợ hoặc kháng cự thường là cú quét lệnh dừng lỗ (Stop Hunt) do cá mập giăng ra để cướp hàng của người mới trước khi giá chạy thật!</li>
                </ul>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-gavel" style="color:var(--bullish);"></i> 4.3 Mức Giá Đóng Cửa (Close Level) &ndash; Phán Quyết Chung Cuộc Của Phiên</h4>
                <p>
                    Trong suốt phiên, giá có thể nhảy múa, tăng giảm liên tục, nhưng chỉ có <strong>mức giá đóng cửa mới là phán quyết cuối cùng</strong> khẳng định bên nào giành chiến thắng khi tiếng chuông hết giờ vang lên:
                </p>
                <ul>
                    <li><strong>Đóng cửa sát đỉnh cao nhất của nến:</strong> Phe Mua kiểm soát hoàn toàn tới tận giây cuối cùng. Đà tăng có xác suất rất cao sẽ tiếp diễn sang các nến tiếp theo.</li>
                    <li><strong>Đóng cửa sát đáy thấp nhất của nến:</strong> Phe Bán làm chủ tuyệt đối, đà giảm sẽ tiếp tục duy trì.</li>
                    <li><strong>Đóng cửa ở chính giữa cây nến:</strong> Thế trận cân bằng, phiên giao dịch kết thúc với sự lưỡng lự cao độ.</li>
                </ul>
            </div>

            <!-- HÌNH MINH HỌA MỤC 4 -->
            <div class="watermark-box">
                <img src="../assets/images/naked_candlestick_structure.svg" alt="Bóc Tách 3 Thành Phần Cốt Lõi Của Nến Trần">
                <div class="watermark-stamp"><i class="fa-solid fa-shield-halved"></i> PTvolume.com</div>
                <div class="watermark-caption">Hình 1.4: Cấu tạo 3 thành phần cốt lõi của nến trần (Thân nến, Râu nến, Giá đóng cửa) và ý nghĩa chiến lược.</div>
            </div>

            <!-- ==================== PHẦN 5 ==================== -->
            <h2><i class="fa-solid fa-link"></i> 5. Sự Kết Hợp Hoàn Hảo: Nến Trần &amp; Khối Lượng VSA (Quy Luật Nỗ Lực vs Kết Quả)</h2>
            <p>
                Nhiều trường phái Price Action hiện đại khuyên trader "chỉ cần nhìn nến là đủ". Nhưng trong thực chiến chuyên nghiệp, chúng ta luôn khẳng định dứt khoát: <strong>Nến trần nếu thiếu vắng Khối lượng VSA (Volume Spread Analysis) thì mới chỉ là một nửa sự thật!</strong>
            </p>
            <p>
                Giá cả trên biểu đồ là những gì bạn nhìn thấy (What happened), nhưng Khối lượng mới là câu trả lời cho việc <strong>tại sao nó xảy ra và Smart Money đã bỏ ra bao nhiêu nỗ lực tiền bạc để làm điều đó (Why &amp; How much effort)</strong>. Theo Quy luật thứ 3 của Richard Wyckoff &ndash; <em>Quy luật Nỗ Lực và Kết Quả (Law of Effort vs Result)</em>:
            </p>
            <blockquote>
                <strong>Giá (Thân nến) là KẾT QUẢ hiển thị ra bên ngoài &ndash; Khối lượng (Volume) là NỖ LỰC thực tế bỏ ra ở bên dưới.</strong>
            </blockquote>
            <p>
                Hãy tưởng tượng bạn đang lái một chiếc xe ô tô leo dốc:
            </p>
            <ul>
                <li>Nếu bạn đạp ga mạnh (Nỗ lực lớn = Cột Volume to), chiếc xe phải vọt nhanh lên dốc (Kết quả lớn = Thân nến dài). Điều đó hoàn toàn bình thường và hợp lý.</li>
                <li>Nhưng nếu bạn đạp lút chân ga, động cơ gầm rú vang trời (Nỗ lực cực lớn = Volume bùng nổ), mà chiếc xe lại đứng yên hoặc chỉ nhích lên được vài centimet (Kết quả nhỏ = Thân nến ngắn cũn hoặc râu trên dài ngoằng) &ndash; chắc chắn đang có một vật cản khổng lồ chặn trước đầu xe!</li>
            </ul>

            <p>
                Áp dụng nguyên lý này vào biểu đồ, người mới chỉ cần ghi nhớ <strong>3 kịch bản đối chiếu cốt lõi</strong>:
            </p>

            <div class="step-card">
                <h4><i class="fa-solid fa-check-double" style="color:var(--bullish);"></i> Kịch Bản 1: Đồng Thuận Hoàn Hảo (Nỗ Lực Lớn = Kết Quả Lớn)</h4>
                <p>
                    <strong>Dấu hiệu:</strong> Nến tăng thân dài dứt khoát đi kèm cột Volume bùng nổ cao vượt trội so với trung bình các phiên trước.<br>
                    <strong>Bản chất:</strong> Dòng tiền thông minh (Smart Money) thực sự chi tiền mạnh tay để đẩy giá. Cung và Cầu đồng lòng ủng hộ hướng đi này.<br>
                    <strong>Hành động của Trader:</strong> Tự tin giữ lệnh và đi theo hướng của thanh nến (Thuận buồm xuôi gió).
                </p>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-triangle-exclamation" style="color:var(--bearish);"></i> Kịch Bản 2: Bất Thường Cực Độ (Nỗ Lực Khủng Nhưng Kết Quả Nhỏ &ndash; Cảnh Báo Bẫy)</h4>
                <p>
                    <strong>Dấu hiệu:</strong> Nến có thân rất ngắn (hoặc có râu nến dài ngoằng), nhưng cột Khối lượng lại cao đột biến một cách bất thường.<br>
                    <strong>Bản chất:</strong> Phe Mua cố gắng đẩy giá nhưng gặp phải một lượng hàng xả ngầm khổng lồ của phe Bán hấp thụ sạch sành sanh; hoặc ngược lại, phe Bán đạp giá nhưng phe Mua âm thầm kê lệnh hứng hết.<br>
                    <strong>Hành động của Trader:</strong> Cảnh giác cao độ! Đây là dấu hiệu kinh điển báo hiệu giá sắp đảo chiều hoặc cá mập đang phân phối đỉnh / gom hàng đáy. Tuyệt đối không mua đuổi!
                </p>
            </div>

            <div class="step-card">
                <h4><i class="fa-solid fa-ban" style="color:var(--accent-gold);"></i> Kịch Bản 3: Thiếu Hụt Nỗ Lực (Giá Tăng Rướn Nhưng Khối Lượng Tụt Dốc)</h4>
                <p>
                    <strong>Dấu hiệu:</strong> Giá vẫn tiếp tục tăng lên các mốc cao mới, nhưng các cột Khối lượng lại teo tóp và giảm dần qua từng phiên.<br>
                    <strong>Bản chất:</strong> Dòng tiền lớn của các tay to hoàn toàn đứng ngoài cuộc. Đợt tăng này chỉ là do vài nhà đầu tư nhỏ lẻ mua đuổi với nhau trong nghi ngờ.<br>
                    <strong>Hành động của Trader:</strong> Tuyệt đối không FOMO! Cú tăng không có nỗ lực bảo chứng này rất mong manh và có thể sụp đổ bất cứ lúc nào khi gặp một lực bán nhỏ.
                </p>
            </div>

            <!-- HÌNH MINH HỌA MỤC 5 -->
            <div class="watermark-box">
                <img src="../assets/images/naked_vsa_effort_result.svg" alt="Sự Kết Hợp Hoàn Hảo: Nến Trần Và Khối Lượng VSA">
                <div class="watermark-stamp"><i class="fa-solid fa-shield-halved"></i> PTvolume.com</div>
                <div class="watermark-caption">Hình 1.5: 3 Kịch bản đối chiếu giữa Thân nến (Kết quả) và Cột Khối lượng VSA (Nỗ lực) theo phương pháp Wyckoff.</div>
            </div>

            <!-- ==================== PHẦN 6 ==================== -->
            <h2><i class="fa-solid fa-calendar-check"></i> 6. Lộ Trình 7 Ngày Làm Quen &amp; Tự Tin Với Biểu Đồ Nến Trần (Kèm Bài Tập Rèn Luyện)</h2>
            <p>
                Chuyển đổi từ thói quen phụ thuộc vào chỉ báo sang một Naked Chart Trader không thể diễn ra chỉ sau một đêm. Đây là một quá trình <strong>chuyển giao về nhận thức và xây dựng trực giác thị trường</strong>. Hãy áp dụng lộ trình 7 ngày sau đây để từng bước làm chủ biểu đồ nến trần:
            </p>

            <ol>
                <li><strong>Chặng 1 (Ngày 1 &ndash; 3): Tập Quan Sát Thuần Túy (Pure Observation):</strong>
                    <p>Mở đồ thị khung thời gian H4 hoặc Daily của Vàng (XAU/USD), Dầu Thô hoặc Cổ phiếu yêu thích của bạn. Tắt toàn bộ chỉ báo, chỉ để lại nến và Volume. Hãy tập tìm các cây nến có thân dài nhất và nến có râu dài nhất. Tự đặt câu hỏi: <em>Cột khối lượng tại cây nến đó to hay nhỏ? Nỗ lực bỏ ra có tương xứng với độ dài thân nến không?</em></p>
                </li>
                <li><strong>Chặng 2 (Ngày 4 &ndash; 5): Nhận Diện Vùng Bị Từ Chối Giá (Spotting Rejections):</strong>
                    <p>Khoanh tròn tất cả các cây nến Pin Bar có râu dài đâm thấu qua các mức đỉnh hoặc đáy trước đó. Quan sát xem giá đã phản ứng đảo chiều ra sao sau khi các cây nến từ chối giá này xuất hiện.</p>
                </li>
                <li><strong>Chặng 3 (Ngày 6 &ndash; 7): Ghi Chép Nhật Ký Phát Hiện Bất Thường (Logging Anomalies):</strong>
                    <p>Ghi lại ít nhất 3 trường hợp bạn phát hiện sự "Bất thường" giữa Thân nến và Khối lượng (ví dụ: Volume cực lớn nhưng thân nến bé tí). Quan sát xem thị trường sau đó đã diễn biến ra sao để kiểm chứng quy luật Nỗ lực vs Kết quả.</p>
                </li>
            </ol>

            <div class="highlight-box">
                <h3><i class="fa-solid fa-lightbulb"></i> Lời Khuyên Chân Thành Cho Người Mới Bắt Đầu</h3>
                <p>
                    Ban đầu, khi mới gỡ bỏ toàn bộ chỉ báo, bạn có thể sẽ cảm thấy hơi "trống trải" và ngượng tay vì đã quen dựa dẫm vào các tín hiệu cắt nhau có sẵn. Nhưng chỉ sau 1 đến 2 tuần kiên trì quan sát nến và khối lượng nguyên bản, bạn sẽ nhận ra một sự thật giải phóng tâm lý: <strong>bạn bắt đầu nhìn thấy thị trường một cách sáng rõ, không còn bị nhiễu loạn, và điểm vào lệnh sẽ chuẩn xác hơn gấp nhiều lần</strong>.
                </p>
            </div>
    """,
    "comments": [
        ("Minh Triết (Trader 4 năm)", "12/09/2026 10:15:30", "Bài viết phân tích quá chuẩn xác! Dọn sạch biểu đồ chỉ để lại Nến và Volume theo đúng nguyên lý Wyckoff kinh điển giúp tâm lý giao dịch nhẹ nhõm hơn hẳn."),
        ("Vũ Hải Nam (F0 Hàng Hóa)", "12/09/2026 11:22:45", "Phần ví dụ camera trực tiếp và bản tin phát lại dễ hiểu thật sự. Hình minh họa từng mục rõ ràng, trực quan, giúp người mới nắm bài rất nhanh!"),
        ("Đặng Đình Quân (VSA Scalper)", "12/09/2026 12:40:10", "Các sơ đồ SVG sắc nét, chữ to rõ ràng và không bị che khuất. Sự kết hợp giữa nến trần và khối lượng VSA là kim chỉ nam trong sự nghiệp trading của mình.")
    ]
}

# Lấy các bài tiếp theo và đánh lại số thứ tự từ Bài 2 đến Bài 21
raw_lessons = [LESSON_1_CONTENT] + P1_LESSONS + LESSONS_REMAINING
# Chú ý: raw_lessons hiện có:
# 0: Lesson 1 gốc
# 1: Lesson 1b (Cấu trúc thị trường) -> Trở thành Bài 2
# 2: Lesson 2 cũ (Ngôn ngữ nến đơn) -> Trở thành Bài 3
# 3: Lesson 3 cũ (Vùng nén Build-up) -> Trở thành Bài 4
# 4: Lesson 4 cũ (Đa khung) -> Trở thành Bài 5
# 5: Lesson 5 cũ (VSA căn bản) -> Trở thành Bài 6
# ...
# 20: Lesson 20 cũ (Mindmap) -> Trở thành Bài 21

def rebuild_all_21_lessons():
    print(f"Tổng số bài học cần đánh số lại: {len(raw_lessons)}")
    
    updated_lessons = []
    
    for idx, item in enumerate(raw_lessons):
        lesson_num = idx + 1
        
        # Xác định học phần
        if lesson_num <= 5:
            hp_num = 1
            hp_name = "Naked Price Action"
        elif lesson_num <= 9:
            hp_num = 2
            hp_name = "Volume Spread Analysis"
        elif lesson_num <= 13:
            hp_num = 3
            hp_name = "Phương Pháp Wyckoff"
        elif lesson_num <= 16:
            hp_num = 4
            hp_name = "Hệ Thống Setup Thực Chiến"
        else:
            hp_num = 5
            hp_name = "Quản Trị Rủi Ro & Tâm Lý"
            
        badge = f"Học Phần {hp_num} • {hp_name} • Bài {lesson_num}"
        
        # Tách tiêu đề gốc loại bỏ phần "Bài X: " hoặc "Bài 1 (Phần 2): "
        orig_title = item["title"]
        if ":" in orig_title:
            pure_title = orig_title.split(":", 1)[1].strip()
        else:
            pure_title = orig_title
            
        new_title = f"Bài {lesson_num}: {pure_title}"
        
        # Tạo slug mới
        # Lấy phần mô tả slug từ slug cũ
        old_slug = item["slug"]
        # Loại bỏ tiền tố cũ
        parts = old_slug.split("-")
        # Tìm phần sau 'bai-X' hoặc 'phan-X'
        meaningful_parts = []
        skip = True
        for p in parts:
            if p in ["bai", "phan", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "1b"]:
                continue
            if p in ["khoa", "hoc", "vsa", "wyckoff"]:
                continue
            meaningful_parts.append(p)
            
        core_slug = "-".join(meaningful_parts)
        new_slug = f"khoa-hoc-vsa-wyckoff-bai-{lesson_num}-{core_slug}"
        
        updated_lessons.append({
            "num": lesson_num,
            "id": lesson_num,
            "slug": new_slug,
            "title": new_title,
            "badge": badge,
            "desc": item["desc"],
            "read_time": item["read_time"],
            "views": item["views"],
            "date": item["date"],
            "image": item["image"],
            "image_caption": item["image_caption"],
            "takeaways": item["takeaways"],
            "quote": item["quote"],
            "quote_author": item["quote_author"],
            "html_content": item["html_content"],
            "comments": item["comments"]
        })

    # Cập nhật liên kết Next / Prev
    total = len(updated_lessons)
    for i in range(total):
        prev_idx = (i - 1 + total) % total
        next_idx = (i + 1) % total
        updated_lessons[i]["prev_slug"] = updated_lessons[prev_idx]["slug"]
        updated_lessons[i]["prev_title"] = updated_lessons[prev_idx]["title"]
        updated_lessons[i]["next_slug"] = updated_lessons[next_idx]["slug"]
        updated_lessons[i]["next_title"] = updated_lessons[next_idx]["title"]
        
    return updated_lessons

def main():
    target_dir = r"D:\PHAN DUA CẤM XÓA\AI_Agent_Trading\hoc-tap"
    
    # Xóa các file cũ có tiền tố khoa-hoc-vsa-wyckoff- để dọn dẹp sạch sẽ
    old_files = glob.glob(os.path.join(target_dir, "khoa-hoc-vsa-wyckoff-*.html"))
    for f in old_files:
        try:
            os.remove(f)
        except Exception:
            pass
    print(f"Đã dọn dẹp {len(old_files)} file bài học cũ.")

    lessons = rebuild_all_21_lessons()
    
    print(f"Bắt đầu khởi tạo {len(lessons)} bài học mới (Từ Bài 1 đến Bài 21)...")
    for l in lessons:
        html = generate_lesson_html(l)
        fpath = os.path.join(target_dir, f"{l['slug']}.html")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[{l['num']:02d}/21] Đã tạo thành công: {l['slug']}.html -> {l['title']}")

    print("=" * 70)
    print("HOÀN TẤT TẠO 21 BÀI HỌC VỚI SỐ THỨ TỰ MỚI TỪ BÀI 1 ĐẾN BÀI 21!")

if __name__ == "__main__":
    main()
