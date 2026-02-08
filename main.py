from scripts.data_cleaning import clean_data
from scripts.analysis import statistical_analysis
from scripts.sql_queries import store_data, revenue_by_category

df = clean_data("data/sales_data.csv")

print("\n📊 Statistical Analysis")
stats = statistical_analysis(df)

for k, v in stats.items():
    print(f"{k}: {v}")

store_data(df)

print("\n💾 Revenue by Category (SQL Results)")
for row in revenue_by_category():
    print(row)
