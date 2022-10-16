
from tkinter import *
root = Tk()

def myClick():
	myLabel = Label(root, text=" Look! i clicked a Button! ")
	myLabel.pack()

myButton = Button(root, text=" Click Me! ", command=myClick)
myButton.pack()

root.mainloop()