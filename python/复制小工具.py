# -*- coding:utf-8-*-
import tkinter as tk

top = tk.Tk()
top.title("复制工具")
top.geometry('640x640')  # 设置窗体大小
label1 = tk.Label(top, text="输入")  # 文本显示
entry3 = tk.Entry(top)
list = tk.Listbox(top)  # 列表框
entry3.pack()
list.pack()


def button_clicked():
    count3 = float(entry3.get())
    text3 = str(count3)
    list.insert(3, text3)


btn = tk.Button(top, text="复制", command=button_clicked)
btn.pack()
top.mainloop()
