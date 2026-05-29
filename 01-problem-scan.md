| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Vinhomes | **Lặp lại (Repetitive)** | Tiếp nhận, đọc hiểu và phân loại (loại sự cố, tòa nhà, ưu tiên) từ hàng ngàn ticket báo hỏng điện, nước, kỹ thuật do cư dân gửi lên App mỗi ngày để tự động điều phối trực tiếp. |
| 2 | Vinhomes | **Tốn thời gian (Time-consuming)** | Nhân sự Ban quản lý mất nhiều thời gian đọc và tự soạn thảo câu trả lời cá nhân hóa để phản hồi các khiếu nại gay gắt hoặc đánh giá 1-star của cư dân trên App . |
| 3 | Vinhomes | **AI có thể tốt hơn (AI-upgrade)** | Nâng cấp hệ thống Chatbot  hỗ trợ cư dân từ dạng kịch bản cứng (Rule-based) lên Conversational AI (LLM) để tư vấn nội quy đô thị, quy trình làm thẻ và tự động đặt lịch tiện ích nội khu . |
| 4 | Vinhomes | **Pain từ người khác (Stakeholder Pain)** | Cư dân phàn nàn gay gắt về tình trạng xe vãng lai đỗ sai quy định chắn lối đi, trong khi lực lượng bảo vệ thực địa bị quá tải, không thể liên tục đi tuần tra xua đuổi. |
| 5 | Vinhomes | **Pain từ người khác (Stakeholder Pain)** | Cư dân bức xúc khi mất nước sinh hoạt do máy bơm gặp sự cố kỹ thuật mà hệ thống bảo trì định kỳ bằng tay không dự báo trước được. |





# ĐỀ XUẤT 3 BÀI TOÁN AI TRỌNG ĐIỂM TỐI ƯU VẬN HÀNH TẠI VINHOMES

---

## 1. Tự động hóa Phân loại và Điều phối Kỹ thuật (Smart Service Desk)

Tại các đại đô thị của **Vinhomes**, hệ thống tiếp nhận yêu cầu từ cư dân thường xuyên rơi vào trạng thái quá tải vào các khung giờ cao điểm khi hàng ngàn ticket báo hỏng điện, nước, hoặc hạ tầng được gửi lên App cùng lúc. 

* **Thực trạng và Nỗi đau (Actor: Nhân sự BQL & Kỹ thuật viên):** Hiện tại, quy trình vận hành hoàn toàn thủ công. Sau khi cư dân gửi ticket, nhân sự trực ca thuộc Ban quản lý (BQL) phải đọc từng nội dung, gắn tag phân loại loại sự cố, xác định tòa nhà và mức độ ưu tiên, rồi mới tạo lệnh điều phối trên hệ thống để giao việc cho kỹ thuật viên thực địa. Bước đọc hiểu và phân loại thủ công này đang là "nút thắt cổ chai", tiêu tốn trung bình tới **15 phút cho mỗi lượt xử lý** và rất dễ xảy ra sai sót như giao sai chuyên môn hoặc sai vị trí, khiến đội ngũ kỹ thuật viên thực địa gặp nhiều bất tiện.
* **Giải pháp AI đề xuất:** Áp dụng kiến trúc **AI Agent**. Hệ thống AI sẽ tự động phân tích văn bản và hình ảnh từ ticket của cư dân để trích xuất thông tin, tự động phân loại sự cố và áp dụng thuật toán tối ưu ràng buộc (Constraint Optimization) nhằm gán việc trực tiếp cho kỹ thuật viên gần nhất có kỹ năng phù hợp.
* **Mục tiêu đo lường (Metrics):** Cắt giảm thời gian định tuyến ticket từ 15 phút xuống **dưới 1 phút**; giảm tỷ lệ điều phối sai chuyên môn xuống **dưới 2%**, giúp tối ưu hóa tối đa giờ công của đội ngũ kỹ thuật thực địa.
* **Kiến trúc công nghệ đề xuất:** `[x] Agent`

---

## 2. Tự động soạn thảo câu phản hồi đồng cảm cho khiếu nại và đánh giá 1-star

Đối với mảng dịch vụ quản lý bất động sản cao cấp như **Vinhomes**, việc xoa dịu các khiếu nại gay gắt hoặc các đánh giá 1-star của cư dân trên App là nhiệm vụ cực kỳ quan trọng nhưng cũng đầy áp lực cho đội ngũ Chăm sóc khách hàng (CSKH).

* **Thực trạng và Nỗi đau (Actor: Nhân sự CSKH & Ban quản lý):** Quy trình hiện tại đòi hỏi nhân sự CSKH phải tra cứu lịch sử căn hộ để hiểu rõ ngữ cảnh, sau đó tự tay soạn thảo từng câu trả lời cá nhân hóa nhằm đảm bảo sự khéo léo và đồng cảm, tránh tối đa việc dùng các câu mẫu (template) rập khuôn gây ức chế thêm cho cư dân. Bản nháp này sau đó phải qua Trưởng bộ phận duyệt lại trước khi chính thức phản hồi. Toàn bộ quá trình soạn thảo này ngốn tới **12 phút cho mỗi trường hợp**, gây chậm trễ trong việc phản hồi và tạo áp lực lớn lên nhân sự khi có sự cố diện rộng xảy ra.
* **Giải pháp AI đề xuất:** Sử dụng công nghệ **LLM (Mô hình ngôn ngữ lớn)** đóng vai trò trợ lý đắc lực. Ngay khi nhận được phản ánh tiêu cực, LLM sẽ tự động phân tích nội dung khiếu nại kết hợp với dữ liệu lịch sử của căn hộ để tạo ra một bản nháp phản hồi tối ưu, mang văn phong đồng cảm và chuẩn mực thương hiệu của tập đoàn.
* **Mục tiêu đo lường (Metrics):** Rút ngắn thời gian soạn phản hồi từ 12 phút xuống **dưới 2 phút**; đạt tỷ lệ **trên 85%** bản nháp do AI tạo ra được duyệt ngay và gửi đi mà không cần chỉnh sửa lại.
* **Kiến trúc công nghệ đề xuất:** `[x] LLM`

---

## 3. Nâng cấp Chatbot hỗ trợ cư dân thành Trợ lý ảo AI thông minh

Hoạt động tương tác, giải đáp và cung cấp dịch vụ tiện ích cho cư dân tại **Vinhomes** hiện vẫn phụ thuộc rất nhiều vào yếu tố con người, dẫn đến việc khó tối ưu hiệu suất khi quy trình mang tính lặp lại cao.

* **Thực trạng và Nỗi đau (Actor: Cư dân & Lễ tân BQL):** Khi cư dân có nhu cầu tra cứu nội quy đô thị, tìm hiểu quy trình làm thẻ hoặc đặt lịch các tiện ích nội khu (như sân Tennis, khu nướng BBQ), họ phải chat hoặc gọi điện trực tiếp cho lễ tân hoặc tổng đài BQL. Nhân viên lễ tân sau đó phải tra cứu thủ công các file tài liệu, kiểm tra lịch trống trên hệ thống, giữ chỗ bằng tay rồi mới gửi tin nhắn xác nhận kèm hướng dẫn cho cư dân. Quy trình tương tác thủ công này mất trung bình **6 phút cho mỗi lượt**, khiến cư dân phải chờ đợi lâu và đội ngũ vận hành bị quá tải bởi các tác vụ lặp đi lặp lại.
* **Giải pháp AI đề xuất:** Nâng cấp toàn diện bằng giải pháp **AI Agent kết hợp công nghệ RAG (Retrieval-Augmented Generation)**. Trợ lý ảo mới không chỉ hiểu được ngôn ngữ tự nhiên của cư dân để tự tra cứu kho dữ liệu nội khu, mà còn có khả năng tự động gọi API kết nối với hệ thống backend của Vinhomes để giữ chỗ, đặt lịch và gửi xác nhận theo thời gian thực mà không cần con người can thiệp.
* **Mục tiêu đo lường (Metrics):** Nâng tỷ lệ tự động hóa giải quyết yêu cầu (Self-service rate) đạt **trên 70%**; cắt giảm thời gian đặt lịch tiện ích và giải đáp từ 6 phút xuống **dưới 30 giây** cho mỗi trải nghiệm của cư dân.
* **Kiến trúc công nghệ đề xuất:** `[x] Agent`