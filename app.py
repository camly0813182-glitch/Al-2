import streamlit as st
import random

# 1. CẤU HÌNH GIAO DIỆN
st.set_page_config(page_title="Hệ thống Khủng hoảng Thông minh", page_icon="🧠", layout="wide")

# --- CÂU MỞ ĐẦU CHO 3 TÌNH HUỐNG ---
CAU_MO_DAU = {
    "Sản phẩm lỗi": "Này con kia,sao giao tao cái áo rách ? ",
    "Nhân viên thái độ": "Tôi yêu cầu gặp quản lý! Nhân viên thu ngân ở đây có thái độ cực kỳ lồi lõm với khách hàng!",
    "Giao hàng/Dịch vụ": "Hẹn giao buổi sáng mà giờ tối mịt mới tới, lại còn giao sai size! Định lừa khách à?"
}

# 2. KHO TỪ KHÓA THÔNG MINH (KẾT HỢP ĐẦY ĐỦ)
KHO_THONG_MINH = {
    "xin lỗi": {
        "Nhẹ": ["Xin lỗi là xong à? Làm ăn cho cẩn thận vào!", "Lại bài ca xin lỗi, tôi nghe phát chán rồi.", "Biết lỗi thì sửa đi chứ đừng nói suông."],
        "Trung bình": ["Lại xin lỗi! Định diễn đến bao giờ nữa?", "Xin lỗi suông thế này trẻ con cũng nói được!", "Tôi cần giải pháp, không cần lời xin lỗi rẻ tiền!"],
        "Cao": ["Câm miệng! Đừng có vác cái mặt đó ra xin lỗi tôi!", "Đồ giả tạo! Xin lỗi để chuẩn bị lừa người khác tiếp chứ gì?", "Cút đi với cái lời xin lỗi rác rưởi đó!"]
    },
    "nhanh": {
        "Nhẹ": ["Nhanh là bao giờ? Hứa lèo vừa thôi!", "Tôi đợi mệt mỏi lắm rồi đấy!", "Làm nhanh giúp tôi cái, trễ hết việc rồi."],
        "Trung bình": ["Hẹn nhanh mà bắt đợi mốc mồm, các người đùa tôi à?", "Làm ăn lề mề, coi thường thời gian của khách!", "Đừng có dùng chữ 'nhanh' để câu giờ nữa!"],
        "Cao": ["Dẹp tiệm đi nếu không làm nhanh được!", "Định để khách đợi đến Tết Công-gô à? Đồ vô dụng!", "Thời gian của tôi là vàng bạc, ai đền bù nổi sự chậm chạp này?"]
    },
    "đền bù": {
        "Nhẹ": ["Đền bù thế nào cho thỏa đáng đây?", "Voucher 10k à? Đừng có khinh người!", "Tôi cần mức đền bù thực tế hơn."],
        "Trung bình": ["Định dùng tiền để bịt miệng khách hàng à?", "Đền bù không xứng đáng tôi sẽ làm tới cùng!", "Tôi không thiếu tiền, tôi cần sự công bằng!"],
        "Cao": ["Đền bù 200% hóa đơn ngay hoặc là ra tòa!", "Trả tiền gấp đôi và biến ngay cho khuất mắt tôi!", "Quá trơ trẽn khi đưa ra mức đền bù như sỉ nhục khách!"]
    },
    "quản lí": {
        "Nhẹ": ["Quản lý kiểu gì mà để xảy ra sai sót này?", "Tôi cần gặp quản lý ngay, bạn không giải quyết được.", "Đào tạo lại quản lý đi, làm việc quá lỏng lẻo!"],
        "Trung bình": ["Gọi quản lý ra đây, đừng có đẩy đưa nữa!", "Quản lý cái kiểu gì mà nhân viên thái độ lồi lõm với khách?", "Quản lý công ty này lặn đâu hết rồi?"],
        "Cao": ["Cấp dưới láo lếu là do quản lý vô dụng!", "Giám đốc các người đâu? Ra đây mà xem nhân viên làm loạn này!", "Tôi sẽ kiện cả cái ban quản lý này ra tòa!"]
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
    },
    "nhân viên": {
        "Nhẹ": ["Nhân viên bên mình cần được đào tạo lại thái độ nhé.", "Bạn nhân viên đó làm việc hơi thiếu chuyên nghiệp."],
        "Trung bình": ["Nhân viên thái độ lồi lõm thế này mà shop vẫn giữ lại à?", "Tôi yêu cầu nhân viên đó phải trực tiếp xin lỗi tôi!"],
        "Cao": ["Vô học! Loại nhân viên mất dạy đó shop tuyển ở đâu về vậy?", "Cả cái hệ thống này nát từ quản lý đến nhân viên!"]
    },
    "chậm": {
        "Nhẹ": ["Chậm trễ thế này làm lỡ hết việc của tôi rồi!", "Sao làm ăn lề mề quá vậy?"],
        "Trung bình": ["Hẹn một đằng làm một nẻo, quá chậm trễ!", "Chậm như sên vậy mà cũng đòi làm dịch vụ sao?"],
        "Cao": ["Dẹp tiệm đi! Làm ăn chậm chạp thế này thì kinh doanh gì?", "Lừa đảo! Bảo giao ngay mà bắt đợi mục xương!"]
    },
    "quá tải": {
        "Nhẹ": ["Quá tải là việc của shop, shop phải tự sắp xếp chứ?", "Đừng lấy lý do quá tải ra để bào chữa!"],
        "Trung bình": ["Làm ăn không có kế hoạch mới để quá tải, quá kém!", "Quá tải là cái cớ để trốn tránh trách nhiệm đúng không?"],
        "Cao": ["Tham tiền mà lừa dối khách hàng rồi kêu quá tải!", "Biến ngay! Tôi không nghe bất cứ lời bào chữa nào về quá tải đơn!"]
    },
    "size": {
        "Nhẹ": ["Giao nhầm size rồi shop ơi, đổi lại giúp tôi.", "Tôi dặn là size L mà sao lại giao size S thế này?"],
        "Trung bình": ["Làm ăn cẩu thả, cái size cơ bản cũng giao sai được!", "Giao sai size rồi giờ bắt khách chịu phí ship đổi trả à?"],
        "Cao": ["Mù chữ à? Đơn ghi XL mà giao sang M là sao?", "Lừa đảo! Giao sai size để đẩy hàng tồn chứ gì?"]
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

st.title("🛡️ Crisis Simulation Bot 6.0")

# 4. HIỂN THỊ CHAT
if "messages" not in st.session_state or len(st.session_state.messages) == 0:
    st.session_state.messages = [{"role": "assistant", "content": CAU_MO_DAU[tinh_huong]}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 5. BỘ NÃO NHẬN DIỆN THÔNG MINH
if prompt := st.chat_input("Nhân viên phản hồi..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    cau_nhap = prompt.lower()
    reply = ""
    found = False

    for key in KHO_THONG_MINH:
        if key in cau_nhap:
            reply = random.choice(KHO_THONG_MINH[key][muc_do])
            found = True
            break
    
    if not found:
        fallback_data = ["Giải quyết đi, đừng lôi thôi!", "Tóm lại là bao giờ xong?", "Đừng có lảm nhảm nữa!"]
        reply = random.choice(fallback_data)

    with st.chat_message("assistant"):
        st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
