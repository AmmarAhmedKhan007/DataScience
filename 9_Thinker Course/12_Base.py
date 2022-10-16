
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('New Window in Thinker')
root.iconbitmap('Pics\iconn.ico')

def open():
	global my_img
	top = Toplevel()
	top.title('My Second Window')
	top.iconbitmap('Pics\iconn.ico')
	my_img = ImageTk.PhotoImage(Image.open("Pics\icon.png"))
	my_label = Label(top, image=my_img).pack()
	btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Windo", command=open).pack()

mainloop()