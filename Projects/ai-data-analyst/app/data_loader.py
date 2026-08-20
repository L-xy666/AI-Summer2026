import pandas as pd

"""加载CSV文件并返回DataFrame对象。"""
def load_csv(file_path):
    return pd.read_csv(file_path)