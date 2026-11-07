# Đọc đầu tiên — chatbot tạo âm thanh

## Yêu cầu người dùng
Người dùng muốn có mục hướng dẫn riêng để chatbot sau biết tự thực hiện quy
trình ElevenLabs. Người dùng nói còn nhiều credit sắp hết hạn, muốn tận dụng
để chuẩn bị âm thanh cho game. **Lượt bàn giao này chỉ làm tài liệu và ZIP,
chưa phải yêu cầu tiêu hết credit hoặc chạy một lô chưa xác định.**

## Vào Live-Youtube-American để dùng khóa API
Theo chỉ dẫn của người dùng, **ưu tiên vào repo
[tai23082004l02-svg/Live-Youtube-American](https://github.com/tai23082004l02-svg/Live-Youtube-American)
để dùng khóa ElevenLabs đã cấu hình**, không yêu cầu người dùng gửi lại khóa
trước khi kiểm tra đường này.

- Đọc hướng dẫn repo và workflow `.github/workflows/swarm-sfx-library.yml`,
  script `tools/swarm_sfx_library.py`; kiểm trigger và phạm vi trước khi sửa/chạy.
- Khóa nằm ở GitHub Actions secret **`ELEVENLABS_API_KEY`**. Workflow truyền
  secret thành biến môi trường cùng tên cho script gọi API.
- GitHub không cho đọc lại plaintext của secret. “Lấy khóa mà dùng” ở đây là
  **chạy công việc tạo âm trong Actions của repo có secret**, không trích xuất
  hoặc in khóa vào log, chat, artifact, ZIP hay repo game.
- Khi đã có yêu cầu tạo âm và ngân sách rõ trong phiên, chuẩn bị batch mới và
  chạy qua workflow phù hợp; không hỏi lại từng âm. Không dispatch lô cũ một
  cách máy móc vì script cũ có danh sách âm và marker chống tạo trùng riêng.
- Lấy audio/manifest đầu ra từ artifact hoặc đường dẫn workflow đã công bố,
  rồi xử lý và đưa file local vào game. Không chuyển secret sang repo game.
- Nếu thiếu quyền repo/Actions hoặc secret chưa được cấp cho job, báo đúng phần
  thiếu và xin cấp quyền phù hợp; không kết luận phải dán khóa vào chat. Với
  workflow ở repo khác, secret không tự truyền sang chỉ vì gọi hoặc clone repo.

## Những gì đã biết
Game-create đã có23 hiệu ứng và2 loop nền, tạo từ ElevenLabs Sound Effects và
phát file local. Model ghi nhận `eleven_text_to_sound_v3`. Hai loop8 giây được
tạo qua Sound Effects, không phải Music Generation. Đừng tự chuyển sang endpoint
Music rồi coi phạm vi/cước/quyền giống nhau.

## Làm việc tiếp theo
1. Đọc WORKFLOW/CREDIT_PLAN và kiểm tài sản đang có; tránh tạo lại âm tốt.
2. Kiểm quyền repo/Actions Live-Youtube-American theo mục trên, rồi model và
   quota. Dùng secret qua job; không tìm giá trị khóa trong file mã nguồn.
3. Chốt một lần mục tiêu: game nào, số credit tối đa, hạn dùng theo múi giờ và
   loại âm cần tạo. Nếu phiên hiện tại đã có các thông tin này thì tiếp tục,
   không hỏi lại. “Còn nhiều” không phải sốbudget cụ thể; không mặc định được
   phép tiêu hết tài khoản. Xác nhận credit nào thực sự hết hạn theo tài khoản.
4. Trình kế hoạch cụ thể gồm tênâm, prompt, duration, sốvariant, phí ước lượng
   nếu xác định được và đầu ra. Giữ dự phòng cho những âm chưa đạt.
5. Khi người dùng yêu cầu tạo lô trongbudget đã rõ, chủ động làm đủ lô đó,
   không hỏi từng âm. Mặc định không trả phí retry khi chưa xác định trạng thái
   request trước; xem cách ghiattempt bềnvững trong WORKFLOW.
6. Lưu audio gốc + bản game-ready + manifest. Nghekiểm chất lượng khi có công cụ;
   nếu chỉ đo waveform, ghi đúng giới hạn, không nói “đã nghe”.
7. Gắnâm vào marker/sự kiện phù hợp, giới hạn overlap. Game chạyoffline,
   không cóAPI key hoặc gọiElevenLabs lúcchơi.

## Đường đã được kiểm tra
Repo tạo âm cũ: tai23082004l02-svg/Live-Youtube-American,
`.github/workflows/swarm-sfx-library.yml` + `tools/swarm_sfx_library.py`.
Secret `ELEVENLABS_API_KEY`. Workflow cũ cócảpush-trigger khi sửa chínhfile
workflow, nên phải đọctrigger trước khi sửa; đừng vô tình tạo âm bằng việcpush.
Script cũ cóASSETS cốđịnh, marker vàbudget riêng: **không chạy nguyênscript cũ
để tạo mộtpack game mới**. DùngbatchID/đầu ra/queue mới theo phạm vi đã yêu cầu.

## Prompt tiếp nối
“Đọc guides/elevenlabs-game-audio/START_HERE.md. Lập một lô âm thanh gốc cho
[game], ngân sách tối đa [N credit], hạn [ngày/giờ/múi giờ]. Kiểm âm sẵn có,
tạo theo quy trình cómanifest/attempt và không gọiAPI khi gamechạy.”
