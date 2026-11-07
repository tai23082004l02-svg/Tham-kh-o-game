"""Validate this research handoff, without reading APK/private archives or network."""
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'research' / 'eternal-senia-2'
CAT = BASE / 'catalogs'


def main():
    files = sorted(CAT.glob('*.json'))
    assert len(files) == 8, 'Expected eight research catalogues'
    catalogues = {p.stem: json.loads(p.read_text()) for p in files}
    schemas = catalogues['table_schemas']
    assert len(schemas) == 46
    for name, table in schemas.items():
        assert table['root_entry_count'] >= 0 and isinstance(table['fields'], dict), name
        assert 0 <= table['dictionary_row_count'] <= table['root_entry_count'], name
    for name, count in {'partner':70, 'skill':20, 'weapon':180, 'mob':673,
                        'area':1167, 'offline_reward':100}.items():
        assert schemas[name]['root_entry_count'] == count, name
    assert len(catalogues['sprite_metadata']['sprites']) == 3178
    assert len(catalogues['core_class_map']) == 33
    assert len(catalogues['verified_clip_samples']) == 3
    for record in catalogues['provenance']['inputs']:
        assert len(record['sha256']) == 64 and record['size'] > 0
    docs = [ROOT/'README.md', ROOT/'AGENTS.md', *BASE.rglob('*.md'),
            *(ROOT/'guides'/'elevenlabs-game-audio').glob('*.md')]
    links = 0
    for path in docs:
        content = path.read_text()
        for link in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in link or link.startswith('#'):
                continue
            target = unquote(link.split('#', 1)[0])
            assert (path.parent/target).exists(), f'Broken link {path}: {link}'
            links += 1
    for path in BASE.rglob('*'):
        if not path.is_file():
            continue
        assert path.suffix not in ['.apk', '.so', '.dll', '.sav', '.key', '.png', '.wav']
        assert path.stat().st_size < 4_000_000
    raw = (CAT/'core_class_map.json').read_text()
    assert 'TABLE_ENCRYPT_KEY' not in raw and 'RVA:' not in raw
    module_path = BASE/'examples'/'validate_and_simulate.py'
    spec = importlib.util.spec_from_file_location('reference_example', module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.check_examples()
    print(f'PASS: eight catalogues, 46 JSON schemas, 3178 Sprite records, 33 classes, three clips and {links} local links')
    print('This checks handoff consistency, not full original-game behaviour or asset rights.')


if __name__ == '__main__':
    main()
