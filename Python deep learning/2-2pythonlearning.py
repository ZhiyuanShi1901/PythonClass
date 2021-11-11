import numpy as np
x = np.array(12)
print(x)
print(x.ndim)

x = np.array([12, 3, 6, 14, 7])  # 1D张量
print(x)
print(x.ndim)  # 输出张量的阶，即轴的个数

x = np.array([[5, 78, 2, 34, 0],  # 2D张量
              [6, 79, 3, 35, 1],
              [7, 80, 4, 36, 2]])
print(x.ndim)

x = np.array([[[5, 78, 2, 34, 0],    # 3D张量
              [6, 79, 3, 35, 1],
              [7, 80, 4, 36, 2]],
              [[5, 78, 2, 34, 0],
               [6, 79, 3, 35, 1],
               [7, 80, 4, 36, 2]],
              [[5, 78, 2, 34, 0],
               [6, 79, 3, 35, 1],
               [7, 80, 4, 36, 2]]
              ])
print(x.ndim)

# 深度学习一般处理0-4D张量，视频数据可能遇到5D张量

from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.ndim) # 轴的个数
print(train_images.shape) # 形状
print(train_images.dtype) # 数据属性

# 显示第四个数字
digit = train_images[4]   # 张量切片：选择特定的元素

import matplotlib.pyplot as plt
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

# 在numpy中操作张量
my_slice = train_images[10:100]
print(my_slice)

'''batch = train_images[:128]
batch = train_images[128:256]
batch = train_images[128 * n:128 * (n + 1)]'''






