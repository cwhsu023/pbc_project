from tkinter import Tk
import tkinter as tk

root = Tk()  # 視窗
root.geometry('700x700')
my_canvas = tk.Canvas(root, width=630, height=630, bg='white')
my_canvas.master.title('try this canvas')
my_canvas.pack()  # 忘記這行在幹嘛 好像是確保可以使用功能 很重要 記得打

# make a rectangle and fit in the oval
# 設定每一個圓'70x70'之後再改
circle1 = my_canvas.create_oval(280, 2, 350, 72, fill = 'cyan')
circle2 = my_canvas.create_oval(210, 140, 280, 210, fill = 'cyan')
circle3 = my_canvas.create_oval(350, 140, 420, 210, fill = 'cyan')
circle4 = my_canvas.create_oval(140, 280, 210, 350, fill = 'cyan')
circle5 = my_canvas.create_oval(280, 280, 350, 350, fill = 'cyan')
circle6 = my_canvas.create_oval(420, 280, 490, 350, fill = 'cyan')
circle7 = my_canvas.create_oval(70, 420, 140, 490, fill = 'cyan')
circle8 = my_canvas.create_oval(210, 420, 280, 490, fill = 'cyan')
circle9 = my_canvas.create_oval(350, 420, 420, 490, fill = 'cyan')
circle10 = my_canvas.create_oval(490, 420, 560, 490, fill = 'cyan')
circle11 = my_canvas.create_oval(2, 558, 72, 628, fill = 'cyan')
circle12 = my_canvas.create_oval(140, 558, 210, 628, fill = 'cyan')
circle13 = my_canvas.create_oval(280, 558, 350, 628, fill = 'cyan')
circle14 = my_canvas.create_oval(420, 558, 490, 628, fill = 'cyan')
circle15 = my_canvas.create_oval(558, 558, 628, 628, fill = 'cyan')

aline = list()
flaglist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp_flag = []
def line(aline):  # 畫線
    my_canvas.create_line(aline, fill='red', width=5)
    # 現在設定從兩個圓的中心到中心
    flaglist.remove(temp_flag[0])  # 移除畫過的圓
    flaglist.remove(temp_flag[1])
    for i in range(4):
        aline.pop(0)
    for i in range(2):
        temp_flag.pop(0)
    
def self_line(aline):
    x = aline[0] + 45
    y = aline[1] + 45
    my_canvas.create_line(x, y, x-90, y-90, fill='red', width=5)
    flaglist.remove(temp_flag[0])  # 只移除一個圓
    for i in range(4):
        aline.pop(0)
    for i in range(2):
        temp_flag.pop(0)

def place(event):
    if 1 in flaglist:
        aline.append(315)  # 圓心座標
        aline.append(37)
        temp_flag.append(1)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)
    
def place2(event):
    if 2 in flaglist:
        aline.append(245)
        aline.append(175)
        temp_flag.append(2)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)
    
def place3(event):
    if 3 in flaglist:
        aline.append(385)
        aline.append(175)
        temp_flag.append(3)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)
    
def place4(event):
    if 4 in flaglist:
        aline.append(175)
        aline.append(315)
        temp_flag.append(4)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)

def place5(event):
    if 5 in flaglist:
        aline.append(315)
        aline.append(315)
        temp_flag.append(5)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)
    
def place6(event):
    if 6 in flaglist:
        aline.append(455)
        aline.append(315)
        temp_flag.append(6)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)
    
def place7(event):
    if 7 in flaglist:
        aline.append(105)
        aline.append(455)
        temp_flag.append(7)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)
    
def place8(event):
    if 8 in flaglist:
        aline.append(245)
        aline.append(455)
        temp_flag.append(8)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)
   
def place9(event):
    if 9 in flaglist:
        aline.append(385)
        aline.append(455)
        temp_flag.append(9)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
            for i in range(4):
                aline.pop(0)
    print(aline)
    print(flaglist)

def place10(event):
    if 10 in  flaglist:
        aline.append(525)
        aline.append(455)
        temp_flag.append(10)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    
def place11(event):
    if 11 in flaglist:
        aline.append(37)
        aline.append(593)
        temp_flag.append(11)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)
    
def place12(event):
    if 12 in  flaglist:
        aline.append(175)
        aline.append(593)
        temp_flag.append(12)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)
    
def place13(event):
    if 13 in flaglist:
        aline.append(315)
        aline.append(593)
        temp_flag.append(13)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)
    
def place14(event):
    if 14 in flaglist:
        aline.append(455)
        aline.append(593)
        temp_flag.append(14)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)
    
def place15(event):
    if 15 in flaglist:
        aline.append(593)
        aline.append(593)
        temp_flag.append(15)
        if len(aline) == 4:
            if aline[0] == aline[2] and aline[1] == aline[3]:
                self_line(aline)
            else:
                line(aline)
    print(aline)
    print(flaglist)

# bind 結合鍵盤或滑鼠的指令和函數
my_canvas.tag_bind(circle1, '<Button-1>', place)  # 用tag_bind可以只連結特定位置
my_canvas.tag_bind(circle2, '<Button-1>', place2)
my_canvas.tag_bind(circle3, '<Button-1>', place3)
my_canvas.tag_bind(circle4, '<Button-1>', place4)
my_canvas.tag_bind(circle5, '<Button-1>', place5)
my_canvas.tag_bind(circle6, '<Button-1>', place6)
my_canvas.tag_bind(circle7, '<Button-1>', place7)
my_canvas.tag_bind(circle8, '<Button-1>', place8)
my_canvas.tag_bind(circle9, '<Button-1>', place9)
my_canvas.tag_bind(circle10, '<Button-1>', place10)
my_canvas.tag_bind(circle11, '<Button-1>', place11)
my_canvas.tag_bind(circle12, '<Button-1>', place12)
my_canvas.tag_bind(circle13, '<Button-1>', place13)
my_canvas.tag_bind(circle14, '<Button-1>', place14)
my_canvas.tag_bind(circle15, '<Button-1>', place15)
root.mainloop()