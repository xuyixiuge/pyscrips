#!/usr/bin/env python
#-*-coding:utf-8-*-
#AUTH:mingju.xu
#DATE:18-12-24
import jenkins
import os
import shutil
import time
import getpass
import xml.etree.ElementTree as ET
jenkins_url = 'http://localhost:8080'
jenkins_user = input("请输入Jenkins用户名:")
jenkins_pass = getpass.getpass("请输入jenkins密码:")
new_branch = input("请输入新分支：")
server = jenkins.Jenkins(jenkins_url,username=jenkins_user, password=jenkins_pass)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
date = time.strftime("%Y%m%d-%H:%M:%S",time.localtime())
jobs_path = "/var/lib/jenkins/jobs/"
job_workspace_path = "/var/lib/jenkins/workspace/"
with open('jobs.txt') as jobs:
    for job in jobs.readlines():
        job = job.strip('\n')
        for jobpath, jobnames, jobfile in os.walk(job_workspace_path):
            if jobpath == job_workspace_path:
                for jobname in jobnames:
                    if jobname == (job + "-build"):
                        print("removing workspace of job: {}".format(jobname))
                        shutil.rmtree(os.path.join(jobpath, jobname))
        config = jobs_path + job +'-build/config.xml'
        tree = ET.parse(config)
        root = tree.getroot()
        old_brach = root.getchildren()[4].getchildren()[2].getchildren()[0].getchildren()[0]
        old_brach.text = '*/' + new_branch
        tree.write(config)
        print("^^^^^^开始替换分支^^^^^^")
        os.system("/usr/bin/curl -X POST http://{}:{}@localhost:8080/reload".format(jenkins_user,jenkins_pass))
        time.sleep(5)
        job_build = (job + "-build")
        print("^^^^^^分支替换成功,请检查^^^^^^\n",job_build + ":" + old_brach.text)
        print("^^^^^^开始构建项目^^^^^^")
        server.build_job(job_build)
        num = server.get_job_info(name=job_build)['lastBuild']['number']
        time.sleep(20)
        a = server.get_build_info(name=job_build, number=num)['building']
        if a == True:
            print(job_build + ":\033[1;32m build started! \033[0m" + date)
        else:
            print(job_build + ":\033[1;31m build Faild! \033[0m" + date)
