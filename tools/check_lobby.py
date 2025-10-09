from importlib.util import spec_from_file_location, module_from_spec
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
spec = spec_from_file_location('vl_app', os.path.join(ROOT, 'app.py'))
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
app = mod.app

with app.test_client() as c:
    c.post('/start', data={'team_name':'check'}, follow_redirects=False)
    r = c.get('/lobby')
    text = r.get_data(as_text=True)
    if 'Salle 6' in text or 'Salle 6' in text:
        print('Lobby shows Salle 6')
    else:
        print('Lobby does NOT show Salle 6')
