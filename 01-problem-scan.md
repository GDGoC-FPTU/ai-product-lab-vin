# 01 - Problem Scan & Quick Cards

## Phase 1 - SCAN

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | Xanh SM | Tốn thời gian | Điều phối viên xử lý thủ công sự cố xe điện sắp hết pin, phải tra cứu vị trí xe, trạm sạc trống và soạn tin nhắn hướng dẫn cho tài xế. |
| 2 | Xanh SM | Lặp lại | Tổng hợp lý do hủy chuyến từ ghi chú tài xế và cuộc gọi khách hàng để tìm pattern gây rò rỉ cuốc. |
| 3 | VinFast | AI-upgrade | Trợ lý gợi ý trạm sạc phù hợp theo mức pin, dòng xe, loại cổng sạc và mật độ trạm sạc quanh vị trí hiện tại. |
| 4 | Vinhomes | Stakeholder Pain | Phân loại phản ánh cư dân trên app Vinhomes Resident đến đúng bộ phận xử lý, tránh chuyển nhầm ticket. |
| 5 | Vinmec | Tốn thời gian | Bác sĩ mất nhiều thời gian tóm tắt hồ sơ xuất viện từ bệnh án, xét nghiệm và ghi chú điều trị. |
| 6 | Vinpearl | AI-upgrade | Tự động đọc email đặt phòng đoàn, trích xuất ngày, số lượng phòng, nhu cầu ăn uống và draft yêu cầu kiểm tra phòng trống. |
git
## Phase 2 - QUICK-ASSESS

### Quick Problem Card #1

```text
BÀI TOÁN:
Điều phối viên Xanh SM xử lý sự cố xe điện sắp hết pin và cần hướng dẫn đến trạm sạc an toàn.

Công ty thành viên: Xanh SM
Actor: Điều phối viên trung tâm vận hành và tài xế Xanh SM.

Workflow thủ công hiện tại:
1. Tài xế gọi tổng đài báo sự cố pin.
2. Điều phối viên tra cứu biển số, dòng xe và vị trí GPS.
3. Điều phối viên mở dashboard trạm sạc VinFast để tìm trụ sạc trống gần nhất.
4. Điều phối viên soạn tin nhắn hướng dẫn và gửi cho tài xế.
5. Nếu pin quá thấp, điều phối viên liên hệ đội xe sạc pin di động/cứu hộ.

Bước tốn thời gian/lỗi nhất:
Bước 3-4, khoảng 10-12 phút/lượt, dễ sai khi cao điểm hoặc thông tin vị trí không rõ.

AI có thể hỗ trợ:
Tra cứu/nhận diện tình huống, soạn bản nháp hướng dẫn và cảnh báo nếu pin < 5%.

Metric:
Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút/lượt; 98% draft đúng ranh giới an toàn.

Quick Architecture: LLM Feature + rule guardrail
```

### Quick Problem Card #2

```text
BÀI TOÁN:
Tự động tổng hợp và phân loại lý do khách hàng hủy chuyến Xanh SM.

Công ty thành viên: Xanh SM
Actor: Nhân viên vận hành chất lượng dịch vụ.

Workflow thủ công hiện tại:
1. Lấy file ghi âm/ghi chú hủy chuyến.
2. Đọc hoặc nghe từng trường hợp.
3. Gắn nhãn lý do hủy chuyến.
4. Tổng hợp thành báo cáo theo khu vực/giờ cao điểm.

Bước tốn thời gian/lỗi nhất:
Bước 2-3, khoảng 5 phút/lượt, dễ gắn nhãn không nhất quán.

AI có thể hỗ trợ:
Tóm tắt nội dung và gắn nhãn lý do hủy chuyến theo taxonomy có sẵn.

Metric:
80% trường hợp được gắn nhãn trong dưới 30 giây; giảm thời gian báo cáo từ 4 giờ xuống dưới 45 phút/ngày.

Quick Architecture: LLM Feature
```

### Quick Problem Card #3

```text
BÀI TOÁN:
Phân loại phản ánh cư dân Vinhomes đến đúng bộ phận xử lý.

Công ty thành viên: Vinhomes
Actor: Nhân viên CSKH/Ban quản lý tòa nhà.

Workflow thủ công hiện tại:
1. Cư dân gửi phản ánh trên app.
2. CSKH đọc nội dung và xác định loại vấn đề.
3. CSKH chuyển ticket đến kỹ thuật, an ninh, vệ sinh hoặc kế toán.
4. Bộ phận nhận ticket phản hồi trạng thái.

Bước tốn thời gian/lỗi nhất:
Bước 2-3, khoảng 6-8 phút/ticket, dễ chuyển nhầm bộ phận khi nội dung mơ hồ.

AI có thể hỗ trợ:
Phân loại intent, trích xuất tòa/căn hộ/mức độ khẩn cấp, draft nội dung chuyển ticket.

Metric:
85% ticket được phân loại dưới 10 giây; giảm tỷ lệ chuyển nhầm từ 12% xuống dưới 3%.

Quick Architecture: Rule + LLM Feature
```
