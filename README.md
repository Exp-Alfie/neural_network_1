# 代码简介

# main.py

主程序包含：
1、待调整参数：batch_size、epochs,layers：[25,35,45],learning_rates:[0.02, 0.03, 0.04],weight_decaies:[0.01, 0.02, 0.03]等。
2、网格化调整并找到最佳参数组合。
3、优化器SGD。
4、将训练和测试所得loss曲线、准确度曲线以及每层网格参数绘制出来并保存于figs文件夹中。

# model.py

程序包括：
1、定义激活函数、激活梯度函数。
2、定义神经网络类。

# utils

程序包括：
1、定义测试准确度函数。
2、定义拟合函数。
3、定义y结果向量化函数。
4、定义加载mnist数据集函数。
5、定义绘图函数。

# 参数查找
1、主程序遍历layers、learning_rates、weight_decaies，获得最佳超参数为：
	{'accuracy': 94.73, 'layer': [784, 45, 10], 'learning_rate': 0.04, 'weight_decay': 0.01}

# 可视化结果
使用折线图绘制loss和accuracy,使用直方图可视化网格参数。绘制结果保存在figs文件夹中。

# 模型结果


