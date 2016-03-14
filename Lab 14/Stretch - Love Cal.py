from tkinter import *

width = int(input("Enter the width: "))
height = int(input("Enter the hegith: "))

size = str(width)+'x'+str(height)

window = Tk()
window.geometry(size)

board = Label(window, text="Love Calculator")
board.place(x = width/10, y=50)

nameEntry1 = Entry(window, width=25)
nameEntry1.place(x=width/10, y=height/4)

nameEntry2 = Entry(window, width=25)
nameEntry2.place(x=width/10, y=height/2)

def changeText():
    score = 0
    name1 = nameEntry1.get().lower()
    name2 = nameEntry2.get().lower()
    for i in name1:
        for j in name2:
            if i == j:
                score += 5
    scoreboard["text"] = score

testButton = Button(window, text="Test", command=changeText)
testButton.place(x=width-50, y=height/2)

board = Label(window, text="Score is")
board.place(x = width/10, y=height-50)

scoreboard = Label(window, text="")
scoreboard.place(x = width/10 + 50, y=height-50)

window.mainloop()
