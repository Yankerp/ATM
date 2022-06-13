from db import dbrunning


def flowingwaterinterface(username):
    code, userdict = dbrunning.select(username, password=None)
    if code:
        return True, "您当前的余额为：{moy} 元".format(moy=userdict['quota'])
    else:
        return True, '查询余额失败，系统故障........'


def Withdrawalinterface(username, count:int):
    code, userdict = dbrunning.select(username, password=None)
    if code:
        if count > userdict['quota']:
            return False, '提现失败，余额不足!!!'
        else:
            code, res = dbrunning.update(username, count)
            if code:
                return True, res
            else:
                return False, '提现失败，系统错误.......'


def liushuiinterface(username):
    '''查询流水接口'''
    code, res = dbrunning.liushuier(username)
    if code:
        return code, res
    else:
        return False, '查询失败'
