from fabric.api import (
    cd,
    env,
    require,
    run,
    sudo,
)
from fabric.colors import green

env.use_ssh_config = True

def staging():
    env.host_string = "righttobeoffensive.com"
    env.dir = "/var/www/depl"
    env.git_branch = "develop"

def git_fetch():
    require("dir")

    with cd(env.dir):
        print(green("Fetching."))
        run("git fetch")

def git_reset_hard():
    require("git_branch", "dir")

    with cd(env.dir):
        print(green("Switching branch if needed."))
        run("git checkout {branch}".format(branch=env.git_branch))

        print(green("Updating files to latest version."))
        run("git reset --hard HEAD")

def reload_nginx():
    sudo("nginx -s reload")

def deploy():
    require("host_string", "user", "dir", "git_branch")

    git_fetch()
    git_reset_hard()

    reload_nginx()
