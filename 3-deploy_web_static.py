#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""

from datetime import datetime
from fabric.api import put, run, env, local
from os.path import exists, isdir
env.hosts = ['34.74.116.197', '3.85.112.73']


def do_pack():
    '''this function generates a .tgz file'''
    now = datetime.utcnow()
    tarWeb_static = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                                  now.month,
                                                                  now.day,
                                                                  now.hour,
                                                                  now.minute,
                                                                  now.second)
    if not isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local('tar -cvzf {} web_static'.format(tarWeb_static)).failed:
        return None
    return tarWeb_static


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    '''that creates and distributes an archive to your web servers,
    using the function deploy'''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
