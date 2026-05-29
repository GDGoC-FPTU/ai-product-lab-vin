# 01 - Problem Scan & Quick Cards

## Phase 1 - SCAN

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | Vinhomes | Stakeholder Pain | Tự động phân loại và điều phối ticket kỹ thuật từ cư dân đến đúng kỹ thuật viên theo loại sự cố, vị trí và mức độ ưu tiên. |
| 2 | Vinhomes | Tốn thời gian | Soạn phản hồi ban đầu cho cư dân về trạng thái tiếp nhận ticket và yêu cầu bổ sung thông tin còn thiếu. |
| 3 | Vinhomes | Lặp lại | Tổng hợp các ticket lặp lại theo tòa/khu vực để phát hiện điểm nóng về điện, nước, thang máy hoặc hạ tầng. |
| 4 | VinFast | AI-upgrade | Trợ lý gợi ý trạm sạc phù hợp theo mức pin, dòng xe, loại cổng sạc và mật độ trạm sạc quanh vị trí hiện tại. |
| 5 | Vinmec | Tốn thời gian | Bác sĩ mất nhiều thời gian tóm tắt hồ sơ xuất viện từ bệnh án, xét nghiệm và ghi chú điều trị. |
| 6 | Vinpearl | AI-upgrade | Tự động đọc email đặt phòng đoàn, trích xuất ngày, số lượng phòng, nhu cầu ăn uống và draft yêu cầu kiểm tra phòng trống. |

## Phase 2 - QUICK-ASSESS

### Quick Problem Card #1

```text
BÀI TOÁN:
Tự động hóa phân loại và điều phối kỹ thuật cho ticket cư dân Vinhomes.

Công ty thành viên: Vinhomes
Actor: Nhân sự trực ca Ban quản lý, kỹ thuật viên thực địa và cư dân.

Workflow thủ công hiện tại:
1. Cư dân gửi ticket kèm mô tả/hình ảnh trên App Vinhomes Resident.
2. Nhân sự BQL đọc nội dung và xác định loại sự cố.
3. BQL xác định tòa/căn hộ/khu vực và mức độ ưu tiên.
4. BQL tra danh sách kỹ thuật viên phù hợp theo chuyên môn/vị trí.
5. BQL tạo lệnh điều phối và gửi cho kỹ thuật viên.

Bước tốn thời gian/lỗi nhất:
Bước 2-4, khoảng 15 phút/ticket, dễ sai chuyên môn hoặc sai vị trí khi cao điểm.

AI có thể hỗ trợ:
AI Agent trích xuất thông tin từ text/hình ảnh, phân loại intent, xác định mức ưu tiên và đề xuất kỹ thuật viên phù hợp để BQL duyệt.

Metric:
Giảm thời gian định tuyến ticket từ 15 phút xuống dưới 1 phút; giảm tỷ lệ điều phối sai chuyên môn xuống dưới 2%.

Quick Architecture: Agentic Loop + rule guardrail + human-in-the-loop
```

### Quick Problem Card #2

```text
BÀI TOÁN:
Soạn phản hồi ban đầu cho cư dân Vinhomes sau khi ticket được tiếp nhận.

Công ty thành viên: Vinhomes
Actor: Nhân viên CSKH/Ban quản lý tòa nhà.

Workflow thủ công hiện tại:
1. Cư dân gửi phản ánh trên app.
2. CSKH đọc nội dung và kiểm tra thông tin còn thiếu.
3. CSKH soạn phản hồi xác nhận đã tiếp nhận hoặc yêu cầu bổ sung ảnh/vị trí.
4. CSKH gửi phản hồi và cập nhật trạng thái ticket.

Bước tốn thời gian/lỗi nhất:
Bước 2-3, khoảng 6-8 phút/ticket, dễ phản hồi rập khuôn hoặc thiếu thông tin cần hỏi.

AI có thể hỗ trợ:
LLM draft phản hồi ban đầu theo tone chuẩn Vinhomes, kèm danh sách thông tin cần bổ sung.

Metric:
85% phản hồi ban đầu được draft dưới 20 giây; giảm thời gian phản hồi từ 8 phút xuống dưới 1 phút.

Quick Architecture: LLM Feature + human approval
```

### Quick Problem Card #3

```text
BÀI TOÁN:
Phát hiện điểm nóng sự cố vận hành lặp lại tại các tòa/khu vực Vinhomes.

Công ty thành viên: Vinhomes
Actor: Trưởng ca vận hành và đội bảo trì hạ tầng.

Workflow thủ công hiện tại:
1. Xuất danh sách ticket theo ngày/tuần.
2. Nhân sự vận hành lọc ticket theo tòa, loại sự cố và thời gian.
3. Tổng hợp thủ công các cụm sự cố lặp lại.
4. Đề xuất kế hoạch kiểm tra bảo trì phòng ngừa.

Bước tốn thời gian/lỗi nhất:
Bước 2-3, khoảng 2-3 giờ/ngày, dễ bỏ sót pattern khi volume ticket lớn.

AI có thể hỗ trợ:
Tự động gom nhóm ticket tương đồng, phát hiện khu vực bất thường và draft báo cáo vận hành.

Metric:
Giảm thời gian tổng hợp báo cáo từ 3 giờ xuống dưới 30 phút; phát hiện ít nhất 80% cụm sự cố lặp lại trong ngày.

Quick Architecture: Rule + LLM Feature
```
