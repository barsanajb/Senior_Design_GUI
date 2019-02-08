from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os


class Root(Tk):
    # Creates the window for the GUI
    def __init__(self):
        super(Root, self).__init__()
        self.title("MFC Test Unit")
        self.minsize(500, 300)
        self.wm_iconbitmap('GUIicon.ico')

        self.createLabels()
        self.createComboBox()
        self.createButtons()

    # Creates the GUI labels
    def createLabels(self):
        title = Label(self, text="System Control", font=("Frutiger", 35))
        title.place(x=100, y=0)

        MFCLabel = Label(self, text="MFC", font=("Helvetica", 20))
        MFCLabel.place(x=30, y=125)

    # Creates the GUI buttons
    def createButtons(self):
        self.selectButton = ttk.Button(self, text="Select", command=self.openMessage)
        self.selectButton.place(x=375, y=130)

        self.addDeviceButton = ttk.Button(self, text="Add A Device", command=self.openMessage)
        self.addDeviceButton.place(x=200, y=250)
    # Creates the GUI combo box
    def createComboBox(self):

        self.device = StringVar()

        self.MFCcombo = ttk.Combobox(self, width=40)
        self.MFCcombo['values'] = ("Device: GM50A | Communication: DeviceNet",
                                   "Device: GM50A | Communication: ModBus",
                                   "Device: GE50A | Communication: DeviceNet",
                                   "Device: GE50A | Communication: ModBus")
        self.MFCcombo.place(x=100, y=133)

    def openMessage(self):
        tkinter.messagebox.showinfo('MFC Test Unit', 'Opening Virtual Instrument')
        os.startfile('test.txt')


root = Root()

root.mainloop()