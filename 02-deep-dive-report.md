# 02 - Deep-Dive Report

## Thông Tin Nhóm

- Tên nhóm: Vin Smart Future Lab Team
- Thành viên: Vui lòng điền tên và MSSV của các thành viên trước khi nộp.

## Quyết Định Lựa Chọn

Nhóm chọn bài toán: **Xanh SM - Trợ lý điều phối sự cố xe điện sắp hết pin**.

Lý do chọn: bài toán có workflow rõ, xảy ra trong vận hành thời gian thực, có tác động trực tiếp đến thời gian chờ của tài xế và có ranh giới an toàn để kiểm thử bằng prompt prototype.

## 3.1 Current-State Workflow

```text
Tài xế báo sự cố pin
  -> Điều phối viên nhận cuộc gọi và ghi nhận biển số (2 phút) [handoff]
  -> Tra cứu vị trí GPS và dòng xe trên dashboard nội bộ (2 phút)
  -> Tra cứu trạm sạc VinFast còn trụ trống, phù hợp loại xe (5 phút) [bottleneck]
  -> Soạn tin nhắn hướng dẫn đường đi cho tài xế (5 phút) [bottleneck]
  -> Nếu pin quá thấp, liên hệ đội xe sạc pin di động/cứu hộ (1 phút) [handoff]
```

Tổng thời gian thủ công trung bình: **15 phút/lượt**.

## 3.2 Problem Statement 6-Field

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên trung tâm vận hành Xanh SM và tài xế xe điện đang gặp sự cố pin. |
| **2. Current Workflow** | Điều phối viên nhận cuộc gọi, tra cứu vị trí xe, kiểm tra trạm sạc còn trụ trống, soạn tin nhắn hướng dẫn và quyết định có cần gọi xe sạc pin di động hay không. |
| **3. Bottleneck** | Tra cứu trạm sạc phù hợp và soạn nội dung hướng dẫn mất 10-12 phút/lượt, dễ sai khi cao điểm hoặc khi dữ liệu vị trí không rõ. |
| **4. Business Impact** | Mỗi sự cố chậm xử lý làm tài xế mất thời gian chờ, giảm khả năng nhận cuốc và tăng rủi ro xe cạn pin giữa đường. Nếu có 60-80 sự cố/ngày, đội điều vận mất khoảng 15-20 giờ công/ngày. |
| **5. Success Metric** | Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút/lượt; 98% draft đúng ranh giới pin và khoảng cách; 100% tin nhắn gửi ra phải qua điều phối viên duyệt. |
| **6. Operational Boundary** | AI chỉ được tạo bản nháp có tag `[DRAFT_ONLY]` (nghĩa là "bản nháp chờ điều phối viên duyệt, chưa được gửi thật"). AI không được tự động gửi tin, không được xác nhận đã điều xe. Nếu pin < 5%, AI không được đề xuất trạm sạc xa hơn 5km và phải trả về action `dispatch_mobile_charger`. |

## 3.3 Future-State Flow & AI Fit

AI Fit: **LLM Feature + rule guardrail**.

```text
Tài xế báo sự cố
  -> Hệ thống lấy biển số, dòng xe, mức pin, GPS
  -> Rule guardrail kiểm tra pin < 5% và khoảng cách trạm sạc
  -> LLM draft nội dung hướng dẫn hoặc JSON dispatch_mobile_charger
  -> Điều phối viên review, sửa nếu cần và bấm gửi
  -> Log kết quả để đánh giá chất lượng draft
```

Human-in-the-loop: Điều phối viên bắt buộc review trước khi gửi cho tài xế.

Fallback: Nếu LLM lỗi, thiếu dữ liệu, output không bắt đầu bằng `[DRAFT_ONLY]` (nhãn bản nháp chờ duyệt), hoặc không parse được JSON trong tình huống critical, hệ thống chuyển sang quy trình thủ công hiện tại.

## Phase 4 - Prompt Prototype

File prototype đã được hoàn thiện tại `starter-code/prompt_prototype.py` với:

- System prompt yêu cầu mọi output bắt đầu bằng `[DRAFT_ONLY]` để nhấn mạnh đây chỉ là bản nháp, không phải tin nhắn đã gửi.
- Guardrail pin critical: pin < 5% và trạm sạc > 5km thì trả về `dispatch_mobile_charger`.
- Ba adversarial tests để thử tấn công bỏ tag draft, ép đề xuất trạm sạc xa khi pin 2%, và ép AI tự xác nhận đã gửi tin/điều xe khi chưa có điều phối viên duyệt.

## Phase 5 - Evaluate

### AI Readiness Checklist

| Câu hỏi | Đánh giá |
|---|---|
| Có đủ dữ liệu mẫu/logs sạch để test? | Có thể bắt đầu với log cuộc gọi, GPS, mức pin, trạm sạc và output mẫu của điều phối viên. |
| Rủi ro khi AI sai có nằm trong tầm kiểm soát? | Có, vì output chỉ là draft và bắt buộc có human approval. |
| Stakeholders sẵn sàng thay đổi workflow? | Khả thi, vì AI giảm thao tác tra cứu/soạn tin nhưng không thay quyền quyết định của điều phối viên. |

### Quyết Định

**GO - Bắt đầu xây dựng prototype scope hẹp.**

Justification: bài toán có đầu vào có cấu trúc, ranh giới an toàn đo được bằng rule, chi phí prototype thấp vì chỉ dùng LLM để draft nội dung và guardrail để chặn các tình huống nguy hiểm. Rủi ro vẫn được kiểm soát bằng human-in-the-loop và fallback thủ công.
