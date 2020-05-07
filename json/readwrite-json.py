import glob
import json


json_files = glob.glob('*.json')

output = {}
output['data'] = []
# print(json_files)

for file in json_files:
    with open(file, "r") as f:
        raw = f.read()
    
    jsondata = json.loads(raw)
    name = jsondata['metadata_storage_name']
    content = jsondata['merged_content']
    
    output['data'].append({
        'filename': name,
        'content': content
    })

with open('allfiles.json', 'w') as outfile:
    json.dump(output, outfile)
    
    
