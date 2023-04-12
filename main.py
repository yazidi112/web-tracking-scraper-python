import json
from scraper import *
f = open('sites.json')
data = json.load(f)
f.close()
data_start = 0
data_end = 100
id_min_length = 6
Scraper.run(data,data_start,data_end,id_min_length)