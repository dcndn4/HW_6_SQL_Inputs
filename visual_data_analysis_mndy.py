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