import streamlit as st
import random
from openai import OpenAI

# ===== API =====
client = OpenAI(api_key="YOUR_API_KEY")

# 1. CẤU HÌNH GIAO DIỆN
st.set_page_config(page_title="Hệ thống Khủng hoảng Mega AI", page_icon="🔥", layout="wide")

# 2. KHO TỪ KHÓA (GIỮ NGUYÊN CỦA BẠN)
KHO_TU_KHOA = {
    "xin lỗi": {
        "Nhẹ": ["Xin lỗi là xong à?", "Biết lỗi thì sửa đi chứ đừng nói suông!", "Lần nào cũng xin lỗi, chán chẳng muốn nghe.", "Lời xin lỗi không giải quyết được vấn đề đâu!", "Xin lỗi thì có lấy lại được thời gian cho tôi không?", "Thôi bớt văn vở đi, giải quyết đi!"],
        "Trung bình": ["Lại bài ca xin lỗi, các người định diễn đến bao giờ?", "Xin lỗi suông thế này thì trẻ con cũng nói được!", "Tôi cần giải pháp, không cần cái câu xin lỗi rẻ tiền này!", "Bao nhiêu lần rồi? Lời xin lỗi của các người quá rẻ rúng!", "Đừng dùng từ xin lỗi để lấp liếm sự yếu kém!", "Xin lỗi mà xong thì cần gì đến pháp luật?"],
        "Cao": ["Câm miệng ngay! Lời xin lỗi của các người làm tôi buồn nôn!", "Đồ lừa đảo! Xin lỗi để chuẩn bị đi lừa người khác tiếp chứ gì?", "Cút đi với cái lời xin lỗi giả tạo đó!", "Tôi sẽ đăng lời xin lỗi này lên mạng cho thiên hạ cười vào mặt các người!", "Quá trơ trẽn! Xúc phạm khách hàng xong rồi bảo xin lỗi là xong à?", "Đừng có vác cái mặt đó ra đây mà xin lỗi tôi!"]
    },
    "nhanh": {
        "Nhẹ": ["Nhanh là bao giờ?", "Đừng có hứa lèo, làm nhanh giúp tôi!", "Tôi đợi mệt mỏi lắm rồi đấy!", "Nhanh lên chút đi, trễ hết việc rồi!", "Nói nhanh mà làm thì như sên vậy!", "Nhanh lên, kiên nhẫn của tôi có hạn!"],
        "Trung bình": ["Hẹn nhanh mà bắt đợi mốc mồm, các người đùa tôi à?", "Nhanh của các người là tính bằng năm đúng không?", "Làm ăn lề mề, coi thường thời gian của khách!", "Tôi không rảnh để nghe các người hứa nhanh!", "Đừng có dùng chữ 'nhanh' để câu giờ nữa!", "Quá thất vọng với cái tiến độ 'nhanh' này!"],
        "Cao": ["Dẹp tiệm đi nếu không làm nhanh được!", "Định để khách đợi đến Tết Công-gô à? Đồ vô dụng!", "Thời gian của tôi là vàng bạc, ai đền bù nổi cái sự chậm chạp này?", "Cút! Làm ăn kiểu dây thun thế này mà cũng đòi kinh doanh?", "Tôi sẽ đốt cái cửa hàng này nếu các người còn bảo tôi đợi!", "Lừa đảo! Bảo nhanh mà bắt đợi cả ngày trời!"]
    }
}

# 3. SIDEBAR (GIỮ NGUYÊN)
with st.sidebar:
    st.header("⚙️ BẢNG ĐIỀU KHIỂN")
    tinh_huong = st.selectbox("🎯 Tình huống:", ["Sản phẩm lỗi", "Nhân viên thái độ", "Giao hàng trễ"])
    muc_do = st.select_slider("🔥 Độ nóng giận:", options=["Nhẹ", "Trung bình", "Cao"])
    st.write("---")
    if st.button("🗑️ Xóa hội thoại"):
        st.session_state.messages = []
        st.rerun()

st.title("🛡️ Crisis Simulation 6.0")
st.info(f"Mô phỏng: **{tinh_huong}** | Cấp độ: **{muc_do}**")

# 4. SESSION
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ===== CÂU MỞ ĐẦU THEO TÌNH HUỐNG =====
def mo_dau_tinh_huong(tinh_huong):
    if tinh_huong == "Sản phẩm lỗi":
        return "Sản phẩm tôi nhận bị lỗi ngay khi mở ra. Giải thích thế nào đây?"
    elif tinh_huong == "Nhân viên thái độ":
        return "Thái độ nhân viên bên bạn thực sự không chấp nhận được."
    elif tinh_huong == "Giao hàng trễ":
        return "Đơn hàng của tôi trễ hơn dự kiến khá lâu rồi."
    return ""

# 5. XỬ LÝ CHAT
if prompt := st.chat_input("Phản hồi khách hàng..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    cau_nhap = prompt.lower()
    found_key = None

    for key in KHO_TU_KHOA.keys():
        if key in cau_nhap:
            found_key = key
            break

    # ===== Nếu có từ khóa → dùng kho cũ =====
    if found_key:
        reply = random.choice(KHO_TU_KHOA[found_key][muc_do])
    else:
        # ===== Nếu không có → AI tự sinh thông minh =====
        system_prompt = f"""
Bạn đang đóng vai khách hàng cực kỳ bức xúc.
Tình huống: {tinh_huong}
Mức độ: {muc_do}

Phản hồi thực tế, gay gắt nhưng không đe dọa.
Trả lời ngắn 2-3 câu.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=1.2,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response.choices[0].message.content

    # ===== Thêm câu mở đầu nếu là tin nhắn đầu =====
    if len(st.session_state.messages) == 1:
        reply = mo_dau_tinh_huong(tinh_huong) + "\n\n" + reply

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})