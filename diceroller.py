from tkinter import *
import random
import time

root = Tk()
root.iconbitmap("d20.ico")
root.title("Ichiro's Dice Roller")

#Shows what to do
tutorial = Label(root, text="Please choose the type of dice, number, and modifier")
tutorial.grid(row=0, column=0)

#Shows type of dice
tutorialtype = Label(root, text="Number of sides on Dice")
tutorialtype.grid(row=1, column=0)
dicerolling = StringVar(root)
dicerolling.set("4")  # default value

diceoption = OptionMenu(root, dicerolling, "4", "6", "8", "10", "12", "20", "100")
diceoption.grid(row = 2, column = 0)

dicenum = Entry(root, width=50)
dicenum.insert(0, "1")

#Modifier
tutorialmod = Label(root, text="Modifier of dice")
tutorialmod.grid(row=5, column=0)
entry = Entry(root, width=50)
entry.insert(0,"0")
entry.grid(row = 6,column = 0 )

#random number generator
def randomnumber():
    i = 1
    dicetype = int(dicerolling.get())
    dicenumber = int(dicenum.get())
    modifier = int(entry.get())
    for i in range(dicenumber):
        rollresult = random.randint(1, dicetype)
        rollandmod = rollresult + modifier
    rolldone = Label(root, text="You rolled " + str(rollandmod))
    rolldone.grid(row = 8, column = 0)

#button that uses randomnumber
thebutton = Button(root, text="Roll!", padx=50,command=randomnumber)
thebutton.grid(row = 7, column = 0)

root.mainloop()