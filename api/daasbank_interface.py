from db import dbrunning

def transfer_accounts_interface(your_name, ta_name, count:int):
    code, res = dbrunning.daasbank(your_name, ta_name, count)
    return code, res