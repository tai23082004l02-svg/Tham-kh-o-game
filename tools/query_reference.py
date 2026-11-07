"""Small targeted catalogue reader so chatbots need not load megabytes of JSON."""
import argparse
import json
from pathlib import Path

CAT = Path(__file__).resolve().parents[1]/'research'/'eternal-senia-2'/'catalogs'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('kind', choices=['table', 'class', 'sprite', 'clip', 'textasset', 'script', 'asset'])
parser.add_argument('name', help='Exact table/class name; substring for other kinds')
parser.add_argument('--limit', type=int, default=20)
args = parser.parse_args()
if not 1 <= args.limit <= 100:
    parser.error('--limit must be between 1 and 100')

def load(name):
    return json.loads((CAT/(name+'.json')).read_text())

if args.kind in ['table', 'class']:
    data = load('table_schemas' if args.kind == 'table' else 'core_class_map')
    if args.name not in data:
        parser.error('Name not found; available: '+', '.join(sorted(data)))
    result = data[args.name]
else:
    if args.kind == 'sprite':
        rows = load('sprite_metadata')['sprites']
    elif args.kind == 'clip':
        rows = load('verified_clip_samples')
    elif args.kind == 'textasset':
        rows = load('textasset_index')
    elif args.kind == 'script':
        rows = load('script_index')
    else:
        rows = [{'type': typ, 'name': name}
                for typ, names in load('asset_inventory')['names_by_type'].items() for name in names]
    matches = [r for r in rows if args.name.casefold() in str(r.get('name', r.get('class', ''))).casefold()]
    result = {'matches':len(matches), 'shown':matches[:args.limit], 'limit':args.limit}
print(json.dumps(result, ensure_ascii=False, indent=2))
