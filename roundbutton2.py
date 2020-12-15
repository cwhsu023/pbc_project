# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:38:47 2020

@author: 1234
"""
import tkinter as tk

class roundbutton(tk.Frame):
    def __init__(self):  # 照抄
        tk.Frame.__init__(self)
        self.grid()
        self.createbutton()
    def createbutton(self):
        # relief = "flat" 去除button的陰影
        self.button1 = tk.Button(self, text = '1', command = None, relief = 'flat')
        self.button2 = tk.Button(self, text = '2', command = None, relief = 'flat')
        self.button3 = tk.Button(self, text = '3', command = None, relief = 'flat')
        self.button4 = tk.Button(self, text = '4', command = None, relief = 'flat')
        self.button5 = tk.Button(self, text = '5', command = None, relief = 'flat')
        self.button6 = tk.Button(self, text = '6', command = None, relief = 'flat')
        self.button7 = tk.Button(self, text = '7', command = None, relief = 'flat')
        self.button8 = tk.Button(self, text = '8', command = None, relief = 'flat')
        self.button9 = tk.Button(self, text = '9', command = None, relief = 'flat')
        self.button10 = tk.Button(self, text = '10', command = None, relief = 'flat')
        self.button11 = tk.Button(self, text = '11', command = None, relief = 'flat')
        self.button12 = tk.Button(self, text = '12', command = None, relief = 'flat')
        self.button13 = tk.Button(self, text = '13', command = None, relief = 'flat')
        self.button14 = tk.Button(self, text = '14', command = None, relief = 'flat')
        self.button15 = tk.Button(self, text = '15', command = None, relief = 'flat')
        self.button1.grid(row = 0, column = 4, columnspan = 1, sticky = tk.NE + tk.SW)  # 指定位置
        self.button2.grid(row = 1, column = 3, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button3.grid(row = 1, column = 5, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button4.grid(row = 2, column = 2, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button5.grid(row = 2, column = 4, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button6.grid(row = 2, column = 6, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button7.grid(row = 3, column = 1, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button8.grid(row = 3, column = 3, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button9.grid(row = 3, column = 5, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button10.grid(row = 3, column = 7, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button11.grid(row = 4, column = 0, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button12.grid(row = 4, column = 2, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button13.grid(row = 4, column = 4, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button14.grid(row = 4, column = 6, columnspan = 1, sticky = tk.NE + tk.SW)
        self.button15.grid(row = 4, column = 8, columnspan = 1, sticky = tk.NE + tk.SW)

        
button = roundbutton()
button.master.title("Round Button")  # 視窗名稱
button.mainloop()  # 持續執行，看有沒有指令
'''
現在有15個button按照我們想要的陣型排好
要想辦法變成圓形和連線
看要改用canvas做還是繼續用frame
'''