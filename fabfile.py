from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, env, lcd
from fabric.contrib.console import confirm

import os

from local_config import BLOG_DIR

env.BLOG_DIR = BLOG_DIR
env.use_ssh_config = True
env.hosts = ['dod']

def hello(name="world", last=''):
    print("Hello %s %s!" % (name, last))

def status():
    res = local('git status', capture=True)
    if 'Untracked files' in res:
        print res
        if confirm('Untracked files. Add them?'):
            local('git add .')

def commit():
    local("git add -p && git commit")

def push():
    local("git push -u origin master")

def deploy():
    code_dir = env.BLOG_DIR
    with cd(code_dir):
        res = run("git pull")
        if not 'Already up-to-date.' in res:
            run("jekyll build")

def sync():
    status()
    commit()
    push()
    deploy()