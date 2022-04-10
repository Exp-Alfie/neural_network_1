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
### accuracy:
![accuracy](https://user-images.githubusercontent.com/83007344/162627576-50638349-6dea-4118-99bc-ed7a353b8e09.png)

### loss:
![loss](https://user-images.githubusercontent.com/83007344/162627619-d651cdfe-4915-4833-9e6c-0c835c0e83f8.png)


### layer1_biases
![layer1_biases](https://user-images.githubusercontent.com/83007344/162627628-672a592d-84dc-43fc-a8c0-2ffc9b6bf26b.png)

### layer2_biases
![layer2_biases](https://user-images.githubusercontent.com/83007344/162627651-a6b98303-e620-4a68-b9b6-04e212113340.png)

### layer1_weights:
![layer1_weights](https://user-images.githubusercontent.com/83007344/162627667-5d3dfba2-0699-4ba1-a64d-f4cb7c53fcdf.png)

### layer2_weights:
![layer2_weights](https://user-images.githubusercontent.com/83007344/162627683-2982387c-10f6-4292-a5f0-41488b9dd9e4.png)


