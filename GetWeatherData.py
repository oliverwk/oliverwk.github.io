#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, json
from bs4 import BeautifulSoup
url_xml_feed = "https://data.buienradar.nl/1.0/feed/xml"
page_xml_feed = requests.get(url_xml_feed)
soup = BeautifulSoup(page_xml_feed.content, "xml")
luchtdruk = []
for station in soup.find_all('weerstation'):
    ll = float(station.luchtdruk.get_text()) - 1010.0 if station.luchtdruk.get_text() != "-" else 0.0
    luchtdruk.append({"luchtdruk":ll,"lat":station.lat.get_text(),"lon":station.lon.get_text(),"windrichting":station.windrichting.get_text()})


jsons = json.loads(str(json.dumps(luchtdruk, indent=4)).replace('"',""))
csv = "luchtdruk,lat,lon\n"

for i in jsons:
    csv += str(str(i["luchtdruk"])+","+i["lat"]+","+i["lon"]+"\n")

print(csv)
file = open("./weather.csv","w")
file.writelines(csv)
file.close()
