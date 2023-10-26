# import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 讀取csv檔案
data = pd.read_csv("graduatesc.csv")

# 以0填補缺失值
data = data.replace(" -", 0)

# Q1: 各細學類系所數量表
category_counts = data["細學類名稱"].value_counts()
category_counts_df = pd.DataFrame(
    {"細學類名稱": category_counts.index, "系所數量": category_counts.values}
)
category_counts_df = category_counts_df.sort_values(by="系所數量", ascending=False)

print(category_counts_df)
category_counts_df.to_csv("各細學類系所數量表.csv", index=False, encoding="big5")
