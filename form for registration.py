# from openpyxl import *
from tkinter import *
root = Tk ()
root.geometry('500x300')

def getvals():
    print('ACCEPTED')

Label(root, text='PYTHON REGISTRATION FORM', font='ar 15 bold').grid(row=0,column=3)

#form label
name = Label(root, text='NAME')
phone = Label(root, text='PHONE')
gender = Label(root, text='GENDER')
form_n0 = Label(root, text='FORM NUMBER')
emergency = Label(root, text='EMERGENCY')
contact_n0 = Label(root, text='CONTACT N0')
address = Label(root, text='address')
payment_mode = Label(root, text='PAYMENT MODE')

#grid to assign the keys a visible postion. or to peg keys
name.grid(row=1, column=1)
phone.grid(row=2, column=1)
gender.grid(row=3, column=1)
emergency.grid(row=4, column=1)
contact_n0.grid(row=5, column=1)
form_n0.grid(row=6, column=1)
payment_mode.grid(row=7, column=1)

#values are created to store the details entered
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
contact_n0value = StringVar
emergencyvalue = StringVar
form_novalue = StringVar
payment_modevalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable= phonevalue)
genderentry = Entry(root, textvariable= gendervalue)
contact_n0entry = Entry(root, textvariable= contact_n0value)
emergencyentry = Entry(root, textvariable= emergencyvalue)
form_n0entry = Entry(root, textvariable= form_novalue)
payment_modeentry = Entry(root, textvariable= payment_modevalue)

#Peging entry
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
contact_n0entry.grid(row=5, column=3)
form_n0entry.grid(row=6, column=3)
payment_modeentry.grid(row=7, column=3)

#creating checkBox
checkbtn = Checkbutton(text= 'remember me?', variable= checkvalue)
checkbtn.grid(row=8, column=3)

#sumbitting
Button(text='Submit', command=getvals).grid(row=9, column=3)
root.mainloop()
