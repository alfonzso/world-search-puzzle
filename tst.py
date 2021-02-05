from tkinter import *

root = Tk()


# # def spinbox1_callback():
# #     print("faff")

frame = Frame(root, height=400, width=450, )
frame.pack()


T = Text(frame)  # , height=2, width=30, )  # command=spinbox1_callback)
# T.set
hei = 50
T.place(x=10, y=115, height=hei, width=400)
# T.pack()

_max = -1


def motion(event):
    # T.set
    global hei
    global _max
    # print(T.winfo_width)
    hei += 12.5
    _str = T.get("1.0", END)
    print(
        _str,
        len(_str.splitlines())
    )
    if _max < len(_str.splitlines()):
        _max = len(_str.splitlines())

    if len(_str.splitlines()) >= 2:
        T.place(x=10, y=115, height=hei, width=400)
    print("Mouse position: (%s %s)" % (event.x, event.y))
    return


def neg_motion(event):
    # T.set
    global hei
    global _max
    # print(T.winfo_width)

    _str = T.get("1.0", END)
    print(
        _str,
        len(_str.splitlines())
    )
    if _max > len(_str.splitlines()):
        hei -= 12.5
        _max = len(_str.splitlines())
        T.place(x=10, y=115, height=hei, width=400)
    # print("Mouse position: (%s %s)" % (event.x, event.y))
    return


T.bind('<Return>', motion)
T.bind('<BackSpace>', neg_motion)

# # myvar = StringVar()
# # myvar.set('')
# mywidget = Entry(root,textvariable=T,width=10)
# mywidget.pack()

# def oddblue(a,b,c):
#     if len(T.get())%2 == 0:
#         mywidget.config(bg='red')
#     else:
#         mywidget.config(bg='blue')
#     mywidget.update_idletasks()

# T.trace('w',oddblue)

root.mainloop()

# import tkinter as tk
# from tkinter import messagebox as tk_messagebox

# root = tk.Tk()


# def callback(event):
#     tk_messagebox.showinfo("clicked at", "%d %d" % (event.x, event.y))


# frame = tk.Frame(root, width=100, height=100)
# frame.bind("<Button-1>", callback)
# frame.pack()

# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox as tk_messagebox

# def spinbox1_callback():
#     tk_messagebox.showinfo("Spinbox callback", "You changed the spinbox.")

# if __name__ == "__main__":
#     master = tk.Tk()
#     spinbox1 = tk.Spinbox(master, from_=0, to=10, command=spinbox1_callback)
#     spinbox1.pack()
#     tk.mainloop()
