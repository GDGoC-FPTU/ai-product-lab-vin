# 01-problem-scan.md

## 1. Scan & Quick Cards (Cá nhân)

### 1.1. List bài toán đã quét (Scan)
| # | Công ty thành viên | Lens | Mô tả ngắn bài toán |
|---|--------------------|------|---------------------|
| 1 | VinFast | Time-consuming | Nhân viên kiểm thử khối lượng dữ liệu sau sản xuất phải đối chiếu hàng trăm báo cáo chất lượng và lập biên bản sai sót bằng tay. |
| 2 | Xanh SM | Repetitive | Điều phối viên Xanh SM thường xuyên phải kiểm tra, phân loại và chỉnh sửa thủ công các đề nghị hủy/chuyển chuyến của tài xế. |
| 3 | Vinhomes | Stakeholder Pain | Bộ phận CSKH Vinhomes mất nhiều thời gian trả lời phản hồi của cư dân về báo hỏng thiết bị và yêu cầu bảo trì. |
| 4 | Vinmec | AI-upgrade | Bác sĩ và y tá phải đọc hàng loạt hồ sơ khám bệnh để gợi ý chẩn đoán sơ bộ, trong khi thông tin bệnh án thường ở nhiều định dạng khác nhau. |
| 5 | Vinpearl | Time-consuming | Nhân viên du lịch tại Vinpearl phải đối soát thủ công lịch đặt phòng, tour và yêu cầu thay đổi để cập nhật tồn kho trong hệ thống. |

---

### 1.2. Quick Problem Card #1

**Bài toán (1 câu):** Tự động hóa phân loại và phản hồi nhanh các phản ánh bảo trì của cư dân Vinhomes.

**Công ty thành viên:** [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  [ ] Vinmec  [ ] Khác (Ghi rõ) ______

**Ai đang đau (Actor)?**
Nhân viên CSKH/tổ vận hành tòa nhà tại Vinhomes.

**Workflow thủ công hiện tại (3-5 bước):**
1. Cư dân gửi ticket hoặc phản hồi về sự cố bảo trì.
2. Nhân viên đọc nội dung, phân loại loại sự cố và mức độ khẩn cấp.
3. Gõ thủ công phản hồi ban đầu hoặc chuyển cho bộ phận kỹ thuật.
4. Theo dõi trạng thái và cập nhật lại cho cư dân.

**Bước nào tốn thời gian/lỗi nhất?**
Bước 2: đọc và phân loại ticket thủ công (⏱ 8-12 phút/lượt).

**AI có thể nhảy vào hỗ trợ ở bước nào?**
Bước 2 và 3: AI tự động phân loại sự cố, đánh giá khẩn cấp, và đề xuất phản hồi chuẩn.

**Đo thành công bằng gì (Metric có số)?**
Giảm thời gian xử lý ban đầu từ 10 phút xuống còn dưới 2 phút; ít nhất 80% ticket được phân loại đúng ngay lần đầu.

**Quick Architecture:** [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent

---

### 1.3. Quick Problem Card #2

**Bài toán (1 câu):** Giảm tải thao tác thủ công cho điều phối viên Xanh SM khi xử lý yêu cầu thay đổi và hủy chuyến.

**Công ty thành viên:** [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Khác (Ghi rõ) ______

**Ai đang đau (Actor)?**
Điều phối viên và nhân viên hỗ trợ chuyến của Xanh SM.

**Workflow thủ công hiện tại (3-5 bước):**
1. Tài xế hoặc khách hàng gửi yêu cầu hủy/chuyển chuyến.
2. Điều phối viên mở ticket, đọc nội dung và kiểm tra lịch trình.
3. Nhập tay dữ liệu mới vào hệ thống và tính toán lại quãng đường.
4. Gửi xác nhận / phản hồi cho tài xế hoặc khách.

**Bước nào tốn thời gian/lỗi nhất?**
Bước 2 và 3: đọc yêu cầu phi cấu trúc và cập nhật manual trong hệ thống (⏱ 7-10 phút/lượt).

**AI có thể nhảy vào hỗ trợ ở bước nào?**
Bước 2: phân tích intent và chỉnh sửa văn bản yêu cầu; bước 3: gợi ý phương án chuyển tour và cập nhật trạng thái.

**Đo thành công bằng gì (Metric có số)?**
Giảm thời gian xử lý mỗi yêu cầu từ 9 phút xuống dưới 3 phút; đạt ít nhất 90% phản hồi tự động chính xác.

**Quick Architecture:** [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent

---

### 1.4. Quick Problem Card #3

**Bài toán (1 câu):** Hỗ trợ tự động tổng hợp và kiểm thử báo cáo chất lượng tại VinFast để giảm sai sót nhập dữ liệu.

**Công ty thành viên:** [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Khác (Ghi rõ) ______

**Ai đang đau (Actor)?**
Kỹ sư QC và chuyên viên kiểm thử chất lượng tại VinFast.

**Workflow thủ công hiện tại (3-5 bước):**
1. Nhận báo cáo kiểm thử, thông số kỹ thuật và lỗi phát hiện.
2. Đối chiếu từng bản ghi với tiêu chuẩn kỹ thuật và đưa ra trạng thái OK/NG.
3. Ghi nhận kết quả vào báo cáo tổng hợp.
4. Gửi lại cho bộ phận sản xuất hoặc quản lý.

**Bước nào tốn thời gian/lỗi nhất?**
Bước 2: đối chiếu hàng loạt dữ liệu kỹ thuật và đánh giá thủ công (⏱ 12-15 phút/lượt).

**AI có thể nhảy vào hỗ trợ ở bước nào?**
Bước 2: AI đọc dữ liệu, so khớp với tiêu chuẩn và gợi ý trạng thái cũng như lý do lỗi.

**Đo thành công bằng gì (Metric có số)?**
Giảm thời gian đối chiếu từ 15 phút xuống 4 phút; giảm lỗi nhập báo cáo xuống dưới 5%.

**Quick Architecture:** [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent

---

## 1.5. Tổng kết

Trong 5 bài toán đã quét, tôi ưu tiên chọn các vấn đề có: 1) lượng dữ liệu văn bản lớn, 2) thao tác thủ công dễ lặp lại, và 3) lợi ích rõ ràng khi dùng AI để phân loại/sinh phản hồi nhanh. Ba thẻ bài trên tập trung vào Vinhomes, Xanh SM và VinFast, phù hợp với mục tiêu cá nhân lấy điểm `Scan & Cards` và bước đầu định hướng prototype AI.
