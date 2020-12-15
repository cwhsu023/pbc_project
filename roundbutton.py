from tkinter import Tk
import tkinter as tk

root = Tk()

class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0, 
            relief="flat", highlightthickness=0, bg=bg)
        self.command = command

        if cornerradius > 0.5*width:
            print("Error: cornerradius is greater than width.")
            return None

        if cornerradius > 0.5*height:
            print("Error: cornerradius is greater than height.")
            return None

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

def test1():
    print("愛")
def test2():
    print("我")
def test3():
    print("你")
    

canvas = tk.Canvas(root, height=500, width=700, bg = 'white')
canvas.pack()

button1 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test2)
button2 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test3)
button3 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test1)
button4 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test2)
button5 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test3)
button6 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test1)
button7 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test2)
button8 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test3)
button9 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test1)
button10 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test2)
button11 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test3)
button12 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test1)
button13 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test2)
button14 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test3)
button15 = RoundedButton(root, 100, 100, 50, 0.02, 'pink', 'white', command=test1)
button1.place(relx= .4, rely= 0)
button2.place(relx= .3, rely=.2)
button3.place(relx= .5, rely=.2)
button4.place(relx= .2, rely=.4)
button5.place(relx= .4, rely=.4)
button6.place(relx= .6, rely=.4)
button7.place(relx= .1, rely=.6)
button8.place(relx= .3, rely=.6)
button9.place(relx= .5, rely=.6)
button10.place(relx= .7, rely=.6)
button11.place(relx= .0, rely=.8)
button12.place(relx= .2, rely=.8)
button13.place(relx= .4, rely=.8)
button14.place(relx= .6, rely=.8)
button15.place(relx= .8, rely=.8)
button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15.master.title('round button')

# ,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15

root.mainloop()