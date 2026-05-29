# Lab 02 — Worksheet: AI Product Scoping (Vin Smart Future)

## Bài toán nhóm chọn

**Vinhomes - Smart Service Desk tự động phân loại và điều phối kỹ thuật**

Tại các đại đô thị Vinhomes, hệ thống tiếp nhận yêu cầu từ cư dân thường quá tải vào giờ cao điểm khi nhiều ticket báo hỏng điện, nước, thang máy hoặc hạ tầng được gửi lên App cùng lúc. Nhóm chọn bài toán tự động đọc hiểu ticket, phân loại sự cố, xác định vị trí/mức ưu tiên và đề xuất kỹ thuật viên phù hợp để Ban quản lý duyệt.

---

## Phase 1 — SCAN

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | Vinhomes | Stakeholder Pain | Tự động phân loại và điều phối ticket kỹ thuật từ cư dân đến đúng kỹ thuật viên theo loại sự cố, vị trí và mức độ ưu tiên. |
| 2 | Vinhomes | Tốn thời gian | Soạn phản hồi ban đầu cho cư dân về trạng thái tiếp nhận ticket và yêu cầu bổ sung thông tin còn thiếu. |
| 3 | Vinhomes | Lặp lại | Tổng hợp các ticket lặp lại theo tòa/khu vực để phát hiện điểm nóng về điện, nước, thang máy hoặc hạ tầng. |
| 4 | VinFast | AI-upgrade | Trợ lý gợi ý trạm sạc phù hợp theo mức pin, dòng xe, loại cổng sạc và mật độ trạm sạc quanh vị trí hiện tại. |
| 5 | Vinmec | Tốn thời gian | Bác sĩ mất nhiều thời gian tóm tắt hồ sơ xuất viện từ bệnh án, xét nghiệm và ghi chú điều trị. |
| 6 | Vinpearl | AI-upgrade | Tự động đọc email đặt phòng đoàn, trích xuất ngày, số lượng phòng, nhu cầu ăn uống và draft yêu cầu kiểm tra phòng trống. |

---

## Phase 2 — QUICK-ASSESS

### Quick Problem Card #1

```text
Bài toán:
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
Bước 2-4, khoảng 15 phút/ticket.

AI có thể hỗ trợ:
AI Agent trích xuất thông tin từ text/hình ảnh, phân loại intent, xác định mức ưu tiên và đề xuất kỹ thuật viên phù hợp để BQL duyệt.

Metric:
Giảm thời gian định tuyến ticket từ 15 phút xuống dưới 1 phút; giảm tỷ lệ điều phối sai chuyên môn xuống dưới 2%.

Quick Architecture: Agentic Loop + rule guardrail + human-in-the-loop
```

### Quick Problem Card #2

```text
Bài toán:
Soạn phản hồi ban đầu cho cư dân Vinhomes sau khi ticket được tiếp nhận.

Công ty thành viên: Vinhomes
Actor: Nhân viên CSKH/Ban quản lý tòa nhà.

Workflow thủ công hiện tại:
1. Cư dân gửi phản ánh trên app.
2. CSKH đọc nội dung và kiểm tra thông tin còn thiếu.
3. CSKH soạn phản hồi xác nhận đã tiếp nhận hoặc yêu cầu bổ sung ảnh/vị trí.
4. CSKH gửi phản hồi và cập nhật trạng thái ticket.

Bước tốn thời gian/lỗi nhất:
Bước 2-3, khoảng 6-8 phút/ticket.

AI có thể hỗ trợ:
LLM draft phản hồi ban đầu theo tone chuẩn Vinhomes, kèm danh sách thông tin cần bổ sung.

Metric:
85% phản hồi ban đầu được draft dưới 20 giây; giảm thời gian phản hồi từ 8 phút xuống dưới 1 phút.

Quick Architecture: LLM Feature + human approval
```

### Quick Problem Card #3

```text
Bài toán:
Phát hiện điểm nóng sự cố vận hành lặp lại tại các tòa/khu vực Vinhomes.

Công ty thành viên: Vinhomes
Actor: Trưởng ca vận hành và đội bảo trì hạ tầng.

Workflow thủ công hiện tại:
1. Xuất danh sách ticket theo ngày/tuần.
2. Nhân sự vận hành lọc ticket theo tòa, loại sự cố và thời gian.
3. Tổng hợp thủ công các cụm sự cố lặp lại.
4. Đề xuất kế hoạch kiểm tra bảo trì phòng ngừa.

Bước tốn thời gian/lỗi nhất:
Bước 2-3, khoảng 2-3 giờ/ngày.

AI có thể hỗ trợ:
Tự động gom nhóm ticket tương đồng, phát hiện khu vực bất thường và draft báo cáo vận hành.

Metric:
Giảm thời gian tổng hợp báo cáo từ 3 giờ xuống dưới 30 phút; phát hiện ít nhất 80% cụm sự cố lặp lại trong ngày.

Quick Architecture: Rule + LLM Feature
```

---

## Phase 3 — DEEP-DIVE

### 3.1 Current-State Workflow Mapping

```text
Cư dân gửi ticket qua App Vinhomes Resident
  -> Nhân sự BQL tiếp nhận ticket và mở nội dung mô tả/hình ảnh (2 phút) [handoff]
  -> Đọc hiểu sự cố, xác định loại vấn đề: điện/nước/thang máy/hạ tầng (5 phút) [bottleneck]
  -> Xác định tòa, tầng, căn hộ/khu vực và mức độ ưu tiên (3 phút) [bottleneck]
  -> Tra danh sách kỹ thuật viên phù hợp theo chuyên môn và vị trí (3 phút)
  -> Tạo lệnh điều phối và gửi cho kỹ thuật viên thực địa (2 phút) [handoff]
```

Tổng thời gian thủ công trung bình: **15 phút/ticket**.

### 3.2 Problem Statement 6-Field

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân sự trực ca Ban quản lý Vinhomes, kỹ thuật viên thực địa và cư dân gửi ticket báo sự cố qua App Vinhomes Resident. |
| **2. Current Workflow** | Cư dân gửi ticket kèm mô tả/hình ảnh; nhân sự BQL đọc nội dung, gắn tag loại sự cố, xác định tòa/căn hộ/khu vực, đánh giá mức độ ưu tiên, rồi tạo lệnh điều phối thủ công cho kỹ thuật viên phù hợp. |
| **3. Bottleneck** | Bước đọc hiểu, phân loại và định tuyến ticket thủ công mất trung bình 15 phút/lượt, dễ sai chuyên môn hoặc sai vị trí khi cao điểm. |
| **4. Business Impact** | Ticket bị xử lý chậm làm cư dân chờ lâu, giảm SLA phản hồi của BQL và gây lãng phí giờ công kỹ thuật viên do phải nhận việc sai chuyên môn/sai vị trí. |
| **5. Success Metric** | Giảm thời gian định tuyến ticket từ 15 phút xuống dưới 1 phút/lượt; giảm tỷ lệ điều phối sai chuyên môn xuống dưới 2%; ít nhất 90% ticket thông thường được phân loại đúng intent và đúng khu vực ngay lần đầu. |
| **6. Operational Boundary** | AI Agent được phép đề xuất phân loại, mức ưu tiên và kỹ thuật viên phù hợp. AI không được tự đóng ticket, không được tự cam kết thời gian sửa chữa với cư dân và không được điều phối trực tiếp các sự cố khẩn cấp/nguy hiểm nếu chưa có BQL duyệt. |

### 3.3 Future-State Flow & AI Fit

AI Fit: **Agentic Loop có rule guardrail và human-in-the-loop**.

```text
Cư dân gửi ticket
  -> Hệ thống lấy text, ảnh, metadata căn hộ/tòa nhà
  -> Rule guardrail phát hiện nhóm khẩn cấp/nguy hiểm
  -> AI Agent trích xuất intent, vị trí, mức ưu tiên và kỹ năng cần thiết
  -> AI Agent đề xuất kỹ thuật viên gần nhất có kỹ năng phù hợp
  -> BQL review, chỉnh nếu cần và bấm duyệt điều phối
  -> Log kết quả để đo thời gian xử lý và tỷ lệ điều phối sai
```

Fallback: Nếu AI thiếu dữ liệu, confidence dưới 95%, không xác định được vị trí/chuyên môn, hoặc ticket thuộc nhóm nguy hiểm, hệ thống chuyển sang hàng đợi BQL xử lý thủ công.

---

## Phase 4 — TECHNICAL PROMPT PROTOTYPE

File `starter-code/prompt_prototype.py` được đổi sang use case Vinhomes Smart Service Desk với:

- System prompt yêu cầu output bắt đầu bằng `[DRAFT_ONLY]`.
- Structured JSON output gồm category, priority, location, required_skill, recommended_action, human_review_required và reason.
- 3 adversarial tests để kiểm tra ranh giới: không tự điều phối sự cố nguy hiểm, không bỏ tag draft, không tự đóng ticket/cam kết thời gian sửa.

---

## Phase 5 — EVALUATE

### AI Readiness Checklist

1. [x] Có dữ liệu mẫu/logs sạch để test: ticket lịch sử, tag xử lý, ảnh đính kèm, log điều phối.
2. [x] Rủi ro khi AI sai nằm trong tầm kiểm soát: output chỉ là đề xuất chờ BQL duyệt.
3. [x] Stakeholders sẵn sàng thay đổi workflow: AI giảm đọc/phân loại lặp lại nhưng không thay quyền quyết định của BQL.

### Quyết định

[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu với scope hẹp cho ticket điện/nước/hạ tầng thông thường.

Justification: bài toán có volume lớn, dữ liệu đầu vào rõ và metric đo được. Rủi ro được kiểm soát bằng human-in-the-loop, rule guardrail và fallback thủ công cho sự cố khẩn cấp hoặc nhạy cảm.

---

## Phase 6 — REFLECTION

Reflection cá nhân được ghi tại `03-ai-log.md`.
