import pandas as pd


def clean_data(df):

    # 销量转换数字
    df["销量"] = pd.to_numeric(
        df["销量"],
        errors="coerce"
    )

    # 销售额转换数字
    df["销售额"] = pd.to_numeric(
        df["销售额"],
        errors="coerce"
    )


    # 缺失值处理

    df["销量"] = df["销量"].fillna(
        df["销量"].mean()
    )


    df["销售额"] = df["销售额"].fillna(0)


    return df