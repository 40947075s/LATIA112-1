import matplotlib.pyplot as plt

# 示例数据
data = [3, 7, 9, 12, 5]

# 绘制直方图
plt.bar(range(len(data)), data)

# 添加实际数值标签
for i, value in enumerate(data):
    plt.text(i, value, str(value), ha="center", va="bottom")

# 设置X轴标签
plt.xlabel("X轴标签")

plt.savefig("test.png")
