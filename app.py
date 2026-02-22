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
