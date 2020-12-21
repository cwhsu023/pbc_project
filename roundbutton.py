from tkinter import Tk
import tkinter as tk

root = Tk()

class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0, 
            relief="flat", highlightthickness=0, bg=bg)
        self.command = command

        # if cornerradius > 0.5*width:
        #     print("Error: cornerradius is greater than width.")
        #     return None

        # if cornerradius > 0.5*height:
        #     print("Error: cornerradius is greater than height.")
        #     return None

        rad = 2*cornerradius
        def shape():
            self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
            self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)


        id = shape()
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()
aline = []

def test1():
    print("x=200,y=0")
    aline.append([200, 0])
    print(aline)

def test2():
    print("x=150,y=100")
    aline.append([150, 100])
    print(aline)
def test3():
    print("x=250,y=100")
    aline.append([250, 100])
    print(aline)
def test4():
    print("x=100,y=200")
    aline.append([100, 100])
    print(aline)
def test5():
    print("x=200,y=200")
    aline.append([200, 200])
    print(aline)
def test6():
    print("x=300,y=200")
    aline.append([300, 200])
    print(aline)
def test7():
    print("x=50,y=300")
    aline.append([50, 300])
    print(aline)
def test8():
    print("x=150,y=300")
    aline.append([150, 300])
    print(aline)
def test9():
    print("x=250,y=300")
    aline.append([250, 300])
    print(aline)
def test10():
    print("x=350,y=300")
    aline.append([350, 300])
    print(aline)
def test11():
    print("x=0,y=400")
    aline.append([0, 400])
    print(aline)
def test12():
    print("x=100,y=400")
    aline.append([100, 400])
    print(aline)
def test13():
    print("x=200,y=400")
    aline.append([200, 400])
    print(aline)
def test14():
    print("x=300,y=400")
    aline.append([300, 400])
def test15():
    print("x=400,y=400")
    aline.append([400, 400])
    print(aline)

canvas = tk.Canvas(root, height=2000, width=750, bg = 'white')
canvas.pack()

button1 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test1)
button2 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test2)
button3 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test3)
button4 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test4)
button5 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test5)
button6 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test6)
button7 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test7)
button8 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test8)
button9 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test9)
button10 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test10)
button11 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test11)
button12 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test12)
button13 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test13)
button14 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test14)
button15 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test15)
button1.place(x= 200, y= 0)
button2.place(x= 150, y=100)
button3.place(x= 250, y=100)
button4.place(x= 100, y=200)
button5.place(x= 200, y=200)
button6.place(x= 300, y=200)
button7.place(x= 50, y=300)
button8.place(x= 150, y=300)
button9.place(x= 250, y=300)
button10.place(x= 350, y=300)
button11.place(x= 0, y=400)
button12.place(x= 100, y=400)
button13.place(x= 200, y=400)
button14.place(x= 300, y=400)
button15.place(x= 400, y=400)
button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15.master.title('round button')

# ,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15

root.mainloop()

