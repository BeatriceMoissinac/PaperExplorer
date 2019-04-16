'''
Created on Apr 15, 2019

@author: moissinb
'''
import pandas as pd
import csv
import sys
import glob
import os
from macpath import split



# Filter for keywords
def filterKeywords(data, keywords):
    #return data[data['title'].str.contains('|'.join(keywords), case = False)] # OR
    for k in keywords:
        data = data[[k.lower() in x.lower() for x in data['title'] ]]
    return data
    
# Filter for venues
def filterVenues(data, venues = ['nips','aied', 'icer', 'aaai', 'icml', 'kdd', 'its', 'lak']):
    return data[data['venue'].isin(venues)]
  
# Search data set
def search(data):
    return data.sample()
       
   
# Split the input keywords or venues 
def spliter(input):
    output = input.split(",")
    if len(output) == 0:
        print(">> ERROR: Input was empty")
    else :
        return output




# Print the paper selected
def prettyPrint(paper):
    #['title', 'authors', 'venue', 'year', 'url', 'DoNotInclude']
    
    print("\""+str(paper.iloc[0,1])+"\"\nby "+authorsToString(paper.iloc[0,2])
          +"\nin "+str(paper.iloc[0,3]).upper()+" "+str(paper.iloc[0,4]))




# Make the authors string output pretty
def authorsToString(authors):
    authors = authors.replace('[','').replace(']','').replace("'","").split(",")
    output = ""
    for author in authors:
        if output == "":
            output = author
        else :
            output += ", and " + author
    return output



if __name__ == '__main__':
    # Load data
    df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('', "papers/*.csv"))))
   
    menu = input("""
    **************************************************
    ***************What would you like ?**************
    **************************************************
    Enter the option number
    0 - Randomly select a paper
    1 - Randomly select a paper by keywords (AND)     
    2 - Randomly select a paper by venue            
    3 - Randomly select a paper by venue and keywords 
    
    Venues available: aaai, aied, icer, icml, its, kdd, lak, nips
    """)
    

    if menu =="":
        exit()  
    if menu == "1" or menu == "3" :
        keywords = input("Please input keywords separated by commas: ")
        df = filterKeywords(df, spliter(keywords))
    if menu == "2" or menu == "3" :
        venues = input("Please enter venues separated by commas (no space): ")
        df = filterVenues(df, spliter(venues))
    
    # Search
    paper = search(df)
    # Print
    prettyPrint(paper)
    
     
    
    pass