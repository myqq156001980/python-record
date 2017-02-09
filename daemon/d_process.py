import os
import sys
import atexit
import time


def daemonize(pid_file=None):
    pid = os.fork()

    if pid > 0:
        print("the pid is {0} and ppid is {1}".format(os.getpid(), os.getppid()))
        print(pid)
        sys.exit()
    elif pid == 0:
        print("the pid is {0} and ppid is {1}".format(os.getpid(), os.getppid()))
        print(pid)

    os.chdir('/home/szq')
    os.umask(0)
    os.setsid()

    print("the pid is {0} and ppid is {1}".format(os.getpid(), os.getppid()))
    _pid = os.fork()

    if _pid > 0:
        print("the pid is {0} and ppid is {1}".format(os.getpid(), os.getppid()))
        print(_pid)
        sys.exit(0)
    elif _pid == 0:
        print("the pid is {0} and ppid is {1}".format(os.getpid(), os.getppid()))
        print(_pid)

    print("the pid is {0} and ppid is {1}".format(os.getpid(), os.getppid()))
    sys.stdout.flush()
    sys.stderr.flush()

    with open('/dev/null') as read_null, open('/dev/null', 'w') as write_null:
        os.dup2(read_null.fileno(), sys.stdin.fileno())
        os.dup2(write_null.fileno(), sys.stdout.fileno())

    if pid_file:
        with open(pid_file, 'w+') as f:
            f.write(str(os.getpid()))

            atexit.register(os.remove, pid_file)

    f = open('testing', 'a')
    while True:
        time.sleep(1)
        f.write('666666666\n')
        f.flush()


daemonize('pid_file')
