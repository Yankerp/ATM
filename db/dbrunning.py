import json
import time
import os
from conf import settings

def select(username, password, res=None):
    file_dir = settings.USER_PATH + "{username}.json".format(username=username)
    with open(file_dir, mode='rt', encoding='utf-8') as f:
        res = json.load(f)
        return True, res


def save_user(username, password):
    user_dict = settings.userinfo(username, password)
    file_dir = settings.USER_PATH + "{username}.json".format(username=username)
    with open(file_dir, mode='wt', encoding='utf)-8') as f:
        json.dump(user_dict, f)
    return True


def update(username, count):
    file_dir = settings.USER_PATH + "{username}.json".format(username=username)
    with open(file_dir, mode='rt', encoding='utf-8') as f:
        res = json.load(f)
        res['quota'] = res['quota'] - count
        res['flowingwater'].append(
            '用户{username}在{time} 提现了{count} 元人民币'.format(username=username, time=time.strftime('%Y-%m-%d %H:%M:%S'),
                                                         count=count))
        with open(file_dir, mode='wt', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False)

    return True, '用户{username}提现余额{count}成功！！！'.format(username=username, count=count)


def daasbank(your_name, ta_name, count:int):
    file_dir = settings.USER_PATH + "{username}.json".format(username=your_name)
    file2_dir = settings.USER_PATH + "{username}.json".format(username=ta_name)
    if os.path.isfile(file_dir) and os.path.isfile(file2_dir):
        with open(file2_dir, mode='rt', encoding='utf-8') as f:
            res = json.load(f)
            res['quota'] = res['quota'] + int(count)
            res['flowingwater'].append(
                '用户{username}在{time} 获得了来自{your_name}转账的{count} 元人民币'.format(username=ta_name, your_name=your_name, time=time.strftime('%Y-%m-%d %H:%M:%S'),
                                                             count=count))
            with open(file2_dir, mode='wt', encoding='utf-8') as f:
                json.dump(res, f, ensure_ascii=False)

        with open(file_dir, mode='rt', encoding='utf-8') as f:
            res = json.load(f)
            res['quota'] = res['quota'] - int(count)
            res['flowingwater'].append(
                '用户{your_name}在{time} 给{ta_name}转账了{count} 元人民币'.format(username=ta_name, your_name=your_name, ta_name=ta_name, time=time.strftime('%Y-%m-%d %H:%M:%S'),
                                                             count=count))
            with open(file_dir, mode='wt', encoding='utf-8') as f:
                json.dump(res, f, ensure_ascii=False)

        return True, "用户{your_name}给用户{ta_name}转账:{count} 元人民币".format(your_name=your_name, ta_name=ta_name, count=int(count))
    else:
        return False, "转账用户不存在"




def liushuier(username):
    file_dir = settings.USER_PATH + "{username}.json".format(username=username)
    with open(file_dir, mode='rt', encoding='utf-8') as f:
        res = json.load(f)
        return True, res['flowingwater']










