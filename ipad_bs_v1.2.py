#----------------------------------
# iPad booking system
# Date
# version v1.2
# T. Davis
#----------------------------------

import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime
from time import gmtime, strftime

window = Tk()                                                         # define tkinter as window

current_date = datetime.date.today()                                  # declare current date variable
dt = (current_date.strftime("%a  %d/%m/%Y"))                          # declare date variable
hr = (strftime("%H:%M", gmtime()))                                    # declare time variable

# delare global variables  
code = ''                                                             # declare variable as null
ipad_code = ''                                                        # declare variable as null
teacher = ''                                                          # declare variable as null

# declare variables "status" 1 to 16 as global variables
# and set to 'in'
for x in range(0, 17):                                   # iterate  0 to 16
    globals()['status%s' % x] = 'in'                     # add number to "status" variable and set to "in"

                                                         # ie status1 = in , status2 = in etc
#------------- staff dictionary ------------------
staff = {
    "TSG-001" : "Mrs Wood",
    "TSG-002" : "Mrs Kemp",
    "TSG-003" : "Mrs Soor",
    "TSG-004" : "Mrs Rivers",
    "TSG-005" : "Mrs Kew",
    "22222" : "Mrs Vickers",
    "12345" : "Mrs Scott"
}
#----------- iPad dictionary ----------------------
ipad = {
    "TSG-iPad01" : "1",
    "TSG-iPad02" : "2",
    "TSG-iPad03" : "3",
    "44444" : "4",
    "55555" : "5",
    "66666" : "6",
    "TSG-iPad07" : "7",
    "TSG-iPad08" : "8",
    "TSG-iPad09" : "9",
    "TSG-iPad10" : "10",
    "TSG-iPad11" : "11",
    "TSG-iPad12" : "12",
    "TSG-iPad13" : "13",
    "TSG-iPad14" : "14",
    "TSG-iPad15" : "15",
    "TSG-iPad16" : "16",
    "00" :"end"
}

#--------------- set up treeview window which displays ipad, teacher, date and time in rows and columns --------
def treeview_UI():
    global id1, id2, id3, id2, id4, id5, id6, id7,id8, id9,id10, id11, id12, id13, id14, id15, id16
    window.title("iPad Booking System")
    tv.heading("#0", text = '      iPad No', anchor='w')                 # define main heading parameters
    tv["columns"] = ("bookedOut", "dateOut", "timeOut")  # define column variables
    tv.column("bookedOut",width=200 )                                    # define column parameters
    tv.column("dateOut", anchor='center', width=200)                     # define column parameters
    tv.column("timeOut", anchor='center', width=200)                     # define column parameters
    tv.heading("bookedOut", text="Booked out By", anchor='w')            # define heading parameters
    tv.heading("dateOut", text="Date")                                   # define heading parameters
    tv.heading("timeOut", text="Time")                                   # define heading parameters
    tv.grid(row=1,column=0)                                              # place treeview in grid

    var_name1 = " "                                                      # make variable blank
    var_name2 = " "                                                      # make variable blank
    dt = " "                                                             # make variable blank
    hr = " "                                                             # make variable blank
    #---------------- set up treeview table with blank data --------------------------------------------
    tv.tag_configure('oddrow', background='white', font=(None, 10))  # define colour and font of odd rows
    tv.tag_configure('evenrow', background='lightblue', font=(None, 10))  # define colour and font of even tows
    id1 = tv.insert('', 1, text="iPad No 1", values=(var_name1, dt, hr), tags=('oddrow', ))
    id2 = tv.insert('', 2, text="iPad No 2", values=(var_name2, dt, hr), tags=('evenrow',))
    id3 = tv.insert('', 3, text="iPad No 3", values=(var_name1, dt, hr), tags=('oddrow',))
    id4 = tv.insert('', 4, text="iPad No 4", values=(var_name2, dt, hr), tags=('evenrow',))
    id5 = tv.insert('', 5, text="iPad No 5", values=(var_name1, dt, hr), tags=('oddrow',))
    id6 = tv.insert('', 6, text="iPad No 6", values=(var_name2, dt, hr), tags=('evenrow',))
    id7 = tv.insert('', 7, text="iPad No 7", values=(var_name1, dt, hr), tags=('oddrow',))
    id8 = tv.insert('', 8, text="iPad No 8", values=(var_name2, dt, hr), tags=('evenrow',))
    id9 = tv.insert('', 9, text="iPad No 9", values=(var_name1, dt, hr), tags=('oddrow',))
    id10 = tv.insert('',10, text="iPad No 10", values=(var_name2, "", ""), tags=('evenrow',))
    id11 = tv.insert('',11, text="iPad No 11", values=(var_name1, dt, hr), tags=('oddrow',))
    id12 = tv.insert('',12, text="iPad No 12", values=(var_name2, dt, hr), tags=('evenrow',))
    id13 = tv.insert('',13, text="iPad No 13", values=(var_name1, dt, hr), tags=('oddrow',))
    id14 = tv.insert('',14, text="iPad No 14", values=(var_name2, dt, hr), tags=('evenrow',))
    id15 = tv.insert('',15, text="iPad No 15", values=(var_name1, dt, hr), tags=('oddrow',))
    id16 = tv.insert('',16, text="iPad No 16", values=(var_name2, dt, hr), tags=('evenrow',))
    ask_for_barcode()                                                                    # call ask_for_barcode function

def ask_for_barcode():
    global label                                                                         # make variable global
    global label9                                                                        # make variable global
    global label10                                                                       # make variable global
    label = tk.Label(window, text = "Scan your barcode ID ", font = 12)                  # create label
    label.place(x = 50 , y=30)                                                           # place label on screen
    label9 = tk.Label(window, text="                                        ", font=12)  # create blank label
    label9.place(x=50, y=60)                                                             # place blank label on screen
    label10 = tk.Label(window, text="                                        ", font=12) # create blank label
    label10.place(x=50, y=90)                                                            # place label on screen                                                          #
    window.bind('<Key>', get_teacher_barcode)                                            # call get_barcode function


def get_teacher_barcode(event):
    global code                                                    # make variable global
    global teacher                                                 # make variable global
    if event.char in '12345567890TSG-':                            # check to see char in event is in this list
        code += event.char                                         # add char to code variable 
        print('>', code)                                           # print code for debugging
        label['text'] = code                                       # converts code into a string
    elif event.keysym == 'Return':                                 # if event equals return 
        teacher = staff.get(code)                                  # check staff dictionary for name
        print('result:', teacher)                                  # debugging purposes
        code = ''                                                  # set code variable to null
        get_teacher_name(teacher)                                  # call get teacher_name_function

def get_teacher_name(teacher):
    global AFTER                                                          # make variable globel
    AFTER = window.after(15000, ask_for_barcode)                          # start timer running for 60 seconds
    w = tk.Label(window, text = "Recognise " + teacher, font=12)          # create label with "teachers" name
    w.place(x = 50 , y= 60)                                               # place label on screen
    ask_to_scan_ipad()                                                    # call ask_to_scan_ipad function

def ask_to_scan_ipad():
    global label2                                                         # make variable global
    label2 = tk.Label(window, text="Please Scan the iPad ", font=12)      # create label
    label2.place(x=50, y=90)                                              # place label on screen
    window.bind('<Key>', get_ipad_barcode)                                # call get_barcode function

def get_ipad_barcode(event):
    global ipad_code                                                      # make variable global
    global device                                                         # make variable global
    if event.char in '12345567890TSG-iPad':                               # check see scan character is in list
        ipad_code += event.char                                           # if in the list add to ipad_code variable
        print('>', ipad_code)                                             # print "ipad_code" variable to console
        label2['text'] = ipad_code                                        # display ipad_code on screen - debug purposes
    elif event.keysym == 'Return':                                        # detect for "Return key" scan
        device = ipad.get(ipad_code)                                      # device equals entry in ipad dictionary
        ipad_code = ''                                                    # set ipad_code to null ready for next scan
        find_ipad()                                                       # call function

def find_ipad():
    global device                                                         # set variables ad global
    global status1, status2, status3, status4, status5, status6           # set variables ad global
    global status7, status8, status9, status10, status11, status12        # set variables ad global
    global status13,status14, status15,status16                           # set variables ad global

    dt = (current_date.strftime("%a  %d/%m/%Y"))                         # declare date variable
    hr = (strftime("%H:%M", gmtime()))                                   # declare time variable

    if device == "1":                                                    # if device equals "1", received from ipad dictionary
        if status1 == 'in':                                              # if status equals "in"
            status1 = 'out'                                              # change status to "out"
            tv.item(id1, values=(teacher, dt, hr))                       # update treeview  table
        elif status1 == 'out':                                           # if status equals "out"
            status1 = 'in'                                               # change status to "in"
            tv.item(id1, values=("  ", " ", " "))                        # update treeview with blank data
    if device == "2":
        if status2 == 'in':
            status2 = 'out'
            tv.item(id2, values=(teacher, dt, hr))
        elif status2 == 'out':
            status2 = 'in'
            tv.item(id2, values=("  ", " ", " "))
    if device == "3":
        if status3 == 'in':
            status3 = 'out'
            tv.item(id3, values=(teacher, dt, hr))
        elif status3 == 'out':
            status3 = 'in'
            tv.item(id3, values=("  ", " ", " "))
    if device == "4":
        if status4 == 'in':
            status4 = 'out'
            tv.item(id4, values=(teacher, dt, hr))            
        elif status4 == 'out':
            status4 = 'in'
            tv.item(id4, values=("  ", " ", " "))
    if device == "5":
        if status5 == 'in':
            status5 = 'out'
            tv.item(id5, values=(teacher, dt, hr))            
        elif status5 == 'out':
            status5 = 'in'
            tv.item(id5, values=("  ", " ", " "))
    if device == "6":
        if status6 == 'in':
            status6 = 'out'
            tv.item(id6, values=(teacher, dt, hr))            
        elif status6 == 'out':
            status6 = 'in'
            tv.item(id6, values=("  ", " ", " "))   
    if device == "7":
        if status7 == 'in':
            status7 = 'out'
            tv.item(id7, values=(teacher, dt, hr))            
        elif status7 == 'out':
            status7 = 'in'
            tv.item(id7, values=("  ", " ", " "))
    if device == "8":
        if status8 == 'in':
            status8 = 'out'
            tv.item(id8, values=(teacher, dt, hr))            
        elif status8 == 'out':
            status8 = 'in'
            tv.item(id8, values=("  ", " ", " "))
    if device == "9":
        if status9 == 'in':
            status9 = 'out'
            tv.item(id9, values=(teacher, dt, hr))            
        elif status9 == 'out':
            status9 = 'in'
            tv.item(id9, values=("  ", " ", " "))
    if device == "10":
        if status10 == 'in':
            status10 = 'out'
            tv.item(id10, values=(teacher, dt, hr))            
        elif status10 == 'out':
            status10 = 'in'
            tv.item(id10, values=("  ", " ", " "))
    if device == "11":
        if status11 == 'in':
            status11 = 'out'
            tv.item(id11, values=(teacher, dt, hr))            
        elif status11 == 'out':
            status11 = 'in'
            tv.item(id11, values=("  ", " ", " "))
    if device == "12":
        if status12 == 'in':
            status12 = 'out'
            tv.item(id12, values=(teacher, dt, hr))            
        elif status12 == 'out':
            status12 = 'in'
            tv.item(id12, values=("  ", " ", " "))
    if device == "13":
        if status13 == 'in':
            status13 = 'out'
            tv.item(id13, values=(teacher, dt, hr))            
        elif status13 == 'out':
            status13 = 'in'
            tv.item(id13, values=("  ", " ", " "))
    if device == "14":
        if status14 == 'in':
            status14 = 'out'
            tv.item(id14, values=(teacher, dt, hr))            
        elif status14 == 'out':
            status14 = 'in'
            tv.item(id14, values=("  ", " ", " "))
    if device == "15":
        if status15 == 'in':
            status15 = 'out'
            tv.item(id15, values=(teacher, dt, hr))            
        elif status15 == 'out':
            status15 = 'in'
            tv.item(id15, values=("  ", " ", " "))
    if device == "16":
        if status16 == 'in':
            status16 = 'out'
            tv.item(id16, values=(teacher, dt, hr))            
        elif status16 == 'out':
            status16 = 'in'
            tv.item(id16, values=("  ", " ", " "))

    #----- if "end" barcode scanned ----------------
    if device == "end":                                                # if "end" code detected
        window.after_cancel(AFTER)                                     # cancel timer
        ask_for_barcode()                                              # call function
    #----- if "end" barcode not scanned ----------
    if device != "end":                                                # if device not equal to "end"
        ask_to_scan_ipad()                                             # cal function

window.geometry('800x600+0+0')                                         # for Raspberry Pi change to (800x600+0+0)

#---------- set up two frames, one for user input the other for the Treeview list
frame1=Frame(window, width=800, height=130 )                  # define the dimensions of the first frame - background="Blue"
frame1.grid(row=0, column=0)                                  # assign row and column to frame
frame2=Frame(window, width=800, height=250)                   # define the dimensions of the second frame
frame2.grid(row=1, column=0)                                  # assign row and column to frame

tv = ttk.Treeview(window, height = 17)                        # assign rows to the treview widget

treeview_UI()                                                 # call the User Interface function

window.mainloop()                                             # call tkinter main loop

