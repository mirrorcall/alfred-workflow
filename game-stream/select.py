import json
import sys

var = dict()
# passing to alfred filter to tell if performing custom searh
var['custom'] = 'true' if len(sys.argv) > 1 else 'false'

with open('stream.json', 'r') as f:
    stream_data = json.load(f)

items = []
for d in stream_data['website'].keys():
    item = dict()
    item['title'] = stream_data['website'][d]['name']
    item['subtitle'] = 'Watching streaming on ' + stream_data['website'][d]['name']
    item['arg'] = \
            (stream_data['website'][d]['url'] + stream_data['website'][d]['search'] + sys.argv[1]) \
            if len(sys.argv) > 1 else ''
    item['icon'] = {
        'path': 'icon/' + d + '.icns'
    }
    # passing to next script filter
    item['variables'] = {
        'webname': stream_data['website'][d]['name'],
        'website': stream_data['website'][d]['url'] +  stream_data['website'][d]['category']
    }
    items.append(item)

json_data = json.dumps({'variables': var, 'items': items})
print(json_data)
