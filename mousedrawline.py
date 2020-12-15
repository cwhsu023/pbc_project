from tkinter import *


def main():
    root = Tk()
    w = Canvas(root, width=200, height=200, background="white")
    w.pack()

    def _paint(event):
        # event.x 鼠標左鍵的橫坐標
        # event.y 鼠標左鍵的縱坐標
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        w.create_oval(x1, y1, x2, y2, fill="red")

    # 鼠標左鍵一點，就畫出了一個小的橢圓

    # 畫布與鼠標左鍵進行綁定
    w.bind("<B1-Motion>", _paint)

    mainloop()


if __name__ == '__main__':
    main()