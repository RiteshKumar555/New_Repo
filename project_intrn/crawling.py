import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import json
url = "https://www.cpppc.org:8082/inforpublic/homepage.html#/projectDetail/91fe736c280a47b183e2727b40cc8dc4"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)
div = soup. find("div", {"id": "app"})
for row in div:
    row_td = row.find_all('span')
    print(row_td)
df = pd.DataFrame(list_rows)