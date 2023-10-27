# 載入套件
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 設定字體
matplotlib.rc("font", family="Microsoft JhengHei")

# 讀取csv檔案
data = pd.read_csv("graduatesc.csv")

# 以0填補缺失值(" -")，轉換帶有逗號的數字，並轉換數值形態
data = data.replace(" -", 0)
data["上學年畢業生男"] = data["上學年畢業生男"].str.replace(",", "").fillna(0).astype(int)
data["上學年畢業生女"] = data["上學年畢業生女"].str.replace(",", "").fillna(0).astype(int)

# -- Q1: 各細學類系所數量表 -- #
# 統計各細學類出現次數
category_counts = data["細學類名稱"].value_counts()
category_counts_df = pd.DataFrame(
    {"細學類名稱": category_counts.index, "系所數量": category_counts.values}
)
category_counts_df = category_counts_df.sort_values(by="系所數量", ascending=False)

# 儲存與印出圖表
category_counts_df.to_csv("output/各細學類系所數量表.csv", index=False, encoding="big5")
print(category_counts_df.to_string(index=False))

# -- Q2: 各進修別畢業生統計圖 -- #
# 計算畢業生總計
data["畢業生總計"] = data["上學年畢業生男"] + data["上學年畢業生女"]
total_graduates_by_study = data.groupby("日間_進修別")["畢業生總計"].sum().reset_index()

# 繪製圖表
plt.figure(figsize=(12, 9))
plt.bar(
    total_graduates_by_study["日間_進修別"],
    total_graduates_by_study["畢業生總計"],
)
plt.title("各日間_進修別畢業生統計圖", fontsize=14)
plt.xlabel("日間_進修別", fontsize=14)
plt.ylabel("畢業生總計", fontsize=14)

# 添加實際數值標籤
for i, value in enumerate(total_graduates_by_study["畢業生總計"]):
    plt.text(i, value, str(value), ha="center", va="bottom")

# 儲存與印出圖表
plt.savefig("output/各日間_進修別畢業生統計圖.png")
plt.show()

# -- Q3: 各等級別畢業生統計圖 -- #
# 計算畢業生總計
data["畢業生總計"] = data["上學年畢業生男"] + data["上學年畢業生女"]
total_graduates_by_level = data.groupby("等級別")["畢業生總計"].sum().reset_index()

# 繪製圖表
plt.figure(figsize=(12, 9))
plt.bar(
    total_graduates_by_level["等級別"],
    total_graduates_by_level["畢業生總計"],
)
plt.title("各等級別畢業生統計圖", fontsize=14)
plt.xlabel("等級別", fontsize=14)
plt.ylabel("畢業生總計", fontsize=14)

# 添加實際數值標籤
for i, value in enumerate(total_graduates_by_level["畢業生總計"]):
    plt.text(i, value, str(value), ha="center", va="bottom")

# 儲存與印出圖表
plt.savefig("output/各等級別畢業生統計圖.png")
plt.show()

# -- Q4: 畢業生男女比例圓餅圖 -- #
# 計算男女畢業生總數
male_graduates = data["上學年畢業生男"].sum()
female_graduates = data["上學年畢業生女"].sum()


# 客製標籤
def q4_labels(s, d):
    val = int(round(s / 100.0 * sum(d)))
    return f"{s:.1f}%\n( {val}人 )"


# 繪製圖表
plt.pie(
    [male_graduates, female_graduates],
    labels=["男", "女"],
    colors=["lightblue", "lightpink"],
    autopct=lambda i: q4_labels(i, [male_graduates, female_graduates]),
    startangle=90,
    shadow=True,
    explode=(0.1, 0),
)
plt.title("畢業生男女比例圓餅圖", fontsize=14)

# 儲存與印出圖表
plt.savefig("output/畢業生男女比例圓餅圖.png")
plt.show()

# -- Q5: 各進修別男女畢業生人數統計圖 -- #
# 計算各進修別畢業生男女人數
graduates_by_study = data.groupby("日間_進修別")[["上學年畢業生男", "上學年畢業生女"]].sum().reset_index()

# 設定直條寬度、x軸刻度、x軸標籤
bar_width = 0.35
x = range(len(graduates_by_study))
plt.xticks([i + bar_width / 2 for i in x], graduates_by_study["日間_進修別"])

# 繪製圖表
plt.bar(
    x,
    graduates_by_study["上學年畢業生男"],
    width=bar_width,
    label="男",
    color="lightblue",
)
plt.bar(
    [i + bar_width for i in x],
    graduates_by_study["上學年畢業生女"],
    width=bar_width,
    label="女",
    color="lightpink",
)

plt.title("各進修別男女畢業生人數統計圖")
plt.xlabel("進修別")
plt.ylabel("畢業生人數")
plt.legend()

# 添加實際數值標籤
for i, v in enumerate(graduates_by_study["上學年畢業生男"]):
    plt.text(i, v + 5, str(v), ha="center", va="bottom", fontsize=10)
for i, v in enumerate(graduates_by_study["上學年畢業生女"]):
    plt.text(i + bar_width, v + 5, str(v), ha="center", va="bottom", fontsize=10)

# 儲存與印出圖表
plt.savefig("output/各進修別男女畢業生人數統計圖.png")
plt.show()

# -- Q6: 各等級別男女畢業生人數統計圖 -- #
# 計算各等級別畢業生男女人數
graduates_by_level = data.groupby("等級別")[["上學年畢業生男", "上學年畢業生女"]].sum().reset_index()

# 設定直條寬度、x軸刻度、x軸標籤
bar_width = 0.4
x = range(len(graduates_by_level))
plt.xticks([i + bar_width / 2 for i in x], graduates_by_level["等級別"])

# 繪製圖表
plt.bar(
    x,
    graduates_by_level["上學年畢業生男"],
    width=bar_width,
    label="男",
    color="lightblue",
)
plt.bar(
    [i + bar_width for i in x],
    graduates_by_level["上學年畢業生女"],
    width=bar_width,
    label="女",
    color="lightpink",
)

plt.title("各等級別男女畢業生人數統計圖")
plt.xlabel("等級別")
plt.ylabel("畢業生人數")
plt.legend()

# 添加實際數值標籤
for i, v in enumerate(graduates_by_level["上學年畢業生男"]):
    plt.text(i, v + 5, str(v), ha="center", va="bottom", fontsize=10)
for i, v in enumerate(graduates_by_level["上學年畢業生女"]):
    plt.text(i + bar_width, v + 5, str(v), ha="center", va="bottom", fontsize=10)

# 儲存與印出圖表
plt.savefig("output/各等級別男女畢業生人數統計圖.png")
plt.show()
