# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

# title = Label(topFrame, text="System Control GUI")
# title.pack()
# MFCLabel = Label(bottomFrame, text="MFC")
# MFCLabel.pack(side=LEFT)

# button1 = Button(bottomFrame, text="Select", fg="black")
# button2 = Button(topFrame, text="Button 2", fg="blue")
# button3 = Button(topFrame, text="Button 3", fg="green")
# button4 = Button(bottomFrame, text="Button 4", fg="purple")

# button1.pack(side=RIGHT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)

# //////////////////////////////////////////////////////////////////

# Fitting Widgets in your Layout
# one = Label(root, text="One", bg="red", fg="white")
# one.pack()
# two = Label(root, text="Two", bg="green", fg="black")
# two.pack(fill=X)
# three = Label(root, text="Three", bg="blue", fg="white")
# three.pack(side=LEFT, fill=Y)

# //////////////////////////////////////////////////////////////////

# Grid Layout
# label_1 = Label(root, text="Name")
# label_2 = Label(root, text="Password")
# entry_1 = Entry(root)
# entry_2 = Entry(root)

# label_1.grid(row=0, sticky=E)
# label_2.grid(row=1, sticky=E)

# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)

# c = Checkbutton(root, text="Keep me logged in")
# c.grid(columnspan=2)

# //////////////////////////////////////////////////////////////////

# Binding Functions to Layouts
# def printName(event):
    # print("Chello my name is Bucky")


# button_1 = Button(root, text="Print my name")
# button_1.bind("<Button-1>", printName)
# button_1.pack()

# //////////////////////////////////////////////////////////////////

# Mouse Click Events
# def leftClick(event):
    # print("Left")


# def middleClick(event):
    # print("Middle")


# def rightClick(event):
    # print("Right")


# frame = Frame(root, width=300, height=250)
# frame.bind("<Button-1>", leftClick)
# frame.bind("<Button-2>", middleClick)
# frame.bind("<Button-3>", rightClick)
# frame.pack()

# //////////////////////////////////////////////////////////////////

# Using Classes
# class BuckysButtons:

    # def __init__(self, master):
        # frame = Frame(master)
        # frame.pack()

        # self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        # self.printButton.pack(side=LEFT)

        # self.quitButton = Button(frame, text="Quit", command=frame.quit)
        # self.quitButton.pack(side=LEFT)

    # def printMessage(self):
        # print("Wow, this actually worked!")
# b = BuckysButtons(root)

# //////////////////////////////////////////////////////////////////

# Creating Drop Down Menus
# def doNothing():
    # print("ok ok I won't...")
# # ***** Main Menu *****
# menu = Menu(root)
# root.config(menu=menu)

# subMenu = Menu(menu)
# menu.add_cascade(label="File", menu=subMenu)
# subMenu.add_command(label="New Project...", command=doNothing)
# subMenu.add_command(label="New...", command=doNothing)
# subMenu.add_separator()
# subMenu.add_command(label="Exit", command=doNothing)

# editMenu = Menu(menu)
# menu.add_cascade(label="Edit", menu=editMenu)
# editMenu.add_command(label="Redo", command=doNothing)

# # ***** Toolbar *****

# toolbar = Frame(root, bg="blue")

# insertButt = Button(toolbar, text="Insert Image", command=doNothing)
# insertButt.pack(side=LEFT, padx=2, pady=2)
# printButt = Button(toolbar, text="Print", command=doNothing)
# printButt.pack(side=LEFT, padx=2, pady=2)

# toolbar.pack(side=TOP, fill=X)

# # ***** Status Bar *****

# status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)

# //////////////////////////////////////////////////////////////////

# Shapes and Graphics
# canvas = Canvas(root, width=200, height=100)
# canvas.pack()

# blackline = canvas.create_line(0, 0, 200, 50)
# redline = canvas.create_line(0, 100, 200, 50, fill="red")
# greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

# canvas.delete(redline)
# canvas.delete(ALL)

# //////////////////////////////////////////////////////////////////

# Images and Icons
# photo = PhotoImage(file="heartIcon.PNG")
# label = Label(root, image=photo)
# label.pack()