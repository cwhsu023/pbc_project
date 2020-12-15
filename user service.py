# 這是系統的登入介面

import tkinter
from tkinter import messagebox


def verify(account):
    account = account.lower().strip()
    user_list = []
    with open(file='/Users/mba/Desktop/lock_name_file.txt', mode='r', encoding='utf-8') as users:
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
        self.label_account = tkinter.Label(self.root, text='Account: ')

        # 建立一個賬號輸入框,並設定尺寸
        self.input_account = tkinter.Entry(self.root, width=30)

        # 建立一個登入系統的按鈕
        self.login_button = tkinter.Button(self.root, command=self.backstage_interface, text="Login", width=10)
        # 建立一個註冊系統的按鈕
        self.siginUp_button = tkinter.Button(self.root, command=self.siginUp_interface, text="Sign up", width=10)

        # 完成佈局

    def gui_arrang(self):
        self.label_account.place(x=60, y=170)
        self.input_account.place(x=135, y=170)
        self.login_button.place(x=140, y=235)
        self.siginUp_button.place(x=240, y=235)

        # 進入註冊介面

    def siginUp_interface(self):
        #self.root.destroy()
        tkinter.messagebox.showinfo(title='小遊戲要開始啦，還不註冊嗎？', message='進入註冊介面')
        self.root = tkinter.Tk()
        self.root.title('註冊')
        self.root.geometry('450x300')
        self.canvas = tkinter.Canvas(self.root, height=200, width=500)  # 建立畫布
        self.canvas.pack(side='top')
        # 建立一個`label`名為`input username: `
        self.label_username = tkinter.Label(self.root, text='username: ')
        # 建立一個賬號輸入框,並設定尺寸
        self.input_username = tkinter.Entry(self.root, width=30)
        # 進行登入資訊驗證


    def backstage_interface(self):
        account = self.input_account.get().ljust(10, " ")
        # 對賬戶資訊進行驗證，普通使用者返回user，管理員返回master，賬戶錯誤返回noAccount，密碼錯誤返回noPassword
        verifyResult = verify(account)
        if verifyResult == 'yes':
            self.root.destroy()
            tkinter.messagebox.showinfo(title='小遊戲開始！', message='登入成功')
        elif verifyResult == 'noAccount':
            tkinter.messagebox.showinfo(title='小遊戲需要你的登入', message='該賬號不存在請重新輸入!')


def main():
    # 初始化物件
    L = Login()
    # 進行佈局
    L.gui_arrang()
    # 主程式執行
    tkinter.mainloop()


if __name__ == '__main__':
    main()