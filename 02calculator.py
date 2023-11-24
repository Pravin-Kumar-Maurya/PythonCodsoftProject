from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
            scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()
    elif text == "x":
        new=scvalue.get()[:-1]
        scvalue.set(new)
        screen.update
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.minsize("380","530")
root.maxsize("380","530")
root.title("Calculator")

#icon
Image_icon = PhotoImage(file="images/calc.png")
root.iconphoto(False,Image_icon)

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="lucida 33",width=15,borderwidth=1,border=3)
screen.pack(ipadx=5,ipady=5)

f = Frame(root,bg="white")
b = Button(f,text="c",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=[10,5],pady=5)
b = Button(f,text="x",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b = Button(f,text="%",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b = Button(f,text="/",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=[5,10],pady=5)
f.pack()

f = Frame(root,bg="white")
b = Button(f,text="9",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=[10,5],pady=5)
b = Button(f,text="8",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b = Button(f,text="7",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b = Button(f,text="*",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=[5,10],pady=5)
f.pack()

f = Frame(root,bg="white")
b = Button(f,text="6",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=[10,5],pady=5)
b = Button(f,text="5",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b = Button(f,text="4",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b = Button(f,text="4",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b = Button(f,text="-",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=[5,10],pady=5)
f.pack()

f = Frame(root,bg="white")
b = Button(f,text="3",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=[10,5],pady=5)
b = Button(f,text="2",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b = Button(f,text="1",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)
b = Button(f,text="+",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=[5,10],pady=5)
f.pack()

f = Frame(root,bg="white")
b = Button(f,text="0",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=[10,5],pady=[5,10])
b = Button(f,text=".",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=[5,10])
b = Button(f,text="00",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=[5,10])
b = Button(f,text="=",width=3, font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=[5,10],pady=5)
f.pack()






root.mainloop()