from json import load
from tkinter import *
from tkinter import ttk
import tkinter as tk
root = tk.Tk()
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))
root.configure(bg="#2f516f")

root.title("Finsys")
bg_color = "#badc57"

N = Label(root, bg="#243e55", fg="#fff",font=('times new roman', 10, 'bold'), relief=RAISED)
N.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)
tit = Label(N, text="SALES RECORDS", font=('times new roman', 28, 'bold'), pady=2, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack(fill=X)

F = LabelFrame(root, font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#243e55")
F.place(x=5, y=200, width=1345, height=400)

menu= StringVar()
menu.set("New Transaction")

#Create a dropdown Menu
drop= OptionMenu(F, menu,"Invoice", "Payment","Sales Receipt","Credit note","Estimate","Delayed Charge","Time Activity")
drop.grid(row=1, column=0, padx=10, pady=10)

tree = ttk.Treeview(F,height=10)
tree['show'] = 'headings'

sb = ttk.Scrollbar(F, orient="vertical", command=tree.yview)
sb.grid(row=1,column=1,sticky="NS",pady=5)

tree.configure(yscrollcommand=sb.set)

tree["columns"]=("1","2","3","4","5","6","7","8","9","10")

tree.column("1", width=130)
tree.column("2", width=130)
tree.column("3", width=130)
tree.column("4", width=130)
tree.column("5", width=130)
tree.column("6", width=130)
tree.column("7", width=130)
tree.column("8", width=130)
tree.column("9", width=130)
tree.column("10", width=130)

tree.heading("1", text="DATE")
tree.heading("2", text="TYPE")
tree.heading("3", text="NO.")
tree.heading("4", text="CUSTOMER")
tree.heading("5", text="DUE DATE")
tree.heading("6", text="BALANCE")
tree.heading("7", text="TOTAL BEFORE")
tree.heading("8", text="TAX")
tree.heading("9", text="TOTAL")
tree.heading("10", text="ACTION")
datas = ["22-10-2022","artist","1","Alen","12-10-2022","500000","235600","25","725000","ACTION"]
item = tree.insert("", "end", values=(datas))

tree.grid(row=2,column=0,padx=5,pady=5)


root.mainloop()




