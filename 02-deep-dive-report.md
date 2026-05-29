Dao Xuan Bach - 2A202600640
Tran Van Huynh - 2A202600805
LuongTrungDuc - 2A202600704
Phung Gia Bao - 2A202600579

# Lab 02 - Group Deliverable: Deep-Dive Report

## Quyết định lựa chọn

Nhóm chọn bài toán **Vinhomes - AI Agent hỗ trợ phân loại và điều phối ticket sự cố cư dân** để thực hiện deep-dive.

## 3.2. Problem Statement (6-field) & Metrics

| Field | Nội dung chi tiết |
|---|---|
| 1. Actor / Operator | Nhân sự trực ca Ban quản lý Vinhomes, kỹ thuật viên thực địa và cư dân gửi ticket báo sự cố qua App Vinhomes Resident. |
| 2. Current Workflow | Cư dân gửi ticket kèm mô tả/hình ảnh; nhân sự BQL đọc nội dung, gắn tag loại sự cố, xác định tòa/căn hộ/khu vực, đánh giá mức độ ưu tiên, rồi tạo lệnh điều phối thủ công cho kỹ thuật viên phù hợp. |
| 3. Bottleneck | Bước đọc hiểu, phân loại và định tuyến ticket thủ công mất trung bình 15 phút/lượt, dễ sai chuyên môn hoặc sai vị trí khi cao điểm có nhiều ticket báo hỏng điện, nước, thang máy hoặc hạ tầng cùng lúc. |
| 4. Business Impact | Ticket bị xử lý chậm làm cư dân chờ lâu, giảm SLA phản hồi của BQL và gây lãng phí giờ công kỹ thuật viên do phải nhận việc sai chuyên môn/sai vị trí. Khi hàng ngàn ticket phát sinh trong khung giờ cao điểm, bottleneck phân loại có thể tạo backlog lớn và làm tăng khiếu nại cư dân. |
| 5. Success Metric | Giảm thời gian định tuyến ticket từ 15 phút xuống dưới 1 phút/lượt; giảm tỷ lệ điều phối sai chuyên môn xuống dưới 2%; ít nhất 90% ticket thông thường được phân loại đúng intent và đúng khu vực ngay lần đầu. |
| 6. Operational Boundary | AI Agent được phép trích xuất thông tin từ text/hình ảnh, đề xuất phân loại, mức ưu tiên và kỹ thuật viên phù hợp. AI không được tự đóng ticket, không được tự cam kết thời gian sửa chữa với cư dân, không được điều phối trực tiếp các sự cố khẩn cấp/nguy hiểm nếu chưa có nhân sự BQL duyệt. Các ticket liên quan đến an toàn điện, cháy nổ, ngập nước lớn, thang máy kẹt người hoặc tranh chấp phí phải chuyển ngay sang human-in-the-loop. |

---

## Phase 5 - EVALUATE

### AI Readiness Checklist

1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test: log cuộc gọi sự cố pin, vị trí xe, trạng thái pin, danh sách trạm sạc và lịch sử điều phối.
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát: mọi tin nhắn gửi ra đều phải có tag `[DRAFT_ONLY]` và được điều phối viên duyệt trước khi gửi thật.
3. [x] Stakeholders sẵn sàng thay đổi quy trình: điều phối viên vẫn giữ quyền duyệt cuối cùng, AI chỉ giảm thời gian tra cứu và soạn draft.

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future

[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.

[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.

[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

### Justification

Dự án Tự động hóa Phân loại và Điều phối Kỹ thuật (Smart Service Desk) được đánh giá đạt mức độ **GO** vì bài toán cụ thể, có metric rõ ràng, giải pháp công nghệ đơn giản mà hiệu quả (LLM Feature), và ranh giới an toàn được kiểm soát chặt chẽ thông qua lập trình prompt.
