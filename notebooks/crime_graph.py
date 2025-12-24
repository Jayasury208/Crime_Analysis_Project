import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("../database/crime.db")
df = pd.read_sql("SELECT * FROM crime_cases", conn)

# ---------- 1️⃣ Area-wise Crime Count ----------
area_count = df['area'].value_counts()
plt.figure(figsize=(10,6))
bars = plt.bar(area_count.index, area_count.values, color='skyblue')
plt.title("📍 Area-wise Crime Count", fontsize=16)
plt.xlabel("Area", fontsize=12)
plt.ylabel("Number of Crimes", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add data labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.3, str(height), ha='center', fontsize=10)

plt.xticks(rotation=45)
plt.show()

# ---------- 2️⃣ Crime Type Distribution ----------
crime_count = df['crime_type'].value_counts()
plt.figure(figsize=(8,8))
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
plt.pie(crime_count.values, labels=crime_count.index, autopct='%1.1f%%', startangle=140, colors=colors, explode=[0.05]*len(crime_count))
plt.title("🔍 Crime Type Distribution", fontsize=16)
plt.show()

# ---------- 3️⃣ Open vs Closed Cases ----------
status_count = df['status'].value_counts()
plt.figure(figsize=(6,5))
bars = plt.bar(status_count.index, status_count.values, color=['orange', 'green'])
plt.title("🟢 Open vs Closed Cases", fontsize=16)
plt.xlabel("Status", fontsize=12)
plt.ylabel("Number of Cases", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add data labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, str(height), ha='center', fontsize=10)

plt.show()

conn.close()
