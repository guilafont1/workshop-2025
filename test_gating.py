from importlib.util import spec_from_file_location, module_from_spec
spec = spec_from_file_location('vl_app','c:\\Users\\amine\\Documents\\VirusLife\\app.py')
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
app = mod.app

def show(state, room):
    with app.test_request_context():
        r = mod._check_access_for_room(state, room)
        if r is None:
            print(f'room {room} -> Allowed')
        else:
            try:
                print(f'room {room} -> Redirect to', r.location)
            except Exception:
                print('room', room, '-> Redirect')

import time
base = {'started_at': None, 'progress': {'room1': False,'room2':False,'room3':False,'room4':False,'room5':False,'room6':False}}
print('not started:')
show(base,1)

base2 = {'started_at': int(time.time()) - (36*60), 'progress': {'room1': True,'room2':False,'room3':False,'room4':False,'room5':False,'room6':False}}
print('time expired:')
show(base2,2)

base3 = {'started_at': int(time.time()), 'progress': {'room1': True,'room2':False,'room3':False,'room4':False,'room5':False,'room6':False}}
print('after room1 complete, try room2:')
show(base3,2)
print('try room3 (should redirect):')
show(base3,3)

base4 = {'started_at': int(time.time()), 'progress': {'room1': True,'room2': True,'room3': True,'room4': False,'room5': False,'room6': False}}
print('after room3 complete, try room4:')
show(base4,4)
