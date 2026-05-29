# 03-ai-log.md

## AI Log & Reflection

### 1. AI đã giúp gì?
Hôm nay tôi đã dùng AI để:
- Brainstorm các bài toán vận hành trong Vingroup và chọn ra bài toán phù hợp cho Vinhomes.
- Soạn thảo nội dung cho file report, bao gồm Problem Statement, Future-State Flow và Success Metrics.
- Tạo sơ đồ quy trình hiện tại và phân tích bottleneck để đề xuất kiến trúc AI Agent.

### 2. AI đã sai gì?
Một điểm AI có thể sai là khi tự động phân loại ticket, nó dễ bị nhầm lẫn nếu nội dung cư dân gửi không đầy đủ hoặc có nhiều lỗi chính tả. Nếu AI chỉ dựa vào text, nó có thể gán sai chuyên môn hoặc sai tòa nhà, nên cần có cơ chế human review và fallback cho các ticket không chắc chắn.

### 3. Tôi đã sửa đổi ra sao?
Tôi đã xác định rõ ranh giới: AI chỉ thực hiện gợi ý phân loại và định tuyến, không được tự động xử lý khi thông tin thiếu. Tôi thêm điều kiện human-in-the-loop để BQL kiểm duyệt các ticket có mức độ tin cậy thấp, và đề xuất fallback đưa ticket về xử lý manual nếu AI không thể xác định. Điều này giúp giảm nguy cơ sai sót và tăng tính an toàn cho hệ thống.

### 4. Lesson learned
AI là công cụ hỗ trợ mạnh nhưng không phải thay thế hoàn toàn con người trong trường hợp dữ liệu không đầy đủ. Sự kết hợp giữa automation và kiểm duyệt thủ công giúp vừa tiết kiệm thời gian vừa đảm bảo độ chính xác cho vận hành bảo trì tòa nhà.
