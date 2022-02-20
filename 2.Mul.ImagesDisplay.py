from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("MDV")
root.iconbitmap('E:/PythonCode/Extra/images/mdv.ico')

my_img1=ImageTk.PhotoImage(Image.open("E:/PythonCode/Extra/images/display1.png"))
my_img2=ImageTk.PhotoImage(Image.open("E:/PythonCode/Extra/images/display2.png"))
my_img3=ImageTk.PhotoImage(Image.open("E:/PythonCode/Extra/images/display3.png"))
my_img4=ImageTk.PhotoImage(Image.open("E:/PythonCode/Extra/images/display4.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("E:/PythonCode/Extra/images/display1.png"))
#my_img5=ImageTk.PhotoImage(Image.open("E:/PythonCode/Extra/images/CopperClassInfo.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

status=Label(root,text="Ïmage 1 Of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)

my_lab=Label(image=my_img1)
my_lab.grid(row=0,column=0,columnspan=3)

def forward(image_no):
    global btn_back
    global btn_exit
    global btn_forward
    global my_lab
    my_lab.grid_forget()
    #if image_no
    my_lab=Label(image=image_list[image_no-1])
    
    btn_back=Button(root,text="<<",command=lambda:back(image_no-1))
    btn_exit=Button(root,text="EXIT",command=root.quit)
    btn_forward=Button(root,text=">>",command=lambda:forward(image_no+1))
    if image_no==5:
        btn_forward=Button(root,text=">>",state=DISABLED)
    my_lab.grid(row=0,column=0,columnspan=3)
    btn_back.grid(row=1,column=0)
    btn_exit.grid(row=1,column=1)
    btn_forward.grid(row=1,column=2)
    status=Label(root,text="Ïmage "+str(image_no)+" Of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def back(image_no):
    global btn_back
    global btn_exit
    global btn_forward
    global my_lab
    my_lab.grid_forget()
    my_lab=Label(image=image_list[image_no-1])
    btn_back=Button(root,text="<<",command=lambda:back(image_no-1))
    #btn_exit=Button(root,text="EXIT",command=root.quit)
    btn_forward=Button(root,text=">>",command=lambda:forward(image_no+1))
    if image_no==1:
        btn_forward=Button(root,text=">>",state=DISABLED)
    my_lab.grid(row=0,column=0,columnspan=3)
    btn_back.grid(row=1,column=0)
    btn_exit.grid(row=1,column=1)
    btn_forward.grid(row=1,column=2)

    status=Label(root,text="Ïmage "+str(image_no)+" Of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

btn_back=Button(root,text="<<",command=lambda:back(),state=DISABLED)
btn_exit=Button(root,text="EXIT",command=root.quit)
btn_forward=Button(root,text=">>",command=lambda:forward(2))

btn_back.grid(row=1,column=0)
btn_exit.grid(row=1,column=1)
btn_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
#btn_quit=Button(root,text='Exit',command=root.quit)
#btn_quit.pack()
# End of the lines #
root.mainloop()