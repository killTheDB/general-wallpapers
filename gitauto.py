"""
author: @endormi
Automated Git commands
Automate the process of using commands such as clone, commit, branch, pull, merge, blame and stash
"""

import subprocess
from pyfiglet import figlet_format
from termcolor import cprint


logo = 'Git-Commands'


class color:
    NOTICE = '\033[91m'
    END = '\033[0m'


info = color.NOTICE + '''
Automate the process of using commands such as clone, commit, branch, pull, merge, blame and stash.\n''' + color.END


def run(*args):
    return subprocess.check_call(['git'] + list(args))


def clone():
    print("\nYou will be asked for the user first and then the repository name.\n")

    user = input("User: ")
    __user__ = f'{user}'
    repo = input("Repository: ")
    __repo__ = f'{repo}'

    print("\nChoose the local path for your clone.")
    local = input("Local path: ")
    local_path = f'{local}'

    subprocess.Popen(['git', 'clone', "https://github.com/" + __user__ + "/" + __repo__ + ".git", local_path])


def commit():
    message = input("\nType in your commit message: ")
    commit_message = f'{message}'

    run("commit", "-am", commit_message)
    run("push", "-u", "origin", "master")



def add():
    run("add", ".")


def main():
    cprint(figlet_format(logo, font='slant'), 'green')
    print(info + "\n")

    choices = 'clone, commit, branch, pull, fetch, merge, reset, blame and stash'
    print("Commands to use: " + choices)

    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == "clone":
        clone()

    elif choose_command == "add":
        add()
    elif choose_command == "commit":
        commit()

    else:
        print("\nNot a valid command!")
        print("\nUse " + choices)

if __name__ == '__main__':
    main()