# Lab 02 - Individual AI Log & Reflection

## 1. AI đã giúp tôi làm gì?

Trong buổi lab, tôi dùng AI như một thought-partner để mở rộng danh sách bài toán vận hành cho Vin Smart Future, đặc biệt ở các mảng Vinhomes, Vinmec và VinFast. AI giúp tôi nhìn bài toán theo 4 lens trong worksheet: tác vụ lặp lại, tác vụ tốn thời gian, dịch vụ có thể nâng cấp bằng AI và pain point từ stakeholder.

Sau khi có danh sách ban đầu, tôi dùng AI để stress-test từng quick card. Tôi yêu cầu AI đóng vai CFO và trưởng phòng vận hành khó tính để phản biện xem metric có đo được không, bottleneck có thật sự đáng dùng AI không, và rule-based system có thể xử lý tốt hơn LLM không. Cách này giúp tôi sửa bài toán Vinhomes từ ý tưởng "chatbot trả lời cư dân" thành scope hẹp hơn: "AI gợi ý phân loại và route ticket, nhân viên CSKH duyệt".

Tôi cũng dùng AI để hỗ trợ viết operational boundary cho prototype. Ví dụ, với bài toán có rủi ro cao như Vinmec, AI nhắc tôi phải có human-in-the-loop, không cho AI tự chẩn đoán, không tự thay đổi thuốc và không phát hành văn bản y tế nếu bác sĩ chưa duyệt. Với VinFast, AI giúp tôi nghĩ thêm các rule escalation cho dấu hiệu nguy hiểm như mất phanh, khói, mùi khét hoặc xe không vào số.

## 2. AI đã sai hoặc gây nhiễu như thế nào?

Điểm sai rõ nhất là AI ban đầu đưa ra một số con số nghe rất thuyết phục nhưng không có nguồn kiểm chứng, ví dụ số lượng ticket mỗi ngày, tỉ lệ route sai, hoặc chi phí thất thoát. Nếu đưa thẳng vào bài, các con số này dễ bị hiểu nhầm là dữ liệu thật của Vingroup. Tôi phải chuyển chúng thành ước tính scoping và chỉ dùng làm baseline giả định để thiết kế metric.

AI cũng có xu hướng đề xuất giải pháp quá lớn, ví dụ "multi-agent tự động xử lý toàn bộ khiếu nại cư dân" hoặc "agent tự gọi cứu hộ và xác nhận lịch sửa xe". Những đề xuất này vượt quá scope lab và tạo rủi ro vận hành. Với Vinhomes, AI từng gợi ý tự động gửi phản hồi cho cư dân về phí quản lý, nhưng đây là nội dung nhạy cảm vì có thể liên quan đến tranh chấp hoặc chính sách tòa nhà.

Một lỗi khác là AI đôi khi coi LLM là lựa chọn mặc định, trong khi một số bước nên dùng rule-based trước. Với VinFast, các tín hiệu nguy hiểm không nên chờ LLM suy luận mà cần rule cứng để escalation ngay. Điều này làm tôi nhận ra "AI fit" không có nghĩa là dùng LLM cho mọi bước.

## 3. Tôi đã sửa prompt và cách làm như thế nào?

Tôi sửa prompt theo hướng ép AI trả lời có cấu trúc và phải nêu ranh giới vận hành. Thay vì hỏi chung "hãy gợi ý giải pháp AI", tôi đổi thành:

```text
Hãy phân tích bài toán theo Actor, Current Workflow, Bottleneck, Business Impact,
Success Metric, Operational Boundary. Với mỗi giải pháp, so sánh Rule, LLM và Agent.
Nếu số liệu chỉ là ước tính, phải ghi rõ là giả định.
```

Khi stress-test, tôi thêm yêu cầu AI phản biện như người vận hành thực tế:

```text
Đóng vai CFO và Head of Operations. Chỉ ra 3 lý do bài toán này có thể chưa nên dùng AI,
3 metric cần đo trước khi build, và bước nào rule-based xử lý tốt hơn LLM.
```

Cuối cùng, tôi bổ sung các ranh giới bắt buộc vào prompt prototype: AI chỉ tạo draft, không tự gửi hoặc tự phê duyệt; các quyết định y tế, pháp lý, tài chính và an toàn xe phải có người duyệt; output nên là JSON để dễ kiểm tra bằng code. Việc sửa prompt như vậy làm câu trả lời bớt "ảo", dễ kiểm thử hơn và sát hơn với yêu cầu sản phẩm AI trong môi trường vận hành thật.
