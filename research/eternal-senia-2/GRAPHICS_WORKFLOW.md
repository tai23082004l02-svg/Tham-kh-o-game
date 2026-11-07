# Ưu tiên đồ họa: xem thật, dựng thử, kiểm frame

## Chỉ dẫn mới của người dùng
Người dùng đánh giá đồ họa/cắt frame hiện tại chưa đạt và muốn chatbot được tự
tham khảo tài nguyên. Đây là ưu tiên công việc, không chỉ bổ sung menu hoặc logic.
Được chủ động tải/giải nén/xuất tài nguyên cần thiết, dựng preview cục bộ và phân
tích theo START_HERE. Không yêu cầu người dùng duyệt từng bước nghiên cứu.

## Quy trình thực hiện
1. Tra catalog theo nhân vật/clip cụ thể, bắt đầu bằng một bộ đủ idle/run/attack/
   skill/hurt/death nếu thực sự có. Không tự bịa trạng thái còn thiếu.
2. Xuất ảnh bằng công cụ hiểu định dạng Unity. Giữ resource stream và external
   reference. Không dùng chia lưới đều hoặc bounding box alpha thay cho metadata.
3. Đọc vùng texture, trim offset, source size, pivot, pixels-per-unit, packing
   rotation và tight mesh nếu có. Kiểm nguồn gốc tọa độ Unity/Godot và chiều Y.
   Catalog hiện có chưa lưu đủ mọi trường: đọc object gốc khi cần, không đoán.
4. Dựng contact sheet có số thứ tự, kích thước và điểm neo; nền caro để thấy
   alpha. Dựng clip có thể dừng, tiến/lùi frame và phát chậm. Xem bằng công cụ
   xem ảnh thực tế, không chỉ kiểm file tồn tại hoặc có alpha.
5. Lấy thứ tự và thời lượng từ curve/timeline, không sắp tên theo alphabet rồi
   gọi là clip đúng. PPtr mapping và sample rate chưa đủ phục hồi mọi key time.
6. Đối chiếu clip gốc đọc được với bản dựng: chân, tỷ lệ, hướng, đường kiếm,
   nhịp chuẩn bị/ra đòn/hồi đòn và các mốc hiệu ứng. Ghi rõ phần chưa phục hồi.
7. Thiết kế bộ hình riêng theo bài học đó; thử một nhân vật hoàn chỉnh trước
   khi nhân rộng. Nếu artwork từng pose không nhất quán thì sửa artwork, không
   cố che bằng trim/căn giữa. Không tự quay lại rig đã bị người dùng bác bỏ.
8. Đưa vào Godot, chụp màn thật và xem chuyển trạng thái ở x1/x2/x3. Thử runtime
   bằng asset riêng hoặc tài nguyên dự án đã có quyền; giữ mẫu tham khảo tách biệt.

## Tiêu chí chất lượng trước khi nói “đã xong”
- Không mất tay/chân/vũ khí hoặc lấy nhầm góc frame khác.
- Chân đứng yên ở cùng điểm neo; kích thước nhân vật không phồng/co theo frame.
- Không viền nền, halo alpha hoặc cắt mất hiệu ứng do crop quá sát.
- Thứ tự pose có ý nghĩa và nhịp đòn rõ; không lặp pose thừa hoặc bỏ pose cần.
- Hiệu ứng và âm khớp mốc; damage không bị áp dụng hai lần do replay/seek.
- Pause, chuyển trạng thái và x2/x3 không làm mất event hoặc kẹt pose.
- Ảnh chụp/clip kiểm tra phải được xem trực tiếp. Báo đúng môi trường đã thử;
  kiểm headless hoặc kiểm metadata không chứng minh chất lượng mỹ thuật.

## Bàn giao sau mỗi lượt đồ họa
Ghi nhân vật/clip đã xem, nguồn object, cách resolve frame, trường metadata đã
xử lý, ảnh/clip kiểm chứng và vấn đề còn lại. Có thể giữ export/preview ở
`.local-analysis/` (đã gitignore); không vô tình commit save/keys hoặc thư mục
private. Khi cần người dùng xem, trình bày preview phù hợp trong phiên làm việc.
Không coi giấy phép phát hành asset là điều kiện phải có trước khi xem/nghiên
cứu cục bộ; quyền dùng lại asset nguyên gốc trong sản phẩm là vấn đề riêng.

Tài liệu này là hướng dẫn cho bước tiếp theo, **không khẳng định đã xuất toàn bộ
ảnh, dựng lại mọi clip hoặc sửa đồ họa của repo game trong lần sửa bàn giao này**.
