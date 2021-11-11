import numpy as np
import time
import matplotlib.pyplot as plt


def showcontourf(mat, D, cmap=plt.cm.get_cmap('jet'), fsize=(12, 12), vmin=0, vmax=100):  # contourf等高线
    plt.clf()  # 清除所有轴，但是窗口打开，这样它可以被重复使用
    levels = np.arange(vmin, vmax, 1)#返回一个有终点和起点的固定步长的排列
    x = np.linspace(D[0], D[1], mat.shape[1])#在默认情况下，linspace函数可以生成元素为50的等间隔数列。
                                            # 而前两个参数分别是数列的开头与结尾。如果写入第三个参数，可以制定数列的元素个数。
    y = np.linspace(D[2], D[3], mat.shape[0])
    X, Y = np.meshgrid(x, y)#生成网格点坐标矩阵
    z_max = np.max(mat)#求序列的最值
    i_max, j_max = np.where(mat == z_max)[0][0], np.where(mat == z_max)[1][0]
    show_max = "U_max: {:.1f}".format(z_max)
    plt.plot(x[j_max], y[i_max], 'ro')#用于画图它可以绘制点和线, 并且对其样式进行控制.
    plt.contourf(X, Y, mat, 100, cmap=cmap, origin='lower', levels=levels)#画三维等高线图
    plt.annotate(show_max, xy=(x[j_max], y[i_max]), xytext=(x[j_max], y[i_max]), fontsize=14)#用于标注文字
    plt.colorbar()#给子图添加颜色条或渐变色条
    plt.xlabel('x', fontsize=20)#x与y坐标
    plt.ylabel('y', fontsize=20)
    plt.axis('equal')#等长刻度
    plt.draw()
    plt.pause(0.001)#每个图表显示时间
    plt.clf()#清除图表，以便于下一个时间图表的显示


if __name__ == "__main__":
    a = 1
    # 0 <= x <= 12, 0 <= y <= 15
    D = np.array([0, 12, 0, 15])  #
    Mx = 120
    My = 150
    T, Tn = 10, 5
    Nt = 10000

    dx = (D[1] - D[0]) / Mx
    dy = (D[3] - D[2]) / My
    dt = T / Nt
    Frame = 100
    fq = 10
    u0 = 20
    u_env = 20

    # 初始化U、A、B矩阵，各点初始温度u0
    U = u0 * np.ones((My + 1, Mx + 1))
    # x方向二阶导系数矩阵A
    A = (-2) * np.eye(Mx + 1, k=0) + (1) * np.eye(Mx + 1, k=-1) + (1) * np.eye(Mx + 1, k=1)
    # y方向二阶导系数矩阵B
    B = (-2) * np.eye(My + 1, k=0) + (1) * np.eye(My + 1, k=-1) + (1) * np.eye(My + 1, k=1)

    rx, ry, ft = a * dt / dx ** 2, a * dt / dy ** 2, fq * dt
    heat = 1
    start = time.time()
    # 按时间增量逐次计算
    for k in range(Nt + 1):
        tt = k * dt
        # tt>Tn，stop heating
        if tt > Tn: heat = 0

        # solve inside nodes
        U = U + rx * np.dot(U, A) + ry * np.dot(B, U) + heat * ft
        # solve boundary nodes
        U[:, 0] = U[:, -1] = u_env
        U[0, :] = U[-1, :] = u_env

        if k % Frame == 0:
            end = time.time()
            print('T = {:.3f} s    max_U= {:.1f}  min_U = {:.1f}  Heat = {:.1f}  process time = {:.1f}'.format(tt,np.max( U),np.min(U),heat,end - start))
            showcontourf(U, D, vmax=70)