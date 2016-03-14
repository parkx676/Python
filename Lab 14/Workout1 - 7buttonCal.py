## 7-Button Calculator

from tkinter import *

win = Tk()
win.geometry("400x200")
win.title("Calculator")

def add1():
    eqn.insert(END,"1")
    
def add2():
    eqn.insert(END,"2")
    
def add3():
    eqn.insert(END,"3")

def addplus():
    eqn.insert(END,"+")

def addminus():
    eqn.insert(END,"-")
    
def clear():
    eqn.delete(0,END)

def evalu():
    ans = eval(eqn.get())
    eqn.delete(0,END)
    eqn.insert(END, ans)

    
button1 = Button(win, text="Add 1", command=add1)
button1.place(x=30,y=150)

button2 = Button(win, text="Add 2", command=add2)
button2.place(x=80,y=150)

button3 = Button(win, text="Add 3", command=add3)
button3.place(x=130,y=150)

buttonplus = Button(win, text="Add +", command=addplus)
buttonplus.place(x=180,y=150)

buttonminus = Button(win, text="Add -", command=addminus)
buttonminus.place(x=230,y=150)

buttonClear = Button(win, text="Clear", command=clear)
buttonClear.place(x=280,y=150)

buttonEval = Button(win, text="Eval", command=evalu)
buttonEval.place(x=330,y=150)

eqn = Entry(win, width=25)
eqn.place(x=30,y=30)


mainloop()
