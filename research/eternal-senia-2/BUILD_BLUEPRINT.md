# Bản thiết kế độc lập để xây game tương tự

Đây là **đề xuất mới**, không phải logic nguyên bản đã phục hồi. Mục tiêu là bản
chơi nhỏ main hero+assist, nhịp đánh tự động/tap skill, săn đồ và tiến trình local.
Tùy chọn đưa bài học vào gameđội5 hiện có phải được giữ thành hướng riêng.
Không viết lại dự án đã có khi người dùng chỉ yêu cầu tham khảo.

## Đề xuất module Godot4
| Module | Trách nhiệm |
| --- | --- |
| Catalog | ID và dữ liệu hero/skill/enemy/stage/item, validate trước khi chơi |
| BattleModel | HP, mục tiêu, cooldown, action state, hit markers, result |
| BattleView | Sprite/pivot/particle/âm; đọc model, không sửa ví/save |
| ClipPlayer | Frame duration/anchor/event, pause/speed, chống event đôi |
| ProgressStore | Saveversion, migration, backup, atomic transactions |
| Inventory | itemUID, baseID/rank/owner, equip không trùng |
| RewardService | run token, snapshotreward, settle/retry đúng một lần |
| Screens | Sảnh, chọnải, prep, trận, kếtquả, túi, nâng, settings |

## Mốc triển khai
1. **Một trận hoàn chỉnh:** một hero, mộtassist, hailoạiquái, mộtboss và ảnh riêng.
   Vàoải→thắng/thua→thưởng→chơi lại; không làm10menu trước khi trận chơi được.
2. **Frame và cảm giác đánh:** clipmanifest, căn chân, markerđòn/âm/particle,
   slow preview, pause/x1/x2/x3. Đồng hồlogic tách thời gianUI.
3. **Tiến trình an toàn:**5ải, mở tuần tự, thưởngđầu/replay; token chốngsettle đôi,
   savehỏng không reset, migration cóbackup, lỗi ghi không trừ tiền.
4. **Xây nhân vật:** cấp,3skill,2ôđồ, dropUID, giá nâng, trước/sau chỉsố. Làm
   bộ item nhỏ đủ tạo lựa chọn thay vì danh mục hàngtrăm món.
5. **Assist và boss:**2assist khác vai trò, boss báođòn rõ; thêmbuild dựa kếtquả
   chơi. Dùngstat snapshot khi vào trận để equip ngoài trận không sửa trận đang chạy.
6. **Offline và mục tiêu:** thưởng theo elapsed cócap, claimID, lỗi giờmáy;
   không thêmserver/ads/gacha/shopnạp trừ khi người dùng yêu cầu.
7. **Mởrộng nội dung:** thêmcatalogue, kiểmđộkhó vàUI trên máy thật. Chỉ đóngAPK
   khi user muốn; không tự thêmdịchvụ hoặcphí.

## Quyết định mặc định cho mẫu mới
- Battle step cốđịnh1/60s; x2/x3 chạy thêmstep, không dt nhảy xuyênwindup.
- Damage sự kiện mộtlần theoactionID; animationframe không tự sửaHP mỗi lầnrender.
- RNG cóseed trongtest; loot vàreward chốt mộtlần theo runID.
- Save tronguser://, settings riêng; không đổi tênproject khiến “mất save”.
- Offline mẫu tốiđa2giờ; thời gianâm tính thành0; ghi mốcclaim cùng thưởng.
  Đồng hồlocal không chống chỉnhgiờ: đây là giới hạn của bản offline.
- Tất cả con số trongexamples là do bộ bàn giao tự đặt, không cân bằng cuối.

## Tiêu chí kiểm tra
Model: đúngtarget, không đánhngườiđãchết, cooldown, death, bosstelegraph.
Timeline: mốcđúng mộtlần khi qua nhiều frame, pause, seek, replay, loop, x3.
Save: lỗiwrite/rename, retry, snapshot, migrate, backup, future schema.
UI: touchthật, chữ/nút không chồng, safearea, landscape/portrait đúng yêu cầu.
Thưởng: thắng/thua/replay/khođầy/thoát trận không nhậntrùng.
Chỉ tuyên bố FPS/nhiệt/âm/cảm ứng sau phép thử thật trên thiếtbị.
