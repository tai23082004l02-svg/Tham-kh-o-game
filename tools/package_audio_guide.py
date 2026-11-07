"""Build/verify the documentation-only ElevenLabs handoff ZIP. No API calls."""
import argparse
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'guides'/'elevenlabs-game-audio'
ARCHIVE = ROOT/'downloads'/'elevenlabs-game-audio-guide.zip'


def sources():
    return sorted(p for p in SOURCE.rglob('*') if p.is_file())


def validate_source():
    files = sources()
    assert len(files) == 7 and all(p.suffix in ['.md', '.json'] for p in files)
    pack = json.loads((SOURCE/'prompt_pack.json').read_text())
    assert pack['status'] == 'planned_not_generated' and len(pack['assets']) == 28
    assert len({a['id'] for a in pack['assets']}) == len(pack['assets'])
    for asset in pack['assets']:
        assert asset['status'] == 'planned' and asset['duration_seconds'] > 0
        assert asset['variants'] == 1 and isinstance(asset['loop'], bool)
    template = json.loads((SOURCE/'manifest.template.json').read_text())
    assert template['budget_credit_cap'] is None and template['status'] == 'template_not_executed'
    for p in files:
        text = p.read_text()
        assert 'sk_' not in text and 'xi-api-key: sk' not in text
    return files


def verify():
    files = validate_source()
    with zipfile.ZipFile(ARCHIVE) as archive:
        assert archive.testzip() is None
        expected = {'elevenlabs-game-audio/'+p.relative_to(SOURCE).as_posix(): p for p in files}
        assert set(archive.namelist()) == set(expected)
        for name, p in expected.items():
            assert archive.read(name) == p.read_bytes(), name
    print('PASS: documentation ZIP matches seven source files, 28 planned prompts; no API requests')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify without rewriting the ZIP')
    args = parser.parse_args()
    if not args.check:
        files = validate_source()
        ARCHIVE.parent.mkdir(exist_ok=True)
        with zipfile.ZipFile(ARCHIVE, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for p in files:
                info = zipfile.ZipInfo('elevenlabs-game-audio/'+p.relative_to(SOURCE).as_posix(), (2026,11,7,0,0,0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, p.read_bytes())
    verify()


if __name__ == '__main__':
    main()
