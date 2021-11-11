# U2.2
# coding=utf-8

pm2_5 = eval(input("请输入当前的pm2.5的数值："))
if pm2_5 >=0 and pm2_5 <35:
    print("空气优质，快去户外运动！")
elif pm2_5 >=35 and pm2_5 <75:
    print("空气良好，适度户外运动！")
elif pm2_5 >=75:
    print("空气污染，请小心！")
else:
    None
