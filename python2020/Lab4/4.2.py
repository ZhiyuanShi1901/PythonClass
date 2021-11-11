# 4.2
# coding=utf-8
import decimal as dec
condition = True  #设置循环进行的条件
while condition:
    income = input("请输入您的收入，我们将为您计算您的纳税额（输入q停止进行收入的输入）：")
    if income == 'q':
        print("您已结束输入。")
        break
    else:
        income = float(income)-5000
        if income <= 0:
            print("您不需要纳税。")
        elif income <= 3000:
            ratal = income*0.03
        elif income <= 12000:
            ratal = 3000*0.03+(income-3000)*0.10
        elif income <= 25000:
            ratal = 3000*0.03+(12000-3000)*0.10+(income-12000)*0.20
        elif income <= 35000:
            ratal = 3000*0.03+(12000-3000)*0.10+(25000-12000)*0.20+(income - 25000)*0.25
        elif income <= 55000:
            ratal = 3000*0.03+(12000-3000)*0.10+(25000-12000)*0.20+(35000 - 25000)*0.25+(income - 35000)*0.30
        elif income <= 80000:
            ratal = 3000*0.03+(12000-3000)*0.10+(25000-12000)*0.20+(35000 - 25000)*0.25+(55000 - 35000)*0.30 \
                            +(income - 55000)*0.35
        else:
            ratal = 3000*0.03+(12000-3000)*0.10+(25000-12000)*0.20+(35000 - 25000)*0.25+(55000 - 35000)*0.30 \
                            +(80000 - 55000)*0.35+(income - 80000)*0.45
        ratal = dec.Decimal(ratal).quantize(dec.Decimal("0.00"))
        #来自于https://blog.csdn.net/qq_40169708/article/details/99682771?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&dist_request_id=1331979.930.16185739766152741&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control
        print("您的纳税额是：{}".format(ratal))

