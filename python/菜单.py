# 创建一个下拉式菜单
from tkinter import *
import tkinter.messagebox

# 创建主窗口
top = Tk()
top.config(bg='#87CEEB')
top.title("菜单")
top.geometry('450x350+300+200')
top.iconbitmap('C:/Users/黄洋/OneDrive\图片/tp/qw.ico')


# 创建一个执行函数，点击下拉菜单中命令时执行
def menuCommand():
    tkinter.messagebox.showinfo("下拉菜单", "您正在使用下拉菜单功能")


# 创建主目录菜单（顶级菜单）
mainmenu = Menu(top)
# 在顶级菜单上新增"文件"菜单的子菜单，同时不添加分割线
filemenu = Menu(mainmenu, tearoff=False)
# 新增"文件"菜单的菜单项，并使用 accelerator 设置菜单项的快捷键
filemenu.add_command(label="新建", command=menuCommand, accelerator="Ctrl+N")
filemenu.add_command(label="打开", command=menuCommand, accelerator="Ctrl+O")
filemenu.add_command(label="保存", command=menuCommand, accelerator="Ctrl+S")
# 添加一条分割线
filemenu.add_separator()
filemenu.add_command(label="退出", command=top.quit)
# 在主目录菜单上新增"文件"选项，并通过menu参数与下拉菜单绑定
mainmenu.add_cascade(label="文件", menu=filemenu)
# 将主菜单设置在窗口上
top.config(menu=mainmenu)
# 绑定键盘事件，按下键盘上的相应的键时都会触发执行函数
top.bind("<Control-n>", menuCommand)
top.bind("<Control-N>", menuCommand)
top.bind("<Control-o>", menuCommand)
top.bind("<Control-O>", menuCommand)
top.bind("<Control-s>", menuCommand)
top.bind("<Control-S>", menuCommand)
# 显示主窗口
top.mainloop()
