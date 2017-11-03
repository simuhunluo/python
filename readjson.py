# -*- coding: UTF-8 -*-
"""
作者:scc
时间：2017年   11 月  3 日
实现功能：第四次实训-数据库的基本操作
"""

import MySQLdb

db = MySQLdb.connect("localhost", "root", "123qwe", "mytrip")
cursor = db.cursor()
sql="SELECT t.record_time,max(t.vehicle_speed),t.engine_rpm FROM tb_iov_device_obd_41030402427 t where t.device_id='41030402427' GROUP BY t.record_time";
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for rows in results:
        print rows[0]+rows[1]+rows[2]
except:
    print "Error:fecth data failed"


db.close()
