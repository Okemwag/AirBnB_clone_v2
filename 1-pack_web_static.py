#!/usr/bin/python3
""" Fabric script generates .tgz archive
"""
import time
from fabric.api import local


def do_pack():
    """ Archives web_static contents as a tarball to /versions folder
    """
    date_var = time.strftime("%Y%m%d%H%M%S")
    directory = "versions/web_static_{}.tgz".format(date_var)

    try:
        local("mkdir -p ./versions && tar -zcvf ./{} ./web_static"
              .format(directory))
    except:
        return None
    else:
        return directory
