## Tic-Tac-Toe

from tkinter import *

win = Tk()
win.geometry("260x320")
win.title('Tic-Tac-Toe')

checked = {'button1':0, 'button2':0, 'button3':0, 'button4':0, 'button5':0, 'button6':0, 'button7':0, 'button8':0, 'button9':0}
turn ={'turn':0}
def change1():
    if turn['turn'] == 0:
        button1.config(text="X")
        checked['button1'] = 'X'
        turn['turn'] = 1
        if checked['button1'] == "X" and checked['button2'] == "X" and checked['button3'] == "X":
            label['text']='You are winner!'
        elif checked['button4'] == "X" and checked['button5'] == "X" and checked['button6'] == "X":
            label['text']='You are winner!'
        elif checked['button7'] == "X" and checked['button8'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button4'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        elif checked['button2'] == "X" and checked['button5'] == "X" and checked['button8'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button6'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button5'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button5'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        
        
    elif turn['turn'] == 1:
        button1.config(text="O")
        checked['button1'] = 'O'
        turn['turn'] = 0
        if checked['button1'] == "O" and checked['button2'] == "O" and checked['button3'] == "O":
            label['text']='You are winner!'
        elif checked['button4'] == "O" and checked['button5'] == "O" and checked['button6'] == "O":
            label['text']='You are winner!'
        elif checked['button7'] == "O" and checked['button8'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button4'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        elif checked['button2'] == "O" and checked['button5'] == "O" and checked['button8'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button6'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button5'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button5'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'

def change2():
    if turn['turn'] == 0:
        button2.config(text="X")
        checked['button2'] = 'X'
        turn['turn'] = 1
        if checked['button1'] == "X" and checked['button2'] == "X" and checked['button3'] == "X":
            label['text']='You are winner!'
        elif checked['button4'] == "X" and checked['button5'] == "X" and checked['button6'] == "X":
            label['text']='You are winner!'
        elif checked['button7'] == "X" and checked['button8'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button4'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        elif checked['button2'] == "X" and checked['button5'] == "X" and checked['button8'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button6'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button5'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button5'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        
        
    elif turn['turn'] == 1:
        button2.config(text="O")
        checked['button2'] = 'O'
        turn['turn'] = 0
        if checked['button1'] == "O" and checked['button2'] == "O" and checked['button3'] == "O":
            label['text']='You are winner!'
        elif checked['button4'] == "O" and checked['button5'] == "O" and checked['button6'] == "O":
            label['text']='You are winner!'
        elif checked['button7'] == "O" and checked['button8'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button4'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        elif checked['button2'] == "O" and checked['button5'] == "O" and checked['button8'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button6'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button5'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button5'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
    
def change3():
    if turn['turn'] == 0:
        button3.config(text="X")
        checked['button3'] = 'X'
        turn['turn'] = 1
        if checked['button1'] == "X" and checked['button2'] == "X" and checked['button3'] == "X":
            label['text']='You are winner!'
        elif checked['button4'] == "X" and checked['button5'] == "X" and checked['button6'] == "X":
            label['text']='You are winner!'
        elif checked['button7'] == "X" and checked['button8'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button4'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        elif checked['button2'] == "X" and checked['button5'] == "X" and checked['button8'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button6'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button5'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button5'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        
        
    elif turn['turn'] == 1:
        button3.config(text="O")
        checked['button3'] = 'O'
        turn['turn'] = 0
        if checked['button1'] == "O" and checked['button2'] == "O" and checked['button3'] == "O":
            label['text']='You are winner!'
        elif checked['button4'] == "O" and checked['button5'] == "O" and checked['button6'] == "O":
            label['text']='You are winner!'
        elif checked['button7'] == "O" and checked['button8'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button4'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        elif checked['button2'] == "O" and checked['button5'] == "O" and checked['button8'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button6'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button5'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button5'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
            
def change4():
    if turn['turn'] == 0:
        button4.config(text="X")
        checked['button4'] = 'X'
        turn['turn'] = 1
        if checked['button1'] == "X" and checked['button2'] == "X" and checked['button3'] == "X":
            label['text']='You are winner!'
        elif checked['button4'] == "X" and checked['button5'] == "X" and checked['button6'] == "X":
            label['text']='You are winner!'
        elif checked['button7'] == "X" and checked['button8'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button4'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        elif checked['button2'] == "X" and checked['button5'] == "X" and checked['button8'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button6'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button5'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button5'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        
        
    elif turn['turn'] == 1:
        button4.config(text="O")
        checked['button4'] = 'O'
        turn['turn'] = 0
        if checked['button1'] == "O" and checked['button2'] == "O" and checked['button3'] == "O":
            label['text']='You are winner!'
        elif checked['button4'] == "O" and checked['button5'] == "O" and checked['button6'] == "O":
            label['text']='You are winner!'
        elif checked['button7'] == "O" and checked['button8'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button4'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        elif checked['button2'] == "O" and checked['button5'] == "O" and checked['button8'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button6'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button5'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button5'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        
def change5():
    if turn['turn'] == 0:
        button5.config(text="X")
        checked['button5'] = 'X'
        turn['turn'] = 1
        if checked['button1'] == "X" and checked['button2'] == "X" and checked['button3'] == "X":
            label['text']='You are winner!'
        elif checked['button4'] == "X" and checked['button5'] == "X" and checked['button6'] == "X":
            label['text']='You are winner!'
        elif checked['button7'] == "X" and checked['button8'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button4'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        elif checked['button2'] == "X" and checked['button5'] == "X" and checked['button8'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button6'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button5'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button5'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        
        
    elif turn['turn'] == 1:
        button5.config(text="O")
        checked['button5'] = 'O'
        turn['turn'] = 0
        if checked['button1'] == "O" and checked['button2'] == "O" and checked['button3'] == "O":
            label['text']='You are winner!'
        elif checked['button4'] == "O" and checked['button5'] == "O" and checked['button6'] == "O":
            label['text']='You are winner!'
        elif checked['button7'] == "O" and checked['button8'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button4'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        elif checked['button2'] == "O" and checked['button5'] == "O" and checked['button8'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button6'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button5'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button5'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        
def change6():
    if turn['turn'] == 0:
        button6.config(text="X")
        checked['button6'] = 'X'
        turn['turn'] = 1
        if checked['button1'] == "X" and checked['button2'] == "X" and checked['button3'] == "X":
            label['text']='You are winner!'
        elif checked['button4'] == "X" and checked['button5'] == "X" and checked['button6'] == "X":
            label['text']='You are winner!'
        elif checked['button7'] == "X" and checked['button8'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button4'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        elif checked['button2'] == "X" and checked['button5'] == "X" and checked['button8'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button6'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button5'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button5'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        
        
    elif turn['turn'] == 1:
        button6.config(text="O")
        checked['button6'] = 'O'
        turn['turn'] = 0
        if checked['button1'] == "O" and checked['button2'] == "O" and checked['button3'] == "O":
            label['text']='You are winner!'
        elif checked['button4'] == "O" and checked['button5'] == "O" and checked['button6'] == "O":
            label['text']='You are winner!'
        elif checked['button7'] == "O" and checked['button8'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button4'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        elif checked['button2'] == "O" and checked['button5'] == "O" and checked['button8'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button6'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button5'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button5'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        
def change7():
    if turn['turn'] == 0:
        button7.config(text="X")
        checked['button7'] = 'X'
        turn['turn'] = 1
        if checked['button1'] == "X" and checked['button2'] == "X" and checked['button3'] == "X":
            label['text']='You are winner!'
        elif checked['button4'] == "X" and checked['button5'] == "X" and checked['button6'] == "X":
            label['text']='You are winner!'
        elif checked['button7'] == "X" and checked['button8'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button4'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        elif checked['button2'] == "X" and checked['button5'] == "X" and checked['button8'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button6'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button5'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button5'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        
        
    elif turn['turn'] == 1:
        button7.config(text="O")
        checked['button7'] = 'O'
        turn['turn'] = 0
        if checked['button1'] == "O" and checked['button2'] == "O" and checked['button3'] == "O":
            label['text']='You are winner!'
        elif checked['button4'] == "O" and checked['button5'] == "O" and checked['button6'] == "O":
            label['text']='You are winner!'
        elif checked['button7'] == "O" and checked['button8'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button4'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        elif checked['button2'] == "O" and checked['button5'] == "O" and checked['button8'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button6'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button5'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button5'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        
def change8():
    if turn['turn'] == 0:
        button8.config(text="X")
        checked['button8'] = 'X'
        turn['turn'] = 1
        if checked['button1'] == "X" and checked['button2'] == "X" and checked['button3'] == "X":
            label['text']='You are winner!'
        elif checked['button4'] == "X" and checked['button5'] == "X" and checked['button6'] == "X":
            label['text']='You are winner!'
        elif checked['button7'] == "X" and checked['button8'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button4'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        elif checked['button2'] == "X" and checked['button5'] == "X" and checked['button8'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button6'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button5'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button5'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        
        
    elif turn['turn'] == 1:
        button8.config(text="O")
        checked['button8'] = 'O'
        turn['turn'] = 0
        if checked['button1'] == "O" and checked['button2'] == "O" and checked['button3'] == "O":
            label['text']='You are winner!'
        elif checked['button4'] == "O" and checked['button5'] == "O" and checked['button6'] == "O":
            label['text']='You are winner!'
        elif checked['button7'] == "O" and checked['button8'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button4'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        elif checked['button2'] == "O" and checked['button5'] == "O" and checked['button8'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button6'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button5'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button5'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
            
def change9():
    if turn['turn'] == 0:
        button9.config(text="X")
        checked['button9'] = 'X'
        turn['turn'] = 1
        if checked['button1'] == "X" and checked['button2'] == "X" and checked['button3'] == "X":
            label['text']='You are winner!'
        elif checked['button4'] == "X" and checked['button5'] == "X" and checked['button6'] == "X":
            label['text']='You are winner!'
        elif checked['button7'] == "X" and checked['button8'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button4'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        elif checked['button2'] == "X" and checked['button5'] == "X" and checked['button8'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button6'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button1'] == "X" and checked['button5'] == "X" and checked['button9'] == "X":
            label['text']='You are winner!'
        elif checked['button3'] == "X" and checked['button5'] == "X" and checked['button7'] == "X":
            label['text']='You are winner!'
        
        
    elif turn['turn'] == 1:
        button9.config(text="O")
        checked['button9'] = 'O'
        turn['turn'] = 0
        if checked['button1'] == "O" and checked['button2'] == "O" and checked['button3'] == "O":
            label['text']='You are winner!'
        elif checked['button4'] == "O" and checked['button5'] == "O" and checked['button6'] == "O":
            label['text']='You are winner!'
        elif checked['button7'] == "O" and checked['button8'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button4'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        elif checked['button2'] == "O" and checked['button5'] == "O" and checked['button8'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button6'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button1'] == "O" and checked['button5'] == "O" and checked['button9'] == "O":
            label['text']='You are winner!'
        elif checked['button3'] == "O" and checked['button5'] == "O" and checked['button7'] == "O":
            label['text']='You are winner!'
        
button1 = Button(win, text='', command=change1, height=5, width=11)
button1.grid(row=1, column=1)

button2 = Button(win, text='', command=change2, height=5, width=11)
button2.grid(row=1, column=2)

button3 = Button(win, text='', command=change3, height=5, width=11)
button3.grid(row=1, column=3)

button4 = Button(win, text='', command=change4, height=5, width=11)
button4.grid(row=2, column=1)

button5 = Button(win, text='', command=change5, height=5, width=11)
button5.grid(row=2, column=2)

button6 = Button(win, text='', command=change6, height=5, width=11)
button6.grid(row=2, column=3)

button7 = Button(win, text='', command=change7, height=5, width=11)
button7.grid(row=3, column=1)

button8 = Button(win, text='', command=change8, height=5, width=11)
button8.grid(row=3, column=2)

button9 = Button(win, text='', command=change9, height=5, width=11)
button9.grid(row=3, column=3)

label = Label(win, text='')
label.grid(row=4,column=2)

def restart():
    button1.config(text="")
    button2.config(text="")
    button3.config(text="")
    button4.config(text="")
    button5.config(text="")
    button6.config(text="")
    button7.config(text="")
    button8.config(text="")
    button9.config(text="")
    for i in checked:
        checked[i] = 0
    label['text']=''

restart = Button(win, text='Restart?', command=restart)
restart.grid(row=5,column=2)

win.mainloop()
