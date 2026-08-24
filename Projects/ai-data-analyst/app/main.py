from app.data_loader import load_csv
from app.analyzer import (
    get_basic_info,
    get_sales_statistics,
    get_top_product,
    get_sales_ranking,
    get_sales_ratio
)
from app.visualization import(
    draw_sales_bar,
    draw_sales_pie
)
import os
from app.report import generate_report

# 确保输出目录存在
os.makedirs("outputs", exist_ok=True)

"""主程序入口，加载数据并进行分析。"""
df = load_csv("data/raw/sales_big.csv")
df["销售额占比"] = get_sales_ratio(df)
display_df = df.copy()
display_df["销售额占比"] = display_df["销售额占比"].map(lambda x:f"{x:.2%}")
print(display_df)

info = get_basic_info(df)
print("数据行数：",info["rows"])
print("数据列数：",info["columns"])

stats = get_sales_statistics(df)
print("平均销量：",stats["average_sales"])
print("最大销量：",stats["max_sales"])
print("最小销量：",stats["min_sales"])

top_product = get_top_product(df)
print("销售额最高的商品：",top_product["product"])
print("最高销售额：",top_product["sales_amount"])

ranking = get_sales_ranking(df).copy()
ranking["销售额占比"] =ranking["销售额占比"].map(lambda x:f"{x:.2%}")
print("\n销售额排行榜：")
print(ranking)


draw_sales_bar(df)
draw_sales_pie(df)
print("图表生成完成")

generate_report(
    df,
    info,
    stats,
    top_product,
    ranking
)