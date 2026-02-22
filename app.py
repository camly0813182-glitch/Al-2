import streamlit as st
import random

# 1. CẤU HÌNH GIAO DIỆN
st.set_page_config(page_title="Hệ thống Khủng hoảng Thông minh", page_icon="🧠", layout="wide")

# --- PHẦN THÊM MỚI: CÂU MỞ ĐẦU CHO 3 TÌNH HUỐNG ---
CAU_MO_DAU = {
    "Sản phẩm lỗi": "Này shop, cái áo tôi vừa nhận sao bị rách vế bên trái thế này? Làm ăn kiểu gì vậy?",
    "Nhân viên thái độ": "Tôi yêu cầu gặp quản lý! Nhân viên thu ngân ở đây có thái độ cực kỳ lồi lõm với khách hàng!",
    "Giao hàng/Dịch vụ": "Hẹn giao buổi sáng mà giờ tối mịt mới tới, lại còn giao sai size! Định lừa khách à?"
}

# 2. KHO TỪ KHÓA KHỔNG LỒ (Đã kết hợp tất cả từ khóa của bạn)
KHO_THONG_MINH = {
    "xin lỗi": {
        "Nhẹ": ["Xin lỗi là xong à? Làm ăn cho cẩn thận vào!", "Lại bài ca xin lỗi, tôi nghe phát chán rồi.", "Biết lỗi thì sửa đi chứ đừng nói suông.", "Lời xin lỗi của bạn không giải quyết được vấn đề!", "Xin lỗi thì có lấy lại được thời gian cho tôi không?", "Thôi bớt văn vở đi, giải quyết đi!"],
        "Trung bình": ["Lại xin lỗi! Định diễn đến bao giờ nữa?", "Xin lỗi suông thế này trẻ con cũng nói được!", "Tôi cần giải pháp, không cần lời xin lỗi rẻ tiền!", "Bao nhiêu lần rồi? Đừng dùng từ xin lỗi để lấp liếm!", "Lời xin lỗi của các người quá rẻ rúng!", "Xin lỗi mà xong thì cần gì đến pháp luật?"],
        "Cao": ["Câm miệng! Đừng có vác cái mặt đó ra xin lỗi tôi!", "Đồ giả tạo! Xin lỗi để chuẩn bị lừa người khác tiếp chứ gì?", "Cút đi với cái lời xin lỗi rác rưởi đó!", "Xúc phạm khách hàng xong rồi bảo xin lỗi là xong à?", "Tôi sẽ đăng lời xin lỗi này lên mạng cho thiên hạ cười!", "Đừng để tôi nghe thấy chữ 'xin lỗi' từ bạn nữa!"]
    },
    "nhanh": {
        "Nhẹ": ["Nhanh là bao giờ? Hứa lèo vừa thôi!", "Tôi đợi mệt mỏi lắm rồi đấy!", "Làm nhanh giúp tôi cái, trễ hết việc rồi.", "Nhanh lên chút đi, kiên nhẫn của tôi có hạn!", "Nói nhanh mà làm thì như sên vậy!", "Nhanh lên, tôi không rảnh ngồi đây cả ngày!"],
        "Trung bình": ["Hẹn nhanh mà bắt đợi mốc mồm, các người đùa tôi à?", "Nhanh của các người là tính bằng năm đúng không?", "Làm ăn lề mề, coi thường thời gian của khách!", "Đừng có dùng chữ 'nhanh' để câu giờ nữa!", "Quá thất vọng với cái tiến độ 'nhanh' này!", "Tôi không rảnh để nghe các người hứa nhanh!"],
        "Cao": ["Dẹp tiệm đi nếu không làm nhanh được!", "Định để khách đợi đến Tết Công-gô à? Đồ vô dụng!", "Thời gian của tôi là vàng bạc, ai đền bù nổi sự chậm chạp này?", "Cút! Làm ăn kiểu dây thun thế này mà cũng đòi kinh doanh?", "Tôi sẽ đốt cái cửa hàng này nếu các người còn bảo tôi đợi!", "Lừa đảo! Bảo nhanh mà bắt đợi cả ngày trời!"]
    },
    "đền bù": {
        "Nhẹ": ["Đền bù thế nào cho thỏa đáng đây?", "Voucher 10k à? Đừng có khinh người!", "Tôi cần mức đền bù thực tế hơn.", "Làm ăn sai thì phải đền bù cho đáng!", "Đền bù cái gì thì nói thẳng ra đi!", "Đền bù kiểu này thì ai thèm lấy?"],
        "Trung bình": ["Định dùng tiền để bịt miệng khách hàng à?", "Đền bù không xứng đáng tôi sẽ làm tới cùng!", "Tôi không thiếu tiền, tôi cần sự công bằng!", "Đừng có bố thí cho tôi bằng mấy cái mã giảm giá!", "Quá nực cười cho cái chính sách đền bù này!", "Đền bù thế này mà cũng gọi là đền bù sao?"],
        "Cao": ["Đền bù 200% hóa đơn ngay hoặc là ra tòa!", "Cả cái công ty này bán đi cũng không đền bù nổi danh dự của tôi!", "Đừng có lôi tiền ra nhử, tôi sẽ cho các người dép tiệm!", "Trả tiền gấp đôi và biến ngay cho khuất mắt tôi!", "Quá trơ trẽn khi đưa ra mức đền bù như sỉ nhục khách!", "Tiền của các người to lắm à mà đòi đền bù chút đỉnh?"]
    },
    "quản lí": {
        "Nhẹ": ["Quản lý kiểu gì mà để xảy ra sai sót này?", "Tôi cần gặp quản lý ngay, bạn không giải quyết được.", "Đào tạo lại quản lý đi, làm việc quá lỏng lẻo!", "Quản lý có biết nhân viên làm ăn như thế nào không?", "Giao cho tôi gặp người có thẩm quyền cao hơn đi!", "Làm quản lý mà trả lời thế này à?"],
        "Trung bình": ["Gọi quản lý ra đây, đừng có đẩy đưa nữa!", "Quản lý cái kiểu gì mà nhân viên thái độ lồi lõm với khách?", "Tôi muốn làm việc với người biết điều, không phải bạn!", "Quản lý công ty này lặn đâu hết rồi?", "Chính sách của quản lý các người là coi thường khách à?", "Để tôi xem quản lý của các người giỏi đến mức nào!"],
        "Cao": ["Cấp dưới láo lếu là do quản lý vô dụng!", "Giám đốc các người đâu? Ra đây mà xem nhân viên làm loạn này!", "Quản lý nát thế này hèn gì công ty sớm muộn cũng sập!", "Đừng có bao che cho nhau, gọi quản lý ra đây!", "Tôi sẽ kiện cả cái ban quản lý này ra tòa!", "Vô học từ quản lý đến nhân viên, quá kinh khủng!"]
    },
    "xử lí": {
        "Nhẹ": ["Xử lý kiểu gì mà chậm chạp thế?", "Cần giải quyết dứt điểm ngay đi!", "Tôi không hài lòng với cách xử lý này."],
        "Trung bình": ["Làm ăn tắc trách, xử lý quá thiếu chuyên nghiệp!", "Định kéo dài thời gian xử lý đến bao giờ?", "Tôi yêu cầu một phương án xử lý khác thỏa đáng hơn!"],
        "Cao": ["Xử lý rác rưởi! Gọi ngay người có thẩm quyền ra đây!", "Quá trơ trẽn! Xử lý sai rành rành mà vẫn bao biện à?", "Tôi sẽ làm đơn kiện cái cách xử lý coi thường khách này!"]
    },
    "sai sót": {
        "Nhẹ": ["Làm ăn mà để sai sót thế này à?", "Kiểm tra lại đi, sai rành rành ra đấy.", "Lần sau đừng để xảy ra sai sót ngớ ngẩn này nữa."],
        "Trung bình": ["Sai sót hệ thống hay do con người? Quá kém cỏi!", "Một lỗi sai cơ bản mà cũng mắc phải, shop làm ăn kiểu gì vậy?", "Tôi không chấp nhận cái lý do sai sót khách quan này!"],
        "Cao": ["Lừa đảo khách hàng rồi đổ lỗi cho sai sót à?", "Đồ vô dụng! Sai sót này gây thiệt hại lớn cho tôi, ai đền?", "Biến đi! Sai sót nối tiếp sai sót, không thể tin nổi!"]
    },
    "thay mặt": {
        "Nhẹ": ["Thay mặt xin lỗi thì có giải quyết được gì không?", "Đừng nói câu thay mặt, hãy hành động đi.", "Lời xin lỗi thay mặt này nghe quá máy móc."],
        "Trung bình": ["Bạn lấy tư cách gì mà thay mặt? Tôi cần người trực tiếp làm sai!", "Thay mặt mà làm ăn như thế này thì dẹp đi cho rồi!", "Đừng dùng từ 'thay mặt' để trốn tránh trách nhiệm cá nhân."],
        "Cao": ["Cút! Đừng có đứng đó mà thay mặt với thay mũi!", "Quá trơ trẽn! Thay mặt xin lỗi mà thái độ vẫn lồi lõm!", "Tôi không cần cái sự thay mặt giả tạo này, gọi giám đốc ra đây!"]
    }
}

# 3. THANH BÊN (SIDEBAR)
with st.sidebar:
    st.header("⚙️ ĐIỀU KHIỂN")
    tinh_huong = st.selectbox("🎯 Kịch bản:", list(CAU_MO_DAU.keys()))
    muc_do = st.select_slider("🔥 Độ nóng giận:", options=["Nhẹ", "Trung bình", "Cao"])
    
    if st.button("🗑️ Làm mới hội thoại"):
        st.session_state.messages = [{"role": "assistant", "content": CAU_MO_DAU[tinh_huong]}]
        st.rerun()

st.title("🛡️ Crisis Simulation 6.0 (Smart Engine)")

# 4. HIỂN THỊ CHAT
if "messages" not in st.session_state or len(st.session_state.messages) == 0:
    st.session_state.messages = [{"role": "assistant", "content": CAU_MO_DAU[tinh_huong]}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 5. BỘ NÃO NHẬN DIỆN THÔNG MINH
if prompt := st.chat_input("Nhập phản hồi của nhân viên..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    cau_nhap = prompt.lower()
    reply = ""
    found = False

    # Quét từ khóa
    for key in KHO_THONG_MINH:
        if key in cau_nhap:
            reply = random.choice(KHO_THONG_MINH[key][muc_do])
            found = True
            break
    
    if not found:
        fallback_data = [
            "Đừng có lảm nhảm nữa, giải quyết đi!",
            "Càng nói càng thấy vô lý!",
            "Tôi không rảnh ngồi đây nghe các người giải thích!",
            "Tóm lại là bao giờ xong? Đừng có câu giờ!",
            "Làm ăn kiểu gì mà để khách hàng phải gào lên thế này?",
            "Tôi sẽ không bao giờ quay lại đây nữa!"
        ]
        reply = random.choice(fallback_data)

    with st.chat_message("assistant"):
        st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
