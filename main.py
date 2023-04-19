from scraper import *

data_url = "sites.json"
data_start = 10
data_end = 30
id_min_length = 6
Scraper.run(data_url,data_start,data_end,id_min_length)