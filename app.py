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

# 2. KHO TỪ KHÓA KHỔNG LỒ (Giữ nguyên toàn bộ nội dung của bạn)
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
        "Cao": ["Đền bù 200% hóa đơn ngay hoặc là ra tòa!", "Cả cái công ty này bán đi cũng không đền bù nổi danh dự của tôi!", "Đừng có lôi tiền ra nhử, tôi sẽ cho các người dẹp tiệm!", "Trả tiền gấp đôi và biến ngay cho khuất mắt tôi!", "Quá trơ trẽn khi đưa ra mức đền bù như sỉ nhục khách!", "Tiền của các người to lắm à mà đòi đền bù chút đỉnh?"]
    },
    "quản lí": {
        "Nhẹ": ["Quản lý kiểu gì mà để xảy ra sai sót này?", "Tôi cần gặp quản lý ngay, bạn không giải quyết được.", "Đào tạo lại quản lý đi, làm việc quá lỏng lẻo!", "Quản lý có biết nhân viên làm ăn như thế nào không?", "Giao cho tôi gặp người có thẩm quyền cao hơn đi!", "Làm quản lý mà trả lời thế này à?"],
        "Trung bình": ["Gọi quản lý ra đây, đừng có đẩy đưa nữa!", "Quản lý cái kiểu gì mà nhân viên thái độ lồi lõm với khách?", "Tôi muốn làm việc với người biết điều, không phải bạn!", "Quản lý công ty này lặn đâu hết rồi?", "Chính sách của quản lý các người là coi thường khách à?", "Để tôi xem quản lý của các người giỏi đến mức nào!"],
        "Cao": ["Cấp dưới láo lếu là do quản lý vô dụng!", "Giám đốc các người đâu? Ra đây mà xem nhân viên làm loạn này!", "Quản lý nát thế này hèn gì công ty sớm muộn cũng sập!", "Đừng có bao che cho nhau, gọi quản lý ra đây!", "Tôi sẽ kiện cả cái ban quản lý này ra tòa!", "Vô học từ quản lý đến nhân viên, quá kinh khủng!"] ,
            "chậm": {
        "Nhẹ": ["Chậm trễ thế này làm lỡ hết việc của tôi rồi!", "Sao làm ăn lề mề quá vậy? Nhanh lên chút đi.", "Đợi từ sáng đến giờ vẫn chưa thấy đâu, quá chậm!", "Lần sau giao hàng thì tính toán thời gian cho chuẩn vào.", "Chậm một lần thì bỏ qua, chứ lần nào cũng thế này à?", "Tôi không có cả ngày để đợi cái sự chậm chạp này đâu!"],
        "Trung bình": ["Hẹn một đằng làm một nẻo, quá chậm trễ!", "Làm ăn kiểu dây thun thế này thì ai mà tin tưởng được nữa?", "Chậm như sên vậy mà cũng đòi làm dịch vụ sao?", "Càng đợi càng mất kiên nhẫn, giải thích lý do chậm trễ xem nào!", "Tôi cần một mốc thời gian cụ thể, đừng có bảo đợi mãi!", "Sự chậm trễ của các người gây thiệt hại cho tôi, ai chịu trách nhiệm?"],
        "Cao": ["Dẹp tiệm đi! Làm ăn chậm chạp như thế này thì kinh doanh cái gì?", "Cút! Tôi không bao giờ quay lại cái nơi làm việc lề mề này nữa!", "Quá trơ trẽn! Chậm cả tiếng đồng hồ mà vẫn nhởn nhơ được à?", "Tôi sẽ đốt cái shop này nếu hàng không tới ngay bây giờ!", "Lừa đảo! Bảo giao ngay mà bắt đợi đến mục xương!", "Đừng để tôi thấy cái bản mặt chậm chạp của các người thêm giây nào nữa!"]
    },
    "quá tải": {
        "Nhẹ": ["Quá tải là việc của shop, shop phải tự sắp xếp chứ?", "Đừng lấy lý do quá tải ra để bào chữa cho sai sót!", "Biết quá tải thì đừng nhận thêm đơn nữa, mất uy tín quá.", "Quá tải thì cũng phải báo một tiếng cho khách biết chứ?", "Lần sau rút kinh nghiệm, đừng để quá tải làm hỏng dịch vụ.", "Khách hàng không quan tâm bạn quá tải hay không, họ cần chất lượng!"],
        "Trung bình": ["Tham công tiếc việc cho lắm vào rồi bảo quá tải!", "Làm ăn không có kế hoạch mới để quá tải, quá kém cỏi!", "Lý do quá tải nghe quen quá rồi, đổi bài khác đi!", "Quá tải đơn thì tuyển thêm người đi, sao bắt khách chịu trận?", "Đừng đổ lỗi cho khách quan, do các người quản lý kém thôi!", "Quá tải là cái cớ để trốn tránh trách nhiệm đúng không?"],
        "Cao": ["Quá tải thì dẹp đi! Đừng có tham tiền mà lừa dối khách hàng!", "Cút ngay với cái lý do quá tải rẻ tiền đó!", "Sự yếu kém của các người là vô hạn, đừng có đổ lỗi cho đơn hàng!", "Tôi sẽ cho cả thế giới biết cái sự bết bát mang tên quá tải này!", "Quá trơ trẽn! Làm ăn kiểu chộp giật rồi kêu ca quá tải!", "Biến ngay! Tôi không nghe bất cứ lời bào chữa nào về việc quá tải đơn!"]
    },
    "nhân viên": {
        "Nhẹ": ["Nhân viên bên mình cần được đào tạo lại thái độ nhé.", "Bạn nhân viên đó làm việc hơi thiếu chuyên nghiệp.", "Góp ý với shop là nhân viên nên niềm nở hơn chút.", "Nhân viên trả lời khách mà cứ như đi ban ơn vậy?", "Tôi không hài lòng với cách phục vụ của nhân viên hôm nay.", "Nhân viên làm sai thì shop phải chấn chỉnh ngay đi!"],
        "Trung bình": ["Nhân viên thái độ lồi lõm thế này mà shop vẫn giữ lại à?", "Tôi yêu cầu nhân viên đó phải trực tiếp xin lỗi tôi!", "Đào tạo kiểu gì mà nhân viên cãi khách nhem nhẻm vậy?", "Nhân viên làm việc tắc trách, coi thường khách hàng quá mức!", "Đừng có bao che cho nhân viên, tôi có bằng chứng hết đấy!", "Tôi sẽ không bao giờ quay lại nếu còn thấy nhân viên đó ở đây!"],
        "Cao": ["Vô học! Loại nhân viên mất dạy đó shop tuyển ở đâu về vậy?", "Câm mồm ngay! Đừng để tôi phải động tay động chân với nhân viên của các người!", "Cả cái hệ thống này nát từ quản lý đến nhân viên!", "Tôi sẽ kiện nhân viên đó vì tội xúc phạm danh dự khách hàng!", "Đồ mất dạy! Nhân viên kiểu gì mà dám thách thức khách hàng?", "Biến đi! Đừng để tôi nhìn thấy cái bản mặt nhân viên đó nữa!"]
    },
    "tiền": {
        "Nhẹ": ["Tiền nào của nấy, nhưng hàng này không xứng đáng với giá tiền!", "Tôi bỏ tiền ra để mua chất lượng chứ không phải mua rác.", "Trả tiền lại cho tôi nếu không xử lý được vấn đề này.", "Cân nhắc lại giá cả đi, làm ăn thế này là đắt đỏ quá!", "Tiền của tôi chứ có phải lá đa đâu mà các người làm ăn thế?", "Shop xem lại hóa đơn đi, tính tiền sai cho tôi rồi này!"],
        "Trung bình": ["Đừng có hám tiền mà làm ăn chộp giật như thế!", "Tôi muốn hoàn tiền ngay lập tức, không nói nhiều!", "Tiền mất tật mang, shop làm ăn quá thất đức!", "Định ăn chặn tiền của khách hàng à? Đồ lừa đảo!", "Tiền mồ hôi nước mắt của tôi, trả lại đây nhanh!", "Bỏ ra một đống tiền mà nhận lại cái thứ này, thật nhục nhã!"],
        "Cao": ["Ăn cướp à? Thu tiền khách rồi giao cái thứ rẻ rách này!", "Đồ thất đức! Tiền đó để mua thuốc cho các người đấy!", "Trả tiền đây nhanh không tôi gọi công an đến xích cả lũ lại!", "Tôi sẽ cho shop sập tiệm vì cái tội lừa đảo chiếm đoạt tài sản!", "Tiền của tôi không phải để các người tiêu xài kiểu này, biến!", "Cả cái công ty này sống trên xương máu khách hàng à? Trả tiền đây!"]
    },
    "size": {
        "Nhẹ": ["Giao nhầm size rồi shop ơi, đổi lại giúp tôi.", "Size này mặc chật quá, xem lại đơn hàng đi.", "Bảng size của shop có chuẩn không vậy? Mặc không vừa tí nào.", "Nhầm size làm mất công tôi phải đi đổi trả.", "Tôi dặn là size L mà sao lại giao size S thế này?", "Lần sau kiểm tra kỹ size trước khi đóng gói nhé."],
        "Trung bình": ["Làm ăn cẩu thả, cái size cơ bản cũng giao sai được!", "Bắt khách đợi rồi lại giao sai size, shop đùa tôi à?", "Định bắt tôi mặc cái thứ không vừa này để đi diễn hài sao?", "Giao sai size rồi giờ bắt khách chịu phí ship đổi trả à? Vô lý!", "Làm ăn thiếu chuyên nghiệp quá, giao sai hết lần này đến lần khác!", "Đổi gấp size đúng cho tôi trong hôm nay, không thì hoàn tiền!"],
        "Cao": ["Mù chữ à? Đơn ghi XL mà giao sang M là sao?", "Lừa đảo! Giao sai size để đẩy hàng tồn chứ gì?", "Cút! Mang cái mớ giẻ rách nhầm size này về ngay!", "Tôi sẽ bóc phốt cái sự làm ăn mù quáng giao sai size này!", "Thách thức sự kiên nhẫn của tôi bằng việc giao sai size à?", "Đồ thất đức! Giao sai rồi còn bắt khách chờ đợi, biến đi!"]
    }

# 3. THANH BÊN (SIDEBAR)
with st.sidebar:
    st.header("⚙️ ĐIỀU KHIỂN")
    tinh_huong = st.selectbox("🎯 Kịch bản:", list(CAU_MO_DAU.keys()))
    muc_do = st.select_slider("🔥 Độ nóng giận:", options=["Nhẹ", "Trung bình", "Cao"])
    
    # Khi bấm nút này, lịch sử chat xóa sạch và nạp câu mở đầu của tình huống đang chọn
    if st.button("🗑️ Làm mới hội thoại"):
        st.session_state.messages = [{"role": "assistant", "content": CAU_MO_DAU[tinh_huong]}]
        st.rerun()

st.title("🛡️ Crisis Simulation 6.0 (Smart Engine)")

# 4. HIỂN THỊ CHAT
# Khởi tạo câu mắng đầu tiên nếu chưa có tin nhắn nào
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
    
    # Nếu không có từ khóa -> Phản hồi ngẫu nhiên theo tình huống
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
