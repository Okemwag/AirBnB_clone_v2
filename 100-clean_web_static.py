#!/usr/bin/python3
""" Fabric script to clean up .tgz archives
"""
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['35.243.219.137', '35.237.245.133']


def do_clean(number=0):
    """ Removes .tgz files, all but number of most recent files
    """

    with cd("/data/web_static/releases"):
        run("rm -r `ls -td web_static_* | awk 'NR>{}'`".format(number))

    with lcd("/versions"):
        local("rm `ls -td *.tgz | awk 'NR>{}'`".format(number))
