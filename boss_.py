import user_
import time
import sys

def one():
    print("-"*32)
    print("--|当前位置<管理员操作模块>")
    print("功能实现：待开发\n未来可期！！！")
    choose = input("是否跳转到<用户操作模版>？Yes/No:")
    if choose == 'yes':
        user_.read_file()
        user_.one()
    else:
        print("--|当前位置<管理员操作模块>>exit命令")
        print("延迟<2s>退出")
        time.sleep(2)
        sys.exit()