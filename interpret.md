# HW 7 - SQL

In this homework assignment, you will apply your new SQL skills to analyze historical credit card transactions and consumption patterns in order to identify possible fraudulent transactions.

You are asked to accomplish three main tasks:

1. Define and create a db model to store the data

2. Create a db schema on PostgreSQL, populate it with .csv files

3. Analyze the data, report your observation

## Instructions

### Data Modeling

Look at the .csv files and create an ERD

Figure out how many tables you need, and the relationships. This [Quick Database Diagrams](https://www.quickdatabasediagrams.com) might help.

### Data Engineering

With the ERD, create a db schema for all tables and relationships. Specify data types, PKs/FKs, etc.

Then, import the .csv data.

### Data Analysis
#### Part 1:

Make a Readme.md report. In it, add queries and answers to the following:

* Some fraudsters hack a credit card by making several small transactions (generally less than $2.00), which are typically ignored by cardholders. 

  * How can you isolate (or group) the transactions of each cardholder?

  * Count the transactions that are less than $2.00 per cardholder. 
  
  * Is there any evidence to suggest that a credit card has been hacked? Explain your rationale.

* Take your investigation a step futher by considering the time period in which potentially fraudulent transactions are made. 

  * What are the top 100 highest transactions made between 7:00 am and 9:00 am?

  * Do you see any anomalous transactions that could be fraudulent?

  * Is there a higher number of fraudulent transactions made during this time frame versus the rest of the day?

  * If you answered yes to the previous question, explain why you think there might be fraudulent transactions during this time frame.

* What are the top 5 merchants prone to being hacked using small transactions?

* Create a view for each of your queries.

#### Part 2:

Edit the [starter notebook](Starter_Files/challenge.ipynb) to query your db, generate visualizations, then add the visualizations and observations to Readme.md.

* The two most important customers of the firm may have been hacked. Verify if there are any fraudulent transactions in their history. For privacy reasons, you only know that their cardholder IDs are 2 and 18.

  * Using hvPlot, create a line plot representing the time series of transactions over the course of the year for each cardholder separately. 
  
  * Next, to better compare their patterns, create a single line plot that contains both card holders' trend data.  

  * What difference do you observe between the consumption patterns? Does the difference suggest a fraudulent transaction? Explain your rationale.

* The CEO of the biggest customer of the firm suspects that someone has used her corporate credit card without authorization in the first quarter of 2018 to pay quite expensive restaurant bills. Again, for privacy reasons, you know only that the cardholder ID in question is 25.

  * Using Plotly Express, create a box plot, representing the expenditure data from January 2018 to June 2018 for cardholder ID 25.
  
  * Are there any outliers for cardholder ID 25? How many outliers are there per month?

  * Do you notice any anomalies? Describe your observations and conclusions.

### Challenge

Look for outliers in the data, using std or quartiles.

Use the [challenge starter notebook](Starter_Files/challenge.ipynb) to code two Python functions:

* One that uses std to identify anomalies for any cardholder.

* One that uses interquartile range to identify anomalies for any cardholder.

### Submission

Post a link to your GitHub repository in BootCamp Spot. The following should be included your repo:

* An image file of your ERD.

* The `.sql` file of your table schemata.

* The `.sql` file of your queries.

* The Jupyter Notebook containing your visual data analysis.

* A ReadME file containing your markdown report.

* **Optional:** The Jupyter Notebook containing the optional challenge assignment.
