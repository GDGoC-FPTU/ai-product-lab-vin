# 03 - AI Log & Reflection

Trong bài lab này, tôi dùng AI như một thought-partner để chuyển một pain point vận hành ở Vinhomes thành bài toán AI có scope rõ: Smart Service Desk tự động phân loại và đề xuất điều phối kỹ thuật cho ticket cư dân. AI hỗ trợ brainstorm các bước workflow hiện tại, viết problem statement 6-field, xác định metric đo thành công và chuyển operational boundary thành test case có thể chạy trong Python.

Phần hữu ích nhất là AI giúp tôi nhìn ra rủi ro khi dùng agent tự động: nếu AI tự điều phối sai kỹ thuật viên, tự đóng ticket hoặc tự cam kết thời gian sửa chữa với cư dân, hệ thống có thể làm giảm niềm tin của cư dân và tạo rủi ro vận hành. AI cũng giúp nghĩ ra các prompt tấn công như ép bỏ tag `[DRAFT_ONLY]`, ép tự điều phối sự cố rò điện/cháy nổ, hoặc ép cam kết sửa xong trong 10 phút.

AI cũng có điểm sai. Ban đầu, AI đề xuất tự động hóa quá mạnh theo hướng agent tự route mọi ticket mà không cần Ban quản lý duyệt. Cách này không phù hợp với vận hành đô thị vì các sự cố như rò điện, ngập nước lớn, kẹt thang máy hoặc tranh chấp phí cần người chịu trách nhiệm kiểm tra trước khi hành động.

Tôi đã sửa bằng cách bổ sung ranh giới rõ ràng: mọi output phải bắt đầu bằng `[DRAFT_ONLY]`; AI chỉ được đề xuất category, priority, location, required skill và recommended action; AI không được tự đóng ticket, không được tự xác nhận đã điều phối và không được cam kết thời gian sửa chữa. Các ticket khẩn cấp hoặc nhạy cảm phải trả về `escalate_human_review`. Sau đó tôi thêm adversarial tests để kiểm tra các ranh giới này bằng code.
