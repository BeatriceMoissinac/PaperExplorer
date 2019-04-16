'''
Created on Apr 15, 2019

@author: moissinb
'''

from bs4 import BeautifulSoup
import requests
import re
import sys
import pandas as pd
import json

if __name__ == '__main__':
    
    venue = sys.argv[1]
    year = sys.argv[2]
    
    #years = range(2012,2019,1)
    #venues = ['nips','aied', 'icer', 'aaai', 'icml', 'kdd', 'its', 'lak']
    
    # Download page with JSON info from DBLP
    r = requests.get("https://dblp.org/search/publ/api?q=toc%3Adb/conf/" + venue + "/" + venue + str(year) + ".bht%3A&h=1000&format=json")
    # Extract text
    data = r.text
    # Load data from json provided by DBLP
    jsondata = json.loads(data)
    try :
        listOfPapers = jsondata['result']['hits']['hit']
        rdd = []
        for paper in listOfPapers:
            # Extract info from json
            try:
                title = paper['info']['title']
                authors = paper['info']['authors']['author']
                url = paper['info']['ee']
                rdd.append((title, authors, venue, year, url, False))
            except KeyError:
                print(">> ERROR: " + title + " is missing info")
        # Convert to DataFrame    
        df = pd.DataFrame(rdd, columns=['title', 'authors', 'venue', 'year', 'url', 'DoNotInclude'])
            
        # print(df)
        print(">> Downloaded " + str(len(df.index)) + " papers for " + venue + str(year))
        # Write to file
        df.to_csv("papers/" + venue + str(year) + ".csv")
    
    except KeyError:
        print(">> ERROR: No paper found")
        
    
    pass
