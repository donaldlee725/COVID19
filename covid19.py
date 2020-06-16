# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 22:32:42 2020

@author: Donald's PC
"""

import requests
import json
import pandas as pd
from datetime import date, timedelta

today = date.today() - timedelta(days=1)
begin = date(2020, 1, 21)

def dateRange(begin, end):
    dateDifference = (end - begin).days
    for n in range(dateDifference):
        yield (begin + timedelta(days=n)).strftime("%Y-%m-%d")
    

df = pd.DataFrame()
for day in dateRange(begin, today):
    url = "https://covid-19-data.p.rapidapi.com/report/country/name"
    
    querystring = {"date-format":"YYYY-MM-DD","format":"json","date": day,"name":"China"}
    
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "14614902a9mshf485023edcb0d11p1e441ejsn9f15496c7dfb"
        }
    
    response = json.loads(json.dumps(requests.request("GET", url, headers=headers, params=querystring).json(), indent=4))
    df.append(response[0].get("provinces"))


