'''
Author : Joelle Kuyula
This program converts  temperature values between Celsuis, Fahrenheit and Kelvin scales.

'''

import tkinter as tk
from functools import partial
from tkinter.messagebox import showerror


# global variable
temp_Value = "Celsius"


# getting drop down value
def store_temp(set_temp):
    global temp_Value
    temp_Value = set_temp


# the main function
def convert(label1, labe12, inputn):
    temp = inputn.get()
    if temp_Value == 'Celsius':
        f = float((float(temp) * 9 / 5) + 32)
        k = float((float(temp) + 273.15))
        label1.config(text="%f Fahrenheit" % f)
        labe12.config(text="%f Kelvin" % k)
    if temp_Value == 'Fahrenheit':
        c = float((float(temp) - 32) * 5 / 9)
        k = c + 273
        label1.config(text="%f Celsius" % c)
        labe12.config(text="%f Kelvin" % k)
    if temp_Value == 'Kelvin':
        c = float((float(temp) - 273.15))
        f = float((float(temp) - 273.15) * 1.8000 + 32.00)
        label1.config(text="%f Celsius" % c)
        labe12.config(text="%f Fahrenheit" % f)
    return


# main window configuration and user interface
root = tk.Tk()
root.geometry('360x120')
root.title('Temperature Converter')
root['bg'] = 'silver'
root.resizable(0,0)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

val_Input = tk.StringVar()
var = tk.StringVar()

# label and entry field
input_label = tk.Label(root, text="Enter temperature", background='silver')
input_entry = tk.Entry(root, textvariable=val_Input)
input_label.grid(row=1)
input_entry.grid(row=1, column=1)

# result label's for showing the other two temperatures'
r_label1 = tk.Label(root, background='silver')
r_label1.grid(row=4, columnspan=4)
r_label2 = tk.Label(root, background='silver')
r_label2.grid(row=6, columnspan=4 )


# drop down menu initalization and setup
dropDownList = ["Celsius", "Fahrenheit", "Kelvin"]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=store_temp)
var.set(dropDownList[0])
dropdown.grid(row=1, column=3)
dropdown.config(background='silver' )
dropdown["menu"].config(background='lightgreen')

# convert button 
convert = partial(convert, r_label1, r_label2, val_Input)
r_button = tk.Button(root, text="Convert", command=convert, activebackground="#B22222", )
r_button.grid(row=2, columnspan=4)

root.mainloop()