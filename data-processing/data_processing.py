# 載入套件
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 設定字體
matplotlib.rc("font", family="Microsoft JhengHei")

# 讀取csv檔案
data = pd.read_csv("graduatesc.csv")

# -- Q1: 各細學類系所數量表 --#
# 統計各細學類出現次數
category_counts = data["細學類名稱"].value_counts()
category_counts_df = pd.DataFrame(
    {"細學類名稱": category_counts.index, "系所數量": category_counts.values}
)
category_counts_df = category_counts_df.sort_values(by="系所數量", ascending=False)

# 儲存與印出圖表
category_counts_df.to_csv("output/各細學類系所數量表.csv", index=False, encoding="big5")
print(category_counts_df.to_string(index=False))

# -- Q2: 各等級別畢業生統計圖 --#
# 以0填補缺失值(" -")，轉換帶有逗號的數字，並轉換數值形態
data = data.replace(" -", 0)
data["上學年畢業生男"] = data["上學年畢業生男"].str.replace(",", "").fillna(0).astype(int)
data["上學年畢業生女"] = data["上學年畢業生女"].str.replace(",", "").fillna(0).astype(int)

# 計算畢業生總計
data["畢業生總計"] = data["上學年畢業生男"] + data["上學年畢業生女"]
total_graduates_by_level = data.groupby("等級別")["畢業生總計"].sum().reset_index()

# 繪製圖表
plt.figure(figsize=(12, 9))
plt.bar(total_graduates_by_level["等級別"], total_graduates_by_level["畢業生總計"])
plt.title("各等級別畢業生統計圖", fontsize=14)
plt.xlabel("等級別", fontsize=14)
plt.ylabel("畢業生總計", fontsize=14)

# 添加實際數值標籤
for i, value in enumerate(total_graduates_by_level["畢業生總計"]):
    plt.text(i, value, str(value), ha="center", va="bottom")

# 儲存與印出圖表
plt.savefig("output/各等級別畢業生統計圖.png")
plt.show()
