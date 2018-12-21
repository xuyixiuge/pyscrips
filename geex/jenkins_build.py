#!/usr/bin/env python
#-*-coding:utf-8-*-
#AUTH:mingju.xu
#DATE:18-12-20
from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'http://172.17.0.3:8080/'
    server = Jenkins(jenkins_url, username = 'admin', password = 'admin')
    return server
def get_job_details():
    server = get_server_instance()
    for j in server.get_jobs():
        job_instance = server.get_job(j[0])
        print("Job Name:{}".format(job_instance.name))
        print("Job Description:{}".format(job_instance.get_description()))
        print("Is Job running:{}".format(job_instance.is_running()))
        print("Is Job enabled:{}".format(job_instance.is_enabled()))
if __name__ == '__main__':
    get_job_details()
