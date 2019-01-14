#!/usr/bin/env python
#-*-coding:utf-8-*-
#AUTH:mingju.xu
#DATE:19-1-10
import jenkins
from json import dumps,loads
import xmltodict
import getpass
import re
jenkins_url = 'http://192.168.100.71:8080'
jenkins_user = 'xumingju'
jenkins_pass = 'xmj123.com'
server = jenkins.Jenkins(jenkins_url,username=jenkins_user, password=jenkins_pass)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
with open('jobs.txt') as jobs:
    for job in jobs.readlines():
        job = job.strip('\n')
        job_deploy = job + "-deploy"
        jnf = server.get_job_config(name=job_deploy)
        jnf1 = dumps(xmltodict.parse(jnf))
        tomcat_url = loads(jnf1)['project']['publishers']['hudson.plugins.deploy.DeployPublisher']['adapters']['hudson.plugins.deploy.tomcat.Tomcat7xAdapter']
        ip_list = re.findall(r'\d+.\d+.\d+.\d+',str(tomcat_url))
        for ip  in ip_list:
            with open("iplist.txt","a") as f:
                f.write(ip + "\n")
                # new_ip = ip.readlines()
                # new_iplist = []
                # for ip in new_ip:
                #     if ip not in new_iplist:
                #         new_iplist.append(ip)
                #         f.write(ip)
            f.close()

