# 04-workflow-diagram.md

## Vinhomes Resident Ticket Routing Flow

### 1. Problem Overview
- **Mảng:** Vinhomes đại đô thị
- **Bài toán:** Tiếp nhận ticket bảo trì điện/nước/hạ tầng quá tải vào giờ cao điểm
- **Actor:** Nhân sự trực ca Ban quản lý (BQL)
- **Nút thắt:** Đọc hiểu và phân loại thủ công ticket khiến quy trình chậm và sai sót
- **Mục tiêu:** Giảm thời gian định tuyến ticket từ 15 phút xuống dưới 1 phút và giảm tỷ lệ điều phối sai chuyên môn xuống dưới 2%

---

## 3.1. Current-State Workflow Mapping (25 min)

**Vẽ quy trình hiện tại lên giấy/whiteboard theo yêu cầu:**
- 🔴 **Bottleneck:** Bước gây tắc nghẽn, tốn thời gian, hoặc dễ sai.
- 🔄 **Handoff:** Điểm chuyển giao thông tin giữa người và hệ thống.
- **Tổng cộng = 15 phút/lượt**

```text
┌─────────────────────────────────────────────────┐
│  Bước 1: Cư dân gửi ticket lên App              │
│  (Digital form)                                 │
└─────────────────────────────────────────────────┘
                |
                v
┌─────────────────────────────────────────────────┐
│  Bước 2: Nhân sự BQL nhận ticket                │
│  🔄 Handoff: App -> Nhân sự                      │
└─────────────────────────────────────────────────┘
                |
                v
┌─────────────────────────────────────────────────┐
│  Bước 3: Nhân sự đọc nội dung text/hình ảnh      │
│  🔴 Bottleneck: đọc hiểu, xác định sự cố         │
└─────────────────────────────────────────────────┘
                |
                v
┌─────────────────────────────────────────────────┐
│  Bước 4: Nhân sự gắn tag phân loại sự cố         │
│  🔴 Bottleneck: phân loại thủ công               │
└─────────────────────────────────────────────────┘
                |
                v
┌─────────────────────────────────────────────────┐
│  Bước 5: Nhân sự xác định tòa nhà, vị trí,       │
│         mức độ ưu tiên                          │
│  🔴 Bottleneck: phân tích địa điểm và ưu tiên    │
└─────────────────────────────────────────────────┘
                |
                v
┌─────────────────────────────────────────────────┐
│  Bước 6: Nhân sự tạo lệnh điều phối trên hệ      │
│         thống                                   │
│  🔄 Handoff: Nhân sự -> Hệ thống điều phối       │
└─────────────────────────────────────────────────┘
                |
                v
┌─────────────────────────────────────────────────┐
│  Bước 7: Kỹ thuật viên thực địa nhận việc        │
│  🔄 Handoff: Hệ thống -> Kỹ thuật viên            │
└─────────────────────────────────────────────────┘
```

### Bottleneck và vấn đề
- **Bước 3-5** là nút thắt cổ chai chính.
- Mỗi ticket mất trung bình **15 phút** để xử lý.
- Dễ xảy ra sai sót: giao sai chuyên môn, sai vị trí, phân loại nhầm mức độ ưu tiên.
- Nhiều ticket dồn vào giờ cao điểm khiến BQL bị quá tải.

---

## 3. Future-State Workflow với AI Agent

```text
[1] Cư dân gửi ticket lên App
       |
       v
[2] Hệ thống AI Agent tiếp nhận ticket
       |
       v
[3] AI phân tích text/hình ảnh và trích xuất:
       - loại sự cố
       - vị trí tòa nhà/căn hộ
       - mức độ ưu tiên
       - yêu cầu chuyên môn
       |
       v
[4] AI áp dụng thuật toán tối ưu định tuyến:
       - chọn kỹ thuật viên gần nhất
       - đảm bảo kỹ năng phù hợp
       - cân bằng tải công việc
       |
       v
[5] AI tự động tạo lệnh điều phối và gửi đến kỹ thuật viên
       |
       v
[6] Nhân sự BQL kiểm tra, phê duyệt (HITL) nếu cần
       |
       v
[7] Kỹ thuật viên thực địa nhận việc và di chuyển
```

### Lý do chọn AI Agent
- **Tự động hóa end-to-end:** từ phân tích ticket đến gán việc.
- **Xử lý đa media:** text và hình ảnh có thể được hiểu bởi Agent.
- **Tối ưu định tuyến:** chọn người phù hợp nhất theo kỹ năng và vị trí.
- **Giảm sai sót:** định nghĩa rõ ràng ranh giới và phê duyệt khi không chắc chắn.

---

## 4. Human-in-the-Loop & Fallback

- **Human-in-the-loop:** Nhân sự BQL chỉ can thiệp khi AI tự tin thấp hoặc phát hiện ticket nghiêm trọng.
- **Fallback:** Khi AI không thể xác định chính xác chuyên môn hoặc vị trí, ticket được đưa về luồng kiểm duyệt thủ công của BQL.

---

## 5. Success Metrics
- Thời gian định tuyến ticket từ **15 phút xuống dưới 1 phút**.
- Tỷ lệ điều phối sai chuyên môn < **2%**.
- Giảm tải nhanh cho BQL vào giờ cao điểm.
- Tăng tốc độ phản hồi và độ chính xác phân loại ticket.
