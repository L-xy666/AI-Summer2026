def build_analysis_prompt(
        df,
        stats,
        top_product
):

    prompt=f"""
你是一名专业的数据分析师。

你正在分析的是一个普通商品销售数据表，
不是公司财报，也不是苹果公司。

请根据以下销售数据生成商业分析建议：

商品数量：
{len(df)}

平均销量：
{stats['average_sales']}

最高销量：
{stats['max_sales']}

最低销量：
{stats['min_sales']}

销售额最高商品：
{top_product['product']}

该商品销售额：
{top_product['sales_amount']}


请输出：

1. 当前销售情况分析
2. 热销商品原因分析
3. 后续销售优化建议


要求：
- 面向企业销售人员
- 简洁专业
- 不要编造不存在的数据
"""

    return prompt