#!/usr/bin/python3
#-*-coding:utf-8-*-
#AUTH:mingju.xu
#DATE:18-11-19
import jenkins
import time
import getpass
jenkins_url = 'http://127.0.0.1:8080'
jenkins_user = input("请输入Jenkins用户名:")
jenkins_pass = getpass.getpass("请输入jenkins密码:")
server = jenkins.Jenkins(jenkins_url,username=jenkins_user, password=jenkins_pass)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
date = time.strftime("%Y%m%d-%H:%M:%S",time.localtime())
with open('jobs.txt') as jobs:
    for job in jobs.readlines():
        job = job.strip('\n')
        job_deploy = (job + "-deploy")
        server.build_job(job_deploy)
        num = server.get_job_info(name=job_deploy)['lastBuild']['number']
        time.sleep(10)
        a = server.get_build_info(name=job_deploy,number=num)['building']
        if a == True :
            print(job_deploy + ":\033[1;32m build started! \033[0m" + date)
        else:
            print(job_deploy + ":\033[1;31m build Faild! \033[0m" + date)
