import numpy as np
import time
import matplotlib.pyplot as plt




def showcontourf(mat, D, cmap=plt.cm.get_cmap('jet'), fsize=(12, 12), vmin=0, vmax=100):
    plt.clf()
    levels = np.arange(vmin, vmax, 1)
    x = np.linspace(D[0], D[1], mat.shape[1])
    y = np.linspace(D[2], D[3], mat.shape[0])
    X, Y = np.meshgrid(x, y)
    z_max = np.max(mat)
    i_max, j_max = np.where(mat == z_max)[0][0], np.where(mat == z_max)[1][0]
    show_max = "U_max: {:.1f}".format(z_max)
    plt.plot(x[j_max], y[i_max], 'go')
    plt.contourf(X, Y, mat, 100, cmap=cmap, origin='lower', levels=levels)
    plt.annotate(show_max, xy=(x[j_max], y[i_max]), xytext=(x[j_max], y[i_max]), fontsize=14)
    plt.colorbar()
    plt.xlabel('x', fontsize=20)
    plt.ylabel('y', fontsize=20)
    plt.axis('equal')
    plt.draw()
    plt.pause(0.001)
    plt.clf()

    if __name__ == "__main__":
        a = 1
        D = np.array([0, 15, 0, 15])
        Mx = 150
        My = 150
        T, Tn = 20, 5
        Nt = 20000

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

        # 用网格化映射矩阵坐标信息
        x = np.linspace(D[0], D[1], U.shape[1])
        y = np.linspace(D[2], D[3], U.shape[0])
        X, Y = np.meshgrid(x, y)
        x0, y0 = 0, 7  # 热源中心位置

        ### 按时间增量逐次计算
        for k in range(Nt + 1):
            tt = k * dt
            # 热源沿着X方向移动
            x0 += 2 * dt
            Qv = 80 * fq * np.exp(-8 * ((X - x0) ** 2 + (Y - y0) ** 2))
            # solve inside nodes
            U = U + dx * np.dot(U, A) + dy * np.dot(B, U) + Qv * dt
            # solve boundary nodes
            # U[:, 0] = U[:, -1] = u_env
            # U[0, :] = U[-1, :] = u_env

            # solve boundary nodes
            U[:, 0] = U[:, -1] = u_env
            U[0, :] = U[-1, :] = u_env

            # 用等温云图显示一下计算结果

    if k % Frame == 0:
        end = time.time()
        start = 0
        print('T = {:.3f} s  process time = {:.1f}'.format(tt, end - start))
        showcontourf(U, D, vmax=120)



