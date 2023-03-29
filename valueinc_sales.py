#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:30:06 2023

@author: raresmos
"""

import pandas as pd

#import file:
# file_name = pd.read_csv("file.csv") <-- format_csv

data = pd.read_csv("transaction.csv")

data = pd.read_csv("transaction.csv" , sep=";")



#summary of the data
data.info()

#working with calculations

#defining variables

CostPerItem = 11.73
SelingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#mathematical operations on Tableau

ProfitperItem = 21.11 - 11.73

ProfitPerItem = SelingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased*ProfitPerItem
CostPerTransaction = CostPerItem*NumberOfItemsPurchased
SelingPricePerTransaction = SelingPricePerItem*NumberOfItemsPurchased


#CostPerTransaction Column calculation
#costpertransaction = costperitem*numberofitemspurchased

#variable = dataframe["column_name"]
CostPerItem = data["CostPerItem"]
NumberOfItemsPurchased = data["NumberOfItemsPurchased"]
CostPerTransaction = CostPerItem*NumberOfItemsPurchased


#adding  new columns in data frame 

#Cost Per Transaction = Cost Per Item * Number Of Items Purchased
data["CostPerTransaction"] = CostPerTransaction

#Sales Per Transaction = Seling price per item * Number or items purchased 
data["SalesPerTransaction"] = data["SellingPricePerItem"] * data["NumberOfItemsPurchased"]

#Pofit Per Transaction = Sales - Cost
data["ProfitPerTransaction"] = data["SalesPerTransaction"] - data["CostPerTransaction"]

#MarkUp = (Sales - Cost) / Cost
data["Markup"] = (data["SalesPerTransaction"] - data["CostPerTransaction"])/data["CostPerTransaction"]


#Rounding MarkUp

roundmarkup = round(data["Markup"], 2)

data["Markup"]  = round(data["Markup"], 2)


#Combining data fields

my_name = "Mos" + " " + "Rares"
my_year = "Day" + "-" + "Month" + "-" + "Year"

#Checking columns data type
print(data["Day"].dtype)

#Change column type
day = data["Day"].astype(str)
year = data["Year"].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+"-"+data["Month"]+"-"+year

data["data"] = my_date


# Using split to split the clients keywords field
#new_var = column.str.split("sep" , expend = True)

split_col = data["ClientKeywords"].str.split("," , expand = True)

#creating new columns from the split columns . 
data["ClientAge"] = split_col[0]
data["clientType"] = split_col[1]
data["LenghtContract"] = split_col[2]


# Using the replce function 

data["ClientAge"] = data["ClientAge"].str.replace("[" , " ")
data["clientType"] = data["clientType"].str.replace("'" , " ")
data["LenghtContract"] = data["LenghtContract"].str.replace("]" , " ")
data["LenghtContract"] = data["LenghtContract"].str.replace("'" , " ")
data["ClientAge"] = data["ClientAge"].str.replace("'" , " ")


#using the lower function to change item to lowercase

data["ItemDescription"] = data["ItemDescription"].str.lower()


#How to merge Files ( enjoy new data set in current data set)

seasons = pd.read_csv("value_inc_seasons.csv" , sep = ";")


#merging files : merge_df = pd.merge(df_old , df_new , on = "key")

data = pd.merge(data , seasons , on = "Month")



#Dropping columns ( detele columns ) = df = df.drop("columne" , axis = 1)

data = data.drop("ClientKeywords" , axis = 1)
data = data.drop("Day" , axis = 1)
data= data.drop("Year" , axis = 1)
data = data.drop("Month" , axis = 1)


#Export into CSV

data.to_csv("ValueInc_Cleaned.csv" , index = False)





































                   