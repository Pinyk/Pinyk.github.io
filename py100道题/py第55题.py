from tkinter import *
def main():
    root = Tk()
    w = Canvas(
        root,
        width=200,
        height=200,
        background="white"
    )
    w.pack()
    w.create_rectangle(
        50, 50,
        100, 100,
    )
    mainloop()
main()
