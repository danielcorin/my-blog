from __future__ import with_statement
from fabric.api import local, run, cd, env, abort
from fabric.contrib.console import confirm

# path to blog on my server
from local_config import BLOG_DIR

env.BLOG_DIR = BLOG_DIR
env.use_ssh_config = True

# specfic Host from ssh config
env.hosts = ['dod']


def add():
    '''
    Check git branch status.
    If branch is dirty, add all unstaged files.
    '''
    res = local('git status', capture=True)
    if 'Untracked files' in res or 'Changes not staged for commit' in res:
        print(res)
        if confirm('Changes not staged. Add files?'):
            local('git add .')
        else:
            abort('Aborted. Changes not staged.')


def commit():
    local("git commit")


def push(b_from='origin', b_to='master'):
    local("git push -u {} {}".format(b_from, b_to))


def deploy():
    '''
    Pull down changes from repo and build the blog on the server
    '''
    code_dir = env.BLOG_DIR
    with cd(code_dir):
        res = run("git pull")
        if 'Already up-to-date.' not in res:
            run("jekyll build")


def sync():
    add()
    commit()
    push()
    deploy()
