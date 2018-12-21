#!/usr/bin/env python
#-*-coding:utf-8-*-
#AUTH:mingju.xu
#DATE:18-12-21
import pymysql
import sys
import getpass
import time
import csv
dbhost = sys.argv[1]
dbuser = input("请输入用户名：")
dbpass = getpass.getpass("请输入密码：")
conn = pymysql.connect(dbhost,dbuser,dbpass)
cursor = conn.cursor()
print("Login database " + dbhost)
cursor.execute("show databases")
dbs = cursor.fetchall()
excludedb = ['mysql','sys','performance_schema','information_schema']
for (db,) in dbs:
    if db in excludedb:
        time.sleep(1)
    else:
        conn.select_db(db)
        cursor.execute("show tables")
        tables = cursor.fetchall()
        with open(dbhost + "_tables.csv", "w") as csvfile:
            for (table,) in tables:
                writer = csv.writer(csvfile)
                writer.writerow([dbhost,db,table])
        csvfile.close()
conn.close()