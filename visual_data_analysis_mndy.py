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

summary_suspect_18=suspect_18[['datetime', 'amount']]
summary_suspect_18=summary_suspect_18.sort_values(['datetime'])

#%%

# avg_price_sqr_ft = mean_housing_units_year_all["sale_price_sqr_foot"]
# df_expensive_neighborhoods_per_year = df_costs_year_sorted[df_costs_year_sorted["Neighborhood"].isin(df_expensive_neighborhoods["neighborhood"])]

# sort by date
# summary_suspect_transactions=summary_suspect_transactions.sort_values(['datetime'])

#%%

# select out # 2 transactions only
# suspect_2=suspect_transactions[suspect_transactions['ccd_owner_id']=(2)]


