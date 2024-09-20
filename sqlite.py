import pandas as pd
import sqlite3
# step1: creat a connettion to SQLite database
conn = sqlite3.connect('my_database.db')
#step2: create a pandas dataframe
df=pd.read_csv ('https://data.cdc.gov/resource/k2e8-8t3h.csv')
#step3: save the dataframe to the SQLite database
df.to_sql('Cholesterol_in_adults_table', conn, if_exists='replace', index=False)
print("Data has been written to SQLite database.")
print(df.info())
print(df.head())
df['subtopic_id'].value_counts()