# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

plt.rc("font", family="SimSun")

# 准备绘制数据
activity = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 56, 56, 52, 62, 60, 60, 60, 58, 60, 58, 62, 58, 64]
res_use_score = [52, 54, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 89, 89, 89, 89, 91, 94, 91]
score = [69, 69, 94, 95, 95, 95, 95, 95, 95, 95, 95, 71, 74, 73, 75, 73, 74, 71, 74, 74, 72, 74, 72, 73]
avg_score = [69, 69, 77, 86, 94, 94, 94, 94, 94, 94, 95, 92, 89, 86, 84, 81, 78, 75, 73, 73, 73, 73, 73, 73]
stats_date = ["2023-01-18", "2023-01-19", "2023-01-25", "2023-01-26", "2023-01-27", "2023-01-28", "2023-01-29",
              "2023-01-30", "2023-01-31", "2023-02-01", "2023-02-02", "2023-02-03", "2023-02-04", "2023-02-05",
              "2023-02-06", "2023-02-07", "2023-02-08", "2023-02-09", "2023-02-10", "2023-02-11", "2023-02-12",
              "2023-02-13", "2023-02-14", "2023-02-15"]

plt.plot(stats_date, activity, c="blue", marker="D", markersize=2, label="活跃度评分")
plt.plot(stats_date, res_use_score, c="green", marker="D", markersize=2, label="资源利用评分")
plt.plot(stats_date, score, c="orange", marker="D", markersize=2, label="综合评分")
plt.plot(stats_date, avg_score, c="red", marker="D", markersize=2, label="周平均分")

# 绘制坐标轴标签
plt.xlabel("日期")
plt.title("月度评分趋势")
# 显示图例
plt.legend(loc="best")
# 调用 text()在图像上绘制注释文本
# x1、y1表示文本所处坐标位置，ha参数控制水平对齐方式, va控制垂直对齐方式，str(y1)表示要绘制的文本
# for x1, y1 in zip(x, y):
#     plt.text(x1, y1, str(y1), ha="center", va="bottom", fontsize=10)
# 保存图片
plt.savefig("2.jpg")
