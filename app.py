import streamlit as st
import random

# 1. CẤU HÌNH GIAO DIỆN
st.set_page_config(page_title="Hệ thống Khủng hoảng Mega", page_icon="☢️", layout="wide")

st.title("☢️ AI Crisis Simulation - Mega Edition")
st.markdown("---")

# 2. SIÊU KHO CÂU TRẢ LỜI (HƠN 50 CÂU THOẠI)
DATABASE = {
    "Sản phẩm lỗi": [
        "Lỗi là lỗi thế nào? Tôi bỏ tiền mua đồ mới chứ có mua đồ thanh lý đâu!",
        "Các người định lừa dối khách hàng đến bao giờ? Tôi sẽ đăng bài bóc phốt ngay!",
        "Đừng có giải thích lòng vòng, trả tiền lại cho tôi ngay lập tức!",
        "Đồ ăn có dị vật mà bảo 'sơ suất nhỏ' à? Định coi thường mạng sống khách hàng sao?",
        "Bỏ tiền triệu ra mua hàng chính hãng mà nhận về cái thứ rác rưởi này?",
        "Tôi sẽ mang cái này đi kiểm định, lúc đó đừng có mà xin lỗi!",
        "Quảng cáo thì lung linh, thực tế thì lừa đảo. Livestream cho cả thế giới biết nhé!",
        "Uy tín gây dựng 10 năm mà bán cái thứ này à? Thất vọng tràn trề!",
        "Nếu tôi không phát hiện ra thì định im lặng lừa khách luôn đúng không?",
        "Cầm cái thứ này về đi, tôi không muốn nhìn thấy nó thêm một giây nào nữa!",
        "Lần đầu cũng như lần cuối, tẩy chay cái thương hiệu làm ăn vớ vẩn này!",
        "Nhìn cái bao bì thì sang mà chất lượng thì như hàng chợ!"
    ],
    "Dịch vụ chậm": [
        "Tôi đã đợi cả tiếng đồng hồ rồi, các người làm ăn kiểu gì vậy?",
        "Hẹn lần hẹn lượt, uy tín của công ty để đâu rồi?",
        "Quá thất vọng! Tôi sẽ không bao giờ quay lại đây nữa.",
        "Thời gian của tôi là vàng bạc, ai đền bù cho tôi đây?",
        "Định để tôi ngồi đây mọc rễ luôn đúng không? Làm việc chậm như sên!",
        "Lúc thu tiền thì nhanh, lúc phục vụ thì lặn mất tăm là sao?",
        "Hẹn 15 phút mà giờ là 2 tiếng rồi! Định để khách đợi đến Tết à?",
        "Làm ăn kiểu dây thun thế này thì dẹp tiệm sớm đi cho rảnh nợ!",
        "Đã nhắc là đang vội mà thái độ vẫn thờ ơ, thách thức kiên nhẫn của tôi à?",
        "Chờ đợi là hạnh phúc à? Không, đây là sự sỉ nhục khách hàng!",
        "Vô trách nhiệm! Nhận đơn xong để khách leo cây thế này à?",
        "Đừng xin lỗi nữa, hành động đi! Tôi không ăn lời xin lỗi của các người được!"
    ],
    "Thái độ nhân viên": [
        "Khách hàng là thượng đế mà nhân viên lại lườm nguýt tôi sao?",
        "Tôi cần gặp quản lý ngay lập tức, thái độ này không chấp nhận được!",
        "Các người cần phải đào tạo lại nhân viên của mình đi. Quá tệ!",
        "Tôi bỏ tiền ra mua dịch vụ chứ không phải mua sự bực mình!",
        "Nhân viên kiểu gì khách hỏi một đường trả lời một nẻo, còn lườm khách?",
        "Thái độ 'không cần khách' thế này thì bảo sao công ty đi xuống!",
        "Nhìn cái mặt nhân viên như kiểu tôi đang đi xin xỏ vậy. Kinh khủng!",
        "Tôi có ghi âm và quay phim lại hết rồi, đừng có mà bao che cho nhau!",
        "Nghỉ việc đi nếu không làm được, đừng đem thái độ đó ra làm việc với khách!",
        "Một lời xin lỗi hời hợt không xóa được sự thiếu chuyên nghiệp này đâu!",
        "Nhân viên cãi khách nhem nhẻm, văn hóa công ty ở đâu ra vậy?",
        "Cậy mình là thương hiệu lớn rồi coi thường khách lẻ chúng tôi à?"
    ],
    "Đòi bồi thường (Gắt)": [
        "Tôi yêu cầu hoàn tiền 200% vì sự cố này, nếu không tôi không để yên đâu!",
        "Voucher giảm giá 10% à? Các người đang sỉ nhục tôi đấy à? Cất đi!",
        "Đền bù không thỏa đáng thì đừng trách tôi tại sao báo chí vào cuộc!",
        "Tôi muốn gặp trực tiếp giám đốc điều hành, cấp dưới các bạn không đủ trình độ giải quyết!",
        "Miễn phí toàn bộ hóa đơn hôm nay, cộng thêm lời xin lỗi công khai trên Page!",
        "Đừng có dùng mấy cái thẻ quà tặng vớ vẩn để bịt miệng khách hàng!"
    ]
}

# 3. SIDEBAR
with st.sidebar:
    st.header("⚙️ Kịch bản")
    tinh_huong = st.selectbox("🎯 Chọn tình huống:", list(DATABASE.keys()))
    if st.button("🗑️ Reset hội thoại"):
        st.session_state.messages = []
        st.rerun()

# 4. CHAT LOGIC
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Nhân viên trả lời khách hàng..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.spinner("Khách hàng đang 'gõ' cực gắt..."):
        reply = random.choice(DATABASE[tinh_huong])
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.write(reply)
