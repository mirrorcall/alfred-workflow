import json
import sys
import os
import re

items = []

kw = sys.argv[1] if len(sys.argv) > 1 else ''

with open('stream.json', 'r') as f:
    game_data = json.load(f)

site = os.environ['webname']
url = os.environ['website']
for g in game_data['game'].keys():
    if kw != '' and (kw.lower() not in game_data['game'][g]['name'].lower() and kw.lower() not in g):
        continue
    if site.lower() not in game_data['game'][g]:
        continue

    item = dict()
    item['title'] = game_data['game'][g]['name']
    item['subtitle'] = 'Watching ' + g.upper() + ' on ' + site
    
    if g == 'all':
        open_url = re.sub(r'com/.*', 'com/', url) + game_data['game'][g][site.lower()]
    else:
        open_url = url + game_data['game'][g][site.lower()]
    item['arg'] = open_url

    if 'icon' in game_data['game'][g]:
        icon_path = 'icon/' + game_data['game'][g]['icon']
    else:
        icon_path = 'icon/' + site.lower().replace('tv', '') + '.icns'
    item['icon'] = {
        'path': icon_path
    }
    items.append(item)

json_data = json.dumps({'items': items})
print(json_data)