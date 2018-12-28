#!/usr/bin/python3
#AUTH:mingju.xu
#DATE:2018/12/4
import os
import shutil
job_workspace_path = "/var/lib/jenkins/workspace/"
with open('jobs.txt') as jobs:
    for job in jobs.readlines():
        job = job.strip('\n')
        for jobpath, jobnames, jobfile in os.walk(job_workspace_path):
            if jobpath == job_workspace_path:
                for jobname in jobnames:
                    if jobname == job:
                        print("removing workspace of job: %s" %jobname)
                        shutil.rmtree(os.path.join(jobpath, jobname))
