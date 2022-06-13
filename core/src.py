import sys
from api import user_interface
from api import commodity_interface
from lib import common
from api import daasbank_interface

user_logi_status = False
user_login_running = ''


def register():
    '''注册功能'''
    print("欢迎来到注册功能，请输入您的账户名密码进行注册".center(50, "*"))
    username = input("请您输入您需要注册的用户名：").strip()
    userpassword = input("请您输入您需要注册的密码：").strip()
    re_userpassword = input("请您再次确认密码：").strip()

    if userpassword == re_userpassword:
        code, res = user_interface.registerinterface(username, userpassword)
        if code:
            print(res)
        else:
            print(res)
    else:
        print("两次输入密码不一致，请重新输入!!!")


def login():
    '''登录功能'''
    user_name = input('请您输入登录的用户名：').strip()
    user_password = input("请您输入登录的密码：").strip()

    if user_name != '' and user_password != '':
        code, res = user_interface.logininterface(user_name, user_password)
        if code:
            print(res)
            global user_logi_status, user_login_running
            user_logi_status = True
            user_login_running = user_name
        else:
            print(res)


@common.check_login
def Shopping():
    '''购物功能'''


@common.check_login
def Withdrawal():
    '''提现功能'''
    while True:
        print("欢迎来到提现功能".center(50, "*"))
        Query_flow()
        res = input("请您输入您需要提取的金额(元)：").strip()
        if not res.isdigit():
            print("请您输入数字!!!")
            continue
        if res == '':
            print("输入不能为空，请再次输入")
            continue
        code, res = commodity_interface.Withdrawalinterface(user_login_running, int(res))
        if code:
            print(res)
            Query_flow()
            return 'ok'
        else:
            print(res)
            return 'error'


@common.check_login
def Query_flow():
    '''查询余额功能'''
    code, res = commodity_interface.flowingwaterinterface(user_login_running)
    if code:
        print(res)
    else:
        print(res)

@common.check_login
def liushui():
    '''查询流水功能'''
    code, res = commodity_interface.liushuiinterface(user_login_running)
    if code:
        for x in res:
            print(x)
        return 'ok'
    else:
        print(res)
        return 'error'

@common.check_login
def Transfer():
    '''转账功能'''
    while True:
        your_name = input("请您输入您的用户名：").strip()
        if your_name != user_login_running:
            print("输入用户与当前登录用户不一致，请重新输入.....")
            continue
        ta_name = input("你要转账给谁：").strip()
        Query_flow()
        count = input("请输入转账金额：").strip()
        code, res = daasbank_interface.transfer_accounts_interface(your_name, ta_name, int(count))
        if code:
            print(res)
            return 'ok'
        else:
            print(res)


def admin():
    '''Administrator'''
    pass


def Exit_function():
    '''exit'''
    print("退出成功，欢迎再次使用，再见".center(50, "*"))
    sys.exit()


def run():
    while True:
        option_dict = {
            '1': ['注册功能', register],
            '2': ['登录功能', login],
            '3': ['购物功能', Shopping],
            '4': ['提现功能', Withdrawal],
            '5': ['查询余额功能', Query_flow],
            '6': ['查询流水功能', liushui],
            '7': ['转账功能', Transfer],
            '8': ['管理员功能', admin],
            '9': ['退出功能', Exit_function]
        }
        print("====================ATM+购物车======================")
        for option in option_dict:
            print(option, option_dict[option][0])

        your_option = input("请您输入选项：").strip()
        if not your_option.isdigit():
            print("请您输入数字!!!")
            continue

        if your_option not in option_dict:
            print("请您输入正确的选项")
            continue
        else:
            option_dict[your_option][1]()


if __name__ == '__main__':
    run()
