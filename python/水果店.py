# -*- coding:utf-8-*-
import tkinter as tk

apple = 6.5
pear = 5.4
bana = 7.2
# 定义
top = tk.Tk()
top.title("便捷水果店")
top.geometry('640x640')  # 设置窗体大小
label1 = tk.Label(top, text="请输入苹果的重量:")  # 文本显示
label2 = tk.Label(top, text="请输入梨的重量:")
label3 = tk.Label(top, text="请输入香蕉的重量:")
entry1 = tk.Entry(top)  # 设置输入框
entry2 = tk.Entry(top)
entry3 = tk.Entry(top)
list = tk.Listbox(top)  # 列表框
# 格式
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
list.pack()


def button_clicked():
    # 输入
    count1 = float(entry1.get())
    count2 = float(entry2.get())
    count3 = float(entry3.get())
    text = "名称   数量   价格"
    text1 = "苹果  " + str(count1) + "k   " + str(apple * count1)
    text2 = "梨      " + str(count2) + "k   " + str(pear * count2)
    text3 = "香蕉  " + str(count3) + "k   " + str(bana * count3)
    text4 = "总价  " + str(apple * count1 + pear * count2 + bana * count3)
    # 显示
    list.insert(0, text)
    list.insert(1, text1)
    list.insert(2, text2)
    list.insert(3, text3)
    list.insert(4, text4)


# 按钮
btn = tk.Button(top, text="结算", command=button_clicked)
btn.pack()
top.mainloop()
