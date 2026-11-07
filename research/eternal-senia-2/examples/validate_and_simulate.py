"""Original, dependency-free executable specification; not recovered game logic."""
from copy import deepcopy
import json
from pathlib import Path

CONFIG = Path(__file__).with_name('original_game_config.json')


def validate(data):
    assert data['schema_version'] == 1 and data['simulation_hz'] == 60
    assert data['offline']['cap_seconds'] > 0
    for group in ['heroes', 'enemies']:
        for actor in data[group].values():
            assert all(isinstance(actor[k], int) and actor[k] > 0
                       for k in ['hp', 'attack', 'attack_interval_ticks'])
    for skill in data['skills'].values():
        assert skill['owner'] in data['heroes'] and skill['clip'] in data['clips']
        assert skill['power'] > 0 and skill['cooldown_ticks'] > 0
    assert [s['id'] for s in data['stages']] == list(range(1, len(data['stages']) + 1))
    for stage in data['stages']:
        assert stage['coins'] >= 0 and stage['first_bonus'] >= 0
        assert stage['enemies'] and all(e in data['enemies'] for e in stage['enemies'])
        assert stage['loot'] and all(i in data['items'] for i in stage['loot'])
    for item in data['items'].values():
        assert item['slot'] in ['weapon', 'armor'] and item['hp'] >= 0 and item['attack'] >= 0
    for clip in data['clips'].values():
        duration = sum(f['duration_ticks'] for f in clip['frames'])
        assert all(f['duration_ticks'] > 0 and len(f['offset']) == 2 for f in clip['frames'])
        assert all(0 <= m['tick'] < duration for m in clip['markers'])
        assert len({m['id'] for m in clip['markers']}) == len(clip['markers'])


def simulate(data, stage_id, speed):
    assert speed in [1, 2, 3]
    stage = data['stages'][stage_id - 1]
    hero = deepcopy(data['heroes']['wanderer'])
    enemies = [deepcopy(data['enemies'][i]) for i in stage['enemies']]
    tick = hero_ready = enemy_ready = target = frames = 0
    while tick < 36000 and hero['hp'] > 0 and target < len(enemies):
        frames += 1
        for _ in range(speed):
            enemy = enemies[target]
            if tick >= hero_ready:
                enemy['hp'] -= hero['attack']
                hero_ready = tick + hero['attack_interval_ticks']
            if enemy['hp'] <= 0:
                target += 1
                enemy_ready = tick + 30  # Original grace period before next foe.
            elif tick >= enemy_ready:
                hero['hp'] -= enemy['attack']
                enemy_ready = tick + enemy['attack_interval_ticks']
            tick += 1
            if hero['hp'] <= 0 or target == len(enemies):
                break
    return {'won': target == len(enemies), 'hp': hero['hp'], 'ticks': tick,
            'simulation_seconds': tick / data['simulation_hz'], 'display_frames': frames}


def settle(save, run_id, stage, won):
    """Pure illustrative transaction; production must persist atomically before display."""
    if save['pending_run'] != run_id or run_id <= save['last_claimed']:
        return save, False
    result = deepcopy(save)
    if won:
        first = stage['id'] not in result['cleared']
        result['coins'] += stage['coins'] + (stage['first_bonus'] if first else 0)
        if first:
            result['cleared'].append(stage['id'])
    result['last_claimed'] = run_id
    result['pending_run'] = None
    return result, True


def check_examples():
    data = json.loads(CONFIG.read_text())
    validate(data)
    for stage in data['stages']:
        results = [simulate(data, stage['id'], speed) for speed in [1, 2, 3]]
        logical = [{k: v for k, v in r.items() if k != 'display_frames'} for r in results]
        assert logical[0] == logical[1] == logical[2] and logical[0]['won']
        assert results[2]['display_frames'] <= results[1]['display_frames'] <= results[0]['display_frames']
    clip = data['clips']['slash']
    # Cross several markers in one update, without emitting them twice.
    emitted = set()
    for start, end in [(0, 3), (3, 10), (10, 15), (3, 10)]:
        for marker in clip['markers']:
            if start <= marker['tick'] < end:
                emitted.add(('action-1', marker['id']))
    assert emitted == {('action-1', 'hit'), ('action-1', 'sound')}
    save = {'pending_run': 1, 'last_claimed': 0, 'coins': 0, 'cleared': []}
    settled, ok = settle(save, 1, data['stages'][0], True)
    assert ok and save['coins'] == 0 and settled['coins'] == 45
    again, ok = settle(settled, 1, data['stages'][0], True)
    assert not ok and again == settled
    lost = deepcopy(settled)
    lost['pending_run'] = 2
    lost, ok = settle(lost, 2, data['stages'][0], False)
    assert ok and lost['coins'] == settled['coins']
    print('PASS: original catalogue references, five sample battles at x1/x2/x3, marker IDs and reward dedup')


if __name__ == '__main__':
    check_examples()
