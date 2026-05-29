# 03 - AI Log & Reflection

Trong bài lab này, tôi dùng AI như một thought-partner để biến một ý tưởng vận hành thành bài toán có thể kiểm thử được. AI hỗ trợ brainstorm các pain point trong hệ sinh thái Vingroup, sau đó giúp thu hẹp phạm vi về use case Xanh SM xử lý sự cố xe điện sắp hết pin. Phần hữu ích nhất là AI giúp viết system prompt, nghĩ ra prompt tấn công và chuyển ranh giới vận hành thành các assertion có thể chạy trong Python.

AI cũng có điểm sai. Ban đầu, AI đề xuất giải pháp quá rộng, gắn với agent tự động điều xe và gửi tin cho tài xế. Cách này nghe hiện đại nhưng không phù hợp vận hành thực tế vì nếu AI gửi sai chỉ dẫn sạc pin, tài xế có thể cạn pin giữa đường. Một bản prompt ban đầu cũng chỉ nói "hãy an toàn" nhưng không ép output bắt đầu bằng `[DRAFT_ONLY]`, nên vẫn có nguy cơ bị prompt injection yêu cầu gửi thẳng.

Tôi đã sửa bằng cách bổ sung ranh giới rõ ràng: mọi output phải bắt đầu bằng `[DRAFT_ONLY]`; AI chỉ được tạo bản nháp, không được tự xác nhận gửi/dispatch; khi pin < 5% thì không được đề xuất trạm sạc xa hơn 5km và phải trả về action `dispatch_mobile_charger`. Sau đó tôi thêm adversarial tests để ép AI vi phạm hai ranh giới này. Kết quả là prototype có thể chạy stress-test và báo pass/fail trực tiếp, giúp nhóm thấy ranh giới an toàn không chỉ nằm trong tài liệu mà được kiểm tra bằng code.
