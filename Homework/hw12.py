## Snake Game
## Juhwan Park (3917664)

from tkinter import *
import random

class SnakeGUI():
    def __init__(self):
        self.window = Tk()
        self.window.title("Snake Game")
        self.window.minsize(600, 630)

        self.frame = Frame(self.window, bg="black")
        self.frame.pack()

        self.canvas = Canvas(self.frame, bg="black", width=600, height=600)
        self.canvas.pack()

        self.scoreboard = Label(self.frame, bg="black", fg="white", text="\n"+"Your Score is 0")
        self.scoreboard.pack()
        
        self.button = Button(self.frame, bg="black", fg="white", text="Start", command=self.b1handler, padx=10)
        self.button.pack(side=BOTTOM)

        ## Initial Value
        self.check = {'firstcount':0}

        ## Keyboard Event
        self.canvas.bind_all('<KeyPress-Up>', self.moveup)
        self.canvas.bind_all('<KeyPress-Down>', self.movedown)
        self.canvas.bind_all('<KeyPress-Left>', self.moveleft)
        self.canvas.bind_all('<KeyPress-Right>', self.moveright)

        self.canvas.bind_all('<KeyPress-w>', self.moveup)
        self.canvas.bind_all('<KeyPress-s>', self.movedown)
        self.canvas.bind_all('<KeyPress-a>', self.moveleft)
        self.canvas.bind_all('<KeyPress-d>', self.moveright)
        
        ## Mainloop
        self.window.mainloop()

    def b1handler(self):
        if self.check['firstcount'] == 0:
            self.restart()
            self.snake()
            self.food()
            
        if self.check['check'] == 0:
            self.button['text'] = 'Pause'
            self.check['check'] = 1
            self.check['firstcount'] = 1

        elif self.check['check'] == 1:
            self.button['text'] = 'Start'
            self.check['check'] = 0

        elif self.check['check'] == 3:
            self.canvas.delete("all")
            self.scoreboard['text'] = "\n"+"Your Score is 0"
            self.restart()
            self.b1handler()

    def restart(self):
        ## Location of snake and food
        self.x = (random.randint(0, 580) // 20) * 20 + 1
        self.y = (random.randint(0, 580) // 20) * 20 + 1
        
        self.x_food= (random.randint(0, 580) // 20) * 20 + 1
        self.y_food= (random.randint(0, 580) // 20) * 20 + 1


        ## Gaming Start/Pause check/moving/length
        self.check = {'check':0, 'firstcount':1,'dx':20, 'dy':0, 'food':1, 'length':1, 'speed':500}

        self.j =0
        self.lst = []
            
    def snake(self):
        if self.check['check'] == 1:
            if len(self.lst) > self.check['length']-1:
                self.canvas.delete(self.lst[0])
                self.lst.pop(0)
            self.lst.append(self.canvas.create_rectangle(self.x, self.y, self.x+18, self.y+18, fill="red"))
            if self.canvas.bbox(self.lst[-1]) == self.canvas.bbox('food'):
                self.check['length'] += 1
                self.check["food"] = 0
                self.scoreboard["text"] = "\n"+"Your Score is " + str(self.check['length']-1)
                if self.check["speed"] > 10:
                    self.check["speed"] -= 10
            if self.canvas.bbox(self.lst[-1])[0] < 0 or self.canvas.bbox(self.lst[-1])[1] < 0 or self.canvas.bbox(self.lst[-1])[2] > 600 or self.canvas.bbox(self.lst[-1])[3] > 600:
                self.scoreboard["text"] = "GAME OVER! " +"\n"+ "Your Score is " + str(self.check['length']-1)
                self.button['text'] = 'Restart?'
                self.check['check'] = 3
            if len(self.lst) > 1:
                for i in self.lst[:-1]:
                    if len(self.canvas.find_overlapping(self.canvas.bbox(i)[0],self.canvas.bbox(i)[1],self.canvas.bbox(i)[2],self.canvas.bbox(i)[3])) > 1:
                        self.scoreboard["text"] = "GAME OVER! " +"\n"+ "Your Score is " + str(self.check['length']-1)
                        self.button['text'] = 'Restart?'
                        self.check['check'] = 3                    
            self.x += self.check['dx']
            self.y += self.check['dy']
        self.canvas.after(self.check["speed"], self.snake)

    def food(self):
        if self.j == 0:
            self.canvas.create_oval(self.x_food, self.y_food, self.x_food+18, self.y_food+18, fill = "green", tags="food")
            self.j += 1
        if self.check["food"] == 0:
            self.canvas.delete("food")
            self.x_food = (random.randint(0, 580) // 20) * 20 + 1
            self.y_food = (random.randint(0, 580) // 20) * 20 + 1
            self.canvas.create_oval(self.x_food, self.y_food, self.x_food+18, self.y_food+18, fill = "green", tags="food")
            self.check["food"] = 1
        self.canvas.after(50, self.food)    

    def moveup(self, event):
        self.check['dx'] = 0
        self.check['dy'] = -20
        
    def movedown(self,event):
        self.check['dx'] = 0
        self.check['dy'] = 20

    def moveleft(self,event):
        self.check['dx'] = -20
        self.check['dy'] = 0

    def moveright(self,event):
        self.check['dx'] = 20
        self.check['dy'] = 0

        
