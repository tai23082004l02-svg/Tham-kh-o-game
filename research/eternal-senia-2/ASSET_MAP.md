# Bản đồ tài nguyên

Nguồn đã có trong repo: `eternal senia/EternalSenia2/EternalSenia2_dump.7z.001`
đến`.003`. Tải đủ3part cùng thư mục. Các bản ghi mô tả ở đây không chứa ảnh/âm
có thể đưa ngay vào game khác.

| Bên trong archive | Vai trò đã quan sát |
| --- | --- |
| base.apk → assets/bin/Data | Serialized Unity assets và resource streams |
| split_config.arm64_v8a.apk → lib/arm64-v8a/libil2cpp.so | Native gameplay đã biên dịch |
| files/il2cpp/Metadata/global-metadata.dat | Metadata31 dùng dựng khai báo |
| files/il2cpp/unity.ver | GUID trong gói này, **không phải chuỗi phiên bản Unity** |
| obb | Có thư mục, không thấy nội dung trong archive này |
| files/game.sav | Save cá nhân, không cần cho catalogue hoặc thiết kế mới |
| data_private.tar.gz | Dữ liệu riêng/caches/preferences; không công khai lại |

Unity version lấy từ header assets; không đọc GUIDunity.ver rồi coi đó là version.
Các filename băm trong Data không nói lên loại nội dung. Dùng TextAsset index
để đi từ tên bảng tới file chứa nó. Luôn lấy resource stream đi kèm, không chép
mỗi serialized header rồi kết luận texture/audio bị mất.

## Tra cứu nhanh bằng Python
```python
import json
from pathlib import Path
p = Path('research/eternal-senia-2/catalogs')
rows = json.loads((p/'textasset_index.json').read_text())
print([r for r in rows if r['name'] == 'skill'])
sprites = json.loads((p/'sprite_metadata.json').read_text())['sprites']
print([r for r in sprites if r['name'].startswith('senia_run_')])
```

asset_inventory.json có tên theo từng loại; script_index.json có class/namespace/
assembly; không phải toàn bộ source hoặc mọi ScriptableObject đã giải mã.
