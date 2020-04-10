#!/usr/bin/python3
''' Write a Fabric script that generates a .tgz archive
from the contents of the web_static'''
import datetime
from fabric.api import local
from os import path


def do_pack():
    '''this function generates a .tgz file'''
    now = datetime.datetime.utcnow
    tarDate = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                            now.month,
                                                            now.day,
                                                            now.hour,
                                                            now.minute,
                                                            now.second)
    if not path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local('tar -cvzf {} web_static'.format(tarDate)).failed:
        return None
    return tarDate
