from tkinter import Tk
import tkinter as tk
from tkinter import messagebox
import random

def pop_up(aline) : #彈出視窗 問你yes/no
    MsgBox = tk.messagebox.askquestion ('注意',"Are you sure?",icon = 'error')
    if MsgBox == 'no':
        for i in range(4):
            aline.pop(0)
        for i in range(2):
            temp_flag.pop(0)
    else:
        if aline[0] == aline[2] and aline[1] == aline[3]:
            self_line(aline)
        else:
            line(aline)
        win(flaglist, playerlist)  # let's see who wins
        #print('now drawing', playerlist[0])
        playerlist.reverse()
        player_win_times_list.reverse()

def cross(triple, start_t_end, remove):  # 解決可能交叉的情況
    for i in triple:
        if remove == i[1]:
            if i[2] in start_t_end[i[0]]:
                start_t_end[i[0]].remove(i[2])
            if i[0] in start_t_end[i[2]]:
                start_t_end[i[2]].remove(i[0])

def check_start_t_end(num, temp_flag, aline, start_t_end):
    if len(temp_flag) == 2:
        num = temp_flag[0]
        if temp_flag[1] in start_t_end[num]:
            pop_up(aline)
        else:
            for i in range(4):
                aline.pop(0)
            for i in range(2):
                temp_flag.pop(0)
            messagebox.showinfo('注意','不能畫啦')
    elif len(temp_flag) == 1:
        if temp_flag[0] not in flaglist:
            for i in range(2):
                aline.pop(0)
            for i in range(1):
                temp_flag.pop(0)
            messagebox.showinfo('注意','不能畫啦')

def line(aline):  # 畫線
    a = my_canvas.create_line(aline, fill='red', width=5)
    linemark.append(a)  # 紀錄線
    sort_flag = sorted(temp_flag)
    for i in triple:
        if sort_flag[0] == i[0] and sort_flag[1] == i[2]:
            flaglist.remove(i[1])  # 從flaglist移除中間項
            cross(triple, start_t_end, i[1])
            for j in start_t_end.values():
                if i[1] in j:
                    j.remove(i[1])  # 從start_t_end移除中間項
    # 現在設定從兩個圓的中心到中心
    flaglist.remove(temp_flag[0])  # 移除畫過的圓
    flaglist.remove(temp_flag[1])
    cross(triple, start_t_end, temp_flag[0])
    cross(triple, start_t_end, temp_flag[1])
    for i in start_t_end.values():
        if temp_flag[0] in i:
            i.remove(temp_flag[0])
        if temp_flag[1] in i:
            i.remove(temp_flag[1])
    for i in range(4):
        aline.pop(0)
    for i in range(2):
        temp_flag.pop(0)

def self_line(aline):
    x = aline[0] + 45
    y = aline[1] + 45
    a = my_canvas.create_line(x, y, x-90, y-90, fill='red', width=5)
    linemark.append(a)
    flaglist.remove(temp_flag[0])  # 只移除一個圓
    for i in start_t_end.values():
        if temp_flag[0] in i:
            i.remove(temp_flag[0])
    cross(triple, start_t_end, temp_flag[0])
    for i in range(4):
        aline.pop(0)
    for i in range(2):
        temp_flag.pop(0)
'''
想讓圓圈在被選到但是還沒畫線的時候能出現記號，目前做編筐
def show(x, y):
    if len(temp_flag) == 1:
        print(1)
        a = my_canvas.create_oval(x-35, y-35, x+35, y+35, outline='red', width=5)
    if len(temp_flag) == 2:
        print(2)
        b = my_canvas.create_oval(x-35, y-35, x+35, y+35, outline='red', width=5)
    if len(temp_flag) == 0:
        print(0)
        my_canvas.delete(a)
        my_canvas.delete(b)
'''

player_win_times_list = []
for i in range(2) :
    player_win_times_list.append([])
for i in range(2) :
    player_win_times_list[i].append(0)


def win(flaglist, playerlist):  # 判斷勝利條件
    # playerlist[0] 是這一輪畫線的玩家
    global player_win_times_list
    if len(flaglist) == 1:  # 剩一個自己贏
        messagebox.showinfo('Congratulation', playerlist[0]+' wins!!!')
        reset(linemark)
        player_win_times_list[0][0] += 1
        player1_win_times = player_win_times_list[0][0]
        player1_score = tk.Label(root,font=("Ariel",30),text="You have won {} times.".format(player1_win_times)).place(x=100,y=120)
        print(player_win_times_list)
    if len(flaglist) == 0:  # 不剩對方贏
        messagebox.showinfo('Congratulation', playerlist[1]+' wins!!!')
        reset(linemark)
        player_win_times_list[0][0] += 1
        player2_win_times = player_win_times_list[1][0]
        player2_score = tk.Label(root,font=("Ariel",30),text="You have won {} times.".format(player2_win_times)).place(x=100,y=320)
        print(player_win_times_list)
def reset(linemark):  # 回復原本的設定
    for i in linemark:
            my_canvas.delete(i)  # 移除線
    for i in range(len(linemark)):
        linemark.pop(0)            
    for i in range(1,16):
        if i not in flaglist:
            flaglist.append(i)
    original_start_t_end = {1:[1,2,3,4,6], 2:[1,2,3,4,5,7,9], 3:[1,2,3,5,6,8,10],\
               4:[1,2,4,5,6,7,8,11,13], 5:[2,3,4,5,6,8,9,12,14],\
               6:[1,3,4,5,6,9,13,10,15], 7:[2,4,7,8,9,11,12],\
               8:[3,4,5,7,8,9,10,12,13], 9:[2,5,6,7,8,9,10,13,14],\
               10:[3,6,8,9,10,14,15], 11:[4,7,11,12,13],\
               12:[5,7,8,11,12,13,14], 13:[4,6,8,9,11,12,13,14,15],\
               14:[5,9,10,12,13,14,15], 15:[6,10,13,14,15]}
    for i in range(1,16):
        for j in original_start_t_end[i]:
            if j not in start_t_end[i]:
                start_t_end[i].append(j)
    random.shuffle(playerlist)
    messagebox.showinfo('注意',playerlist[1]+' goes first')
    # 因為後面會reverse()所以我這邊寫playerlist[1]
    


def place(event):
    aline.append(315)  # 圓心座標
    aline.append(37)
    temp_flag.append(1)
    check_start_t_end(1, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)
    
def place2(event):
    aline.append(245)
    aline.append(175)
    temp_flag.append(2)
    check_start_t_end(2, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)
    
def place3(event):
    aline.append(385)
    aline.append(175)
    temp_flag.append(3)
    check_start_t_end(3, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)
    
def place4(event):
    aline.append(175)
    aline.append(315)
    temp_flag.append(4)
    check_start_t_end(4, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)

def place5(event):
    aline.append(315)
    aline.append(315)
    temp_flag.append(5)
    check_start_t_end(5, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)
    
def place6(event):
    aline.append(455)
    aline.append(315)
    temp_flag.append(6)
    check_start_t_end(6, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)
    
def place7(event):
    aline.append(105)
    aline.append(455)
    temp_flag.append(7)
    check_start_t_end(7, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)
    
def place8(event):
    aline.append(245)
    aline.append(455)
    temp_flag.append(8)
    check_start_t_end(8, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)
   
def place9(event):
    aline.append(385)
    aline.append(455)
    temp_flag.append(9)
    check_start_t_end(9, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)

def place10(event):
    aline.append(525)
    aline.append(455)
    temp_flag.append(10)
    check_start_t_end(10, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)
    
def place11(event):
    aline.append(37)
    aline.append(593)
    temp_flag.append(11)
    check_start_t_end(11, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)
    
def place12(event):
    aline.append(175)
    aline.append(593)
    temp_flag.append(12)
    check_start_t_end(12, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)
    
def place13(event):
    aline.append(315)
    aline.append(593)
    temp_flag.append(13)
    check_start_t_end(13, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)
    
def place14(event):
    aline.append(455)
    aline.append(593)
    temp_flag.append(14)
    check_start_t_end(14, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)
    
def place15(event):
    aline.append(593)
    aline.append(593)
    temp_flag.append(15)
    check_start_t_end(15, temp_flag, aline, start_t_end)
#    print(aline)
#    print(flaglist)

class Game(tk.Canvas):
    def __init__(self, my_canvas):
        tk.Canvas.__init__(self)
        self.circle(my_canvas)
        self.tag(my_canvas)
        self.player(playerlist)
        self.my_canvas = my_canvas
#    my_canvas = tk.Canvas(root, width=630, height=630, bg='white')
#    my_canvas.master.title('try this canvas')
#    my_canvas.pack()  # 忘記這行在幹嘛 好像是確保可以使用功能 很重要 記得打
    def circle(self, my_canvas):
    # make a rectangle and fit in the oval
    # 設定每一個圓'70x70'之後再改
        self.circle1 = my_canvas.create_oval(280, 2, 350, 72, fill = 'cyan')
        self.circle2 = my_canvas.create_oval(210, 140, 280, 210, fill = 'cyan')
        self.circle3 = my_canvas.create_oval(350, 140, 420, 210, fill = 'cyan')
        self.circle4 = my_canvas.create_oval(140, 280, 210, 350, fill = 'cyan')
        self.circle5 = my_canvas.create_oval(280, 280, 350, 350, fill = 'cyan')
        self.circle6 = my_canvas.create_oval(420, 280, 490, 350, fill = 'cyan')
        self.circle7 = my_canvas.create_oval(70, 420, 140, 490, fill = 'cyan')
        self.circle8 = my_canvas.create_oval(210, 420, 280, 490, fill = 'cyan')
        self.circle9 = my_canvas.create_oval(350, 420, 420, 490, fill = 'cyan')
        self.circle10 = my_canvas.create_oval(490, 420, 560, 490, fill = 'cyan')
        self.circle11 = my_canvas.create_oval(2, 558, 72, 628, fill = 'cyan')
        self.circle12 = my_canvas.create_oval(140, 558, 210, 628, fill = 'cyan')
        self.circle13 = my_canvas.create_oval(280, 558, 350, 628, fill = 'cyan')
        self.circle14 = my_canvas.create_oval(420, 558, 490, 628, fill = 'cyan')
        self.circle15 = my_canvas.create_oval(558, 558, 628, 628, fill = 'cyan')
    def tag(self, my_canvas):
    # bind 結合鍵盤或滑鼠的指令和函數
        my_canvas.tag_bind(self.circle1, '<Button-1>', place)  # 用tag_bind可以只連結特定位置
        my_canvas.tag_bind(self.circle2, '<Button-1>', place2)
        my_canvas.tag_bind(self.circle3, '<Button-1>', place3)
        my_canvas.tag_bind(self.circle4, '<Button-1>', place4)
        my_canvas.tag_bind(self.circle5, '<Button-1>', place5)
        my_canvas.tag_bind(self.circle6, '<Button-1>', place6)
        my_canvas.tag_bind(self.circle7, '<Button-1>', place7)
        my_canvas.tag_bind(self.circle8, '<Button-1>', place8)
        my_canvas.tag_bind(self.circle9, '<Button-1>', place9)
        my_canvas.tag_bind(self.circle10, '<Button-1>', place10)
        my_canvas.tag_bind(self.circle11, '<Button-1>', place11)
        my_canvas.tag_bind(self.circle12, '<Button-1>', place12)
        my_canvas.tag_bind(self.circle13, '<Button-1>', place13)
        my_canvas.tag_bind(self.circle14, '<Button-1>', place14)
        my_canvas.tag_bind(self.circle15, '<Button-1>', place15)
    def player(self, playerlist):
        random.shuffle(playerlist)
        messagebox.showinfo('注意',playerlist[0]+' goes first')
linemark = []  # 紀錄畫上去的線
aline = list()
flaglist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  # 可以選的
temp_flag = []
# 可以畫的
start_t_end = {1:[1,2,3,4,6], 2:[1,2,3,4,5,7,9], 3:[1,2,3,5,6,8,10],\
               4:[1,2,4,5,6,7,8,11,13], 5:[2,3,4,5,6,8,9,12,14],\
               6:[1,3,4,5,6,9,13,10,15], 7:[2,4,7,8,9,11,12],\
               8:[3,4,5,7,8,9,10,12,13], 9:[2,5,6,7,8,9,10,13,14],\
               10:[3,6,8,9,10,14,15], 11:[4,7,11,12,13],\
               12:[5,7,8,11,12,13,14], 13:[4,6,8,9,11,12,13,14,15],\
               14:[5,9,10,12,13,14,15], 15:[6,10,13,14,15]}
# 會畫到三個的組合
triple = [[1,2,4],[1,3,6],[2,4,7],[2,5,9],[3,5,8],[3,6,10],[4,5,6],\
[4,7,11],[4,8,13],[5,8,12],[5,9,14],[6,9,13], [6,10,15],[7,8,9],[8,9,10],\
[11,12,13],[12,13,14],[13,14,15]]

player1 = 'Max'
player2 = 'Kelly'
playerlist = [player1, player2]
#random.shuffle(playerlist)

root = Tk()  # 視窗
root.geometry('1360x1280')
root.title("畫圈圈")
my_canvas = tk.Canvas(root, width=630, height=630, bg='white')
my_canvas.pack()
root.resizable()



player1_name = tk.Label(root,font=("Ariel",40),text = "{}".format(playerlist[0])).place(x=100,y=20)
player1_score = tk.Label(root,font=("Ariel",30),text = "You have won 0 times.").place(x=100,y=120)
player2_name = tk.Label(root,font=("Ariel",40),text = "{}".format(playerlist[1])).place(x=100,y=220)
player2_score = tk.Label(root,font=("Ariel",30),text = "You have won 0 times.").place(x=100,y=320)

game = Game(my_canvas)

root.mainloop()