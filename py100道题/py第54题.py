from tkinter import *
def main():
    root = Tk()
    w = Canvas(
        root,
        width=400,
        height=400,
        background="white"
    )
    w.pack()

    w.create_line(0, 200,
                  400, 200,
                  fill='red')
    mainloop()
main()
