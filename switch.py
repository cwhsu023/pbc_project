# 這是系統的登入介面
# 兩個玩家
import tkinter
from tkinter import messagebox
from tkinter import Tk
import tkinter as tk
# from tkinter import *
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
player_win_times_list = []  # 記錄贏的次數

# 畫兩個
two = {1: [2, 3], 2: [1, 3, 4, 5], 3: [1, 2, 5, 6], 4: [2, 5, 7, 8], 5: [2, 3, 4, 6, 8, 9], 6: [3, 5, 9, 10], \
       7: [4, 8, 11, 12], 8: [4, 5, 7, 9, 12, 13], 9: [5, 6, 8, 10, 13, 14], 10: [6, 9, 14, 15], \
       11: [7, 12], 12: [7, 8, 11, 13], 13: [8, 9, 12, 14], 14: [9, 10, 13, 15], 15: [10, 14]}
# 畫三個
three = {1: [4, 6], 2: [7, 9], 3: [8, 10], 4: [6, 11, 13], 5: [12, 14], 6: [4, 13, 15], 7: [2, 9], \
         8: [3, 10], 9: [2, 7], 10: [3, 8], 11: [4, 13], 12: [5, 14], 13: [4, 6, 11, 15], \
         14: [5, 12], 15: [6, 13]}
last_round = 15  # 用在computer()
# 數字對應座標
place_dict = {1: [315, 37], 2: [245, 175], 3: [385, 175], 4: [175, 315], 5: [315, 315], \
              6: [455, 315], 7: [105, 455], 8: [245, 455], 9: [385, 455], 10: [525, 455] \
    , 11: [37, 593], 12: [175, 593], 13: [315, 593], 14: [455, 593], 15: [593, 593]}

#切換畫面
class switch_PAGE(tk.Tk):
    def __init__(self):
        self.start = tk.Tk.__init__(self)
        self._frame = None
        self.switchFrame(start_page)

    def switchFrame(self,frame_class):
        print('here')
        print(frame_class)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class start_page(tk.Frame):
    def __init__(self,master):
        print("it here")
        tk.Frame.__init__(self, master)
        # 建立主視窗,用於容納其它元件
        self.root = tkinter.Tk()
        # 給主視窗設定標題內容
        self.root.title("選擇模式")
        self.root.geometry('450x300')
        self.canvas = tkinter.Canvas(self.root, height=200, width=500)  # 建立畫布
        self.canvas.pack(side='top')  # 放置畫布（為上端）
        self.label = tk.Label(self.root, text="Start game ", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        self.button1 = tk.Button(self.root, text = 'Person to Person !!! Real fight between us !' , command=lambda:{ master.switchFrame(Login)}).pack(side="top", fill="x", pady=5)
        self.button2 = tk.Button(self.root, text='Person to Computer !!! lets have some practice first!',
                  command=lambda: {master.switchFrame(Login_with_computer)}).pack()


for i in range(2):
    player_win_times_list.append([])
for i in range(2):
    player_win_times_list[i].append(0)  # 贏次數的list


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
    if (aline[0] - aline[2]) * (aline[1] - aline[3]) > 0:
        x1 = min(aline[0], aline[2]) - 25
        y1 = min(aline[1], aline[3]) - 50
        x2 = max(aline[0], aline[2]) + 25
        y2 = max(aline[1], aline[3]) + 50
    elif (aline[0] - aline[2]) * (aline[1] - aline[3]) < 0:
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
        circle1 = my_canvas.create_oval(x - 35, y - 35, x + 35, y + 35, outline='red', width=5)
        circle_list.append(circle1)
    if len(temp_flag) == 1:
        circle2 = my_canvas.create_oval(x - 35, y - 35, x + 35, y + 35, outline='red', width=5)
        circle_list.append(circle2)
        num_list = [first_num, num]
        num_list.sort()
        for i in triple:
            if num_list[0] == i[0] and num_list[1] == i[2]:
                x = place_dict[i[1]][0]
                y = place_dict[i[1]][1]
                circle3 = my_canvas.create_oval(x - 35, y - 35, x + 35, y + 35, outline='red', width=5)
                circle_list.append(circle3)


def win(flaglist, playerlist):  # 判斷勝利條件
    # playerlist[0] 是這一輪畫線的玩家
    if len(flaglist) == 1:  # 剩一個自己贏
        messagebox.showinfo('Congratulation', playerlist[0] + ' wins!!!')
        if playerlist[0] != 'computer':
            record(playerlist[0])
        if playerlist[0] == player1:
            win_times[player1] += 1
            player1_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18), bg='white',
                                     text="You have won {} times.".format(win_times[player1])).place(x=800, y=170)
            player2_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18), bg='white',
                                     text="You have won {} times.".format(win_times[player2])).place(x=800, y=290)
        else:
            win_times[playerlist[0]] += 1
            player1_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18), bg='white',
                                     text="You have won {} times.".format(win_times[player1])).place(x=800, y=170)
            player2_score = tk.Label(root1, font=("Arial Rounded MT Bold", 18), bg='white',
                                     text="You have won {} times.".format(win_times[player2])).place(x=800, y=290)
        reset(linem
