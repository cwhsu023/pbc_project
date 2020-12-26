# 這是系統的登入介面
#兩個玩家
import tkinter
from tkinter import messagebox
from tkinter import Tk
import tkinter as tk
import random
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
playerlist = list()  # 玩家
player_win_times_list = []

for i in range(2) :
    player_win_times_list.append([])
for i in range(2) :
    player_win_times_list[i].append(0)
    
#win_times = {player1:player_win_times_list[0][0],player2:player_win_times_list[1][0]}


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
        
#        self.root = tkinter.Tk()
#        # 給主視窗設定標題內容
#        self.root.title("畫圈圈")
#        self.root.geometry('700x700')
#        self.canvas = tkinter.Canvas(self.root, width=630, height=630, bg='white')  # 建立畫布
#        self.canvas.pack()
        
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
def verify(account):
    user_list = []
    with open(file='lock_name_file.txt', mode='r', encoding='utf-8') as users:
        user = users.readlines()
        for line in user:
            line = line.strip('\n')
            user_list.append(line)
    #print(user_list)
    users.close()
    #new_user = open('/Users/mba/Desktop/lock_name_file.txt', 'a+')
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
        new_user.write(username)
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
        self.siginUp_button = tkinter.Button(self.root, command= self.siginUp_interface, text="Sign up", width=10)

        # 完成佈局
    def gui_arrang(self):
        self.label_account.pack()
        self.input_account.pack()
        self.login_button.pack()
        self.siginUp_button.pack()
        self.label_account.place(x=60, y=170)
        self.input_account.place(x=135, y=170)
        self.label_account2.place(x=60, y=200)
        self.input_account2.place(x=135, y=200)
        self.login_button.place(x=140, y=240)
        self.siginUp_button.place(x=240, y=240)

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
        label = tkinter.Label(top2, text = 'Is' + '"' + username + '"' + 'your username')
        # Create exit button.
        #回到signin頁面
        nobutton = tkinter.Button(top2, text=" Resign ", command=top2.destroy)
        #回login頁面
        yesbutton = tkinter.Button(top2,text="yes this is my name" , command = lambda:[top2.destroy(),self.verify_interface(username)])
        '''
            80行，siginUp_interface 仍然會打開
        '''
        label.pack()
        yesbutton.pack()
        nobutton.pack()
        # Display untill closed manually.
        top2.mainloop()

    #驗證帳號是否重複
    def verify_interface(self,username):
        result = verify_if_repeated(username)
        print(result)
        if result == 'Username repeated':
            tkinter.messagebox.showinfo(title= None , message = '使用者名稱重複')
            #self.siginUp_interface()
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
                                  width = 30)
        # Create Exit button
        button1 = tkinter.Button(signinWindow, text="Exit",
                                 command=signinWindow.destroy)
        # create button to open toplevel2
        confirmbutton = tkinter.Button(signinWindow, text="Confirm",command=lambda:[self.confirm() ])
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
            root1.geometry('1360x1280')
            root1.title("畫圈圈")
            root1.resizable()
            win_times = {player1:player_win_times_list[0][0],player2:player_win_times_list[1][0]}
            player1_name = tk.Label(root1,font=("Ariel",40),text = "{}".format(player1)).place(x=100,y=20)
            player1_score = tk.Label(root1,font=("Ariel",30),text = "You have won 0 times.").place(x=100,y=120)
            player2_name = tk.Label(root1,font=("Ariel",40),text = "{}".format(player2)).place(x=100,y=220)
            player2_score = tk.Label(root1,font=("Ariel",30),text = "You have won 0 times.").place(x=100,y=320)
            global my_canvas
            my_canvas = tk.Canvas(root1, width=630, height=630, bg='white')
            my_canvas.pack()
            game = Game(my_canvas)
            root1.mainloop()

        elif verifyResult == 'noAccount' and verifyResult2 == 'yes':
            tkinter.messagebox.showinfo(title='小遊戲需要你的註冊', message="'" + account + "'" + '玩家1不存在請重新輸入!')

        elif verifyResult == 'yes' and verifyResult2 == 'noAccount':
            tkinter.messagebox.showinfo(title='小遊戲需要你的註冊', message="'" + account2 + "'" + '玩家2不存在請重新輸入!')

        elif verifyResult == 'noAccount' and verifyResult2 == 'noAccount':
            tkinter.messagebox.showinfo(title='小遊戲需要你的註冊', message="'" + account + "'" + "'" + account2 + "'" + '玩家1&2都不存在請重新輸入!')

def win(flaglist, playerlist):  # 判斷勝利條件
    # playerlist[0] 是這一輪畫線的玩家
    if len(flaglist) == 1:  # 剩一個自己贏
        messagebox.showinfo('Congratulation', playerlist[0]+' wins!!!')
        if playerlist[0] == player1 :
            win_times[player1] += 1
            player1_score = tk.Label(root1,font=("Ariel",30),text="You have won {} times.".format(win_times[player1])).place(x=100,y=120)
            player2_score = tk.Label(root1,font=("Ariel",30),text="You have won {} times.".format(win_times[player2])).place(x=100,y=320)
        else :
            win_times[playerlist[0]] += 1
            player1_score = tk.Label(root1,font=("Ariel",30),text="You have won {} times.".format(win_times[player1])).place(x=100,y=120)
            player2_score = tk.Label(root1,font=("Ariel",30),text="You have won {} times.".format(win_times[player2])).place(x=100,y=320)
        reset(linemark)
    if len(flaglist) == 0:  # 不剩對方贏
        messagebox.showinfo('Congratulation', playerlist[1]+' wins!!!')
        if playerlist[1] == player2 :
            win_times[player2] += 1
            player1_score = tk.Label(root1,font=("Ariel",30),text="You have won {} times.".format(win_times[player1])).place(x=100,y=120)
            player2_score = tk.Label(root1,font=("Ariel",30),text="You have won {} times.".format(win_times[player2])).place(x=100,y=320)
        else :
            win_times[playerlist1[1]] += 1
            player1_score = tk.Label(root1,font=("Ariel",30),text="You have won {} times.".format(win_times[player1])).place(x=100,y=120)
            player2_score = tk.Label(root1,font=("Ariel",30),text="You have won {} times.".format(win_times[player2])).place(x=100,y=320)
        reset(linemark)

def main():
    # 初始化物件
    L = Login()
    # 進行佈局
    L.gui_arrang()
    # 主程式執行
    tkinter.mainloop()
if __name__ == '__main__':
    main()

