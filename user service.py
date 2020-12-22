# 這是系統的登入介面
#兩個玩家
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
    def __init__(self,master=None):
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


    def siginUp_interface(self):
        self.signinWindow = tkinter.Toplevel(self.root)
        self.signinWindow.geometry('450x300')
        self.label_username = tkinter.Label(self.signinWindow,text = 'username')
        self.input_username = tkinter.Entry(self.signinWindow,width = 30)
        username = self.input_username.get().ljust(10, " ")
        '''
            button沒用，confirm鍵不會跳出confirm_username(username)
            然後按signup會直接跳出confirm_username(username)  77行的錯
        '''
        self.confirmButton = tkinter.Button(self.signinWindow,text = 'Confirm',  command = self.confirm_username(username))

        self.label_username.pack()
        self.input_username.pack()
        self.confirmButton.pack()
        self.label_username.place(x=60, y=170)
        self.input_username.place(x=150,y=170)
        self.confirmButton.place(x=140, y=200)
        #self.signinWindow.mainloop()
        #signinWindow.destroy()
        # 進行登入資訊驗證


    def confirm_username(self,username):
        self.confirm = tkinter.messagebox.askyesno(title='確認使用者名稱', message=username)

    def backstage_interface(self):
        account = self.input_account.get().ljust(10, " ")
        account2 = self.input_account2.get().ljust(10, " ")
        # 對賬戶資訊進行驗證，普通使用者返回user，賬戶錯誤返回noAccount
        verifyResult = verify(account)
        verifyResult2 = verify(account2)
        if verifyResult == 'yes' and verifyResult2 == 'yes':
            self.root.destroy()
            tkinter.messagebox.showinfo(title='小遊戲開始！', message='登入成功')

        elif verifyResult == 'noAccount' and verifyResult2 == 'yes':
            tkinter.messagebox.showinfo(title='小遊戲需要你的註冊', message="'" + account + "'" + '玩家1不存在請重新輸入!')

        elif verifyResult == 'yes' and verifyResult2 == 'noAccount':
            self.root.destroy()
            tkinter.messagebox.showinfo(title='小遊戲需要你的註冊', message="'" + account2 + "'" + '玩家2不存在請重新輸入!')

        elif verifyResult == 'noAccount' and verifyResult2 == 'noAccount':
            self.root.destroy()
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