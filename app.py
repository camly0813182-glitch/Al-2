import streamlit as st
import random

# 1. CẤU HÌNH GIAO DIỆN
st.set_page_config(page_title="Hệ thống Khủng hoảng Đa năng", page_icon="🤖")
st.title("🤖 Robot Mô Phỏng Khủng Hoảng (Nâng cấp từ khóa)")

# 2. MỞ RỘNG KHO TỪ KHÓA NHẬN DIỆN (Thêm các câu bạn yêu cầu)
KHO_PHAN_HOI = {
    "xin lỗi": [
        "Xin lỗi là xong à? Các người nghĩ lời xin lỗi đáng giá bao nhiêu?",
        "Đừng có văn vở! Tôi cần hành động chứ không cần mấy câu xin lỗi suông này!",
        "Bao nhiêu khách hàng đã phải nghe câu xin lỗi này rồi? Làm ăn quá kém!"
    ],
    "xử lý thỏa đáng": [
        "Thỏa đáng là thế nào? Định dùng mấy cái voucher rẻ tiền để bịt miệng tôi sao?",
        "Tôi nghe câu này nhiều rồi, tóm lại là bao giờ tôi nhận được tiền đền bù?",
        "Nói thì hay lắm, để xem các người làm được đến đâu hay lại lặn mất tăm!"
    ],
    "nhanh giúp": [
        "Nhanh là bao lâu? Một tiếng, một ngày hay là sang năm?",
        "Lúc nào cũng bảo nhanh mà bắt khách chờ mốc mồm ra!",
        "Tôi không rảnh để ngồi đây đợi cái chữ 'nhanh' hứa lèo của các người đâu!"
    ],
    "nhân viên": [
        "Xử lý nhân viên thì giải quyết được gì cho cái sự bực mình của tôi hiện tại?",
        "Đào tạo kiểu gì mà để nhân viên thái độ lồi lõm với khách rồi giờ mới bảo xử lý?",
        "Tôi muốn thấy hành động cụ thể chứ không phải lời hứa suông về việc kỷ luật nhân viên!"
    ],
    "tiền": [
        "Trả tiền lại cho tôi ngay! Tôi không muốn dùng bất cứ thứ gì của các người nữa!",
        "Các người định ăn chặn tiền của khách hàng đúng không? Đồ lừa đảo!"
    ],
    "mặc định": [
        "Đừng trả lời máy móc, tôi đang rất giận đấy!",
        "Nói gì đi chứ? Làm ăn kiểu gì mà để khách hàng phải gào lên thế này?"
    ]
}

# 3. QUẢN LÝ TIN NHẮN (Giữ nguyên logic cũ)
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 4. LOGIC NHẬN DIỆN CÂU TỪ MỞ RỘNG
if prompt := st.chat_input("Nhân viên nhắn tin xử lý..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    cau_nhap = prompt.lower()
    reply = None
    
    # Kiểm tra các cụm từ khóa bạn yêu cầu
    if "xin lỗi" in cau_nhap:
        reply = random.choice(KHO_PHAN_HOI["xin lỗi"])
    elif "thỏa đáng" in cau_nhap or "xử lý thỏa đáng" in cau_nhap:
        reply = random.choice(KHO_PHAN_HOI["xử lý thỏa đáng"])
    elif "nhanh" in cau_nhap or "giúp" in cau_nhap:
        reply = random.choice(KHO_PHAN_HOI["nhanh giúp"])
    elif "nhân viên" in cau_nhap:
        reply = random.choice(KHO_PHAN_HOI["nhân viên"])
    elif "tiền" in cau_nhap or "hoàn" in cau_nhap:
        reply = random.choice(KHO_PHAN_HOI["tiền"])
    else:
        reply = random.choice(KHO_PHAN_HOI["mặc định"])

    with st.chat_message("assistant"):
        st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
import streamlit as st
import random

# --- PHẦN 1: GIỮ CẤU HÌNH GIAO DIỆN CŨ ---
st.set_page_config(page_title="Hệ thống Khủng hoảng Mega AI", page_icon="🔥", layout="wide")

# --- PHẦN 2: KHO TỪ KHÓA KHỔNG LỒ (NỐI THÊM VÀO) ---
KHO_DATA = {
    "xin lỗi": {
        "Nhẹ": ["Xin lỗi là xong à?", "Nói thì dễ làm mới khó!", "Lại văn mẫu xin lỗi.", "Biết lỗi thì sửa đi!", "Nghe xin lỗi phát chán!", "Thôi bớt giọng đó đi!"],
        "Trung bình": ["Xin lỗi suông thế này trẻ con cũng nói được!", "Định lấp liếm sự yếu kém à?", "Lời xin lỗi không giá trị!", "Càng nghe càng bực mình!", "Có đâu lại vào đấy không?", "Tôi cần giải pháp thực tế!"],
        "Cao": ["Câm miệng! Đừng vác mặt ra xin lỗi tôi!", "Đồ giả tạo! Định lừa ai nữa?", "Cút đi với lời xin lỗi rẻ rúng!", "Xúc phạm tôi xong bảo xin lỗi là hết?", "Tôi đăng lời xin lỗi rác rưởi này lên mạng!", "Đừng để tôi nghe chữ này lần nữa!"]
    },
    "giao sai size": {
        "Nhẹ": ["Làm ăn kiểu gì nhầm size vậy?", "Đổi ngay đi, mất thời gian!", "Size này mặc kiểu gì?", "Treo đầu dê bán thịt chó à?", "Cẩn thận lại đi nhé!", "Tôi dặn kỹ là size M mà?"],
        "Trung bình": ["Không biết đọc đơn hàng à?", "Làm ăn cẩu thả quá mức!", "Bắt khách mặc đồ không vừa sao?", "Giao sai rồi bắt khách chịu ship đổi?", "Quá thiếu chuyên nghiệp!", "Đổi gấp hoặc trả tiền đây!"],
        "Cao": ["Lừa đảo! Giao sai để đẩy hàng tồn?", "Đồ mù chữ! Nhìn XL ra S được à?", "Cút! Mang mớ giẻ rách này về!", "Tôi sẽ bóc phốt cái đơn hàng sai này!", "Thách thức sự điên tiết của tôi à?", "Làm ăn thất đức, quá tồi tệ!"]
    },
    "quá tải": {
        "Nhẹ": ["Quá tải là lỗi của tôi à?", "Làm ăn không tính toán trước sao?", "Đừng lấy lý do đó ra bào chữa.", "Quá tải thì đừng nhận đơn nữa!", "Lần sau sắp xếp cho tốt vào.", "Đợi chờ quá lâu vì cái sự quá tải này!"],
        "Trung bình": ["Quản lý kém mới để quá tải đơn!", "Khách hàng không quan tâm lý do của bạn!", "Đừng đổ lỗi cho khách quan nữa!", "Làm ăn tham lam rồi để quá tải!", "Hứa lèo xong bảo do quá tải đơn?", "Tôi cần hàng chứ không cần lý do!"],
        "Cao": ["Dẹp tiệm đi nếu không xử lý nổi đơn!", "Lừa dối khách hàng bằng lý do quá tải!", "Sự yếu kém của các người là vô hạn!", "Biến ngay! Đừng lôi cái văn quá tải ra đây!", "Tôi sẽ cho cả thế giới biết sự bết bát này!", "Quá trơ trẽn và vô trách nhiệm!"]
    }
    # (Tương tự cho các từ khóa: tiền, đền bù, xử lý, nhân viên...)
}

# --- PHẦN 3: THANH BÊN (SIDEBAR) ĐIỀU KHIỂN ---
with st.sidebar:
    st.header("⚙️ BẢNG ĐIỀU KHIỂN")
    tinh_huong = st.selectbox("🎯 Tình huống:", ["Sản phẩm lỗi", "Nhân viên thái độ", "Dịch vụ/Giao hàng"])
    muc_do = st.select_slider("🔥 Độ nóng giận:", options=["Nhẹ", "Trung bình", "Cao"])
    if st.button("🗑️ Xóa hội thoại"):
        st.session_state.messages = []
        st.rerun()

st.title("🛡️ Crisis Management Simulator 5.0")

# --- PHẦN 4: HIỂN THỊ TIN NHẮN ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- PHẦN 5: LOGIC NỐI KẾT (TỪ KHÓA + THÔNG MINH) ---
if prompt := st.chat_input("Nhân viên nhắn tin..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    cau_nhap = prompt.lower()
    reply = ""

    # Quét từ khóa trong code mới nối vào
    found = False
    for key in KHO_DATA:
        if key in cau_nhap:
            reply = random.choice(KHO_DATA[key][muc_do])
            found = True
            break
    
    # Nếu không thấy từ khóa, dùng logic thông minh dự phòng
    if not found:
        if "dạ" in cau_nhap or "em" in cau_nhap:
            reply = f"Dạ vâng cái gì! {random.choice(KHO_DATA['xin lỗi'][muc_do])}"
        else:
            reply = "Đừng có lảm nhảm nữa, giải quyết nhanh đi!"

    with st.chat_message("assistant"):
        st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
