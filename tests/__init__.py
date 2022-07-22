import os
import shutil
import functools




class BaseTest(object):
    root_path = os.path.split(os.path.abspath(__name__))[0]


def rmdir(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def chdir(path):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            cwd = os.getcwd()
            if not os.path.exists(path):
                os.makedirs(path)
            os.chdir(path)
            func(*args, **kwargs)
            os.chdir(cwd)
        return inner
    return wrapper
