# Kho tham khảo game

## Tạo âm thanh game bằng ElevenLabs

**[Chatbot đọc hướng dẫn tại đây](guides/elevenlabs-game-audio/START_HERE.md)** ·
[Tải hướng dẫn ZIP](downloads/elevenlabs-game-audio-guide.zip).
Có quy trình API/GitHub Actions, kế hoạch credit sắp hết hạn,28prompt mẫu và
manifest. Đây là mục riêng, chưa chạy tạo âm hoặc sử dụng credit trong lần bàn giao.

## Tham khảo cấu trúc và tài nguyên game

Bắt đầu tại **[Bàn giao Eternal Senia 2](research/eternal-senia-2/START_HERE.md)**.

- [Mục lục nghiên cứu và catalog](research/eternal-senia-2/README.md): kết quả đã đọc,
  bằng chứng, hoạt ảnh, schema46JSON và bản thiết kế Godot độc lập.
- [Mẫu cấu hình và mô phỏng tự viết](research/eternal-senia-2/examples/README.md).
- [Gói Eternal Senia 2 gốc](eternal%20senia/EternalSenia2/README.md): archive có sẵn,
  không phải tài nguyên được cấp phép đưa vào game khác.
- `apk-extracted/com.superplanet.swordmaster_2.0.0`: APK Sword Master Story trước đó;
  **không thuộc các kết luận Eternal Senia 2**.

**Người dùng đã cho phép chatbot chủ động xuất/xem tài nguyên để tham khảo**,
không hỏi lại từng bước. Ưu tiên [chất lượng đồ họa và frame](research/eternal-senia-2/GRAPHICS_WORKFLOW.md).

Nghiên cứu tĩnh; không phải project Unity gốc hoặc phục hồi100% logic.
Xem [bằng chứng và giới hạn](research/eternal-senia-2/EVIDENCE.md),
[riêng tư và quyền sử dụng](research/eternal-senia-2/PRIVACY_AND_RIGHTS.md).

Archive hiện có chứa dữ liệu riêng trên máy. Nên giữ repoPrivate; bộ bàn giao
mới không sao chép thêm save, token hoặc khóa công cụ.

Kiểm bộ tài liệu: `python3 tools/validate_handoff.py`.
