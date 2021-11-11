# 16.3
# coding=utf-8

import datetime

print("昨天的日期为：{:}".format(datetime.date.today()-datetime.timedelta(days=1)))