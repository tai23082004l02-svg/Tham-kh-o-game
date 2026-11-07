# Riêng tư và quyền sử dụng

Người dùng đã cho phép chatbot tự tham khảo: tải, giải nén, xuất ảnh/clip để
xem cục bộ, dựng preview và phân tích cấu trúc. Các bước này được thực hiện
chủ động, không cần hỏi lại người dùng. Xem START_HERE và GRAPHICS_WORKFLOW.

Phân tích do người dùng yêu cầu trên dump họ cung cấp. Việc cóAPK hoặc export
không cấp quyền dùng lại artwork, tên, câu chuyện, âm thanh hoặc source của nhà
phát triển. Kết quả dùng tham khảo cấu trúc và xây hệ thống/nội dung riêng.
Đây không phải giấy phép thay cho chủ sở hữu game.

Archive đã có trênrepo chứa game.sav, thư mục dữ liệu riêng và cấu hình/khóa công
cụ trên máy. Vì vậy bộ bàn giao không chép lại chúng, không đọc giá trị tài khoản,
không đưa raw dump.cs/stringliteral/dummyDLL lên để tránh lẫn constants nhạy cảm.
Không tự xóaarchive hoặc rewrite lịch sử người dùng trong lượt bàn giao này.

Nếu repo công khai: nên chuyểnPrivate; chỉ xóa tệp ởcommit mới không xóa lịch sử.
Nếu xác định credential/token còn hiệu lực bị công khai thì thu hồi/thay thế nó.
Không cần gửi lại save/shared_prefs để chatbot xây cơ chế giống thể loại.

Ví dụ trongexamples được tự viết cho bản thiết kế mới, không lấy tham số/bảng
truyện/hình gốc làm cấu hình sản xuất. Catalog chỉ chứa thông tin cấu trúc và
metadata nghiên cứu; liên kết archive gốc giữ ởASSET_MAP để chatbot chủ động
đối chiếu trên máy trong phạm vi tham khảo đã được người dùng cho phép.
