import os
from lib import common

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
USER_PATH = BASE_PATH + r'/db/userdb/'


def userinfo(username, userpassword, quota=15000):
    userpassword = common.hashpwd(userpassword)
    userinfodict = {'username': username, 'userpassword': userpassword, 'quota': quota, 'status': False,
                    'flowingwater': []}

    return userinfodict
