import pandas as pd
import numpy as np
import scipy.stats as stats
import re

nhl_df=pd.read_csv("assets/nhl.csv")
cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

def nhl_correlation(): 
    # YOUR CODE HERE
    raise NotImplementedError()
    
    population_by_region = [] # pass in metropolitan area population from cities
    win_loss_by_region = [] # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]

    assert len(population_by_region) == len(win_loss_by_region), "Q1: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"
    
    return stats.pearsonr(population_by_region, win_loss_by_region)



split_data=[0]
all_Team=[]

for i in range(len(cities["NHL"])):
        data=cities["NHL"][i]
        split_data=[0]
        for i in range(len(data)):
            if data[i]=="—":
                break;
            if data[i]=="[":
                split_data.append(i)
                break;
            if i==len(data)-1:
                split_data.append(i+1)
            if i!=0 and data[i].isupper() and data[i-1].islower():
                split_data.append(i)
        for i in range(len(split_data)-1):
            all_Team.append(data[split_data[i]:split_data[i+1]])

all_Team
finalTeam=[]
for i in range(len(all_Team)):
     if all_Team[i]!="":
        finalTeam.append(all_Team[i])
(finalTeam)
data=nhl_df
data_final=[]
check=False
for i in range(len(nhl_df["GP"])):

    if nhl_df["GP"][i]=="Metropolitan Division":
        data_final.append(i)
        
    
    if nhl_df["GP"][i]=="Central Division":
        data_final.append(i)
    
        
        

# data_final
# for i in range(len(data_final)):
#         if i%2==0:
            
          
#             new_nhl_df=nhl_df[data_final[i]-1:data_final[i+1]]
           
new_nhl_df=nhl_df[data_final[0]+1:data_final[0+1]]
new_nhl_df.pd.concat(nhl_df[data_final[1]+1:data_final[1+1]])
new_nhl_df