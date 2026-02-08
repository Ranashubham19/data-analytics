import numpy as np

def statistical_analysis(df):
    stats = {
        "total_revenue": np.sum(df["total_sales"]),
        "average_order_value": np.mean(df["total_sales"]),
        "max_order_value": np.max(df["total_sales"]),
        "min_order_value": np.min(df["total_sales"]),
        "std_dev_sales": np.std(df["total_sales"])
    }
    return stats