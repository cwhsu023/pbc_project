# 這是系統的登入介面
# 兩個玩家
import tkinter
from tkinter import messagebox
from tkinter import Tk
import tkinter as tk
#from tkinter import *
import random
import pygame
from PIL import ImageTk, Image

linemark = []  # 紀錄畫上去的線
circle_list = []  # 用在show()
aline = list()
flaglist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # 可以選的
temp_flag = []
# 可以畫的
start_t_end = {1: [1, 2, 3, 4, 6], 2: [1, 2, 3, 4, 5, 7, 9], 3: [1, 2, 3, 5, 6, 8, 10], \
               4: [1, 2, 4, 5, 6, 7, 8, 11, 13], 5: [2, 3, 4, 5, 6, 8, 9, 12, 14], \
               6: [1, 3, 4, 5, 6, 9, 13, 10, 15], 7: [2, 4, 7, 8, 9, 11, 12], \
               8: [3, 4, 5, 7, 8, 9, 10, 12, 13], 9: [2, 5, 6, 7, 8, 9, 10, 13, 14], \
               10: [3, 6, 8, 9, 10, 14, 15], 11: [4, 7, 11, 12, 13], \
               12: [5, 7, 8, 11, 12, 13, 14], 13: [4, 6, 8, 9, 11, 12, 13, 14, 15], \
               14: [5, 9, 10, 12, 13, 14, 15], 15: [6, 10, 13, 14, 15]}
# 會畫到三個的組合
triple = [[1, 2, 4], [1, 3, 6], [2, 4, 7], [2, 5, 9], [3, 5, 8], [3, 6, 10], [4, 5, 6], \
          [4, 7, 11], [4, 8, 13], [5, 8, 12], [5, 9, 14], [6, 9, 13], [6, 10, 15], [7, 8, 9], [8, 9, 10], \
          [11, 12, 13], [12, 13, 14], [13, 14, 15]]
playerlist = list()  # 玩家
player_win_times_list = [] #記錄贏的次數

# 畫兩個
two = {1:[2,3], 2:[1,3,4,5], 3:[1,2,5,6], 4:[2,5,7,8],5:[2,3,4,6,8,9], 6:[3,5,9,10],\
       7:[4,8,11,12], 8:[4,5,7,9,12,13], 9:[5,6,8,10,13,14], 10:[6,9,14,15],\
       11:[7,12], 12:[7,8,11,13], 13:[8,9,12,14], 14:[9,10,13,15],15:[10,14]}
# 畫三個
three = {1:[4,6],2:[7,9], 3:[8,10], 4:[6,11,13],5:[12,14],6:[4,13,15], 7:[2,9],\
         8:[3,10], 9:[2,7], 10:[3,8], 11:[4,13], 12:[5,14], 13:[4,6,11,15],\
         14:[5,12], 15:[6,13]}
last_round = 15  # 用在computer()
# 數字對應座標
place_dict = {1:[315,37], 2:[245,175], 3:[385,175], 4:[175,315], 5:[315,315],\
                  6:[455,315], 7:[105,455], 8:[245,455], 9:[385,455], 10:[525,455]\
                  , 11:[37,593], 12:[175,593], 13:[315,593], 14:[455,593], 15:[593,593]}

for i in range(2):
    player_win_times_list.append([])
for i in range(2):
    player_win_times_list[i].append(0)   #贏次數的list




def pop_up(aline):  # 彈出視窗 問你yes/no
    MsgBox = tk.messagebox.askquestion('注意', "Are you sure?", icon='error')
    if MsgBox == 'no':
        for i in range(4):
            aline.pop(0)
        for i in range(2):
            temp_flag.pop(0)
        for i in circle_list:
            my_canvas.delete(i)
        for i in range(len(circle_list)):
            circle_list.pop(0)
    else:
        if aline[0] == aline[2] and aline[1] == aline[3]:
            self_line(aline)
        else:
            line(aline)
        win(flaglist, playerlist)  # let's see who wins
        # print('now drawing', playerlist[0])
        playerlist.reverse()
        if playerlist[0] == 'computer':
            computer(flaglist, start_t_end)
            win(flaglist, playerlist)
            playerlist.reverse()


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
            for i in circle_list:
                my_canvas.delete(i)
            for i in range(len(circle_list)):
                circle_list.pop(0)
            messagebox.showinfo('注意', '不能畫啦')
    elif len(temp_flag) == 1:
        if temp_flag[0] not in flaglist:
            for i in range(2):
                aline.pop(0)
            for i in range(1):
                temp_flag.pop(0)
            for i in circle_list:
                my_canvas.delete(i)
            for i in range(len(circle_list)):
                circle_list.pop(0)
            messagebox.showinfo('注意', '不能畫啦')


def line(aline):  # 畫線
    if (aline[0] - aline[2])*(aline[1] - aline[3]) >  0:
        x1 = min(aline[0], aline[2]) - 25
        y1 = min(aline[1], aline[3]) - 50
        x2 = max(aline[0], aline[2]) + 25
        y2 = max(aline[1], aline[3]) + 50
    elif (aline[0] - aline[2])*(aline[1] - aline[3]) <  0:
        x1 = max(aline[0], aline[2]) + 25
        y1 = min(aline[1], aline[3]) - 50
        x2 = min(aline[0], aline[2]) - 25
        y2 = max(aline[1], aline[3]) + 50
    else:
        x1 = min(aline[0], aline[2]) - 55
        x2 = max(aline[0], aline[2]) + 55
        y1 = aline[1]
        y2 = aline[3]
    a = my_canvas.create_line(x1, y1, x2, y2, fill='red', width=5)
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
    for i in circle_list:
        my_canvas.delete(i)
    for i in range(len(circle_list)):
        circle_list.pop(0)


def self_line(aline):
    if aline[0] >= 315:
        x = aline[0] + 25
        y = aline[1] + 50
        a = my_canvas.create_line(x, y, x - 50, y - 100, fill='red', width=5)
    else:
        x = aline[0] + 25
        y = aline[1] - 50
        a = my_canvas.create_line(x, y, x - 50, y + 100, fill='red', width=5)
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
    for i in circle_list:
        my_canvas.delete(i)
    for i in range(len(circle_list)):
        circle_list.pop(0)



# 想讓圓圈在被選到但是還沒畫線的時候能出現記號，目前做編筐
def show(num):
    global circle1, circle2, first_num
    x = place_dict[num][0]
    y = place_dict[num][1]
    if len(temp_flag) == 0:
        first_num = num
        circle1 = my_canvas.create_oval(x-35, y-35, x+35, y+35, outline='red', width=5)
        circle_list.append(circle1)
    if len(temp_flag) == 1:
        circle2 = my_canvas.create_oval(x-35, y-35, x+35, y+35, outline='red', width=5)
        circle_list.append(circle2)
        num_list = [first_num, num]
        num_list.sort()
        for i in triple:
            if num_list[0] == i[0] and num_list[1] == i[2]:
                x = place_dict[i[1]][0]
                y = place_dict[i[1]][1]
                circle3 = my_canvas.create_oval(x-35, y-35, x+35, y+35, outline='red', width=5)
                circle_list.append(circle3)


def win(flaglist, playerlist):  # 判斷勝利條件
    # playerlist[0] 是這一輪畫線的玩家
    if len(flaglist) == 1:  # 剩一個自己贏
        messagebox.showinfo('Congratulation', playerlist[0] + ' wins!!!')
        if playerlist[0] != 'computer':
            record(playerlist[0])
        if playerlist[0] == player1:
            win_times[player1] += 1
            player1_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18), bg = 'white',
                                     text="You have won {} times.".format(win_times[player1])).place(x=800, y=170)
            player2_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18),  bg = 'white',
                                     text="You have won {} times.".format(win_times[player2])).place(x=800, y=290)
        else:
            win_times[playerlist[0]] += 1
            player1_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18), bg = 'white',
                                     text="You have won {} times.".format(win_times[player1])).place(x=800, y=170)
            player2_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18),  bg = 'white',
                                     text="You have won {} times.".format(win_times[player2])).place(x=800, y=290)
        reset(linemark)
    if len(flaglist) == 0:  # 不剩對方贏
        messagebox.showinfo('Congratulation', playerlist[1] + ' wins!!!')
        if playerlist[1] != 'computer':
            record(playerlist[1])
        if playerlist[1] == player2:
            win_times[player2] += 1
            player1_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18), bg = 'white',
                                     text="You have won {} times.".format(win_times[player1])).place(x=800, y=170)
            player2_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18),  bg = 'white',
                                     text="You have won {} times.".format(win_times[player2])).place(x=800, y=290)
        else:
            win_times[playerlist[1]] += 1
            player1_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18), bg = 'white',
                                     text="You have won {} times.".format(win_times[player1])).place(x=800, y=170)
            player2_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18), bg = 'white',
                                     text="You have won {} times.".format(win_times[player2])).place(x=800, y=290)
        reset(linemark)

def record(player):
    all_line = []
    playername = []
    print('read')
    with open('rank.txt', 'r') as ranks:
        rank = ranks.readlines()
        for line in rank:
            line = line.split(',')
            line[1] = line[1].strip('\n')
            print(line[0])
            playername.append(line[0])
            if line[0] == player:
                line[1] = str(int(line[1]) + 1)
            all_line.append(line)
    if player in playername:
        with open('rank.txt', 'w') as ranks:
            for i in all_line:
                score = str(i[1])
                name = str(i[0])
                text = name+','+score+'\n'
                ranks.write(text)
    else:
        with open('rank.txt', 'a') as ranks:
            score = str(1)
            text = player+','+score+'\n'
            ranks.write(text)

def reset(linemark):  # 回復原本的設定
    for i in linemark:
        my_canvas.delete(i)  # 移除線
    for i in range(len(linemark)):
        linemark.pop(0)
    for i in range(1, 16):
        if i not in flaglist:
            flaglist.append(i)
    original_start_t_end = {1: [1, 2, 3, 4, 6], 2: [1, 2, 3, 4, 5, 7, 9], 3: [1, 2, 3, 5, 6, 8, 10], \
                            4: [1, 2, 4, 5, 6, 7, 8, 11, 13], 5: [2, 3, 4, 5, 6, 8, 9, 12, 14], \
                            6: [1, 3, 4, 5, 6, 9, 13, 10, 15], 7: [2, 4, 7, 8, 9, 11, 12], \
                            8: [3, 4, 5, 7, 8, 9, 10, 12, 13], 9: [2, 5, 6, 7, 8, 9, 10, 13, 14], \
                            10: [3, 6, 8, 9, 10, 14, 15], 11: [4, 7, 11, 12, 13], \
                            12: [5, 7, 8, 11, 12, 13, 14], 13: [4, 6, 8, 9, 11, 12, 13, 14, 15], \
                            14: [5, 9, 10, 12, 13, 14, 15], 15: [6, 10, 13, 14, 15]}
    for i in range(1, 16):
        for j in original_start_t_end[i]:
            if j not in start_t_end[i]:
                start_t_end[i].append(j)
    global last_round
    last_round = 15
    random.shuffle(playerlist)
    messagebox.showinfo('注意',playerlist[1]+' goes first')
    # 因為後面會reverse()所以我這邊寫playerlist[1]
    if playerlist[1] == 'computer':
        global second
        second = False
        computer(flaglist, start_t_end)
        playerlist.reverse()
    else:
        second = True

def computer(flaglist, start_t_end):
    global last_round
    m = len(flaglist)
    print('m=',m)
    print('last_round=',last_round)
    diff = last_round - m  # 玩家上一輪選的數量
    bline = []
    if second is False:
        if diff == 1:
            for i in range(50):
                start = random.choice(flaglist)  # 電腦隨機選兩點
                end = random.choice(start_t_end[start])
                print('start', start)
                print('end1=', end)
                if end in three[start]:
                    break
        elif diff == 2 or diff == 0:
            for i in range(50):
                start = random.choice(flaglist)  # 電腦隨機選兩點
                end = random.choice(start_t_end[start])
                print('start', start)
                print('end1=', end)
                if end in two[start]:
                    break
        elif diff == 3:
            for i in range(50):
                start = random.choice(flaglist)  # 電腦隨機選兩點
                end = random.choice(start_t_end[start])
                print('start', start)
                print('end1=', end)
                if start == end:
                    break
    else:
        if diff ==1 or diff == 3:
            for i in range(50):
                start = random.choice(flaglist)  # 電腦隨機選兩點
                end = random.choice(start_t_end[start])
                print('start', start)
                print('end1=', end)
                if end in two[start]:
                    break
        elif diff == 2:
            for i in range(50):
                start = random.choice(flaglist)  # 電腦隨機選兩點
                end = random.choice(start_t_end[start])
                print('start', start)
                print('end1=', end)
                if end in three[start] or end == start:
                    break
    if len(flaglist) == 2:
        end = start
    print('end2=',end)
    bline.append(place_dict[start][0])
    bline.append(place_dict[start][1])
    bline.append(place_dict[end][0])
    bline.append(place_dict[end][1])
    temp_flag.append(start)
    temp_flag.append(end)
    if start == end:
        self_line(bline)
    else:
        line(bline)
    last_round = len(flaglist)

def place(event):
    show(1)
    aline.append(315)  # 圓心座標
    aline.append(37)
    temp_flag.append(1)
    check_start_t_end(1, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place2(event):
    show(2)
    aline.append(245)
    aline.append(175)
    temp_flag.append(2)
    check_start_t_end(2, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place3(event):
    show(3)
    aline.append(385)
    aline.append(175)
    temp_flag.append(3)
    check_start_t_end(3, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place4(event):
    show(4)
    aline.append(175)
    aline.append(315)
    temp_flag.append(4)
    check_start_t_end(4, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place5(event):
    show(5)
    aline.append(315)
    aline.append(315)
    temp_flag.append(5)
    check_start_t_end(5, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place6(event):
    show(6)
    aline.append(455)
    aline.append(315)
    temp_flag.append(6)
    check_start_t_end(6, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place7(event):
    show(7)
    aline.append(105)
    aline.append(455)
    temp_flag.append(7)
    check_start_t_end(7, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place8(event):
    show(8)
    aline.append(245)
    aline.append(455)
    temp_flag.append(8)
    check_start_t_end(8, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place9(event):
    show(9)
    aline.append(385)
    aline.append(455)
    temp_flag.append(9)
    check_start_t_end(9, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place10(event):
    show(10)
    aline.append(525)
    aline.append(455)
    temp_flag.append(10)
    check_start_t_end(10, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place11(event):
    show(11)
    aline.append(37)
    aline.append(593)
    temp_flag.append(11)
    check_start_t_end(11, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place12(event):
    show(12)
    aline.append(175)
    aline.append(593)
    temp_flag.append(12)
    check_start_t_end(12, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place13(event):
    show(13)
    aline.append(315)
    aline.append(593)
    temp_flag.append(13)
    check_start_t_end(13, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place14(event):
    show(14)
    aline.append(455)
    aline.append(593)
    temp_flag.append(14)
    check_start_t_end(14, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)

def place15(event):
    show(15)
    aline.append(593)
    aline.append(593)
    temp_flag.append(15)
    check_start_t_end(15, temp_flag, aline, start_t_end)


#    print(aline)
#    print(flaglist)
def rule(event):
    text = 'text'
    messagebox.showinfo('遊戲規則',text)

class Game(tk.Canvas):
    def __init__(self, my_canvas, photo, ring2_image, snowman, tree, scoreb):
        tk.Canvas.__init__(self)

        #        self.root = tkinter.Tk()
        #        # 給主視窗設定標題內容
        #        self.root.title("畫圈圈")
        #        self.root.geometry('700x700')
        #        self.canvas = tkinter.Canvas(self.root, width=630, height=630, bg='white')  # 建立畫布
        #        self.canvas.pack()
        self.background(my_canvas, photo, ring2_image, snowman, tree, scoreb)
        self.circle(my_canvas)
        self.tag(my_canvas)
        self.player(playerlist)
        self.my_canvas = my_canvas

    #    my_canvas = tk.Canvas(root, width=630, height=630, bg='white')
    #    my_canvas.master.title('try this canvas')
    #    my_canvas.pack()  # 忘記這行在幹嘛 好像是確保可以使用功能 很重要 記得打
    def background(self, my_canvas, photo, ring2_image, snowman,tree,scoreb):
        self.bg = my_canvas.create_image(0,0 , image=photo)
        self.dec2 = my_canvas.create_image(900,650, image = snowman)
        self.dec = my_canvas.create_image(550,50, image = ring2_image)
        self.dec3 = my_canvas.create_image(318,325, image = tree)
        self.dec4 = my_canvas.create_image(910, 160, image = scoreb)
    def circle(self, my_canvas):
        # make a rectangle and fit in the oval
        # 設定每一個圓'70x70'之後再改
        self.circle1 = my_canvas.create_oval(280, 2, 350, 72, fill='yellow', outline='yellow')
        self.circle2 = my_canvas.create_oval(210, 140, 280, 210, fill='pink',outline='pink')
        self.circle3 = my_canvas.create_oval(350, 140, 420, 210, fill='#CD5C5C',outline='#CD5C5C')
        self.circle4 = my_canvas.create_oval(140, 280, 210, 350, fill='#CAFF70',outline='#CAFF70')
        self.circle5 = my_canvas.create_oval(280, 280, 350, 350, fill='#FFEC8B',outline='#FFEC8B')
        self.circle6 = my_canvas.create_oval(420, 280, 490, 350, fill='#F4A460',outline='#F4A460')
        self.circle7 = my_canvas.create_oval(70, 420, 140, 490, fill='#FFC1C1',outline='#FFC1C1')
        self.circle8 = my_canvas.create_oval(210, 420, 280, 490, fill='#E6E6FA',outline='#E6E6FA')
        self.circle9 = my_canvas.create_oval(350, 420, 420, 490, fill='#008000',outline='#008000')
        self.circle10 = my_canvas.create_oval(490, 420, 560, 490, fill='#008B8B',outline='#008B8B')
        self.circle11 = my_canvas.create_oval(2, 558, 72, 628, fill='#7FFFD4',outline='#7FFFD4')
        self.circle12 = my_canvas.create_oval(140, 558, 210, 628, fill='#C1FFC1',outline='#C1FFC1')
        self.circle13 = my_canvas.create_oval(280, 558, 350, 628, fill='#1E90FF',outline='#1E90FF')
        self.circle14 = my_canvas.create_oval(420, 558, 490, 628, fill='#8FBC8F',outline='#8FBC8F')
        self.circle15 = my_canvas.create_oval(558, 558, 628, 628, fill='#DDA0DD',outline='#DDA0DD')
        self.rule = my_canvas.create_rectangle(1050, 500, 1080, 520, fill='blue')                              
    # def rectangle(self, my_canvas):
    #     self.rectangle = my_canvas.create_rectangle(750, 90 ,850, 240, fill = 'pink')
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
        my_canvas.tag_bind(self.rule, '<Button-1>', rule)

    def player(self, playerlist):
        random.shuffle(playerlist)
        messagebox.showinfo('注意', playerlist[0] + ' goes first')
        if playerlist[0] == 'computer':
            global second
            second = False
            computer(flaglist, start_t_end)
            playerlist.reverse()
        else:
            second = True


def verify(account):
    user_list = []
    with open(file='lock_name_file.txt', mode='r', encoding='utf-8') as users:
        user = users.readlines()
        for line in user:
            line = line.strip('\n')
            user_list.append(line)
    # print(user_list)
    users.close()
    # new_user = open('/Users/mba/Desktop/lock_name_file.txt', 'a+')
    c = 0
    for i in range(len(user_list)):
        if account == user_list[i]:
            return 'yes'
            c += 1
            break
        else:
            c += 1
            if c == len(user_list):
                return 'noAccount'  # 要請使用著確認是否是他的名稱
            else:
                continue


def verify_if_repeated(username):
    '''驗證帳號是否重複'''
    username = username.strip()
    user_list = []
    with open(file='lock_name_file.txt', mode='r', encoding='utf-8') as users:
        user = users.readlines()
        for line in user:
            line = line.strip('\n')
            user_list.append(line)
    users.close()
    tempt = 0
    for i in range(len(user_list)):
        if username == user_list[i]:
            tempt = 1
            return 'Username repeated'
    '''未重複則紀錄'''
    if tempt == 0:
        new_user = open('lock_name_file.txt', 'a+')
        username = username+'\n'
        new_user.write(username)
        new_user.close()
        return 'sign accepted'


class Login(object):
    def __init__(self):
        # 建立主視窗,用於容納其它元件
        self.root = tkinter.Tk()
        # 給主視窗設定標題內容
        self.root.title("畫圈圈")
        self.root.geometry('450x300')
        self.canvas = tkinter.Canvas(self.root, height=200, width=500)  # 建立畫布
        self.canvas.pack(side='top')  # 放置畫布（為上端）

        # 建立一個`label`名為`Account: `
        self.label_account = tkinter.Label(self.root, text='Player1: ')
        self.label_account2 = tkinter.Label(self.root, text='Player2: ')
        # 建立一個賬號輸入框,並設定尺寸
        self.input_account = tkinter.Entry(self.root, width=30)
        self.input_account2 = tkinter.Entry(self.root, width=30)
        # 建立一個登入系統的按鈕
        self.login_button = tkinter.Button(self.root, command=self.backstage_interface, text="Login", width=10)
        # 建立一個註冊系統的按鈕
        self.siginUp_button = tkinter.Button(self.root, command=self.siginUp_interface, text="Sign up", width=10)
        # 建立一個ranking按鈕
        self.ranking_button = tkinter.Button(self.root, command=self.ranking, text = 'Ranking',width=10 )
        # 完成佈局

    def gui_arrang(self):
        self.label_account.pack()
        self.input_account.pack()
        self.login_button.pack()
        self.siginUp_button.pack()
        self.ranking_button.pack()
        self.label_account.place(x=60, y=170)
        self.input_account.place(x=135, y=170)
        self.label_account2.place(x=60, y=200)
        self.input_account2.place(x=135, y=200)
        self.login_button.place(x=120, y=240)
        self.siginUp_button.place(x=220, y=240)
        self.ranking_button.place(x=320,y=240)

    def ranking(self):
        self.ranking_window = tkinter.Toplevel()
        self.ranking_window.geometry('450x300')
        self.ranking_window.title("遊戲排名")
        rank_list = []
        with open('rank.txt','r') as ranks:
            rank = ranks.readlines()
            for line in rank:
                tempt = []
                print(line)
                line = line.split(',')
                line[1] = line[1].strip('\n')
                tempt = [int(line[1]),line[0]]
                rank_list.append(tempt)
        rank_list  = sorted(rank_list ,reverse = True)
        self.rank1 = tkinter.messagebox.showinfo(title = '天下最強玩小遊戲第一名是誰勒？？？' , message = '恭賀'+ rank_list[0][1] + '蟬聯第一名')
        print(rank_list)
        #1
        rank1 = tkinter.Label(self.ranking_window, text=rank_list[0][1]+'-------' +str(rank_list[0][0]))
        rank1.pack()
        rank1.place(x=150, y=30)
        #2
        rank2 = tkinter.Label(self.ranking_window ,text=rank_list[1][1]+'-------' +str(rank_list[1][0]))
        rank2.pack()
        rank2.place(x=150, y=60)
        #3
        rank3 = tkinter.Label(self.ranking_window ,text=rank_list[2][1]+'-------' +str(rank_list[2][0]))
        rank3.pack()
        rank3.place(x=150, y=90)
        #4
        rank4 = tkinter.Label(self.ranking_window ,text=rank_list[3][1]+'-------' +str(rank_list[3][0]))
        rank4.pack()
        rank4.place(x=150, y=120)
        #5
        rank5 = tkinter.Label(self.ranking_window,text=rank_list[4][1]+'-------' +str(rank_list[4][0]))
        rank5.pack()
        rank5.place(x=150, y=150)
        #6
        rank6 = tkinter.Label(self.ranking_window,text=rank_list[5][1]+'-------' +str(rank_list[5][0]))
        rank6.pack()
        rank6.place(x = 150,y = 180)
        #7
        rank7 = tkinter.Label(self.ranking_window ,text=rank_list[6][1]+'-------' +str(rank_list[6][0]))
        rank7.pack()
        rank7.place(x = 150,y = 210)
        #8
        rank8 = tkinter.Label(self.ranking_window,text=rank_list[7][1]+'-------' +str(rank_list[7][0]))
        rank8.pack()
        rank8.place(x = 150,y = 240)
        #9
        rank9 = tkinter.Label(self.ranking_window ,text=rank_list[8][1] +'-------' +str(rank_list[8][0]))
        rank9.pack()
        rank9.place(x = 150,y = 270)
        #10
        rank10 = tkinter.Label(self.ranking_window ,text=rank_list[9][1]+'-------' +str(rank_list[9][0]))
        rank10.pack()
        rank10.place(x = 150, y=300)




        # 進入註冊介面

    def confirm(self):
        # Create widget
        top2 = tkinter.Toplevel()
        # define title for window
        top2.title("Confirm")
        # specify size
        top2.geometry("450x300")
        username = self.entry.get()
        # Create label
        label = tkinter.Label(top2, text='Is' + '"' + username + '"' + 'your username')
        # Create exit button.
        # 回到signin頁面
        nobutton = tkinter.Button(top2, text=" Resign ", command=top2.destroy)
        # 回login頁面
        yesbutton = tkinter.Button(top2, text="yes this is my name",
                                   command=lambda: [top2.destroy(), self.verify_interface(username)])
        '''
            80行，siginUp_interface 仍然會打開
        '''
        label.pack()
        yesbutton.pack()
        nobutton.pack()
        # Display untill closed manually.
        top2.mainloop()

    # 驗證帳號是否重複
    def verify_interface(self, username):
        result = verify_if_repeated(username)
        print(result)
        if result == 'Username repeated':
            tkinter.messagebox.showinfo(title=None, message='使用者名稱重複')
            # self.siginUp_interface()
            '''若上面問題有解決，這行加上去'''
        '''
        elif result == 'sign accepted':
            #應該要回到root但是還是卡在signup interface
        '''

    # define a function for 1st toplevel
    # which is associated with root window.
    def siginUp_interface(self):
        # Create widget
        signinWindow = tkinter.Toplevel(self.root)
        # Define title for window
        signinWindow.title("signup")
        # specify size
        signinWindow.geometry("450x300")
        # Create label
        label = tkinter.Label(signinWindow,
                              text="Player username : ")
        self.entry = tkinter.Entry(signinWindow,
                                   width=30)
        # Create Exit button
        button1 = tkinter.Button(signinWindow, text="Exit",
                                 command=signinWindow.destroy)
        # create button to open toplevel2
        confirmbutton = tkinter.Button(signinWindow, text="Confirm", command=lambda: [self.confirm()])
        label.pack()
        self.entry.pack()
        confirmbutton.pack()
        button1.pack()
        # Display untill closed manually
        signinWindow.mainloop()

        # 進行登入資訊驗證

    def backstage_interface(self):
        account = self.input_account.get()
        account2 = self.input_account2.get()
        print(account)
        print(account2)
        # 對賬戶資訊進行驗證，普通使用者返回user，賬戶錯誤返回noAccount
        verifyResult = verify(account)
        verifyResult2 = verify(account2)
        if verifyResult == 'yes' and verifyResult2 == 'yes':
            tkinter.messagebox.showinfo(title='小遊戲開始！', message='登入成功')
            self.root.destroy()
            '''開啟小遊戲連結'''
            global player1
            player1 = account
            global player2
            player2 = account2
            global playerlist
            playerlist = [player1, player2]
            global root1
            root1 = Tk()  # 視窗
            root1.geometry('1200x700')
            root1.title("畫圈圈")
            root1.resizable()
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load('Holly Dazed - RKVC.mp3')
            pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.
            
            global my_canvas
            my_canvas = tk.Canvas(root1, width=1500, height=1300, bg='#8B0000')
            imgpath = 'bg.gif'
            img = Image.open(imgpath)
            photo = ImageTk.PhotoImage(img)
            ring2_image = tk.PhotoImage(file='ring2.gif')
            snowman = tk.PhotoImage(file = 'snowman.gif')
            tree = tk.PhotoImage(file = 'tree.gif')
            scoreb = tk.PhotoImage(file = 'scoreb.gif')
            arrow = tk.PhotoImage(file = 'arrow.gif')
            global win_times
            win_times = {player1: player_win_times_list[0][0], player2: player_win_times_list[1][0]}
            title_score = tk.Label(root1, font=("Arial Rounded MT Bold", 35, "bold"),  bg = 'white',text='SCORE:', foreground = 'black' ).place(x=800, y=50)
            player1_name = tk.Label(root1, font=("Arial Rounded MT Bold", 18),   bg = 'white',text="{}".format("NAME:  "+player1), foreground = 'black' ).place(x=800, y=110)
            player1_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18), bg = 'white',   text="You have won 0 times.", foreground = 'black').place(x=800, y=170)
            player2_name = tk.Label(root1, font=("Arial Rounded MT Bold", 18),  bg = 'white', text="{}".format("NAME:  "+player2), foreground = 'black').place(x=800, y=230)
            player2_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18), bg = 'white', text="You have won 0 times.", foreground = 'black').place(x=800, y=290)
            my_canvas.pack(fill = tk.BOTH)
            if playerlist[1] == player1 :
                point1_label = tk.Label(root1,image=arrow).place(x=1000,y=90)
            elif playerlist[1] == player2 :
                point2_label = tk.Label(root1,image=arrow).place(x=1000,y=210)
            game = Game(my_canvas, photo, ring2_image, snowman, tree, scoreb)
            root1.mainloop()

        elif verifyResult == 'noAccount' and verifyResult2 == 'yes':
            tkinter.messagebox.showinfo(title='小遊戲需要你的註冊', message=" '" + account + "' " + '玩家1不存在請重新輸入!')

        elif verifyResult == 'yes' and verifyResult2 == 'noAccount':
            tkinter.messagebox.showinfo(title='小遊戲需要你的註冊', message=" '" + account2 + "' " + '玩家2不存在請重新輸入!')

        elif verifyResult == 'noAccount' and verifyResult2 == 'noAccount':
            tkinter.messagebox.showinfo(title='小遊戲需要你的註冊',
                                        message="'" + account + "' " + " '" + account2 + "'" + '玩家1&2都不存在請重新輸入!')


def main():
    # 初始化物件
    L = Login()
    # 進行佈局
    L.gui_arrang()
    # 主程式執行
    tkinter.mainloop()


if __name__ == '__main__':
    main()

# 備份