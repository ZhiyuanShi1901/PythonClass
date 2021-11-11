def naive_relu(x):
    assert len(x.shape) == 2

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = max(x[i, j], 0)
    return x

def naice_add(x, y):
    assert len(x.shape) == 2   # x和y是Numpy的2D张量
    assert x.shape == y.shape

    x = x.copy()   # 避免覆盖输入张量
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[i, j]
    return x
'''import numpy as np

z = x + y
z = np.maximum(z, 0.)'''

# 想象向量沿着新轴重复十次
def naive_add_matrix_and_vector(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 1
    assert x.shape[1] == y.shape[0]

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[j]
    return x


# 将逐元素的maximum运算应用于两个形状不同的张量
import numpy as np0
x = np.random.random((64, 3, 32, 10))
y = np.random.random((32, 10))

z = np.maximum(x, y)

z = np.dot(x, y)  # dot实现点积运算

z=x.y





