def edit_product():
    
        selected_item = treevv.selection()[0]
        global B
        B=tk.Toplevel(A)
        B.title('Add products')
        B.title('edit products')
        B.geometry('1400x700')
        mycanvas=tk.Canvas(B,width=1500,height=1200)
        mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
        yscrollbar =ttk.Scrollbar(B,orient='vertical',command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT,fill=Y)
        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
        frame=tk.Frame(mycanvas)
        frame['bg']='#2f516f'
        mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1000)
        #head frame

        head1 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
        f1 = font.Font(family='poppins',size=30)#font
        lb1=tk.Label(head1,text='PRODUCT / SERVICE INFORMATION',bg='#243e54',foreground='white')
    
        lb1['font']=f1
        lb1.place(relx=0.2,rely=0.2)
        head1.place(relx=0,rely=0.05,relwidth=1,relheight=0.08)
    
        head3 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
        f2 = font.Font(family='poppins',size=25)#font
        lb2=tk.Label(head3,text='INVENTORY',bg='#243e54',foreground='white')
        bu = Button(head3,text = "Choose Type",command=selectproduct,bg="#5193e6",fg="#fff",font=('mali', 10, 'bold'))  
        bu.place(relx=0.5,rely=0.2,width=250,height=40) 
    
        lb2['font']=f2
        lb2.place(relx=0.3,rely=0.2)
        head3.place(relx=0,rely=0.15,relwidth=1,relheight=0.08)
    
    
    
    
    
    


    #contents frame
        hd1= tk.LabelFrame(frame,borderwidth=0,bg='#243e54') 
   
        f3 = font.Font(family='poppins',size=18)#font
        hd1.place(relx=0,rely=0.06,relwidth=1,relheight=0.1)
    
        but2 = Button(hd1,text = "UPLOAD IMAGE",command=upload_file,bg="black",fg="#fff",font=('mali', 10, 'bold'))  
        but2.place(relx=0.8,rely=0.02,width=250,height=30) 

        tk.Label(hd1,text='Name',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.02,rely=0.05)
    #title.grid(row=3,column=2,padx=20,pady=20)
        productname=tk.Entry(hd1,bg='#2f516f').place(relx=0.02,rely=0.08,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='SKU',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.35,rely=0.05)
        sku=tk.Entry(hd1,bg='#2f516f').place(relx=0.35,rely=0.08,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='HSN Code',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.05)
        phsncode=tk.Entry(hd1,bg='#2f516f').place(relx=0.68,rely=0.08,relwidth=0.3,relheight=0.035)
    
    
        tk.Label(hd1,text='Unit',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.13)
        valu=['CHOOSE','BAG Bags','BAL Bale BOU','BDL Bundles','BKL Buckles','BOX Box','BTL Bottles','CAN Cans','CTN Cartons','CCM Cubic centimeters','CBM Cubic meters','CMS Centimeters','DRM Drums','DOZ Dozens','GGK Great gross GYD','GRS GrossGMS','KME Kilometre','KGS Kilograms','KLR Kilo litre','MTS Metric ton','MLT Mili litre','MTR Meters','NOS Numbers','PAC Packs','PCS Pieces','PRS Pairs','QTL Quintal','ROL Rolls','SQY Square Yards','SET Sets','SQF Square feet','SQM Square meters','TBS Tablets','TUB Tubes','TGM Ten Gross','THD Thousands','TON Tonnes','UNT Units','lons','YDS Yards']
        punit=ttk.Combobox(hd1,values=valu)
        punit.current(0)
        punit.place(relx=0.02,rely=0.16,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Catogory',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.13)
        eemail=tk.Entry(hd1,bg='#2f516f')
        eemail.place(relx=0.35,rely=0.16,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Low stock alert',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.13)
        emobile=tk.Entry(hd1,bg='#2f516f').place(relx=0.68,rely=0.16,relwidth=0.3,relheight=0.035)
    
        tk.Label(hd1,text='Description',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.20)
        eopen=tk.Entry(hd1,bg='#2f516f').place(relx=0.02,rely=0.24,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Sales price/rate',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.20)
        e_accno=tk.Entry(hd1,bg='#2f516f').place(relx=0.35,rely=0.24,relwidth=0.3,relheight=0.035)

        web=tk.Label(hd1,text='Initial quantity on hand',font=('poppins', 14),bg='#243e54',foreground='white')
        web.place(relx=0.68,rely=0.20)
        eweb=tk.Entry(hd1,bg='#2f516f')
  
        eweb.place(relx=0.68,rely=0.24,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Purchasing information',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.28)
        ebill=tk.Entry(hd1,bg='#2f516f').place(relx=0.02,rely=0.31,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Cost',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.28)
        Checkbutton(frame, text = "Inclusive of purchase tax ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.4,rely=0.55)
        eterms=tk.Entry(hd1,bg='#2f516f').place(relx=0.35,rely=0.31,relwidth=0.3,relheight=0.035)
    

        tk.Label(hd1,text='TAX',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.35)
        gstvalues=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
        egst=ttk.Combobox(hd1,values=gstvalues)
        egst.current(0)
        egst.place(relx=0.02,rely=0.38,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Purchase TAX',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.35)
        purchasetaxvalues=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
        egst_in=ttk.Combobox(hd1,values=purchasetaxvalues)
        egst_in.current(0)
        egst_in.place(relx=0.35,rely=0.38,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Income account',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.35)
        incometaxvalues=['Billable Expense Income','Product Sales','Sales','Sales-Hardware','Sales-Software','Sales-Support and Maintanance','Sales of Product Income','Uncategorised Income']
        inctax_in=ttk.Combobox(hd1,values=incometaxvalues)
        inctax_in.current(0)
        inctax_in
        inctax_in.place(relx=0.68,rely=0.38,relwidth=0.27,relheight=0.035)  
    

        date=tk.Label(hd1,text='As of date',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.42)
        edate=DateEntry(hd1,bg='#2f516f').place(relx=0.02,rely=0.45,relwidth=0.3,relheight=0.035)
        tk.Button(hd1,text='+',font=(14),command=stplus).place(relx=0.955,rely=0.38,relwidth=0.025,relheight=0.035)
    
        defexp=tk.Label(hd1,text='Inventory asset account',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.42)
        defvalues=['Inventory Assets']
        edefexp=ttk.Combobox(hd1,values=defvalues)
        edefexp.current(0)
        edefexp.place(relx=0.35,rely=0.45,relwidth=0.27,relheight=0.035)  

        tk.Button(hd1,text='+',font=(14),command=splus).place(relx=0.625,rely=0.45,relwidth=0.025,relheight=0.035)

    

        tds=tk.Label(hd1,text='Expense account',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.42)
        defvalue=['Cost of sales']
        etds=ttk.Combobox(hd1,values=defvalue)
        etds.current(0)
        etds.place(relx=0.68,rely=0.45,relwidth=0.27,relheight=0.035) 
        tk.Button(hd1,text='+',font=(14),command=suplus).place(relx=0.955,rely=0.45,relwidth=0.025,relheight=0.035)
    
    

        street=tk.Label(hd1,text='Reverse Charge %',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.02,rely=0.53)
        estreet=tk.Entry(hd1,bg='#2f516f').place(relx=0.02,rely=0.57,relwidth=0.63,relheight=0.035)  
    
        city=tk.Label(hd1,text='Preferred Supplier',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.68,rely=0.53)
        ecity=tk.Entry(hd1,bg='#2f516f').place(relx=0.68,rely=0.57,relwidth=0.3,relheight=0.035)

    

    


        sub=tk.Button(hd1,text='SUBMIT',font=15,bg='#5193e6',foreground='white').place(relx=0.02,rely=0.65)

        hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)
    

        tk.Frame(frame, bg='#243e54').place(relx=0.02, rely=0.95, relwidth=0.90, relheight=0.8)
        B.mainloop()