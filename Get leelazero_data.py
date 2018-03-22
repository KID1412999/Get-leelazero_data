import requests
import json
import demjson
js_url="http://zero.sjeng.org/data/elograph.json"
data=requests.get(js_url)
data=data.text
data=json.dumps(data)
text = demjson.decode(data)
print(text)
