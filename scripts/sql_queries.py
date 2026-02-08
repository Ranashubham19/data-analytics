import sqlite3

def store_data(df):
    conn = sqlite3.connect("database/analytics.db")
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()

def revenue_by_category():
    conn = sqlite3.connect("database/analytics.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(total_sales) AS revenue
        FROM sales
        GROUP BY category
    """)

    results = cursor.fetchall()
    conn.close()
    return results
