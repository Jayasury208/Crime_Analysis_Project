import pandas as pd
import sqlite3

# Load CSV file
df = pd.read_csv("../data/crime_data.csv")

# Connect to database
conn = sqlite3.connect("../database/crime.db")

# Insert data
df.to_sql("crime_cases", conn, if_exists="replace", index=False)

print("✅ Data inserted successfully")

conn.close()
