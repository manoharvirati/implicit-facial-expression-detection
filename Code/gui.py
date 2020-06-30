from tkinter import *
import win32gui, win32con
import applicationlayer as app
import cnnlayer as cnn
import dataLayer as data

#The_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)

def option1():
    app.detectFacesInWebcam()

def option2():
    data.storeFacesInEmotionDir()
    data.storeLabledImagesInFile()

def option3():
    cnn.interface()

def option4():
    root.destroy()


root = Tk()

Title=Label(root,text="**WELCOME TO EXPRESSION RECOGNISING SYSTEM**")
Title.pack()
l1 = Label(root,text="Run the application?")
b1 = Button(root,text="Run",command=option1)
#frame1.pack(fill=X)
#l1.pack(side=LEFT)
#b1.pack()
l2 = Label(root,text="Process data for training")
#l2.pack(side=LEFT)
b2 = Button(root,text="Process")
l3=Label(root,text="Build and test Network?")
b3 = Button(root,text="Start")
l4 = Label(root,text="Select any of the above options or exit")
b4 = Button(root,text="EXIT",command=option4)

l1.pack()
b1.pack()

l2.pack()
b2.pack()
l3.pack()
b3.pack()
l4.pack()
b4.pack()
cnn.loadModel()
root.mainloop()
exit(0)

