from app.data_loader import load_csv
from app.analyzer import get_basic_info,get_sales_statistics,get_top_product

df = load_csv("data/raw/test.csv")
print(df)
info = get_basic_info(df)
print("数据行数：",info["rows"])
print("数据列数：",info["columns"])

stats = get_sales_statistics(df)
print("平均销量：",stats["averages_sales"])
print("最大销量：",stats["max_sales"])
print("最小销量：",stats["min_sales"])

top_product = get_top_product(df)
print("销售额最高的商品：",top_product["product"])
print("最高销售额：",top_product["sales_amount"])