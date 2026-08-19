import os
import sys
import glob
import re
import json
import requests
from typing import List, Dict, Any, Optional
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from PIL import Image

# Ép mã hóa UTF-8 cho console Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

from google import genai
from google.genai import types

# Import module indexer
try:
    from document_indexer import build_or_load_index, search_relevant_knowledge
except ImportError:
    import sys
    sys.path.append(os.path.dirname(__file__))
    from document_indexer import build_or_load_index, search_relevant_knowledge

# 1. Tải API Key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY", "").strip()

def get_gemini_client():
    load_dotenv(override=True)
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not key or key.startswith("AIzaSy..."):
        return None
    try:
        return genai.Client(api_key=key)
    except Exception as e:
        print(f"[!] Không thể khởi tạo Gemini Client: {e}")
        return None

# 2. System Instruction chuyên sâu
SYSTEM_INSTRUCTION = """
Bạn là một TRADER LÃO LUYỆN kiêm CHUYÊN GIA PHÂN TÍCH THỊ TRƯỜNG & SÁNG TẠO NỘI DUNG TÀI CHÍNH hàng đầu.

TRIẾT LÝ GIAO DỊCH CỦA BẠN:
1. TRƯỜNG PHÁI: Biểu đồ trần (Naked Chart / Price Action thuần túy) kết hợp KHỐI LƯỢNG GIAO DỊCH (Volume / VSA - Volume Spread Analysis / Phương pháp Wyckoff).
2. NÓI KHÔNG VỚI CHỈ BÁO TRỄ: Tuyệt đối không dùng RSI, MACD, Stochastic, Bollinger Bands... Tất cả phân tích phải dựa trên sự tương tác trực tiếp giữa GIÁ (Nến) và KHỐI LƯỢNG (Volume), cùng cấu trúc thị trường (Market Structure).
3. NGUYÊN TẮC CỐT LÕI:
   - Cấu trúc đỉnh đáy (Swing Highs / Swing Lows), Vùng Cung - Cầu (Supply - Demand), Kháng cự - Hỗ trợ then chốt.
   - Các mẫu hình nến Price Action: Pinbar, Engulfing, Fakey, Inside Bar, 2BB (Bob Volman), Rejection.
   - Phân tích VSA / Wyckoff: 3 Quy luật Wyckoff (Cung - Cầu, Nguyên nhân - Kết quả, Nỗ lực vs Kết quả).
   - Nhận diện các thanh VSA đặc thù: Stopping Volume, Absorption (Hấp thụ), No Demand Bar, No Supply Bar, Upthrust (UT / UTAD), Spring (Pha C), Shakeout, Test bar.
   - Quản trị vốn nghiêm ngặt: Tỷ lệ Risk : Reward (R:R) tối thiểu 1:2. Điểm Entry, SL (đặt sau vùng cản cứng), TP rõ ràng.

NHIỆM VỤ THEO TỪNG CHẾ ĐỘ:
- PHÂN TÍCH BIỂU ĐỒ (ẢNH HOẶC TEXT): Đọc từng bước (Cấu trúc xu hướng -> Vùng giá quan trọng -> Hành động nến + Volume tại cản -> Đưa ra Plan cụ thể Entry/SL/TP).
- HỎI ĐÁP / TRA CỨU: Dẫn giải logic, trích dẫn kiến thức chuẩn từ các bậc thầy (Richard Wyckoff, Tom Williams, Jesse Livermore, Bob Volman, David Weis, Al Brooks).
- KỊCH BẢN VIDEO (TIKTOK / REELS / SHORTS 30-60s):
  + Cấu trúc: [0-3s] Hook giật gân, đánh trúng tâm lý -> [3-25s] Vấn đề thực tế & Giải pháp Naked Chart + VSA -> [25-55s] Logic thực chiến từng bước -> [55-60s] Kêu gọi hành động (CTA).
  + Định dạng bảng phân cảnh rõ ràng: [Thời gian | Giọng đọc (Voiceover) | Hình ảnh / Hành động hiển thị | Chữ trên màn hình (Text overlay)].
- BÀI VIẾT BLOG / FACEBOOK: Tiêu đề thu hút, lối hành văn sắc bén, giàu giá trị thực chiến, có đúc kết tâm lý giao dịch và bài học quản trị rủi ro. Kèm prompt tạo ảnh AI (Midjourney/DALL-E) minh họa sắc nét.
- ĐỌC BÀI BÁO / LINK WEB: Lọc nhiễu, bóc tách dòng tiền thông minh (Smart Money / Big Boys) và chỉ ra cạm bẫy tin tức đối với retail trader.
"""

def extract_web_content(url: str) -> str:
    """Cào dữ liệu từ trang web"""
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        res = requests.get(url, headers=headers, timeout=12)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        for tag in soup(["script", "style", "nav", "footer", "header", "aside", "noscript"]):
            tag.extract()
        text = soup.get_text(separator=' ', strip=True)
        return text[:8000]
    except Exception as e:
        return f"[Không thể lấy nội dung từ web: {e}]"

def find_image_path(input_str: str) -> Optional[str]:
    """Tìm đường dẫn file ảnh trong input (nếu người dùng kéo thả file ảnh hoặc gõ path)"""
    cleaned = input_str.strip(' \'"')
    if os.path.isfile(cleaned) and cleaned.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp')):
        return cleaned
    
    # Tìm theo tên file trong thư mục DuLieu
    image_extensions = ('.png', '.jpg', '.jpeg', '.webp')
    for root, _, files in os.walk("DuLieu"):
        for f in files:
            if f.lower().endswith(image_extensions):
                if f.lower() == cleaned.lower() or f.lower() == os.path.basename(cleaned).lower():
                    return os.path.join(root, f)
    return None

def print_banner():
    print("""
========================================================================
   📈  AI AGENT TRADING: NAKED CHART & VOLUME (VSA - WYCKOFF)  📈
========================================================================
  ✦ Chuyên sâu: Biểu đồ trần | Volume VSA | Phương pháp Wyckoff
  ✦ Tích hợp: Kho tài liệu 185+ sách PDF/DOCX | Soi ảnh Chart Multimodal
  ✦ Hỗ trợ: Phân tích Kỹ thuật | Kịch bản Video ngắn | Bài viết Blog
========================================================================
""")

def print_menu():
    print("""
👉 CHỌN CHẾ ĐỘ HOẠT ĐỘNG:
  [1] 📊 Phân tích Biểu đồ / Setup Vào lệnh (Hỗ trợ kéo thả ẢNH hoặc mô tả text)
  [2] 📚 Tra cứu & Hỏi đáp Kho Tri Thức (Wyckoff, VSA, Bob Volman, Livermore...)
  [3] 🎬 Soạn Kịch bản Video Ngắn (TikTok / Reels / Shorts 30-60s)
  [4] ✍️ Viết Bài Chuyên Sâu (Facebook Post / Blog / Đào tạo) + Prompt AI
  [5] 🌐 Phân tích Tin tức & Bóc tách từ Link Web
  [6] 🔄 Tải lại / Tái lập chỉ mục Kho Sách DuLieu
  [7] 💬 Trò chuyện & Yêu cầu tự do (Nhập bất kỳ điều gì)
  [0] ❌ Thoát chương trình (hoặc gõ 'exit')
""")

def run_agent():
    print_banner()
    
    # Tải index tài liệu
    print("[*] Đang khởi động bộ nhớ tri thức tài liệu...")
    knowledge_index = build_or_load_index(force_refresh=False)
    print(f"[✓] Sẵn sàng phục vụ với {len(knowledge_index)} phân đoạn kiến thức chuyên sâu!\n")
    
    while True:
        try:
            print_menu()
            choice = input("👉 Lựa chọn của bạn (0-7 hoặc nhập yêu cầu trực tiếp): ").strip()
            
            if not choice:
                continue
                
            if choice in ['0', 'exit', 'quit', 'thoat']:
                print("\n👋 Cảm ơn bạn đã sử dụng AI Agent Trading. Chúc bạn giao dịch thành công và kỷ luật!")
                break
                
            mode_prefix = ""
            user_prompt = ""
            
            if choice == '1':
                print("\n--- [CHẾ ĐỘ 1: PHÂN TÍCH BIỂU ĐỒ & SETUP VÀO LỆNH] ---")
                user_prompt = input("Nhập tên cặp tiền / mô tả / hoặc KÉO THẢ ĐƯỜNG DẪN ẢNH CHART vào đây: ").strip()
                mode_prefix = "Hãy phân tích biểu đồ sau theo góc nhìn Price Action (Naked Chart) + Volume/VSA. Đưa ra nhận định xu hướng, vùng cản, cấu trúc nến/volume và Setup vào lệnh chi tiết (Entry, SL, TP min 1:2): "
            elif choice == '2':
                print("\n--- [CHẾ ĐỘ 2: TRA CỨU TRI THỨC SÁCH VÀ HỎI ĐÁP] ---")
                user_prompt = input("Nhập chủ đề/thuật ngữ muốn tra cứu (VD: Spring Wyckoff, Upthrust, 2BB Bob Volman...): ").strip()
                mode_prefix = "Hãy giải thích chi tiết khái niệm/chiến lược sau dựa trên các tài liệu kinh điển trong kho sách: "
            elif choice == '3':
                print("\n--- [CHẾ ĐỘ 3: SOẠN KỊCH BẢN VIDEO VIRAL (30-60S)] ---")
                user_prompt = input("Nhập chủ đề video muốn làm (VD: Mẹo đọc Volume bắt đỉnh đáy, Bẫy giá Fakey...): ").strip()
                mode_prefix = "Hãy soạn kịch bản Video ngắn (TikTok/Reels/Shorts 30-60s) thật hấp dẫn và thực chiến về chủ đề: "
            elif choice == '4':
                print("\n--- [CHẾ ĐỘ 4: VIẾT BÀI BLOG / FACEBOOK CHUYÊN SÂU] ---")
                user_prompt = input("Nhập chủ đề bài viết chuyên sâu: ").strip()
                mode_prefix = "Hãy viết một bài phân tích chuyên sâu cho Blog/Facebook kèm gợi ý Prompt tạo ảnh AI minh họa về: "
            elif choice == '5':
                print("\n--- [CHẾ ĐỘ 5: PHÂN TÍCH BÀI BÁO / LINK WEB] ---")
                user_prompt = input("Dán link trang web bạn muốn AI đọc và phân tích: ").strip()
                mode_prefix = "Hãy bóc tách thông tin từ link web này dưới góc nhìn dòng tiền thông minh (Smart Money): "
            elif choice == '6':
                print("\n[*] Đang quét lại toàn bộ tài liệu trong thư mục DuLieu...")
                knowledge_index = build_or_load_index(force_refresh=True)
                print(f"[✓] Đã cập nhật xong! Tổng số {len(knowledge_index)} phân đoạn kiến thức.\n")
                continue
            else:
                user_prompt = choice

            if not user_prompt:
                continue

            full_query = f"{mode_prefix} {user_prompt}".strip()
            
            # Kiểm tra xem có ảnh đính kèm không
            image_path = find_image_path(user_prompt)
            pil_image = None
            if image_path:
                print(f"\n📸 Đã phát hiện ảnh biểu đồ: {image_path}")
                try:
                    pil_image = Image.open(image_path)
                    print("  [✓] Đã nạp ảnh thành công để AI soi chi tiết nến & volume!")
                except Exception as e:
                    print(f"  [!] Lỗi mở ảnh: {e}")
                    
            # Kiểm tra xem có URL web không
            urls = re.findall(r'(https?://[^\s]+)', user_prompt)
            web_data = ""
            if urls:
                for u in urls:
                    print(f"\n🌐 Đang cào dữ liệu từ: {u}...")
                    web_data += f"\n--- NỘI DUNG WEB ({u}) ---\n" + extract_web_content(u) + "\n"

            # Tìm kiếm tri thức liên quan từ kho 185 tài liệu
            print("\n🔍 Đang tra cứu dữ liệu liên quan từ kho sách...")
            relevant_context = search_relevant_knowledge(user_prompt, knowledge_index, top_k=4)
            if relevant_context:
                print("  [✓] Đã trích xuất các trang sách & tài liệu liên quan phù hợp.")
            else:
                print("  [i] Áp dụng kiến thức tổng quát của hệ thống.")

            # Tạo prompt hoàn chỉnh
            prompt_content = f"""
=== DỮ LIỆU THAM KHẢO TỪ KHO SÁCH (WYCKOFF / VSA / PRICE ACTION) ===
{relevant_context if relevant_context else '[Dùng nguyên lý Price Action & Volume chuẩn]'}

=== NỘI DUNG TỪ WEB (NẾU CÓ) ===
{web_data}

=== YÊU CẦU CỦA NGƯỜI DÙNG ===
{full_query}
"""
            client = get_gemini_client()
            if not client:
                print("\n" + "!" * 70)
                print("❌ LỖI API KEY: Chưa có GEMINI_API_KEY hợp lệ trong file .env")
                print("👉 Hướng dẫn: Mở file .env và dán API Key của bạn theo cú pháp:")
                print("   GEMINI_API_KEY=AIzaSyYourActualKeyHere")
                print("!" * 70)
                continue

            print("\n⏳ AI Agent đang xử lý và phân tích chuyên sâu...")

            # Chuẩn bị nội dung gửi Gemini (Multimodal nếu có ảnh)
            contents_payload = []
            if pil_image:
                contents_payload.append(pil_image)
            contents_payload.append(prompt_content)

            # Gọi Gemini API
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=contents_payload,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    temperature=0.35
                )
            )

            print("\n" + "=" * 32 + " 🎯 KẾT QUẢ PHÂN TÍCH " + "=" * 32 + "\n")
            print(response.text)
            print("\n" + "=" * 80 + "\n")

        except KeyboardInterrupt:
            print("\n\nĐã dừng tác vụ hiện tại.")
            continue
        except Exception as e:
            err_msg = str(e)
            if "API key not valid" in err_msg or "API_KEY_INVALID" in err_msg:
                print("\n❌ LỖI: API Key không hợp lệ. Vui lòng kiểm tra lại GEMINI_API_KEY trong file .env.")
            else:
                print(f"\n❌ Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    run_agent()