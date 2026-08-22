import matplotlib.pyplot as plt
import matplotlib


# 设置中文字体
matplotlib.rcParams["font.family"]="SimHei"
# 设置负号正常显示
matplotlib.rcParams["axes.unicode_minus"]=False

def draw_sales_bar(df):
    """绘制商品销售额柱状图"""
    plt.figure(figsize=(8,5))
    plt.bar(
        df["商品"],
        df["销售额"],
    )
    plt.title("商品销售额分析")
    plt.xlabel("商品")
    plt.ylabel("销售额")

    #在柱状图上显示每个柱子的数值
    for i,value in enumerate(df["销售额"]):
        plt.text(
            i,
            value,
            f"{value:,}",
            ha="center",
            va="bottom"
        )

    #设置y轴的范围，使柱状图更美观
    plt.ylim(
        0,
        df["销售额"].max()*1.15
    )

    plt.savefig("outputs/sales_bar.png")
    plt.close()

def draw_sales_pie(df):
    """绘制商品销售额占比饼图"""
    plt.figure(figsize=(6,6))
    plt.pie(
        df["销售额"],
        labels=df["商品"],
        autopct="%1.2f%%"
    )

    plt.title("商品销售额占比")
    plt.savefig("outputs/sales_pie.png")
    plt.close()