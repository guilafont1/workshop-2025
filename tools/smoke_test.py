import sys, os
from importlib.util import spec_from_file_location, module_from_spec
# ensure project root is on sys.path so `game` package imports work
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
spec = spec_from_file_location('vl_app', os.path.join(ROOT, 'app.py'))
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
app = mod.app

with app.test_client() as c:
    # start a new game
    resp = c.post('/start', data={'team_name':'testteam'}, follow_redirects=False)
    assert resp.status_code in (302, 301)
    assert '/lobby' in resp.location

    # access room1 GET should be allowed
    r1 = c.get('/room/1')
    assert r1.status_code == 200

    # submit wrong password -> page shows message (200)
    r1w = c.post('/room/1', data={'password':'wrong'}, follow_redirects=False)
    assert r1w.status_code == 200

    # submit correct password -> redirect to room2
    r1c = c.post('/room/1', data={'password':'Nightingale_1860'}, follow_redirects=False)
    assert r1c.status_code in (301,302)
    assert '/room/2' in r1c.location

    print('SMOKE OK')
