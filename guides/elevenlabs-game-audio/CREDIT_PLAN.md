# Tận dụng credit sắp hết hạn

## Đầu vào cần biết một lần
- Số credit có thể dùng và số credit **tối đa được chi** cho lô này.
- Hạn hiệu lực chínhxác, múigiờ, loạicredit; kiểm thôngtin tài khoản thayvì đoán.
- Phạm vi game, artdirection âm vàasset đã có.
- Có cầnvariant/loop dài/voice không; không trộnMusic/TTS vào budget SFX tựđộng.

Không có số dư hoặcngày hết hạn hiện tại trongrepo. Không suy ra mọicredit sẽ
hết hạn giốngnhau hoặccounter trước đây làsố dư hiện tại. Đừng đợi đếnphútcuối:
cầnthời gianđể nghechọn,xửlý vàtải đủfile.

## Thứ tự ưu tiên
1. Pack dùngchung: UIclick/back/confirm,error,reward,openchest,levelup,win/lose.
2. Combatcốt lõi: swordslash/hit,arrow,spell,fire,ice,thunder,shield,heal,playerhurt.
3. Variants2–3 choâm lặp nhiều, chỉ sau mẫuđầu đạt; đây giúpđỡnhàm hơn là
   hàngchụcâm đơnlẻ chưa cóevent sử dụng.
4. Boss: xuất hiện,telegraph,attack,death; âmhiếm cầnrõ vànổi hơnhitthường.
5. Ambience/loop/menu/battle: stylethốngnhất, nghethử nối, tránhvòng8s quángắn
   nếu dễnhàm. Durationdài vàendpoint khác cầnướcphí riêng.

Cóthể chia ngân sách phần trăm như50%SFXcốt lõi,20%variants,15%boss/UIđặcbiệt,
15%dựphòng. Đây làgợi ýphân bổ, **không phải bảnggiá hoặc phêduyệtchi phí**.
Nếuâm cũtốt, chuyểnbudget sangthiếu hụt; không cốtiêu hết cho đủmục tiêu.

## Chi phí quan sát trước đây
Game-create:24mẫu mới, mộtMagicBullet táisử dụng. Tổngresponse-cost-header325,
trongkhiaggregatecountersnapshot tăng76; chưa chứngminh quyếttoán bằngcon sốnào.
MagicBullet trướcđóheader5. Đây làlịch sử của mộtlô, không phải bảnggiá hiện tại.
Không khẳngđịnh APIluôn8credit,giálinear theo giây hoặcloop luôn80credit.
Kiểmpricing/model,gói/quota hiện tại; dựphòng vàdừng sớm khiusage chưa rõ.

## Đầu ra nên có trước khi gọiAPI
BảngID/prompt/duration/variants/endpoint/ướcphí, batchID mới, budgetcap cụthể,
đường dẫn đầu ra vàcáchgiữattempt qua run. Promptpack hiện có28mẫu gợiý;
không tựtạo toànbộ chỉ vì file queue tồn tại.
