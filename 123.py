from tkinter import Tk
import tkinter as tk

root = Tk()  # 視窗
root.geometry('700x700')
my_canvas = tk.Canvas(root, width=1480, height=1260, bg='white')
my_canvas.master.title('try this canvas')
def back() :
    print("hello")
b = tk.Button(my_canvas,text= "hit me",width=15,height=2,command=back)
my_canvas.pack()  # 這個好像是版面配置 不傳入東西就是由上至下

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
def line(aline):  # 畫線
    my_canvas.create_line(aline, fill='red', width=5)
    # 現在設定從兩個圓的中心到中心

def place(event):
    aline.append(315)  # 圓心座標
    aline.append(37)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
#    print(aline)
    
def place2(event):
    aline.append(245)
    aline.append(175)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
#    print(aline)
    
def place3(event):
    aline.append(385)
    aline.append(175)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
#    print(aline)
    
def place4(event):
    aline.append(175)
    aline.append(315)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
#    print(aline)

def place5(event):
    aline.append(315)
    aline.append(315)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
    #print(aline)
    
def place6(event):
    aline.append(455)
    aline.append(315)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
    #print(aline)
    
def place7(event):
    aline.append(105)
    aline.append(455)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
    #print(aline)
    
def place8(event):
    aline.append(245)
    aline.append(455)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
    #print(aline)
   
def place9(event):
    aline.append(385)
    aline.append(455)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
    #print(aline)

def place10(event):
    aline.append(525)
    aline.append(455)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
    #print(aline)
    
def place11(event):
    aline.append(37)
    aline.append(593)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
    #print(aline)
    
def place12(event):
    aline.append(175)
    aline.append(593)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
    #print(aline)
    
def place13(event):
    aline.append(315)
    aline.append(593)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
    #print(aline)
    
def place14(event):
    aline.append(455)
    aline.append(593)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
    #print(aline)
    
def place15(event):
    aline.append(593)
    aline.append(593)
    if len(aline) == 4:
        line(aline)
        for i in range(4):
            aline.pop(0)
    #print(aline)

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