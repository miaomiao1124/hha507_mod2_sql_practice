import pandas as pd
import sqlite3
# step1: creat a connettion to SQLite database
conn = sqlite3.connect('my_database.db')
#step2: create a pandas dataframe
df=pd.read_csv ('https://data.cdc.gov/resource/k2e8-8t3h.csv')
df['topic'].value_counts()
#step3: save the dataframe to the SQLite database
df.to_sql('Cholesterol_in_adults_table', conn, if_exists='replace', index=False)
print("Data has been written to SQLite database.")
print(df.info())
print(df.head())
#step4:Query the table to verify the data
query_1='SELECT* FROM Cholesterol_in_adults_table'
query_2='SELECT SUBTOPIC FROM Cholesterol_in_adults_table WHERE GROUP=Total'
#saving the string into the query variable. 
#this is a example how we could write a raw SQL query
#save it as Python string, and use pandas to execute that query
result_df =pd.read_sql(query_1, conn)
result_df =pd.read_sql(query_2, conn)

#query is the variable name, conn represents the database, where the data from

#step5: display the results

print(result_df)
# close the connection
conn.close()
