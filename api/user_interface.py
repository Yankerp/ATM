import os
from conf import settings
from db import dbrunning
from lib import common


def registerinterface(username, userpassword):
    "用户的注册"
    if os.path.isfile(settings.USER_PATH + "{username}.json".format(username=username)):
        return False, f'用户 {username} 注册失败，用户名已存在'
    else:
        code = dbrunning.save_user(username, userpassword)
        return code, f'用户 {username} 注册成功......'


def logininterface(username, userpassword):
    "用户的登录"
    if os.path.isfile(settings.USER_PATH + "{username}.json".format(username=username)):
        "存在时候的操作"
        userpassword = common.hashpwd(userpassword)
        code, res = dbrunning.select(username, userpassword)
        if code:
            if username == res['username'] and userpassword == res['userpassword']:
                return True, '用户名密码正确，登录成功'
            else:
                return False, '用户名或密码错误，登录失败'
    else:
        return False, '用户名不存在，请先去注册.......'

def user_true(username):
    if os.path.isfile(settings.USER_PATH + "{username}.json".format(username=username)):
        return True
