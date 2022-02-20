from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("MDV")
root.iconbitmap('E:/PythonCode/Extra/images/mdv.ico')

frame=LabelFrame(root,text="Displayed Frame...",padx=5,pady=5)
frame.pack(padx=50,pady=50)

b=Button(frame,text='Display')
b2=Button(frame,text='Dont Display')
b.grid(row=0,column=0)
b2.grid(row=1,column=0)
# End of the lines #
root.mainloop()