# Quy trình tạo và đưa âm vào Godot

## 0. Đường dùng khóa: Live-Youtube-American
Vào [repo hỗ trợ](https://github.com/tai23082004l02-svg/Live-Youtube-American)
và đọc workflow/script tạo âm trước. Nơi cấu hình: Settings → Secrets and
variables → Actions → `ELEVENLABS_API_KEY` (chỉ người có quyền mới quản lý được).
Secret đã lưu không có nút đọc lại giá trị; dùng trực tiếp trong job:

```yaml
# Đoạn minh họa trong một job của repo có secret, không phải workflow tự chạy.
- name: Generate the authorized audio batch
  env:
    ELEVENLABS_API_KEY: ${{ secrets.ELEVENLABS_API_KEY }}
  run: python tools/<script-cua-batch-da-chuan-bi>.py
```

Đây là snippet hướng dẫn, không phải file workflow để copy chạy ngay. Script
phải tồn tại và batch/budget phải được chuẩn bị trước. Không in biến môi trường.
Sau run, kiểm manifest rồi lấy audio từ artifact hoặc đường dẫn đã cấu hình.
Chỉ clone repo không đem secret về máy; job fork hoặc workflow tái sử dụng cũng
không mặc nhiên nhận secret. Khi thiếu quyền, dùng kết nối GitHub/Actions phù hợp.

## 1. Chuẩn bị
- Âm gameplay: một event rõ, onset nhanh, ít đuôi, khôngvoice/music/ambience lẫn.
- Ambience: không cố nhét tiếngđòn đánh vào nền. Nhạc menu/combat tách asset.
- CóID,category,prompt,duration,loop,variant vàevent phát. prompt_pack.json là
  queue tham khảo mới, chưa phải số lượt đã được phép chạy.
- Đọc thưviện cũ và manifest trước; duplicateID hoặchash thì ưu tiênreuse.
- Thử vài âm đại diện trước, rồi mở rộng style nhấtquán nếu chất lượng đạt.

## 2. API đã dùng trong dự án cũ
Tài liệu chínhthức để kiểm model/parameter/quyền/cước ở thời điểm chạy:
https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert

Ví dụ cấu trúc request đã quan sát (chưa được chạy bởi tài liệu này):
```http
POST https://api.elevenlabs.io/v1/sound-generation?output_format=mp3_44100_128
xi-api-key: <biến môi trường hoặc Actions secret>
Content-Type: application/json
Accept: audio/mpeg
```
```json
{
  "text": "One sharp fantasy sword slash. Fast dry metallic whoosh, immediate onset. No voice, no music, no background ambience, no long reverb.",
  "duration_seconds": 0.7,
  "prompt_influence": 0.3,
  "loop": false,
  "model_id": "eleven_text_to_sound_v3"
}
```
Không dùngpayload/parameter lịch sử như bảođảmAPI hiện tại vẫn giốnghệt. Khi
cần nhạc dài/hát/TTS, kiểm endpoint, quyền vàpricing riêng; guide này tập trung
SoundEffects. Loop nhạc8 giây cũ được tạo bằngSoundEffects, không Music endpoint.

## 3. Kiểm soát mỗi request trả phí
1. Tạobatch mới,ID ổnđịnh và mộtconcurrency lock; không haiworker chạy cùngqueue.
2. Kiểmbalance/estimatedcost trước từngasset, cộng cảrequest đangpending.
3. Ghiattempt xuống nơi bềnvững **trướcPOST**, gồmID,prompt hash,model,duration,
   batch/requesttime và trạngthái pending. Marker chỉ trongrunner tạm không đủ
   cho lầnrun sau; phải dùngbranch/state-store/artifact có thể phục hồi.
4. MộtPOST/variant. Nhận2xx phải kiểmContent-Type,audio decode,duration vàhash;
   ghiresponse/requestID/usage header nếu có. LỗiJSON không được lưu thànhMP3.
5. Timeout/mấtkết nối sauPOST: trạngthái unknown, không tựPOSTlại. Đối chiếu
   history/requestID khi tài khoản/API hỗ trợ trước khi quyếtđịnh retry.
6. Dừng khi vượtbudget,không đủquyền,429 hoặc lỗi chưa rõ; retryfreeGET có thể
   backoff, nhưng không coiPOST trả phí là retryan toàn. Không resetmarker cũ.
7. Không logkey hoặcheader xi-api-key; không đưa secrets vàoZIP/APK/.tres.

## 4. Xử lý file
Giữbản original. DùngFFmpeg/công cụâm để tạo bản phát: cắt leading silence vừa
phải, fadeedge ngắn tránhclick, kiểmpeak/RMS và điều chỉnhgain. Không cắt mất
transient/đuôiđòn. SFX thườngmono; nhạc cóthể giữstereo/MP3/OGG phù hợpGodot.
Không coi loudnessnormalization thaythế cho nghe kiểm; những âm rấtngắn cần
cân bằng bằngtai và bối cảnhmix. Loopphải thửđiểm nối thật, không chỉ setloop=true.

## 5. Godot
LưuStreamWAV/OGGVorbis/MP3 hoặc native.tres như dự án cũ. Preload/resource-path
đểexport không bỏasset. Master/Music/SFX bus riêng, poolvoice cốđịnh, cooldown
choevent spam, ưu tiênboss/skill hơnđònthường, limiter vàpause/focus stop.
Vũkhíphát một lần ởmarker tungđòn/va chạm phùhợp; đừng phátmỗi_frame, mỗi
projectile trongvolley hoặc mỗiđịch nếu khiếnmix quá dày. x2/x3 không tăngpitch
mặcđịnh; giới hạnvoice/retrigger theo thời gianthực để âm không thànhtiếngrè.

## 6. Bàn giao
Filegốc, file đãxửlý, manifest,theo dõi usage, cácâm đạt/chưa đạt, screenshot hoặc
clipgame nếu đã gắn. Phânbiệt đo kỹthuật/nghe kiểm và thửloađiệnthoại thật.
Không dùnghạncredit như lýdo spamvariant không cómụcđích.
