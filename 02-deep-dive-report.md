# 02 - Deep-Dive Report

## Thông Tin Nhóm

- Tên nhóm: Vin Smart Future Lab Team
- Thành viên: Luong Trung Duc - 2A202600704

## Quyết Định Lựa Chọn

Nhóm chọn bài toán: **Vinhomes - Smart Service Desk tự động phân loại và điều phối kỹ thuật**.

Lý do chọn: bài toán có workflow rõ, phát sinh thường xuyên trong vận hành đô thị quy mô lớn, ảnh hưởng trực tiếp đến SLA phản hồi cư dân và hiệu suất đội kỹ thuật. Đây là bài toán phù hợp để dùng AI Agent có human-in-the-loop vì cần đọc hiểu text/hình ảnh, phân loại intent, xác định vị trí và đề xuất điều phối đúng kỹ năng.

## 3.1 Current-State Workflow

```text
Cư dân gửi ticket qua App Vinhomes Resident
  -> Nhân sự BQL tiếp nhận ticket và mở nội dung mô tả/hình ảnh (2 phút) [handoff]
  -> Đọc hiểu sự cố, xác định loại vấn đề: điện/nước/thang máy/hạ tầng (5 phút) [bottleneck]
  -> Xác định tòa, tầng, căn hộ/khu vực và mức độ ưu tiên (3 phút) [bottleneck]
  -> Tra danh sách kỹ thuật viên phù hợp theo chuyên môn và vị trí (3 phút)
  -> Tạo lệnh điều phối và gửi cho kỹ thuật viên thực địa (2 phút) [handoff]
```

Tổng thời gian thủ công trung bình: **15 phút/ticket**.

## 3.2 Problem Statement 6-Field

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân sự trực ca Ban quản lý Vinhomes, kỹ thuật viên thực địa và cư dân gửi ticket báo sự cố qua App Vinhomes Resident. |
| **2. Current Workflow** | Cư dân gửi ticket kèm mô tả/hình ảnh; nhân sự BQL đọc nội dung, gắn tag loại sự cố, xác định tòa/căn hộ/khu vực, đánh giá mức độ ưu tiên, rồi tạo lệnh điều phối thủ công cho kỹ thuật viên phù hợp. |
| **3. Bottleneck** | Bước đọc hiểu, phân loại và định tuyến ticket thủ công mất trung bình 15 phút/lượt, dễ sai chuyên môn hoặc sai vị trí khi cao điểm có nhiều ticket báo hỏng điện, nước, thang máy hoặc hạ tầng cùng lúc. |
| **4. Business Impact** | Ticket bị xử lý chậm làm cư dân chờ lâu, giảm SLA phản hồi của BQL và gây lãng phí giờ công kỹ thuật viên do phải nhận việc sai chuyên môn/sai vị trí. Khi hàng ngàn ticket phát sinh trong khung giờ cao điểm, bottleneck phân loại có thể tạo backlog lớn và làm tăng khiếu nại cư dân. |
| **5. Success Metric** | Giảm thời gian định tuyến ticket từ 15 phút xuống dưới 1 phút/lượt; giảm tỷ lệ điều phối sai chuyên môn xuống dưới 2%; ít nhất 90% ticket thông thường được phân loại đúng intent và đúng khu vực ngay lần đầu. |
| **6. Operational Boundary** | AI Agent được phép trích xuất thông tin từ text/hình ảnh, đề xuất phân loại, mức ưu tiên và kỹ thuật viên phù hợp. AI không được tự đóng ticket, không được tự cam kết thời gian sửa chữa với cư dân, không được điều phối trực tiếp các sự cố khẩn cấp/nguy hiểm nếu chưa có nhân sự BQL duyệt. Các ticket liên quan đến an toàn điện, cháy nổ, ngập nước lớn, thang máy kẹt người hoặc tranh chấp phí phải chuyển ngay sang human-in-the-loop. |

## 3.3 Future-State Flow & AI Fit

AI Fit: **Agentic Loop có rule guardrail và human-in-the-loop**.

```text
Cư dân gửi ticket
  -> Hệ thống lấy text, ảnh, metadata căn hộ/tòa nhà
  -> Rule guardrail phát hiện nhóm khẩn cấp/nguy hiểm
  -> AI Agent trích xuất intent, vị trí, mức ưu tiên và kỹ năng cần thiết
  -> AI Agent đề xuất kỹ thuật viên gần nhất có kỹ năng phù hợp
  -> Nhân sự BQL review, chỉnh nếu cần và bấm duyệt điều phối
  -> Log kết quả để đo thời gian xử lý, tỷ lệ sửa và tỷ lệ điều phối sai
```

Human-in-the-loop: BQL bắt buộc duyệt trước khi ticket được điều phối chính thức, đặc biệt với sự cố khẩn cấp, an toàn cư dân hoặc tranh chấp phí.

Fallback: Nếu AI thiếu dữ liệu, confidence dưới 95%, không xác định được vị trí/chuyên môn, hoặc ticket thuộc nhóm nguy hiểm, hệ thống chuyển sang hàng đợi BQL xử lý thủ công.

## Phase 4 - Prompt Prototype

File prototype đã được hoàn thiện tại `starter-code/prompt_prototype.py` với:

- System prompt yêu cầu mọi output bắt đầu bằng `[DRAFT_ONLY]` để nhấn mạnh đây chỉ là đề xuất chờ BQL duyệt.
- Structured output gồm `category`, `priority`, `location`, `required_skill`, `recommended_action`, `human_review_required`, `reason`.
- Guardrail khẩn cấp: các ticket liên quan đến cháy nổ, rò điện, ngập nước lớn, thang máy kẹt người hoặc tranh chấp phí phải trả về action `escalate_human_review`.
- Ba adversarial tests để thử ép AI tự đóng ticket, tự cam kết thời gian sửa chữa và tự điều phối sự cố nguy hiểm không qua BQL.

## Phase 5 - Evaluate

### AI Readiness Checklist

| Câu hỏi | Đánh giá |
|---|---|
| Có đủ dữ liệu mẫu/logs sạch để test? | Có thể bắt đầu với lịch sử ticket từ App Vinhomes Resident, tag xử lý cũ, ảnh đính kèm và log điều phối kỹ thuật viên. |
| Rủi ro khi AI sai có nằm trong tầm kiểm soát? | Có, nếu output chỉ là đề xuất chờ BQL duyệt và các nhóm khẩn cấp luôn bị chuyển sang human-in-the-loop. |
| Stakeholders sẵn sàng thay đổi workflow? | Khả thi, vì AI giảm thao tác đọc/phân loại lặp lại nhưng vẫn giữ quyền quyết định cuối ở nhân sự BQL. |

### Quyết Định

**GO - Bắt đầu xây dựng prototype scope hẹp.**

Justification: bài toán có volume lớn, metric rõ, dữ liệu đầu vào có thể thu thập từ ticket log và tác động vận hành trực tiếp. Prototype nên bắt đầu với một nhóm sự cố hẹp như điện/nước/hạ tầng thông thường, dùng AI để đề xuất phân loại và kỹ thuật viên, nhưng vẫn bắt buộc BQL duyệt trước khi điều phối. Các tình huống nguy hiểm hoặc nhạy cảm được chặn bằng rule guardrail và fallback thủ công.
