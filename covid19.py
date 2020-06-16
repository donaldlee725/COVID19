# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 22:32:42 2020

@author: Donald's PC
"""

import requests
import json
import pandas as pd
from datetime import date, timedelta

today = date.today()
d1 = today.strftime("%Y-%m-%d")
begin = date(2020, 1, 21)

def daterange(begin, end):
    for n in range(int((end - begin).days)):
        yield begin + timedelta(n)
        
def dataCollection():
    dfList = list()
    for day in daterange(begin, today):
        url = "https://covid-19-data.p.rapidapi.com/report/country/name"
        
        querystring = {"date-format":"YYYY-MM-DD","format":"json","date": day,"name":"China"}
        
        headers = {
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
            'x-rapidapi-key': "14614902a9mshf485023edcb0d11p1e441ejsn9f15496c7dfb"
            }
        
        response = json.loads(json.dumps(requests.request("GET", url, headers=headers, params=querystring).json(), indent=4))
        df = pd.DataFrame(response[0].get("provinces"))
        dfList.append(df)
    df = pd.concat(dfList)
    return df

dataCollection()


    