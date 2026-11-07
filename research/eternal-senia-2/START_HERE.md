# Đọc đầu tiên — dành cho chatbot tiếp theo

## Mục tiêu và phạm vi
Người dùng muốn xây một game tương tự Eternal Senia 2 cho dễ triển khai, tham
khảo cách tổ chức tài nguyên, hoạt ảnh, tiến trình và vòng chơi. Nghiên cứu tĩnh
đã được thực hiện; dùng kết quả ở đây trước khi tải lại archive hoặc chạy tool.

Hai game trong repo khác nhau: `apk-extracted/com.superplanet.swordmaster_2.0.0`
là Sword Master Story cũ; phần nghiên cứu này chỉ là `com.sanctumstudio.eternalsenia2`.
Không gán kết luận của Eternal Senia 2 sang Sword Master Story.

## Đọc nhanh theo thứ tự
1. EVIDENCE: giới hạn hiểu biết và dẫn chứng.
2. ARCHITECTURE + DATA_MODEL: cấu trúc, bảng và mô hình người chơi.
3. ANIMATION: ba clip thật, khác biệt frame/Spine và gốc gây lệch hình.
4. BUILD_BLUEPRINT: bản thiết kế độc lập và tiêu chí hoàn thành từng mốc.
5. Chỉ mở các catalog liên quan; không đưa toàn bộ catalog vào context cùng lúc.

## Tra cứu không tốn context
Từ root repo:
```sh
python3 tools/query_reference.py table skill
python3 tools/query_reference.py class BattleScene
python3 tools/query_reference.py sprite senia_run_ --limit 5
python3 tools/query_reference.py clip anim_senia_run
python3 tools/query_reference.py textasset offline_reward
python3 tools/query_reference.py asset boss --limit 10
```
Kết quả có giới hạn để tránh nạp cả danh mục vào context. `clip` chỉ tìm trong
ba clip đã phân tích sâu; dùng `asset` để tìm tên các clip khác.

## Những việc đã xong, không cần làm lại
- Tải đủ 3 part; giải nén, đọc cấu trúc APK base và split arm64.
- Xác nhận Unity chủ đạo2022.3.62f2, IL2CPP metadata31.
- Quét các loại object bằng UnityPy1.25.4; lập chỉ mục sprite, script, TextAsset.
- Đọc được46JSON, tạo schema mỗi field, giữ số dòng và kiểu biểu diễn.
- Đọc khai báo IL2CPP bằng Il2CppDumper6.7.46; map33lớp cốt lõi.
- Kiểm tra sâu3clip, tham chiếu SpriteRenderer, danh sách sprite và event.
- Tách kết quả nghiên cứu khỏi save, khóa công cụ và nội dung dùng sản xuất.

## Điểm chưa biết
Thân hàm C# gốc chưa được phục hồi, chưa chứng minh toàn bộ công thức damage,
chest pity, offline elapsed/clamp, cooldown hoặc luật phía server. Tên field và
method là bằng chứng cấu trúc, không phải bằng chứng chính xác thuật toán.
Có một số tài nguyên Spine, không được suy ra toàn game đều dùng rig.
Không khẳng định gói chứa mọi tài nguyên có thể tải trong tương lai.

## Trước khi viết game
Repo game trước đó là tai23082004l02-svg/Sword-master-story, tại thời điểm bàn
giao đã có Godot0.8.3 (đội5, frame rời, 30ải, trang bị, hầm/tháp, tốc độ1/2/3).
Đây là thông tin phiên làm việc, cần fetch và đọc AGENTS/README/HANDOFF thật
trong repo triển khai trước khi sửa. Không âm thầm biến dự án đó thành game mới.
Nếu làm dự án mới, xác định đích repo và màn hình ngang/dọc theo yêu cầu mới.
User đã bỏ thử nghiệm bộ xương trong dự án cũ; không tự đưa rig trở lại.

## Quy tắc làm việc
- Dùng asset/code/tên/truyện/cân bằng do dự án mới tạo; không bê nguyên mẫu gốc.
- Phân biệt số dòng catalog và số nội dung thực sự mở cho người chơi.
- Giữ save người chơi; test với profile riêng và kiểm migration/atomic commit.
- Không tự thêm server/PvP/shop nạp/SDK theo những class tìm thấy trong dump.
- Báo đúng môi trường đã thử; không nói đã thử điện thoại hoặc nghe âm nếu chưa làm.
- Mọi phát hiện mới phải có evidence path/object/class hoặc test; cập nhật EVIDENCE.

## Prompt tiếp nối có thể dùng
“Đọc research/eternal-senia-2/START_HERE.md và các tài liệu liên quan. Dùng
BUILD_BLUEPRINT làm bản thiết kế mới, không sao chép nội dung gốc. Fetch repo
triển khai, giữ công việc có sẵn, làm từng mốc có thể chơi và kiểm tra save.”
