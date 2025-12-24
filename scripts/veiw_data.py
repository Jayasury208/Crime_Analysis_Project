import sqlite3
import pandas as pd

conn = sqlite3.connect("../database/crime.db")

df = pd.read_sql("SELECT * FROM crime_cases", conn)
print(df)

conn.close()
