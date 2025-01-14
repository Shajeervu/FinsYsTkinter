
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import tkinter.font as font
from unicodedata import category
import mysql.connector as mysql

# new


def submit():
    payee = drop2.get()
    payment_date = payment_input.get()
    payment_method = drop3.get()
    category1 = pro_drop1.get()
    category2 = pro_drop2.get()
    category3 = pro_drop3.get()
    categorydescription1 = discription_input1.get()
    categorydescription2 = discription_input2.get()
    categorydescription3 = discription_input3.get()
    categoryquantity1 = quantity_input1.get()
    categoryquantity2 = quantity_input2.get()
    categoryquantity3 = quantity_input3.get()
    categoryprice1 = price_input1.get()
    categoryprice2 = price_input2.get()
    categoryprice3 = price_input3.get()
    categorytotal1 = ctotal_input1.get()
    categorytotal2 = ctotal_input2.get()
    categorytotal3 = ctotal_input3.get()
    product1 = pro_drop1.get()
    product2 = pro_drop2.get()
    product3 = pro_drop3.get()
    productdescription1 = description_input1.get()
    productdescription2 = description_input2.get()
    productdescription3 = description_input3.get()
    hsn1 = hsn_input1.get()
    hsn2 = hsn_input2.get()
    hsn3 = hsn_input3.get()
    productquantity1 = pquantity_input1.get()
    productquantity2 = pquantity_input2.get()
    productquantity3 = pquantity_input3.get()
    productprice1 = pprice_input1.get()
    productprice2 = pprice_input2.get()
    productprice3 = pprice_input3.get()
    producttotal1 = ptotal_input1.get()
    producttotal2 = ptotal_input2.get()
    producttotal3 = ptotal_input3.get()
    producttax1 = taxpro_drop1.get()
    producttax2 = taxpro_drop2.get()
    producttax3 = taxpro_drop3.get()
    subtotal = sub_input.get()
    tax = tax_input.get()
    grandtotal = grand_input.get()

    if(payee == "" or payment_date == "" or payment_method == ""):
        MessageBox.showinfo("Insert the values!!!")
    else:
        con = mysql.connect(host="127.0.0.1", user="root",
                            password="", database="fynsystkinter")
        cursor = con.cursor()
        cursor.execute("insert into expenses values('" + payee + "' , '" + payment_date + "', '"+payment_method+"', '" + category1 + "' , '" + category2 + "', '"+category3+"', '" + categorydescription1 + "' , '" + categorydescription2 +
                       "', '"+categorydescription3+"', '" + categoryquantity1 + "' , '" + categoryquantity2 + "', '"+categoryquantity3+"', '" + categoryprice1 + "' , '" + categoryprice2 + "', '"+categoryprice3+"', '" + categorytotal1 + "' , '" + categorytotal2 + "', '"+categorytotal3+"', '" + product1 + "' , '" + product2 + "', '"+product3+"', '" + productdescription1 + "' , '" + productdescription2 + "', '"+productdescription3+"', '" + hsn1 + "' , '" + hsn2 + "', '"+hsn3+"', '" + productquantity1 + "' , '" + productquantity2 + "', '"+productquantity3+"', '" + productprice1 + "' , '" + productprice2 + "', '"+productprice3+"', '" + producttotal1 + "' , '" + producttotal2 + "', '"+producttotal3+"', '" + producttax1 + "' , '" + producttax2 + "', '"+producttax3+"', '" + subtotal + "' , '" + tax + "', '"+grandtotal+"') ")
        cursor.excecute("commit")

        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()


expense_form = tk.Tk()
expense_form.title("finsYs")
expense_form.geometry("1000x1000")
expense_form['bg'] = '#2f516a'
wrappen = ttk.LabelFrame(expense_form)
mycanvas = Canvas(wrappen)
mycanvas.pack(side=LEFT, fill="both", expand="yes")
yscrollbar = ttk.Scrollbar(wrappen, orient='vertical', command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
    scrollregion=mycanvas.bbox('all')))

full_frame = Frame(mycanvas, width=2000, height=1600, bg='#2f516a')
mycanvas.create_window((0, 0), window=full_frame, anchor="nw")


heading_frame = Frame(mycanvas)
mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
headingfont = font.Font(family='Times New Roman', size=25,)
credit_heading = Label(heading_frame, text="EXPENSES", fg='#fff',
                       bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=75)
credit_heading.pack(padx=0, pady=0)

# form fields
sub_headingfont = font.Font(family='Times New Roman', size=20,)
form_frame = Frame(mycanvas, width=1600, height=500, bg='#243e55')
mycanvas.create_window((0, 150), window=form_frame, anchor="nw")


title_lab = tk.Label(form_frame, text="PAYEE", bg='#243e55', fg='#fff')
place_input = StringVar()
drop2 = ttk.Combobox(form_frame, textvariable=place_input)

drop2['values'] = ("PAYEE1 PAYEE2 PAYEE3 PAYEE4")

title_lab.place(x=0, y=100, height=15, width=100)
drop2.place(x=30, y=130, height=40, width=450)
wrappen.pack(fill='both', expand='yes',)


payment_date = Label(form_frame, text="Payment Date", bg='#243e55', fg='#fff')
payment_date.place(x=30, y=200,)
payment_input = Entry(form_frame, width=55, bg='#243e55', fg='#fff')
payment_input.place(x=30, y=230, height=40)


payment_method_lab = tk.Label(
    form_frame, text="Payment Method", bg='#243e55', fg='#fff')
place_input = StringVar()
drop3 = ttk.Combobox(form_frame, textvariable=place_input)

drop3['values'] = ("Cash Cheque Debit_Card Credit_Card")

payment_method_lab.place(x=530, y=200, height=15, width=100)
drop3.place(x=530, y=230, height=40, width=450)
wrappen.pack(fill='both', expand='yes',)

amount = Label(form_frame, text="AMOUNT", bg='#243e55', fg='#fff')
amount.place(x=1130, y=200,)

digit = font.Font(family='Times New Roman', size=35,)
digit = Label(form_frame, text="0.00", bg='#243e55', font=digit, fg='#fff')
digit.place(x=1130, y=250,)


# CATEGORY DETAILS
sub_headingfont = font.Font(family='Times New Roman', size=18,)
form2_frame = Frame(mycanvas, width=1600, height=500,
                    bg='#243e55', bd=1, relief="groove")
mycanvas.create_window((0, 650), window=form2_frame, anchor="nw")

bill_heading = tk.Label(form2_frame, text="Catgory Details", fg='#fff',
                        bg='#243e55', height=2, font=sub_headingfont, width=15)
bill_heading.place(x=30, y=0,)

label = tk.Label(form2_frame, text="CATEGORY\t\tDESCRIPTION\t\tNOT APPLICABLE\t\tPRICE\t\tTOTAL\t\t",
                 bg='#243e55', fg="white", font=('Arial', 15))
label.place(x=120, y=50)

# row1
pro = tk.Label(form2_frame, text="", bg='#243e55', fg='#fff')
pro_drop1 = ttk.Combobox(form2_frame)
pro_drop1['values'] = ("", "", "", "")
pro.place(x=50, y=120, height=15, width=150)
pro_drop1.place(x=50, y=150, height=40, width=200)
# 2
pro = tk.Label(form2_frame, text="", bg='#243e55', fg='#fff')
pro_drop2 = ttk.Combobox(form2_frame)
pro_drop2['values'] = ("", "", "", "")
pro.place(x=50, y=210, height=15, width=150)
pro_drop2.place(x=50, y=240, height=40, width=200)
# 3
pro = tk.Label(form2_frame, text="", bg='#243e55', fg='#fff')
pro_drop3 = ttk.Combobox(form2_frame)
pro_drop3['values'] = ("", "", "", "")
pro.place(x=50, y=280, height=15, width=150)
pro_drop3.place(x=50, y=310, height=40, width=200)


# row 1
discription_input1 = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
discription_input1.place(x=380, y=150, height=40, width=200)
# row2
discription_input2 = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
discription_input2.place(x=380, y=240, height=40, width=200)
# row3
discription_input3 = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
discription_input3.place(x=380, y=310, height=40, width=200)

# row 1
quantity_input1 = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
quantity_input1.place(x=650, y=150, height=40, width=200)
# row2
quantity_input2 = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
quantity_input2.place(x=650, y=240, height=40, width=200)
# row3
quantity_input3 = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
quantity_input3.place(x=650, y=310, height=40, width=200)


# row 1
price_input1 = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
price_input1.place(x=880, y=150, height=40, width=150)
# row2
price_input2 = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
price_input2.place(x=880, y=240, height=40, width=150)
# row3
price_input3 = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
price_input3.place(x=880, y=310, height=40, width=150)

# row 1
ctotal_input1 = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
ctotal_input1.place(x=1080, y=150, height=40, width=100)
# row2
ctotal_input2 = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
ctotal_input2.place(x=1080, y=240, height=40, width=100)
# row3
ctotal_input3 = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
ctotal_input3.place(x=1080, y=310, height=40, width=100)


##################

# ITEM DETAILS
sub_headingfont = font.Font(family='Times New Roman', size=18,)
form4_frame = Frame(mycanvas, width=1500, height=500,
                    bg='#243e55', bd=1, relief="groove")
mycanvas.create_window((0, 1100), window=form4_frame, anchor="nw")

bill_heading = tk.Label(form4_frame, text="Item Details", fg='#fff',
                        bg='#243e55', height=2, font=sub_headingfont, width=15)
bill_heading.place(x=30, y=0,)

label = tk.Label(form4_frame, text="PRODUCT/SERVICE\tHSN\tDESCRIPTION\t\tQUANTITY\t\tPRICE\t\tTOTAL\t\tTAX\t\t",
                 bg='#243e55', fg="white", font=('Arial', 15))
label.place(x=60, y=60)

# row1
prod = tk.Label(form4_frame, text="", bg='#243e55', fg='#fff')
prod_drop1 = ttk.Combobox(form4_frame)
prod_drop1['values'] = ("", "", "", "")
prod.place(x=50, y=120, height=15, width=150)
prod_drop1.place(x=50, y=150, height=40, width=175)
# 2
prod = tk.Label(form4_frame, text="", bg='#243e55', fg='#fff')
prod_drop2 = ttk.Combobox(form4_frame)
prod_drop2['values'] = ("", "", "", "")
prod.place(x=50, y=210, height=15, width=150)
prod_drop2.place(x=50, y=240, height=40, width=175)
# 3
prod = tk.Label(form4_frame, text="", bg='#243e55', fg='#fff')
prod_drop3 = ttk.Combobox(form4_frame)
prod_drop3['values'] = ("", "", "", "")
prod.place(x=50, y=280, height=15, width=150)
prod_drop3.place(x=50, y=310, height=40, width=175)


# row 1
description_input1 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
description_input1.place(x=410, y=150, height=40, width=200)
# row2
description_input2 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
description_input2.place(x=410, y=240, height=40, width=200)
# row3
description_input3 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
description_input3.place(x=410, y=310, height=40, width=200)

# row 1
hsn_input1 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
hsn_input1.place(x=280, y=150, height=40, width=100)
# row2
hsn_input2 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
hsn_input2.place(x=280, y=240, height=40, width=100)
# row3
hsn_input3 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
hsn_input3.place(x=280, y=310, height=40, width=100)

# row 1
pquantity_input1 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
pquantity_input1.place(x=650, y=150, height=40, width=200)
# row2
pquantity_input2 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
pquantity_input2.place(x=650, y=240, height=40, width=200)
# row3
pquantity_input3 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
pquantity_input3.place(x=650, y=310, height=40, width=200)


# row 1
pprice_input1 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
pprice_input1.place(x=880, y=150, height=40, width=150)
# row2
pprice_input2 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
pprice_input2.place(x=880, y=240, height=40, width=150)
# row3
pprice_input3 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
pprice_input3.place(x=880, y=310, height=40, width=150)

# row 1
ptotal_input1 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
ptotal_input1.place(x=1080, y=150, height=40, width=100)
# row2
ptotal_input2 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
ptotal_input2.place(x=1080, y=240, height=40, width=100)
# row3
ptotal_input3 = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
ptotal_input3.place(x=1080, y=310, height=40, width=100)
# row1
taxpro_drop1 = ttk.Combobox(form4_frame)
taxpro_drop1['values'] = ("", "", "", "")
pro.place(x=1250, y=150, height=15, width=150)
taxpro_drop1.place(x=1250, y=150, height=40, width=200)
# row2
taxpro_drop2 = ttk.Combobox(form4_frame)
taxpro_drop2['values'] = ("", "", "", "")
pro.place(x=1250, y=240, height=15, width=150)
taxpro_drop2.place(x=1250, y=240, height=40, width=200)
# row3
taxpro_drop3 = ttk.Combobox(form4_frame)
taxpro_drop3['values'] = ("", "", "", "")
pro.place(x=1250, y=310, height=15, width=150)
taxpro_drop3.place(x=1250, y=310, height=40, width=200)

##################


sub_headingfont = font.Font(family='Times New Roman', size=18,)
form3_frame = Frame(mycanvas, width=1600, height=500,
                    bg='#243e55', bd=1, relief="groove")
mycanvas.create_window((0, 1500), window=form3_frame, anchor="nw")

sub_total = Label(form3_frame, text="SUB TOTAL", bg='#243e55', fg='#fff')
sub_total.place(x=900, y=110)
sub_input = Entry(form3_frame, width=40, bg='#243e55', fg='#fff')
sub_input.place(x=1000, y=100, height=40, width=200)

tax_amount = Label(form3_frame, text="TAX AMOUNT", bg='#243e55', fg='#fff')
tax_amount.place(x=900, y=160)
tax_input = Entry(form3_frame, width=40, bg='#243e55', fg='#fff')
tax_input.place(x=1000, y=150, height=40, width=200)

grand_total = Label(form3_frame, text="GRAND TOTAL", bg='#243e55', fg='#fff')
grand_total.place(x=900, y=210)
grand_input = Entry(form3_frame, width=40, bg='#243e55', fg='#fff')
grand_input.place(x=1000, y=200, height=40, width=200)

submit = tk.Button(form3_frame, text="Submit Form", command=submit)
submit.place(x=1050, y=280, width=100)


expense_form.mainloop()
