# Mẫu thiết kế mới, không phải game gốc

`original_game_config.json` tự đặt thông số vàID để minh họa mô hình mới.
Không phải các bảng đã giải mã của Eternal Senia 2, không có asset của họ.
Đường dẫn hình là placeholder cho artwork riêng, chưa có PNG tương ứng.

Chạy từ root: `python3 research/eternal-senia-2/examples/validate_and_simulate.py`.
Không cần thư viện ngoài. Chương trình kiểm liên kết catalogue, chạy trận mẫu
ởx1/x2/x3 bằngstep60Hz, kiểm timeline marker và rewardtoken chống nhận đôi.
Không tạo save người chơi hoặc gọi mạng. Đây là executable specification nhỏ,
không thay thế project Godot, animationplayer, inventory hay saveatomic thật.

Dùngschema này để bắt đầu viết module Godot theo BUILD_BLUEPRINT, rồi thay số
bằng cân bằng của dự án mới. Không thêm assist/skill trong mô phỏng nếu chưa
nối thật: bản mô phỏng hiện chỉ có hero đánh thường, chuỗiđịch và reward.
