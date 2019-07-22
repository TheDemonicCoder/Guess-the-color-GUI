import tkinter
import random
from tkinter import messagebox
colors = ["red", "yellow", "green", "black", "white", "pink", "blue", "brown", "orange", "purple", "cyan", "grey", "maroon", "magenta"]
score = 0
timeL = 3

def startGame(event):
    global timeL
    if timeL == 3:
        startCountdown()
    nextColor()
    if timeL == 0:
        gameOver()
        timeL = 3
        startGame

def startCountdown():
    global timeL
    if timeL > 0:
        timeL -= 1
        timeLabel.config(text = "Time Left: " + str(timeL))
        timeLabel.after(1000, startCountdown)

def gameOver():
    global score
    global timeL
    g = tkinter.Tk()
    g.wm_title("!")
    def again():
        g.destroy()
        timeL = 3
        restart()
    def quitB3():
        g.destroy()
        root.destroy()

    gLabel = tkinter.Label(g, text="GAME OVER!!!!!" , font = ("Verdana", 12))
    gLabel.pack()
    gLabel = tkinter.Label(g, text="Your Score: " + str(score) , font = ("Verdana", 10))
    gLabel.pack()
    #B1 = tkinter.Button(g, text="Okay", command = g.destroy)
    #B1.pack()
    B2 = tkinter.Button(g, text = "Play Again" , command = again)
    B2.pack()
    B3 = tkinter.Button(g, text = "Quit" , command = quitB3)
    B3.pack()
    g.mainloop()

def restart():
    global timeL
    if timeL == 3:
        startCountdown()
    nextColor()
    if timeL == 0:
        gameOver()

def nextColor():
    global score
    global timeL

    if timeL > 0:
        d.focus_set()
        if d.get().lower() == colors[1].lower():
            score +=1
        d.delete(0, tkinter.END)

        random.shuffle(colors)
        label.config(fg = str(colors[1]), text = str(colors[0]))
        scoreLabel.config(text = "Score: " + str(score))

#TKINTER START

root = tkinter.Tk()

root.title("Guess the color?")
root.geometry("400x300")
instructions = tkinter.Label(root, text = "Type in the colour"
                        "of the words, and not the word text!", font = ('Comic Sans MS', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text = "Press enter to START!!!", font = ('Comic Sans MS', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text = "Time Left: ", font = ('Comic Sans MS', 12))
timeLabel.pack()

label = tkinter.Label(root, font = ('Comic Sans MS', 60))
label.pack()

d = tkinter.Entry(root)

#keypress
root.bind('<Return>', startGame)
d.pack()

d.focus_set()
root.mainloop()