import streamlit as st
import os

from app.data_loader import load_csv

from app.analyzer import (
    get_basic_info,
    get_sales_statistics,
    get_top_product,
    get_sales_ranking
)

from app.visualization import (
    draw_sales_bar,
    draw_sales_pie
)

from app.cleaner import clean_data
from app.report import generate_report
from app.llm import generate_ai_analysis


# 页面设置
st.set_page_config(
    page_title="AI Data Analyst",
    layout="wide"
)


st.title("AI Data Analyst")

st.write(
    "基于 Python 的智能数据分析系统"
)


# 上传文件
uploaded_file = st.file_uploader(
    "上传CSV文件",
    type=["csv"]
)


if uploaded_file:

    # ======================
    # 数据读取与清洗
    # ======================

    df = load_csv(uploaded_file)

    df = clean_data(df)


    # 数据预览

    st.subheader(
        "数据预览"
    )

    st.dataframe(df)



    # ======================
    # 数据概览
    # ======================

    info = get_basic_info(df)


    st.subheader(
        "数据概览"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "数据行数",
            info["rows"]
        )


    with col2:

        st.metric(
            "数据列数",
            info["columns"]
        )



    # ======================
    # 销售统计
    # ======================

    stats = get_sales_statistics(df)


    st.subheader(
        "销售统计"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "平均销量",
            stats["average_sales"]
        )


    with col2:

        st.metric(
            "最大销量",
            stats["max_sales"]
        )


    with col3:

        st.metric(
            "最小销量",
            stats["min_sales"]
        )



    # ======================
    # 最佳商品
    # ======================

    top_product = get_top_product(df)


    st.subheader(
        "最佳商品"
    )


    st.success(
        f"{top_product['product']}  销售额：{top_product['sales_amount']}"
    )



    # ======================
    # 销售排行榜
    # ======================

    ranking = get_sales_ranking(df)


    st.subheader(
        "销售额排行榜"
    )


    st.dataframe(
        ranking
    )









    # ======================
    # 生成普通报告
    # ======================

    generate_report(
        df,
        info,
        stats,
        top_product,
        ranking
    )



    # ======================
    # 数据可视化
    # ======================

    draw_sales_bar(df)

    draw_sales_pie(df)



    st.subheader(
        "数据可视化"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.image(
            "outputs/sales_bar.png",
            caption="商品销售额分析"
        )


    with col2:

        st.image(
            "outputs/sales_pie.png",
            caption="销售额占比"
        )


    # ======================
    # AI分析
    # ======================

    if st.button("开始AI分析"):
        with st.spinner("🤖 AI正在分析数据，请稍候..."):

            ai_text = generate_ai_analysis(
                df,
                stats,
                top_product
            )


        st.subheader(
            "AI数据分析"
        )


        st.markdown(
            ai_text
        )



    # ======================
    # 下载报告
    # ======================

    if os.path.exists(
        "outputs/analysis_report.txt"
    ):

        with open(
            "outputs/analysis_report.txt",
            "r",
            encoding="utf-8"
        ) as f:

            report_content = f.read()


        st.download_button(
            label="下载分析报告",
            data=report_content,
            file_name="analysis_report.txt",
            mime="text/plain"
        )



else:

    st.info(
        "请上传CSV文件开始分析"
    )