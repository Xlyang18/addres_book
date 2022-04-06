import os
import sys
import time

one_list = []  # 空列表
one_dict = {}  # 空字典


def one():
    print("-" * 32)
    print("--|当前位置<用户操作模块>")
    print("【新建联系人】-add     【抹除联系人】-del")
    print("【修改联系人】-alter   【展开联系人】-all")
    print("【查找联系人】-find    【 退   出 】-exit")

    choose = str(input("输入对于命令："))
    if choose == 'add':
        add()
    elif choose == 'all':
        all_()
    elif choose == 'find':
        find()
    elif choose == 'alter':
        alter()
    elif choose == 'del':
        del_()
    elif choose == 'exit':
        print("--|当前位置<用户操作模块>>exit命令")
        print("延迟<2s>退出")
        time.sleep(2)
        sys.exit()


def add():
    print("--|当前位置<用户操作模块>>add命令")
    name = input("name：")
    phone = input("phone:")

    one_dict = {"name": name, "phone": phone}
    print("--|操作成功")

    # 将该字典添加到列表当中
    one_list.append(one_dict)
    save_file()
    choose = str(input("是否继续操作？Yes/No:"))
    if choose == 'yes':
        one()
    else:
        sys.exit()


def all_():
    print("--｜当前位置<用户操作模块>>all命令")
    # 确定test_list的参数长度不为0
    # 即确定列表中有数据，进行后续操作
    if len(one_list) > 0:

        # 此处的输出语句中[""]里的值，要与开始 写入数据到字典 里的值对应。
        for one_dict_1 in one_list:
            print("%s\t\t%s" % (one_dict_1["name"], one_dict_1["phone"]))

    else:
        print("--|暂无数据")
    print("-" * 32)
    print("--|操作成功")
    choose = str(input("是否继续操作？Yes/No:"))
    if choose == 'yes':
        one()
    else:
        sys.exit()


def find():
    # 通过 value1 来查找数据
    print("--｜当前位置<用户操作模块>>find命令")
    find_name = input("find name：")

    for one_dict_1 in one_list:
        if find_name == one_dict_1["name"]:
            print("%s\t\t%s" % (one_dict_1["name"], one_dict_1["phone"]))
            go_on()
    else:
        print("--|未找到数据")
        go_on()


def alter():
    # 通过查找name的值来确定需要修改的一组数据
    print("--｜当前位置<用户操作模块>>alter命令")
    alter_name = input("alter name:：")
    for one_dict_1 in one_list:
        if alter_name in one_dict_1["name"]:
            print("修改前的数据为：")
            print(
                "%s\t\t%s" % (one_dict_1["name"], one_dict_1["phone"]))

            # 修改新的参数内的内容
            one_dict_1["phone"] = new_input(one_dict_1["phone"], "输入新的phone<使用enter键跳过该值修改>:")

            # 调用保存数据到文件的函数，保存当前修改操作
            save_file()
            go_on()

    else:
        print("未找到数据")
        go_on()


def del_():
    delete_name = input("delete_name:")
    for one_dict_1 in one_list:
        if delete_name in one_dict_1["name"]:

            # 删除数据
            one_list.remove(one_dict_1)

            # 调用保存数据到文件的函数，保存当前的修改操作
            save_file()
            go_on()

    else:
        print("未找到数据")
        go_on()



def go_on():
    print("--|操作成功")
    choose = str(input("是否继续操作？Yes/No:"))
    if choose == 'yes':
        one()
    else:
        sys.exit()



def read_file():
    # 判断‘目标文本文件.txt’是否存在，存在则为True
    if os.path.exists("user.txt"):
        # 打开需要读取数据的文件，读取模式，使用‘utf-8’编译
        f = open("user.txt", 'r', encoding='utf-8')

        # 读取目标文件，并将值赋给ret
        ret = f.read()

        # global：声明 test_list 为全局变量
        global one_list

        # 将读取到的目标文件里的数据赋给test_list
        # eval（）类似于str（），将参数ret转化为可被列表储存的数据
        one_list = eval(ret)
        f.close()


def save_file():
    # 打开需要你写入数据的文件，写入模式，使用‘utf-8’编译
    f = open("user.txt", 'w', encoding='utf-8')

    # 写入数据，
    # 在此前将列表test_list通过str()强制转换为字符串类型
    f.write(str(one_list))

    # 关闭文件
    f.close()


def new_input(start_value: object, message: object) -> object:
    input_str = input(message)

    if len(input_str) > 0:
        return input_str
    else:
        return start_value
