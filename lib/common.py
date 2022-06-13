import hashlib
from core import src


def check_login(func):
    def check_status(*args, **kwargs):
        if src.user_logi_status == False:
            print("功能无法使用，请先登录".center(50, "-"))
        else:
            func(*args, **kwargs)

    return check_status


def hashpwd(password):
    res = hashlib.md5()
    res.update(password.encode('utf-8'))
    hashp = res.hexdigest()

    return hashp
