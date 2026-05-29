# Lab 02 - Individual Deliverable: Problem Scan & Quick Cards

## Phase 1 - SCAN: List bài toán của tôi

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Vinmec | Tốn thời gian | Bác sĩ và điều dưỡng mất 20-30 phút để tổng hợp hồ sơ xuất viện từ bệnh án, kết quả xét nghiệm, đơn thuốc và ghi chú điều trị. |
| 2 | Vinmec | Stakeholder Pain | Bệnh nhân mô tả triệu chứng qua hotline/app nhưng nhân viên tổng đài phải hỏi lại nhiều lần để chọn đúng chuyên khoa và mức độ ưu tiên. |
| 3 | Vinmec | Lặp lại | Nhân viên quầy tiếp nhận kiểm tra thủ công giấy tờ bảo hiểm, thông tin đặt lịch, mã bệnh nhân và hồ sơ cần bổ sung trước khi khám. |
| 4 | Vinmec | AI-upgrade | Chatbot CSKH hiện trả lời lịch khám, hướng dẫn chuẩn bị xét nghiệm và chính sách viện phí còn rập khuôn, khó xử lý câu hỏi tiếng Việt tự nhiên. |
| 5 | Vinmec | Tốn thời gian | Điều dưỡng phải đọc ghi chú sau khám để soạn tin nhắn nhắc uống thuốc, tái khám và chuẩn bị xét nghiệm cho từng bệnh nhân. |
| 6 | Vinmec | Lặp lại | Bộ phận quản lý chất lượng phải đọc phản hồi bệnh nhân sau khám để phân loại phàn nàn về chờ đợi, thái độ phục vụ, chi phí hoặc cơ sở vật chất. |

---

## Phase 2 - QUICK-ASSESS: 3 Quick Problem Cards

### QUICK PROBLEM CARD #1

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tạo bản nháp tóm tắt xuất viện Vinmec từ  │
│ bệnh án điện tử, kết quả xét nghiệm và ghi chú điều trị.    │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị, điều dưỡng hành chính │
│ và bệnh nhân chờ giấy xuất viện.                            │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Bác sĩ mở bệnh án điện tử                              │
│   ──> 2. Đọc diễn biến điều trị và kết quả xét nghiệm       │
│   ──> 3. Tổng hợp chẩn đoán, thuốc, dặn dò tái khám         │
│   ──> 4. Viết bản tóm tắt xuất viện                         │
│   ──> 5. Bác sĩ kiểm tra và ký                              │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-4                   │
│ (⏱ 20-30 phút/bệnh nhân, dễ thiếu thông tin dặn dò)         │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4: trích xuất │
│ thông tin chính và tạo bản nháp theo template Vinmec.       │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian soạn bản nháp từ 25 phút xuống dưới 7 phút; │
│ 100% bản nháp phải được bác sĩ duyệt trước khi phát hành.   │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

**Nhận xét nhanh:** Giá trị vận hành cao nhưng rủi ro y tế lớn. AI không được đưa ra chẩn đoán mới, không tự thay đổi đơn thuốc và không phát hành giấy xuất viện nếu chưa có bác sĩ xác nhận.

### QUICK PROBLEM CARD #2

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Phân loại triệu chứng ban đầu để gợi ý    │
│ đúng chuyên khoa và mức độ ưu tiên lịch hẹn Vinmec.         │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên tổng đài đặt lịch, điều phối │
│ phòng khám và bệnh nhân chưa biết nên khám chuyên khoa nào. │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Bệnh nhân gọi hotline/nhắn app mô tả triệu chứng       │
│   ──> 2. Tổng đài viên hỏi thêm tuổi, thời gian, mức đau    │
│   ──> 3. Tra cứu bảng chuyên khoa và slot lịch còn trống    │
│   ──> 4. Chọn chuyên khoa, bác sĩ hoặc gói khám phù hợp     │
│   ──> 5. Gửi hướng dẫn chuẩn bị trước khám                  │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-4                   │
│ (⏱ 10-15 phút/lượt, dễ chọn sai chuyên khoa khi triệu chứng│
│ chồng chéo như đau ngực, khó thở, đau bụng)                 │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4: tóm tắt    │
│ triệu chứng, hỏi thông tin thiếu, gợi ý chuyên khoa.        │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ 85% lịch hẹn được gợi ý đúng chuyên khoa trong dưới 2 phút;│
│ 100% ca có dấu hiệu khẩn cấp được chuyển nhân viên y tế.    │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

**Nhận xét nhanh:** Bài toán cần kết hợp rule khẩn cấp với LLM. AI chỉ được gợi ý chuyên khoa và câu hỏi bổ sung, không được chẩn đoán bệnh hoặc cam kết phác đồ điều trị.

### QUICK PROBLEM CARD #3

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Kiểm tra hồ sơ bảo hiểm và giấy tờ cần bổ │
│ sung trước khi bệnh nhân đến khám tại Vinmec.               │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên tiếp nhận, bộ phận bảo hiểm  │
│ và bệnh nhân phải chờ bổ sung giấy tờ tại quầy.             │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Bệnh nhân đặt lịch và tải ảnh thẻ bảo hiểm/giấy tờ     │
│   ──> 2. Nhân viên mở từng ảnh để kiểm tra thông tin        │
│   ──> 3. Đối chiếu quyền lợi, thời hạn, giấy chuyển tuyến   │
│   ──> 4. Gọi/nhắn bệnh nhân nếu thiếu hồ sơ                 │
│   ──> 5. Xác nhận trạng thái sẵn sàng tiếp nhận             │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-4                   │
│ (⏱ 8-12 phút/hồ sơ, dễ bỏ sót giấy chuyển tuyến hoặc ảnh mờ)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4: OCR thông  │
│ tin, checklist hồ sơ thiếu và draft tin nhắn nhắc bổ sung.  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian kiểm tra từ 10 phút xuống dưới 3 phút/hồ sơ;│
│ giảm 50% lượt bệnh nhân phải bổ sung giấy tờ tại quầy.      │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

**Nhận xét nhanh:** Rule-based checklist phù hợp để kiểm điều kiện bảo hiểm cố định, còn LLM/OCR hỗ trợ đọc ảnh giấy tờ và soạn tin nhắn dễ hiểu. Nhân viên vẫn phải duyệt trước khi xác nhận quyền lợi bảo hiểm.

---

## Lựa chọn ưu tiên của cá nhân

Nếu phải chọn một bài toán để nhóm deep-dive, tôi ưu tiên **Card #1: Tạo bản nháp tóm tắt xuất viện Vinmec** vì:

1. Đây là tác vụ tốn nhiều thời gian lặp lại hằng ngày và có tác động trực tiếp đến năng suất bác sĩ.
2. Dữ liệu đầu vào chủ yếu là bệnh án, xét nghiệm, đơn thuốc và ghi chú có cấu trúc bán phần, phù hợp để LLM trích xuất và tóm tắt.
3. Metric dễ đo: thời gian tạo bản nháp, tỉ lệ bản nháp cần sửa nhiều, tỉ lệ thiếu thông tin dặn dò.
4. Rủi ro có thể kiểm soát bằng operational boundary rõ ràng: AI chỉ tạo draft, bác sĩ bắt buộc duyệt và ký trước khi phát hành.
