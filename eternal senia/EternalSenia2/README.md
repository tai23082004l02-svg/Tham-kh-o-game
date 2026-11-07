# Eternal Senia 2 — dump tham khảo (KHÔNG phải tài nguyên dùng lại)

Package: `com.sanctumstudio.eternalsenia2` · Unity **IL2CPP** arm64-v8a · metadata v31 · CodeStage Anti-Cheat (ObscuredTypes)

Toàn bộ tài nguyên thuộc **Sanctum Studio**. Chỉ dùng để nghiên cứu kiến trúc engine, cơ chế gameplay, IL2CPP & anti-cheat. **Không** tái sử dụng asset/code/âm thanh/hình ảnh/nội dung vào sản phẩm thương mại.

## File trong thư mục này

| File | Nội dung |
|---|---|
| `EternalSenia2_dump.7z.001` → `.003` | **TRỌN GAME** (~210 MB): `base.apk`, `split_config.arm64_v8a.apk`, `files/` (metadata + Unity settings + `game.sav`), `data_private.tar.gz`, `obb/`, `README.md` |

Giải nén: tải đủ 3 part vào cùng thư mục rồi mở `EternalSenia2_dump.7z.001` (7-Zip tự nối part).

```powershell
# Windows
& "C:\Program Files\7-Zip\7z.exe" x EternalSenia2_dump.7z.001 -o.
```

## Ghi chú kỹ thuật khi mổ

- Code thật: `split_config.arm64_v8a.apk` → `lib/arm64-v8a/libil2cpp.so` + `files/il2cpp/Metadata/global-metadata.dat`
- Dump tên class/method:
  ```
  Il2CppDumper.exe libil2cpp.so global-metadata.dat out_dir
  ```
  → ra `dump.cs`, `script.json`, `stringliteral.json`
- Asset thật (sprite/audio/prefab/scene/text): `base.apk` → `assets/bin/Data/` → xem bằng **AssetRipper** / **AssetStudio**
- Phiên bản Unity: xem `files/il2cpp/unity.ver`
- Save game: `files/game.sav`
