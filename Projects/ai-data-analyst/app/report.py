def generata_report(df,top_product):
    report = []
    report.append(
        "销售额分析报告"
    )
    report.append(
        f"商品数量：{len(df)}"
    )
    report.appeng(
        f"最高销售额商品：{top_product['product']}"
    )
    report.append(
        f"销售额：{top_product['sales_amount']}"
    )
    content = "\n".join(report)
    with open(
        "outputs/analysis_report.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)