
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Message Box')
root.iconbitmap('Pics\iconn.ico')

def popup():
	response = messagebox.showinfo("This is my Popup!", "Hello World!")
	Label(root, text=response).pack()
	#if response == "yes":
	#	Label(root, text="You Clicked Yes!").pack()
	#else:
	#	Label(root, text="You Clicked No!!").pack()

Button(root, text="Popup", command=popup).pack()


mainloop()