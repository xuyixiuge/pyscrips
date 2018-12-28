#!/usr/bin/env python
#-*-coding:utf-8-*-
#AUTH:mingju.xu
#DATE:18-12-26
import jenkins
server = jenkins.Jenkins('http://192.168.100.71:8080', username='xumingju', password='xmj123.com')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
jobs = server._get_view_jobs(name="金融组")
for job in jobs:
    job = job['name']
    print(job)