# Mô hình dữ liệu

Bản máy đọc đầy đủ: catalogs/table_schemas.json. Chỉ mục nguồn TextAsset:
catalogs/textasset_index.json. Dữ liệu gốc có nhiều số lưu dưới dạng string;
validator của game mới cần parse và kiểm miền giá trị, không ép kiểu mù.

## Các nhóm chính
| Nhóm | Bảng và số root entries | Liên kết cần chú ý |
| --- | --- | --- |
| Bản đồ/khu | map45, area1167, level100 | mapid/areaid/mobgroup/background/bgmName |
| Quái | mob673, mob_group755, mob_stats120 | mobid, group, weight và level |
| Đồng hành | partner70, partnerclass10, partner_rankup7 | cardid/model/icon/element/skill/rank |
| Kỹ năng | skill20, skillclass13, passive605 | character/skillid/power/cost/cd/gcd/anim |
| Vũ khí | weapon180, weapon_stat100 | category/element/atkMod/skill/material/anim |
| Loot/rương | dropgroup303, chest319 | group/item/count/weight/protect |
| Nhiệm vụ | quest40, tutorial53 | category/target/count/reward |
| Offline | offline_reward100 | threshold partnerTotalAtk, getSpMin, getSpCap |
| Truyện | chapter27, section156, story16, dialog12303 | unlock/type/id, hội thoại trước/sau |

Tên `protect` trong chest gợi ý cơ chế bảo đảm nhưng không đủ xác định quy tắc
pity; tên `weight` chưa chứng minh đã normalize như thế nào. Không bê xác suất
hoặc hệ gacha chỉ dựa vào vài tên cột.

## Quan hệ mẫu (diễn giải, cần đối chiếu ID khi mở rộng)
Area chọn mobgroup; group chọn mobid và weight; mob tham chiếu model/thông số.
Partner chọn model/icon và skill có điều kiện bậc. Skill chọn anim/cost/cd/gcd.
Weapon có catalogue base, bảng stat theo level và nguyên liệu tiến hóa. Tiến
trình người chơi giữ instanceUID; equip liên kếtUID thay vì chỉ base id.

## Những gì không nên suy luận
-100dòng `character` không đồng nghĩa100nhân vật chọn được.
-70dòngpartner có thể gồm hidden/biến thể; cần visible/order và runtime unlock.
-27chapter không đồng nghĩa27chương nội dung đầy đủ; có tab/visible/story nhánh.
-offline schema có trần, nhưng mốc thời gian và quy tắc nhận phải xem thân hàm.

## Thiết kế mới nên dùng
Tách hero_base, skill_base, enemy_base, stage, loot_pool khỏi save. DùngID ổn
định và version catalogue. Save có version, wallets, hero_instances, item_instances,
equipped_uids, stage_records, pending_run và last_claimed_token. Giao dịch nhận
thưởng/cường hóa phải đổi tài nguyên cùng một commit. Thử migration, lỗi ghi,
retry và dữ liệu số ngoài miền. Xem examples để có dữ liệu mới không sao chép.
