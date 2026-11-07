# Sổ bằng chứng và giới hạn

Nguồn: commit0b67b56, gói `eternal senia/EternalSenia2`, nghiên cứu07/11/2026.
Hash và kích thước: catalogs/provenance.json. Các catalog là kết quả tĩnh,
không phải bằng chứng đã chạy game hay kiểm server.

| Phát hiện | Mức | Dẫn chứng |
| --- | --- | --- |
| Unity chủ đạo2022.3.62f2 | Xác minh | Header serialized assets, asset_inventory.json |
| Có một tài sản báo2022.3.54f1 | Xác minh | Cùng inventory; không đồng nhất mọi object |
| IL2CPP, metadata31, arm64 | Xác minh | Header metadata + split native + khai báo dumper |
| 46 JSON đọc được | Xác minh | table_schemas.json; đếm root entries, không coi tất cả là bảng dòng |
| Thay sprite trong clip chạy Senia | Xác minh | verified_clip_samples.json, typeID212, PPtr binding |
| Clip Hugo có âm/particle/event đánh | Xác minh | Event time và function từ clip |
| Có tài sản Spine3.4.02 | Xác minh | TextAsset Senia/RankBox, xem ANIMATION |
| Mọi nhân vật chiến đấu đều dùng Spine | Không có bằng chứng | Không được kết luận |
| Chia các hệ thống combat/UI/table/player data | Diễn giải có căn cứ | core_class_map.json và script_index.json |
| Công thức damage chính xác | Chưa biết | Có tên CalculateAtkDamage, không có thân hàm |
| Offline reward có ngưỡng/cấp/trần | Xác minh schema | OfflineRewardTable + offline_reward fields |
| Đơn vị thời gian, clamp và công thức offline đầy đủ | Chưa biết | Cần đối chiếu thân hàm/runtime |
| Toàn bộ dữ liệu server | Chưa tiếp cận | Dump cục bộ không đủ |
| Asset có thể dùng lại trong game mới | Không được cấp quyền bởi việc có dump | Xem PRIVACY_AND_RIGHTS |

## Đếm chính xác những gì
Quét gặp3344Texture2D,3178Sprite,1980AnimationClip,433AnimatorController,
87TextAsset,87AudioClip. Có tên/tài nguyên lặp:2176tênSprite và1685tênclip khác
nhau không đồng nghĩa số ảnh/clip duy nhất theo hash. Một số shared resources
xuất hiện lại. Không dùng tổng này để quảng cáo “đã xuất toàn bộ asset”.

4315 lỗi đọc body thuộc MonoBehaviour: thiếu kiểu script, không phải4315ảnh hỏng.
Thống kê object không yêu cầu đọc được body của từng component. Các sample clip
và bảng ở catalog có bằng chứng riêng; không suy rộng thành đọc hết mọi prefab.

## Mức hiểu biết
Ước lượng60% từng nói trong chat là đánh giá chủ quan, không đo được. Thay bằng
các đầu ra đếm được ở trên. Il2CppDumper sinh khai báo và dummy DLL, không sinh
thuật toán C# gốc. Công cụ có cảnh báo bảo vệ ban đầu nhưng tìm được registration
và hoàn tất dump; lỗi Console.ReadKey sau cùng là ở bước thoát không có terminal.
