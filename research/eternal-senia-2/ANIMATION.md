# Tài nguyên nhân vật và hoạt ảnh

## Ba clip đã kiểm chứng
| Clip gốc | Sample rate | Dài | Bằng chứng |
| --- | ---: | ---: | --- |
| anim_senia_run |30|~0.333s|SpriteRenderer PPtr, run01/02/03; ref03 lặp |
| anim_senia_none_tapatk_1 |30|~0.633s|Đổi sprite+transform, event particle và sound |
| anim_pt_hugo_atk |30|~2.2s|SpriteRenderer, event particle/sound/đánh nhiều lần |

Sample rate30 không có nghĩa clip có30ảnh duy nhất hoặc mọi frame cùng thời
lượng. Raw binding/event: catalogs/verified_clip_samples.json. PPtr ref list
không tự nó là toàn bộ timeline key time; chưa dựng playback đầy đủ từ compressed
clip. Khi cần tái dựng, phải đọc cả binding, curve stream và external references.

## Sprite frame
Metadata gốc có m_Rect, m_Pivot, m_RD.textureRect, textureRectOffset, settingsRaw
và texture reference. Pivot mẫu là0.5/0.5 nhưng offset cắt khác nhau; không được
dùng riêng pivot trung tâm của ảnh đã trim để căn chân. Unity có tọa độ texture
và cấu hình packing riêng, cần xử lý chiềuY/rotation/tight mesh khi xuất hình.
settingsRaw không được tự diễn giải là “rotate” chỉ vì khác0.

File catalog sprite ghi tên/file/path_id/rect/pivot/offset/texture_id. Texture_id
chỉ làPathID trong ngữ cảnh serialized file; muốn resolve chắc chắn còn cần
FileID/external mapping. Catalog cũ chưa chứa đầy đủ mọi packing/tight mesh.

## Spine có thật nhưng không phải kết luận cho mọi actor
TextAsset Senia: Spine3.4.02,28bones,30slots, các animation Doya/DoyaIdle/Idle/
NoSpDoya/NoSpIdle/ReturnIdle. RankBox:33bones,19slots,Glow/Open. Có atlas đi kèm,
với region có rotate/xy/size/orig/offset. Tên clip cho thấy những asset này có
phần biểu cảm/giao diện; không suy ra toàn bộ battle actor chạy bằng Spine.

## Pipeline frame độc lập đề xuất cho game mới
1. Tạo artwork riêng từng pose trên canvas chuẩn, có điểm chân thống nhất.
2. Trim alpha và padding có kiểm soát; lưu source size và trim offset.
3. Lưu từng framePNG hoặc atlas có metadata; tuyệt đối không suy vùng cắt bằng
   cách chia đều sheet không có manifest.
4. Clip chứa frame id và duration,loop flag, marker cóid/timestamp.
5. Vẽ frame theo điểm neo chung; kiểm trước/sau, slow motion và alpha edges.
6. Model combat sở hữu hit; nếu marker báo hit thì validate action/token và chỉ
   áp dụng một lần. Render không được tự gâydamage lại khi seek/replay.
7. x2/x3 tăng đồng hồ mô phỏng và presentation tương ứng, không tăng dt lớn gây
   mất event. Khi qua nhiều mốc trong một bước, duyệt tất cả mốc hợp lệ.

Tiêu chí: chân không nhảy giữa pose; không thừa ô/sangframe khác; pause không
mất marker; marker không nhân đôi khi loop, tụtFPS hoặc tăng tốc.
