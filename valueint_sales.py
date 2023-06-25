import pandas as pd

data = pd.read_csv("transaction.csv" , sep = ";")


# summary of the data

data.info()

# Cost per transaction column calculation ( CPT = CPI * NOIP )

# CPT - Cost per transactions
# CPI - Cost per item
# NOIP - Number of items purchased
# SPT - Sales Per Transaction ( SPI * NOIP )
# SPI - Selling price per item



# variable = dataframe["col_name"]

CPI = data["CostPerItem"]
print(CPI)

NOIP = data["NumberOfItemsPurchased"]
print(NOIP)

# Calculating CPT , SPT , Profit , MarkUP
CPT = CPI * NOIP
print(CPT)

SPT = data["SellingPricePerItem"] * data["NumberOfItemsPurchased"]
print(SPT)

profit = SPT - CPT
print(profit)

markup = round((SPT - CPT) / CPT , 2)
print(markup)

# Concatonating Day/Month/Year columns after changing type to string

day = data["Day"].astype(str)
year = data["Year"].astype(str)


date = day + "-" + data["Month"] + "-" + year
print(date)

# Adding calculated  columns to DataFrame

data["CostPerTransaction"] = CPT
data["SalesPerTransaction"] = SPT
data["ProfitPertransaction"] = profit
data["MarkUp"] = markup
data["Date"] = date


# Spliting the Client_Keyword field
# new_var = column.str.split("sep" , expand = True)

split_col = data["ClientKeywords"].str.split("," , expand = True)

# Creating new columns after spliting ClientKeywords field

data["ClientAge"] = split_col[0]
data["ClientOcupation"] = split_col[1]
data["ClientContract"] = split_col[2]

# Using replace function to delete marks from columns
# Data["col_name] = data["col_name"].str.replace("what" , " with what")

data["ClientAge"] = data["ClientAge"].str.replace("[","")
data["ClientAge"] = data["ClientAge"].str.replace("'" , "")
data["ClientContract"] = data["ClientContract"].str.replace("]" , "")
data["ClientContract"] = data["ClientContract"].str.replace("'" , "")
data["ClientOcupation"] = data["ClientOcupation"].str.replace("'" , "")

# Changing from uppercase to lowercase in Item Description fielt
# data["col_name"] = data["col_name].str.lower()

data["ItemDescription"] = data["ItemDescription"].str.lower()

# Bringin in , a new dataset

seasons = pd.read_csv("value_inc_seasons.csv" , sep = ";")

# Merge both files
# new_df = pd.merge[df_old , df_new , on = "key)

data = pd.merge(data , seasons , on = "Month")


# Dropping columns already modified
# df = df.drop("columne" , axis = 1 )

data = data.drop(["ClientKeywords" , "Day" , "Year" , "Month"] , axis = 1)

# Exporting to a CSv file

data.to_csv("ValueInc Cleaned.csv" , index = False)






