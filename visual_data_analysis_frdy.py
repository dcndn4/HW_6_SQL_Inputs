# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 17:32:35 2021

@author: CS_Knit_tinK_SC
"""

# Visual Data Analysis of Fraudulent Transactions¶

# Your CFO has also requested detailed trends data on specific card holders. 
# Use the starter notebook to query your database and generate visualizations 
# that supply the requested information as follows, then add your 
# visualizations and observations to your markdown report.

#%%

# Initial imports
import os
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd
import pathlib
import hvplot.pandas
import psycopg2
from sqlalchemy import create_engine

#%%

# Create a connection to the database
# engine = create_engine("postgresql://postgres:postgres@localhost:5432/fraud_detection")

# Load .env enviroment variables
home = pathlib.Path.home() / ".env"  # for pc 1/2
load_dotenv(dotenv_path=home)  # for pc 2/2


# Set sqlalchemy connection
conn_str_main = os.getenv("conn_str_main")
database = "Unit 7 HW SQL Susp Trns_"

# Define the database URL
db_url = conn_str_main+database

# Create the engine object
engine = create_engine(db_url)

#%%

# look at card-holder data
# Write the SQL query
query = "SELECT * FROM card_holder"

# Read the SQL query into a DataFrame
card_holder_df = pd.read_sql(query, engine)

# Show the DataFrame's head
print(card_holder_df)

#%%

# look at credit card data
# Write the SQL query
query = "SELECT * FROM credit_cards"

# Read the SQL query into a DataFrame
credit_cards_df = pd.read_sql(query, engine)

# Show the DataFrame's head
print(credit_cards_df)

#%%

# look at merchant-category data
# Write the SQL query
query = "SELECT * FROM merchant_cat"

# Read the SQL query into a DataFrame
merchant_cat_df = pd.read_sql(query, engine)

# Show the DataFrame's head
print(merchant_cat_df)

#%%

# look at merchants data
# Write the SQL query
query = "SELECT * FROM merchants"

# Read the SQL query into a DataFrame
merchants_df = pd.read_sql(query, engine)

# Show the DataFrame's head
print(merchants_df)

#%%

# look at transactions data
# Write the SQL query
query = "SELECT * FROM transactions"

# Read the SQL query into a DataFrame
transactions = pd.read_sql(query, engine)

# Show the DataFrame's head
print(transactions)

#%%

# look at transactions data
# Write the SQL query
query = "SELECT * FROM full_transactions"

# Read the SQL query into a DataFrame
full_transactions = pd.read_sql(query, engine)

# Show the DataFrame's head
print(full_transactions)

#%%

# Data Analysis Question 1

# The two most important customers of the firm may have been hacked. 
# Verify if there are any fraudulent transactions in their history. 
# For privacy reasons, you only know that their cardholder IDs are 2 and 18.

# Using hvPlot, create a line plot representing the time series of 
# transactions over the course of the year for each cardholder separately.

# Next, to better compare their patterns, create a single line plot 
# that containins both card holders' trend data.

# What difference do you observe between the consumption patterns? 
# Does the difference suggest a fraudulent transaction? 
# Explain your rationale in the markdown report.


#%%

# look at transactions data
# Write the SQL query
query = "SELECT * FROM suspected"

# Read the SQL query into a DataFrame
suspect_transactions = pd.read_sql(query, engine)

# Show the DataFrame's head
print(suspect_transactions)
#%%

query = "SELECT * FROM suspected_2"

# Read the SQL query into a DataFrame
suspect_2 = pd.read_sql(query, engine)

#%%


query = "SELECT * FROM suspected_18"

# Read the SQL query into a DataFrame
suspect_18 = pd.read_sql(query, engine)

#%%

# df_costs_year_sorted=avg_prices_nhbrhood.sort_values(['year','sale_price_sqr_foot'], ascending=False)
# new_df = sfo_data.set_index(['year', 'neighborhood'])


summary_suspect_transactions=suspect_transactions[['ccd_owner_id', 'datetime', 'amount']]

summary_suspect_2=suspect_2[['datetime', 'amount']]
summary_suspect_2=summary_suspect_2.sort_values(['datetime'])
summary_suspect_2=summary_suspect_2.rename(columns={'amount': 'Amount_2'})

summary_suspect_18=suspect_18[['datetime', 'amount']]
summary_suspect_18=summary_suspect_18.sort_values(['datetime'])

# df_costs=df_costs.rename(columns={'neighborhood': 'Neighborhood'})

summary_suspect_18=summary_suspect_18.rename(columns={'amount': 'Amount_18'})

# neighbor_all =pd.merge(df_costs, map_coord_data, on= 'Neighborhood')

#%%

suspect_all =pd.merge(summary_suspect_2, summary_suspect_18, on='datetime') 

#%%

# avg_price_sqr_ft = mean_housing_units_year_all["sale_price_sqr_foot"]
# df_expensive_neighborhoods_per_year = df_costs_year_sorted[df_costs_year_sorted["Neighborhood"].isin(df_expensive_neighborhoods["neighborhood"])]

# sort by date
# summary_suspect_transactions=summary_suspect_transactions.sort_values(['datetime'])

#%%

# select out # 2 transactions only
# suspect_2=suspect_transactions[suspect_transactions['ccd_owner_id']=(2)]




# summary_suspect_2=suspect_2[['datetime', 'amount']]

#%%

query = "SELECT * FROM suspected_25"

# Read the SQL query into a DataFrame
suspect_25 = pd.read_sql(query, engine)

#%%

summary_suspect_25=suspect_25[['datetime', 'amount']]

#%%

# df[["day", "month", "year"]] = df["date"].str.split("/", expand = True)
# print("\nNew DataFrame:")
# print(df)

# df_25_month_day = summary_suspect_25.str.split("/", expand = True)

# summary_suspect_25[["day", "month", "year"]] = summary_suspect_25["datetime"].str.split("/", expand = True)

# pd.concat([df.drop('datetime_utc', axis = 1), 
#          (df.datetime_utc.str.split("-).str[:3].apply(pd.Series)
#          .rename(columns={0:'year', 1:'month', 2:'day'}))], axis = 1)

# pd.concat([summary_suspect_25.drop('datetime'),
#           (summary_suspect_25.dateime.str.split("-).str[:3].apply(pd.Series)
#            .rename(columns={0:'year', 1:'month', 2:'day'}))], axis = 1)    


# row = ('2002-01-02 00:00:00.3453', 'a')
# x = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f")       

#%%

# import datetime # does not work

# row = ('2002-01-02 00:00:00.3453', 'a')
# x = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f")

# summary_suspect_25_new = datetime.strptime(summary_suspect_25[0], "%m-%d")

# summary_suspect_25['month'] = pd.datetime(summary_suspect_25['datetime']).month

#%%

print(summary_suspect_25.dtypes)
# datetime is object!! 

#%%

# summary_suspect_25['datetime'] = pd.to_datetime(summary_suspect_25['datetime'])

query = "SELECT * FROM suspected_25_detail"

# Read the SQL query into a DataFrame
suspect_25_detail = pd.read_sql(query, engine)
print(suspect_25_detail.dtypes)

#%%

# from pyspark.sql.functions import UserDefinedFunction
# from pyspark.sql.types import StringType

#%%
# switch floats to integers

suspect_25_detail.mon = suspect_25_detail.mon.astype(int)
suspect_25_detail.day = suspect_25_detail.day.astype(int)
print(suspect_25_detail.dtypes)

#%%
#3
# udf = UserDefinedFunction(lambda x: month_lst[int(x%12) - 1], StringType())

# new_25_deet = suspect_25_detail.select(*[udf(mon).alias(name) if column == name else column for column in suspect_25_detail.columns])


#%%

import calendar

#%%

for x in range (1, 13):
    print (x, ":", calendar.month_abbr[x], "-", calendar.month_name[x])

x = 4

print (x, ":", calendar.month_abbr[x], "-", calendar.month_name[x])

#%%
# def(loop)

# loop = UserDefinedFunction(lambda x: month_lst[int(x%12) - 1], StringType())

# new_25_deet = suspect_25_detail.select(*[udf(mon).alias(name) 
#        if column == name 
#        else column for column in suspect_25_detail.columns])

# month_name = {January, Februrary, March, April, May, June, July, August, September, October, November, December}

#%%

for item in suspect_25_detail["mon"]:
        nbr=suspect_25_detail["mon"]
        print(nbr)
        suspect_25_detail["mon"]=calendar.month_name[nbr]
            
#%%

for purchase in suspect_25_detail:
    for nbr in suspect_25_detail["mon"]:
        print (nbr)
        if suspect_25_detail["mon"] in month_lst:
            break
        else:
            suspect_25_detail["mon"]=calendar.month_name[nbr]
    
        
#%%
    
for purchase in suspect_25_detail:
    for nbr in suspect_25_detail["mon"]:
        if nbr == name: break
else:
        nbr = calendar.month_name[nbr]     
        
        
        
# for month_lst
            
            

        

