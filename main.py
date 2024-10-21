import pandas as pd
import matplotlib.pyplot as plt

file_path = 'comptagevelo2014.csv'
df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

df['Month'] = df['Date'].dt.month

df['Total_Visits'] = df.iloc[:, 1:].sum(axis=1)
monthly_visits = df.groupby('Month')['Total_Visits'].sum()

most_popular_month = monthly_visits.idxmax()

print(f"The most popular month for cyclists in 2014 is: {most_popular_month}")

plt.figure(figsize=(10, 6))
monthly_visits.plot(kind='bar', color='skyblue')
plt.title('Monthly Bicycle Path Usage in 2014')
plt.xlabel('Month')
plt.ylabel('Number of Visits')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
