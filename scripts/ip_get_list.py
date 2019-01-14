#!/usr/bin/env python
#-*-coding:utf-8-*-
#AUTH:mingju.xu
#DATE:19-1-14
with open("iplist.txt",'r') as f:
    ip_list = f.readlines()
    new_ip = []
    for ip in ip_list:
        if ip not in new_ip:
            new_ip.append(ip)
            print(ip.strip("\n"))
#             f.write(ip)
# f.close()