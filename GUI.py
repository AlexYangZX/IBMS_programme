# -*- coding=utf-8 -*-
import tkinter
from PIL import Image, ImageTk
from path_programme import output_path, output_path2
from faceRecognition import faceReco
from LinkStart import link_start, link_restart, link_shutdown
import sys


# 判断着火点
def is_fire():
    f5 = faceReco()

    if f5 == 1:
        fire_point = 5

    return fire_point


# 路径规划
def show_path():
    show_fire_point.delete(0.0, tkinter.END)  # 清空显示
    show_end_point.delete(0.0, tkinter.END)
    fire_point = is_fire()
    show_fire_point.insert(tkinter.INSERT, fire_point)
    show_end_point.insert(tkinter.INSERT, '1号出口: 0\n2号出口: 15')  # 显示出口 预先设定
    path = output_path2(0, 15, fire_point)  # 获取的输入是字符，需要转为整型  调用  # 设置出口
    path2 = output_path(0, 15, fire_point)  # 发送给Pi

    for i in range(0, len(path)):
        output_text.insert(tkinter.INSERT, path[i])
        output_text.insert(tkinter.INSERT, '\n')
    output_text.insert(tkinter.INSERT, '-----------------------------')
    output_text.insert(tkinter.INSERT, '\n')

    return path2


# 运行
def run_it():
    link_start(show_path())


# 退出
def exit_bye():
    sys.exit()


# 重启
def restart_it():
    link_restart()

# 界面
root_window = tkinter.Tk()
root_window.title('GUI_Demo')
root_window.minsize(1200, 800)   # 宽 ， 长
output_text = tkinter.Text(root_window, width=80, height=60)
label = tkinter.Label(root_window, text='着火点', )
label2 = tkinter.Label(root_window, text='出口')
run_button = tkinter.Button(root_window, text='运行', width=12, height=1, command=run_it)
exit_button = tkinter.Button(root_window, text='退出', width=12, height=1, command=exit_bye)
restart_button = tkinter.Button(root_window, text='重启',  width=12, height=1, command=restart_it)
# 载入图片
image = Image.open('map2.png')
read_image = ImageTk.PhotoImage(image=image)
label_photo = tkinter.Label(image=read_image)
# 显示着火点
show_fire_point = tkinter.Text(root_window, width=15, height=1)
# 显示终点
show_end_point = tkinter.Text(root_window, width=15, height=2)
# 各元件位置
output_text.place(x=10, y=10)  # 主显示框
label.place(x=600, y=68)  # 着火点文字
label2.place(x=600, y=28)  # 终点文字
run_button.place(x=650, y=110)  # 开始按钮
exit_button.place(x=950, y=110)  # 退出按钮
restart_button.place(x=800, y=110)  # 重启按钮
show_fire_point.place(x=650, y=70)  # 着火点显示
show_end_point.place(x=650, y=30)  # 终点输入
label_photo.place(x=600, y=250)  # 图片

# 检测




root_window.mainloop()