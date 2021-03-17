from tkinter import *
from PIL import Image, ImageTk
from TruthTables import multiply

root = Tk()
root.title("Truth Tables don't lie")
root.geometry("700x400")
bgColour = "#1a614f"
root.configure(background = bgColour)
#http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

#https://www.youtube.com/watch?v=bVnKX0315lo&ab_channel=Codemy.com

def DisplayTruthTableOption(window):
    window.title("Truth Table Filler")
    # def Label():
    #     Label(root, text = "Truth Table Filler", bg = bgColour, fg = "white", font = "Times 20 bold").place(x = 150,y = 10)
    # window.Label()
    # Return = Button(window, text = "Return", command = root.mainloop, borderwidth = 10)
    # window.Return.place(20,20)

def TruthTablesOption():
    TTO = Toplevel()
    TTO.geometry("700x400")
    bgColour = "#1a614f"
    TTO.configure(background = bgColour)
    DisplayTruthTableOption(TTO)
    TTO.mainloop()
    

def labels():
    Label(root, text = "Welcome to Truth Tables don't lie", bg = bgColour, fg = "white", font = "Times 20 bold").place(x = 150,y = 10)

TTOption = PhotoImage(file = "square.png")
# resize = TTOption.subsample(20, 20)
# TTOLabel = Label(image = TTOption).place(x = 200, y = 150)
MyButton = Button(root, image = TTOption, command = TruthTablesOption, borderwidth = 5)
MyButton.place(x=250, y = 130)
# Button(root, text = "Truth Table Generator", command = TruthTablesOption()).place(x = 100, y = 40)

labels()
root.mainloop()

