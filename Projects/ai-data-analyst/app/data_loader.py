import pandas as pd

"""加载CSV文件并返回DataFrame对象。"""
def load_csv(file):
    df=pd.read_csv(file)
    return df