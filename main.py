import numpy as np
import pandas as pd
import utils
import time
from model import NeuralNetwork

time_start = time.time()


# 优化器
class SGD:

    def __init__(self, model, learning_rate, weight_decay, batch_size):
        self.model = model
        self.lr = learning_rate
        self.weight_decay = weight_decay
        self.batch_size = batch_size

        self.nabla_b = [np.zeros(bias.shape) for bias in self.model.biases]
        self.nabla_w = [np.zeros(weight.shape) for weight in self.model.weights]

    def zero_grad(self):
        self.nabla_b = [np.zeros(bias.shape) for bias in self.model.biases]
        self.nabla_w = [np.zeros(weight.shape) for weight in self.model.weights]

    def update(self, delta_nabla_b, delta_nabla_w):
        self.nabla_b = [nb + dnb for nb, dnb in zip(self.nabla_b, delta_nabla_b)]
        self.nabla_w = [nw + dnw for nw, dnw in zip(self.nabla_w, delta_nabla_w)]

    def step(self):
        # 参数更新
        self.model.weights = [(1 - self.lr * self.weight_decay) * w - (self.lr / self.batch_size) * dw for w, dw in
                              zip(self.model.weights, self.nabla_w)]
        self.model.biases = [(1 - self.lr * self.weight_decay) * b - (self.lr / self.batch_size) * db for b, db in
                             zip(self.model.biases, self.nabla_b)]


np.random.seed(0)

batch_size = 20
epochs = 100
layers = [[784, 25, 10], [784, 35, 10], [784, 45, 10]]
learning_rates = [0.02, 0.03, 0.04]
weight_decaies = [0.01, 0.02, 0.03]  # L2 Penalty

print('加载数据集...')
train_data, val_data, test_data = utils.load_mnist()

print('模型训练中...')
# 参数查找
best_config = {'accuracy': 0}

for layer in layers:
    for learning_rate in learning_rates:
        for weight_decay in weight_decaies:
            print(f"**当前层数: {layer}, 当前学习率: {learning_rate}, 当前权重延迟: {weight_decay}")
            model = NeuralNetwork(layer)
            optimizer = SGD(model, learning_rate, weight_decay, batch_size)
            accuracy = utils.fit(model, optimizer, train_data, val_data, epochs)
            if accuracy > best_config['accuracy']:
                best_config['accuracy'] = accuracy
                best_config['layer'] = layer
                best_config['learning_rate'] = learning_rate
                best_config['weight_decay'] = weight_decay

print("测试中——")
model = NeuralNetwork(best_config['layer'])
model.load(f"model_{best_config['layer'][1]}_{best_config['learning_rate']}_{best_config['weight_decay']}.npz")
utils.test(model, test_data)

print("绘图中——")
log = pd.read_csv(
    f"logs/log_{best_config['layer'][1]}_{best_config['learning_rate']}_{best_config['weight_decay']}.csv")
utils.visualize(model, log)

time_total = time.time() - time_start
print('总耗时：' + str(round(time_total / 3600, 4)) + '小时')


