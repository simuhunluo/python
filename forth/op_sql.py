# -*- coding: UTF-8 -*-
"""
作者:scc
时间：2017年   11 月  3 日
实现功能：第四次实训-数据库的基本操作
"""

import MySQLdb
import pandas as pd
import numpy as np
import datetime

db = MySQLdb.connect("localhost", "root", "123qwe", "mytrip")
cursor = db.cursor()
sql = "select t.record_time,max(t.vehicle_speed),t.engine_rpm from tb_iov_device_obd_41030402427 t where Device_ID='41030402427' GROUP BY t.record_time"
cursor.execute(sql)
results = cursor.fetchall()
results = pd.DataFrame(list(results), columns=['record_time', 'vehicle_speed', 'engine_rpm'])
i = 1
trip = 1

results['trip'] = -1
results['Time_diff'] = -1
print "大小是"
size = results.size / 5
print results.size
try:
    while i < size:
        t1 = str(results.iloc[i - 1, 0])
        t2 = str(results.iloc[i, 0])
        date_time1 = datetime.datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
        date_time2 = datetime.datetime.strptime(t2, '%Y-%m-%d %H:%M:%S')
        dif = (date_time2 - date_time1).total_seconds()
        if dif > 600:
            trip = trip + 1
        if dif > 0:
            results.iloc[i, 3] = trip
            results.iloc[i, 4] = dif
        i += 1
    else:
        print "循环到头了"

except IndexError:
    print "越界错误："
    print i
else:
    print "无异常发生"

i = 0
while i < results.size / 5:
    if results.iloc[i, 3] < 0:
        results.iloc[i, 3] = 'BAD'
    i += 1
print results.head()
print "分割"
results['vehicle_speed']=results['vehicle_speed']/3.6
print results.head()

while i < results.size / 5:
    print ""
db.close()
