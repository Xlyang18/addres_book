import sys
import time

import boss_
import user_

j_id = 'xly'
j_key = '123321'
user_1 = {'id': '111', "key": '123321'}
user_2 = {"id": '222', "key": '123321'}


# 登陆界面
def log_in():
    error = 0
    print("------| 欢迎使用<通讯录管理>系 统  |")
    print("-" * 32)
    print("--|当前位置<登录模块>")
    id = str(input("账号："))
    key = str(input("密码："))

    if id == j_id:
        if key == j_key:
            print("-" * 32)
            print("<管理员>账号验证通过")
            succeed_boss()
        else:
            print("-" * 32)
            print("该账号匹配的密码错误")
            print("--|登录失败")
            error = '01'

    elif id == user_1['id']:
        if key == user_1['key']:
            print("-" * 32)
            print("<用户1>账号验证通过")
            succeed_user()
        else:
            print("-" * 32)
            print("该账号匹配的密码错误")
            print("--|登录失败")
            error = '01'
    elif id == user_2['id']:
        if key == user_2['key']:
            print("-" * 32)
            print("<用户2>账号验证通过")
            succeed_user()
        else:
            print("-" * 32)
            print("该账号匹配的密码错误")
            print("--|登录失败")
            error = '01'
    else:
        print("-" * 32)
        print("数据库内暂未绑定该账号信息")
        print("--|登录失败")
        error = '01'

    if error == '01':
        log_in_again()


def log_in_again():
    num = 1
    while num <= 6:
        if num == 6:
            print("-" * 32)
            print("--|系统将于2秒后退出退出")
            time.sleep(3)
            sys.exit()
        else:
            print("-" * 32)
            print("登录失败：", num, "剩余输入次数：", 5 - num)
            num = num + 1

            print("--|当前位置<登录模块>")
            id = str(input("账号："))
            key = str(input("密码："))

            if id == j_id:
                if key == j_key:
                    print("-" * 32)
                    print("<管理员>账号验证通过")
                    succeed_boss()
                    break
                else:
                    print("-" * 32)
                    print("该账号匹配的密码错误")
                    print("--|登录失败")


            elif id == user_1['id']:
                if key == user_1['key']:
                    print("-" * 32)
                    print("<用户1>账号验证通过")
                    succeed_user()
                    break
                else:
                    print("-" * 32)
                    print("该账号匹配的密码错误")
                    print("--|登录失败")

            elif id == user_2['id']:
                if key == user_2['key']:
                    print("-" * 32)
                    print("<用户2>账号验证通过")
                    succeed_user()
                    break
                else:
                    print("-" * 32)
                    print("该账号匹配的密码错误")
                    print("--|登录失败")

            else:
                print("-" * 32)
                print("数据库内暂未绑定该账号信息")
                print("--|登录失败")


def succeed_user():
    print("--|登录成功")
    user_.read_file()
    user_.one()


def succeed_boss():
    print("--|登录成功")
    boss_.one()


log_in()
