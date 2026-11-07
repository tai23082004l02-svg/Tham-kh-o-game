# Kiểm chứng và tái tạo

## Không cần giải nén để bắt đầu
Các catalog có provenance/hash và dẫn chứng. Đọc chúng trước. Chạy
`python3 tools/validate_handoff.py` từ root để kiểm liên kết nội bộ/JSON và ví dụ.

## Khi thật sự cần mở dump
1. Dùng bản sao local, đủ3part, kiểmSHA256 trong provenance.json.
2.7-Zip mở.001 để nối phần và giải nén. Không chạy APK hay binary của game trên
   máy phân tích; đây là kiểm tĩnh. Không gọi server game để lấy thêm dữ liệu.
3. BaseAPK và split làZIP; giải nén assets/bin/Data và libil2cpp tương ứng.
4. UnityPy1.25.4 đọc serialized assets. Với MonoBehaviour thiếu typetree, ghi
   nhận chưa đọc được body; không coi tênobject là dữ liệufield đã xác minh.
5. Il2CppDumper6.7.46 dùngSO + metadata31 để códump.cs/dummyDLL. Khai báo không
   có thân hàm. Không đưa constants/keys/account values vào log hoặc repo.
6. BảngTextAsset có thể cóBOM và lớp làm rối; khi phân tích local phải giữ nguyên
   ký tự điều khiển, không dùng universal-newline làm biến đổi văn bản trước khi
   xử lý. Kết quảJSON đã kiểm parse là cơ sởtable_schemas, không cần làm lại để
   xây thiết kế mới. Không có khóa giải mã hardcode trong gói bàn giao.
7. Vớiclip phải đọc serialized binding/curve/externals; không coi sample rate
   làfps của tất cả ảnh. Mọi khẳng định timing phải trỏ tới clip cụ thể.

## Bộ tái kiểm thực sự có trong repo
- tools/query_reference.py: tra cứu schema/class/sprite/clip theo tên, có giới hạn đầu ra.
- tools/validate_handoff.py: JSON, counts, internal links, riêng tư và ví dụ.
- examples/validate_and_simulate.py: chạy mô phỏng nhỏ từ config tự thiết kế.
- catalogs/provenance.json: hash dữ liệu nguồn và phiên bản tool.

Không kèm pipeline xuất hàng loạtasset, save editor, cheat/hook hoặc scraper.
Bộ này giúp đọc/thiết kế nhanh; không phải gói phục hồi Unity project hoàn chỉnh.
Nếu mở rộng nghiên cứu, viết script riêng với input/output tường minh, profile
local và giới hạn file đọc; giữ kết quảtóm tắt đủ bằng chứng trongcatalog.
