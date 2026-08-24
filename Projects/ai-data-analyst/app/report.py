from app.llm import generate_ai_analysis


def generate_report(
        df,
        info,
        stats,
        top_product,
        ranking
):
    report = []
    report.append(
        "销售额分析报告"
    )
    report.append(
        "="*30
    )
    report.append(
        f"商品数量：{len(df)}"
    )
    report.append(
        f"数据行数：{info['rows']}"
    )
    report.append(
        f"数据列数：{info['columns']}"
    )
    report.append(
        ""
    )
    report.append(
        "销售统计"
    )
    report.append(
        f"平均销量：{stats['average_sales']:.2f}"
    )


    report.append(
        f"最大销量：{stats['max_sales']}"
    )


    report.append(
        f"最小销量：{stats['min_sales']}"
    )


    report.append(
        ""
    )


    report.append(
        "最佳商品"
    )


    report.append(
        f"商品名称：{top_product['product']}"
    )


    report.append(
        f"销售额：{top_product['sales_amount']}"
    )

    report.append(
        ""
    )

    ai_analysis=generate_ai_analysis(
        df,
        stats,
        top_product
    )

    report.append(
        ai_analysis
    )

    report.append(
        ""
    )

    report.append(
        "销售排行榜"
    )
    
    for index,row in ranking.iterrows():

        report.append(
            f"{index+1}. {row['商品']} {row['销售额']}"
        )
    content = "\n".join(report)
    with open(
        "outputs/analysis_report.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)
    print("分析报告生成完成")