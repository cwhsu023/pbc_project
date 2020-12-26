# 這是系統的登入介面
#兩個玩家
import tkinter
from tkinter import messagebox

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
            self.root.destroy()
            messagebox.showinfo(title='小遊戲開始！', message='登入成功')
            '''開啟小遊戲連結'''

        elif verifyResult == 'noAccount' and verifyResult2 == 'yes':
            tkinter.messagebox.showinfo(title='小遊戲需要你的註冊', message="'" + account + "'" + '玩家1不存在請重新輸入!')

        elif verifyResult == 'yes' and verifyResult2 == 'noAccount':
            tkinter.messagebox.showinfo(title='小遊戲需要你的註冊', message="'" + account2 + "'" + '玩家2不存在請重新輸入!')

        elif verifyResult == 'noAccount' and verifyResult2 == 'noAccount':
            tkinter.messagebox.showinfo(title='小遊戲需要你的註冊', message="'" + account + "'" + "'" + account2 + "'" + '玩家1&2都不存在請重新輸入!')


def main():
    # 初始化物件
    L = Login()
    # 進行佈局
    L.gui_arrang()
    # 主程式執行
    tkinter.mainloop()
if __name__ == '__main__':
    main()