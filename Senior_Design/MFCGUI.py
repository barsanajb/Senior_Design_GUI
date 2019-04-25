from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from firebase import firebase
import tkinter.messagebox
import os
import sys


class Root(Tk):
    # Creates the window for the GUI
    def __init__(self):
        super(Root, self).__init__()
        self.title("MFC Test Unit")
        self.minsize(500, 300)
        self.wm_iconbitmap('GUIicon.ico')

        self.create_labels()
        self.create_combo_box()
        self.create_buttons()

    # Creates the GUI labels
    def create_labels(self):
        title = Label(self, text="System Control", font=("Frutiger", 35))
        title.place(x=100, y=0)

        MFCLabel = Label(self, text="MFC", font=("Helvetica", 20))
        MFCLabel.place(x=30, y=125)

    # Creates the GUI buttons
    def create_buttons(self):
        self.selectButton = ttk.Button(self, text="Select", command=self.open_message)
        self.selectButton.place(x=375, y=130)

        self.addDeviceButton = ttk.Button(self, text="Add A Device", command=self.add_device_window)
        self.addDeviceButton.place(x=150, y=250)

        self.refresh_button = ttk.Button(self, text="Refresh", command=self.refresh)
        self.refresh_button.place(x=275, y=250)

    # Creates the GUI combo box
    def create_combo_box(self):
        data = firebase.FirebaseApplication('https://mfctestunit.firebaseio.com/')
        myGetResults = data.get('/Devices', None)
        i = 0
        counter = 0

        device_array = []
        communication_array = []
        values = []

        for keyID in myGetResults:
            device_array.append(myGetResults[keyID]['Device'])
            communication_array.append(myGetResults[keyID]['Communication Protocol'])
            counter += 1

        self.device = StringVar()
        self.MFCcombo = ttk.Combobox(self, width=40)

        while i < counter:
            values.append("Device: {} | Communication: {}".format(device_array[i], communication_array[i]))
            i += 1

        self.MFCcombo['values'] = values
        self.MFCcombo.place(x=100, y=133)

    def open_message(self):
        tkinter.messagebox.showinfo('MFC Test Unit', 'Opening Virtual Instrument')
        os.system('"C:\\Users\\jonba_000\\Desktop\\Senior_Design_GUI\\Senior_Design\\Application.exe"')

    def add_device_window(self):
        top = Toplevel()
        top.title("Add A Device")
        top.minsize(650, 300)
        top.wm_iconbitmap('GUIicon.ico')

        name_label = Label(top, text="Device Name:", font=("Helvetica", 10))
        name_label.place(x=30, y=40)
        entry_box = Entry(top, textvariable=name, width=45)
        entry_box.place(x=200, y=40)

        protocol_label = Label(top, text="Communication protocol:", font=("Helvetica", 10))
        protocol_label.place(x=30, y=110)
        entry_box = Entry(top, textvariable=protocol, width=45)
        entry_box.place(x=200, y=110)

        file_label = Label(top, text="Virtual Instrument File:", font=("Helvetica", 10))
        file_label.place(x=30, y=190)
        top.browse = ttk.Button(top, text="Browse", command=self.browse_file)
        top.browse.place(x=550, y=190)
        top.label = ttk.Label(top, textvariable=file_name)
        top.label.place(x=200, y=190)

        top.add_variable = ttk.Button(top, text="Add", command=self.add_variable)
        top.add_variable.place(x=250, y=250)
        top.close_button = ttk.Button(top, text="Cancel", command=top.destroy)
        top.close_button.place(x=350, y=250)

    def add_variable(self):
        deviceName = str(name.get())
        communication = str(protocol.get())

        data_to_upload = {
            'Device': deviceName,
            'Communication Protocol': communication
        }

        firebase.post('/Devices/', data_to_upload)

        tkinter.messagebox.showinfo('MFC Test Unit', 'Device Added')

    def refresh(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def browse_file(self):
        self.file = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(("executable", "*.exe"), ("All Files", "*.*")))
        file_chosen = self.file
        file_name.set(file_chosen)


root = Root()

name = StringVar()
protocol = StringVar()
file_name = StringVar()

firebase = firebase.FirebaseApplication('https://mfctestunit.firebaseio.com/')

root.mainloop()
