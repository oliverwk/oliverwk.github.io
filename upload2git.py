#!/usr/bin/env python3
import requests, sys, datetime, base64, json
file = open("luchtdruk.html","r")
rHtml = file.read()
file.close()
file = "luchtdruk.html"
content_res = requests.get("https://api.github.com/repos/oliverwk/oliverwk.github.io/contents/"+file)
data = {"message": str("updated {} from Github Actions on {} using the RAW Github api ".format(file, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) , "content": base64.b64encode(rHtml.replace("leaflet", "Luchtdruk", 1).encode('ascii')).decode('utf-8'), "sha": str(json.loads(content_res.text)["sha"])}
update_res = requests.put("https://api.github.com/repos/oliverwk/oliverwk.github.io/contents/"+file, data=json.dumps(data, indent=4), auth=('oliverwk',  str(sys.argv[1])))
print(update_res.status_code)
print(update_res.json())
print("Pushed to Github" if update_res.status_code == 200 else "Didn't pushed to Github" )
sys.exit(0 if update_res.status_code == 200 else 1)
