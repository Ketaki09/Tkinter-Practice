# !/usr/bin/python3
from tkinter import *

root = Tk()
root.title("Titanic Prediction Model")



def menu():

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Clear Model", command=donothing)
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About...", command=Info)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin)
   button.pack()


def Info():

    var = StringVar()
    label = Label(root, textvariable=var, relief=FLAT)
    var.set("This app enables us to do the folowing;" + '\n' + "- Preprocess the titanic Data" + '\n' + "- Build the predictive models" + '\n' + "- Predict on validation set with accuracy calculator" +"\n" + "- Save the models")
    label.pack()


v = StringVar()


def sel():

    selection = v.get()
    label.config(text=selection)


def mainpage():
    global label
    label=Label(root)
    label.grid(row=0, column=2)
    global v
    v = StringVar()
    # this will create a label widget
    rd1 = Radiobutton(root, text='Decision Tree', variable=v, value='Decision Tree', command=sel)
    rd1.grid(row=3, column=1, sticky=W)
    rd2 = Radiobutton(root, text='Random Forest', variable=v, value='Random Forest', command=sel)
    rd2.grid(row=4, column=1, sticky=W)
    rd3 = Radiobutton(root, text='Logistic Regression', variable=v, value='Logistic Regression', command=sel)
    rd3.grid(row=5, column=1, sticky=W)

    # checkbutton widget
    var1 = IntVar()
    var2 = IntVar()
    c1 = Checkbutton(root, text="Save Model",  variable=var1)
    c1.grid(row=3, column=3, sticky=W,)
    c1 = Checkbutton(root, text="Show Accuracy",  variable=var2)
    c1.grid(row=4, column=3, sticky=W)
    button1=Button(root, text="Preprocess")
    button1.grid(row=6, columnspan=6, sticky='nesw')


mainpage()
menu()
root.mainloop()