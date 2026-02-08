import pandas as pd

def clean_data(csv_path):
    df = pd.read_csv(csv_path)

    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df.drop_duplicates()
    df = df.dropna()

    df["total_sales"] = df["price"] * df["quantity"]

    return df
