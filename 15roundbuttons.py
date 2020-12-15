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

def test():
    print("連")

canvas = tk.Canvas(root, height=300, width=500)
canvas.pack()

button1 = RoundedButton(root, 10, 10, 5, 0.2, 'red', 'white', command=test)
button2 = RoundedButton(root, 10, 10, 5, 0.2, 'yellow', 'white', command=test)
button3 = RoundedButton(root, 10, 10, 5, 0.2, 'green', 'white', command=test)
button4 = RoundedButton(root, 10, 10, 5, 0.2, 'blue', 'white', command=test)
button5 = RoundedButton(root, 10, 10, 5, 0.2, 'black', 'white', command=test)
button6 = RoundedButton(root, 10, 10, 5, 0.2, 'grey', 'white', command=test)
button7 = RoundedButton(root, 10, 10, 5, 0.2, 'pink', 'white', command=test)
button8 = RoundedButton(root, 10, 10, 5, 0.2, 'red', 'white', command=test)
button9 = RoundedButton(root, 10, 10, 5, 0.2, 'yellow', 'white', command=test)
button10 = RoundedButton(root, 10, 10, 5, 0.2, 'green', 'white', command=test)
button11 = RoundedButton(root, 10, 10, 5, 0.2, 'blue', 'white', command=test)
button12 = RoundedButton(root, 10, 10, 5, 0.2, 'pink', 'white', command=test)
button13 = RoundedButton(root, 10, 10, 5, 0.2, 'black', 'white', command=test)
button14 = RoundedButton(root, 10, 10, 5, 0.2, 'red', 'white', command=test)
button15 = RoundedButton(root, 10, 10, 5, 0.2, 'green', 'white', command=test)
button1.place(relx=.1, rely=.1)
button2.place(relx=.2, rely=.1)
button3.place(relx=.3, rely=.1)
button4.place(relx=.4, rely=.1)
button5.place(relx=.5, rely=.1)
button6.place(relx=.6, rely=.1)
button7.place(relx=.7, rely=.1)
button8.place(relx=.8, rely=.1)
button9.place(relx=.9, rely=.1)
button10.place(relx=.10, rely=.1)
button11.place(relx=.11, rely=.1)
button12.place(relx=.12, rely=.1)
button13.place(relx=.13, rely=.1)
button14.place(relx=.14, rely=.1)
button15.place(relx=.15, rely=.1)
button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15.master.title('round button')



root.mainloop()