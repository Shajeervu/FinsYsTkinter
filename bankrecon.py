from json import load
from tkinter import *
from tkinter import ttk
import tkinter as tk
root = tk.Tk()
import random
import os
import datetime

from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))
root.configure(bg="#2f516f")

root.title("Finsys")
bg_color = "#badc57"
tit = Label(root, text="Reconcile An Account", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack(fill=X)
head_label = Label(root,text="Open your statement and let's get started.", font=('times new roman', 9, 'bold'), pady=2, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
head_label.pack(fill=X)



F2 = LabelFrame(root, font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#243e55")
F2.place(x=5, y=150, width=500, height=500)
size=(500,500)
ax=ImageTk.PhotoImage(Image.open('bank-building-on-the-background-of-the-city-white-car-near-the-bank-free-vector.jpg').resize(size))
tk.Label(F2,image=ax,bg='#243e54').place(relx=0.00,rely=0.00,relheight=1,relwidth=1)


F2 = LabelFrame(root, text="Which account do you want to reconcile..??", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#243e55")
F2.place(x=510, y=150, width=840, height=500)

sanitizer_lbl = Label(F2, text="Account", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')

menu= StringVar()
menu.set("Select Any Language")

#Create a dropdown Menu
drop= OptionMenu(F2, menu,"C++", "Java","Python","JavaScript","Rust","GoLang")
drop.grid(row=0, column=1, padx=30, pady=10)


sanitize_lbl = Label(F2, text="Enter the following from your statement.", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')


mask_lbl = Label(F2, text="Beginning balance", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
mask_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
mask_txt = Entry(F2, width=22,  font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief=GROOVE)
mask_txt.grid(row=3, column=0, padx=10, pady=10)

hand_gloves_lbl = Label(F2, text="Ending balance", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
hand_gloves_lbl.grid(row=2, column=1, padx=10, pady=10, sticky='W')
hand_gloves_txt = Entry(F2, width=22,  font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief =GROOVE)
hand_gloves_txt.grid(row=3, column=1, padx=10, pady=10)

syrup_lbl = Label(F2, text="Ending date", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
syrup_lbl.grid(row=2, column=2, padx=10, pady=10, sticky='W')
#Create a Calendar using DateEntry
cal = DateEntry(F2, width= 22, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE)
cal.grid(row=3, column=2, padx=10, pady=10)

cream_lbl = Label(F2, text="Date", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
cream_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
#Create a Calendar using DateEntry
cal = DateEntry(F2, width= 22, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE)
cal.grid(row=5, column=0, padx=10, pady=10)

thermal_gun_lbl = Label(F2, text="Service charge", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_gun_lbl.grid(row=4, column=1, padx=10, pady=10, sticky='W')
thermal_gun_txt = Entry(F2, width=22, font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff",relief=GROOVE)
thermal_gun_txt.grid(row=5, column=1, padx=10, pady=10)

thermal_gug_lbl = Label(F2, text="Expense Account", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_gug_lbl.grid(row=4, column=2, padx=10, pady=10, sticky='W')
thermal_gug_txt = Entry(F2, width=22, font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief=GROOVE)
thermal_gug_txt.grid(row=5, column=2, padx=10, pady=10)

thermal_zone_lbl = Label(F2, text="Date", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_zone_lbl.grid(row=6, column=0, padx=10, pady=10, sticky='W')
#Create a Calendar using DateEntry
cal = DateEntry(F2, width= 22, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE)
cal.grid(row=7, column=0, padx=10, pady=10)

thermal_zoo_lbl = Label(F2, text="Interest earned", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_zoo_lbl.grid(row=6, column=1, padx=10, pady=10, sticky='W')
thermal_zoo_txt = Entry(F2, width=22, font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief=GROOVE)
thermal_zoo_txt.grid(row=7, column=1, padx=10, pady=10)

thermal_pin_lbl = Label(F2, text="Income Account", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_pin_lbl.grid(row=6, column=2, padx=10, pady=10, sticky='W')
thermal_pin_txt = Entry(F2, width=22, font=('times new roman', 16, 'bold'),bg="#fff",fg="#243e55", bd=5, relief=GROOVE)
thermal_pin_txt.grid(row=7, column=2, padx=10, pady=10)

b = Button(root,text = "Start Reconciling",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold'))  
b.place(x=805,y=560,width=250,height=40) 







root.mainloop()