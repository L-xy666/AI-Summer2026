import pandas as pd

"""求出数据集的基本信息，包括行数和列数，以及销量的平均值、最大值和最小值。"""
def get_basic_info(df):
    return{
        "rows":len(df),
        "columns":len(df.columns)
    }

def get_sales_statistics(df):
    return{
        "averages_sales":df["销量"].mean(),
        "max_sales":df["销量"].max(),
        "min_sales":df["销量"].min()
    }

"""求出销售额最高的商品及其销售额。"""
def get_top_product(df):
    top_index = df["销售额"].idxmax()

    return {
        "product":df.loc[top_index,"商品"],
        "sales_amount":df.loc[top_index,"销售额"]
    }