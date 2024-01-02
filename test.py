import pandas as pd
import numpy as np
import os

# 文件列表
files = ['AlohomoraCharm.csv', 'ArrestoMomentumCharm.csv', 'AvadaKedavra.csv', 'LocomotorCharm.csv', 'Revelio.csv']

# 创建空的DataFrame用于存储数据
df = pd.DataFrame(columns=['label', 'data'])

# 遍历每个文件
for file in files:
    # 读取CSV文件
    data = pd.read_csv(file, header=None)

    # 获取标签名（去掉.csv后缀）
    label = file.split('.')[0]

    # 分割样本，每119行一个样本
    for i in range(0, len(data), 120):  # 假设每个样本后有一个空行
        # 获取样本数据
        sample = data.iloc[i:i+119]

        # 将样本数据转换为numpy数组
        sample_data = sample.to_numpy()

        # 将标签和样本数据添加到DataFrame
        df = df.append({'label': label, 'data': sample_data}, ignore_index=True)

# 显示DataFrame
print(df)

