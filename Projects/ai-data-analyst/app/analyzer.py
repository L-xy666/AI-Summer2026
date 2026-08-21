import pandas as pd


def get_basic_info(df):
    """获取数据集的基本信息，包括行数和列数。"""
    return {
        "rows":len(df),
        "columns":len(df.columns)
    }

def get_sales_statistics(df):
    """计算销量的平均值、最大值和最小值。"""
    return {
        "average_sales":df["销量"].mean(),
        "max_sales":df["销量"].max(),
        "min_sales":df["销量"].min()
    }

def get_top_product(df):
    """获取销售额最高的商品及其销售额。"""

    #获取销售额最高的商品所在的行索引。
    top_index = df["销售额"].idxmax()
    return {
        "product":df.loc[top_index,"商品"],
        "sales_amount":df.loc[top_index,"销售额"]
    }

def get_sales_ranking(df):
    """按照销售额从高到低对商品进行排序，并重置索引。"""
    return df.sort_values("销售额",ascending=False).reset_index(drop=True)

def get_sales_ratio(df):
    """计算每个商品的销售额占总销售额的比例。"""
    total_sales = df["销售额"].sum()
    return df["销售额"]/total_sales