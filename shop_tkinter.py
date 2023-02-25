import tkinter
import sqlite3
try:
    cnt=sqlite3.connect('shop.db')
    # print("opened database successfully")
except:
    print("an error occured in db connection")
    
#------------------- create a new table --------------------
# query=''' CREATE TABLE users
#     (ID INTEGER PRIMARY KEY,
#       user CHAR(25) NOT NULL,
#       pass CHAR(25) NOT NULL,
#       addr  CHAR(50) NOT NULL,
#       comment CHAR(50) 
#       )'''
# cnt.execute(query)
# print("users Table created successfuly")
# cnt.close()

# ---------------------- insert initial record in users table------------------------------

# query='''INSERT INTO users (user,pass,addr)
# VALUES("admin","123456789","rasht")'''

# cnt.execute(query)
# print("users Table created successfuly")
# cnt.commit()
# cnt.close()

# ---------------------- insert initial record in products table------------------------------

# query='''INSERT INTO products (pname,price,qnt)
# VALUES("nokia n95",100,20)'''

# cnt.execute(query)
# print("users Table created successfuly")
# cnt.commit()
# cnt.close()
#------------------- create products table --------------------
# query=''' CREATE TABLE products
#     (ID INTEGER PRIMARY KEY,
#       pname CHAR(25) NOT NULL,
#       price int NOT NULL,
#       qnt  int NOT NULL
#       )'''
# cnt.execute(query)
# print("products Table created successfuly")
# cnt.close()

# -------------------------create final shop table--------------------
# query=''' CREATE TABLE finalShop
#     (ID INTEGER PRIMARY KEY,
#       uid int NOT NULL,    
#       pid int NOT NULL,
#       qnt int NOT NULL
#       )'''
# cnt.execute(query)
# print(" Table created successfuly")
# cnt.close()
# =============================================================================

# =============================================================================
# -------------------- functions--------------------------------------------
def login():
    global userID
    user=user_txt.get()
    pas=pass_txt.get()
    
    query='''SELECT id FROM users WHERE user=? AND pass=?'''
    result=cnt.execute(query,(user,pas))
    rows=result.fetchall()
    if len(rows)<1:
        msg_lbl.configure(text="wrong username or password",fg="red")
        return
    userID=rows[0][0]
    
    if user=="admin":
        admin_btn.configure(state="active")
    
    
    msg_lbl.configure(text="wellcome to your account",fg="green")
    btn_login.configure(state="disabled")
    btn_logout.configure(state="active")
    btn_shop.configure(state="active")
    btn_p_shop.configure(state="active")
    
    user_txt.delete(0,"end")
    pass_txt.delete(0,"end")
    
    user_txt.configure(state="disabled")
    pass_txt.configure(state="disabled")
    
    
def logout():
    msg_lbl.configure(text="you are logged out now",fg="green")
    btn_login.configure(state="active")
    btn_logout.configure(state="disabled")
    btn_shop.configure(state="disable")
    btn_submit.configure(state="active")
    btn_p_shop.configure(state="disable")
    
    
    user_txt.configure(state="normal")
    pass_txt.configure(state="normal")


# -------------------------------------------------------------------------
def submit():    
    global user1_txt,pass1_txt,addr_txt,lbl_msg2,cpas_txt

    win_submit=tkinter.Toplevel(win)
    win_submit.geometry("400x300")
    win_submit.title("submit")
    
    lbl_user1=tkinter.Label(win_submit,text="username")
    lbl_user1.pack()
    user1_txt=tkinter.Entry(win_submit,width=20)
    user1_txt.pack()
    
    lbl_pass1=tkinter.Label(win_submit,text="password")
    lbl_pass1.pack()
    
    pass1_txt=tkinter.Entry(win_submit,width=20)
    pass1_txt.pack()
    
    lbl_cpas=tkinter.Label(win_submit,text="Re_pass")
    lbl_cpas.pack()
       
    cpas_txt=tkinter.Entry(win_submit,width=20)
    cpas_txt.pack()

    lbl_addr = tkinter.Label(win_submit,text="address")
    lbl_addr.pack()
    addr_txt = tkinter.Entry(win_submit,width=20)
    addr_txt.pack()

    lbl_msg2 = tkinter.Label(win_submit,text="")
    lbl_msg2.pack(pady=10)    
    
    btn_submit2 = tkinter.Button(win_submit,text="submit",command=second_submit)
    btn_submit2.pack() 
    
    win_submit.mainloop()
#----------------------------------------
def second_submit():
    global user1_txt,pass1_txt,addr_txt,lbl_msg2,cpas_txt
        
    user=user1_txt.get()
    pas=pass1_txt.get()
    cpas=cpas_txt.get()
    addr=addr_txt.get()
   
    query = ''' SELECT * FROM users WHERE user = ?'''
    result = cnt.execute(query,(user,))
    rows = result.fetchall()    
   
    if len(rows) != 0:
        lbl_msg2.configure(text="username alredy Exist!",fg = "red")
        return  
    if len(pas) < 8:
        lbl_msg2.configure(text="your password should be at least 8 char",fg="red")
        return        
    if user == "" or pas == "" or  cpas=="" or addr == "":
        lbl_msg2.configure(text="please Fill all blanks",fg="red")
        return 
    if pas != cpas:
        lbl_msg2.configure(text="password and confirmation mismatch",fg="red")
        return 
    
        
    query = ''' INSERT INTO users (user,pass,addr) VALUES (?,?,?) '''
    cnt.execute(query,(user,pas,addr))
    cnt.commit() 

    # cnt.close()
    btn_submit.configure(state="disabled")
    lbl_msg2.configure(text="submit done!!",fg="green")

    
    user1_txt.delete(0,"end")
    pass1_txt.delete(0,"end")
    cpas_txt.delete(0,"end")
    addr_txt.delete(0,"end")     
#--------------------------------------------------------------------- 
def shop_win():
    global txt_id,txt_qnt,lbl_msg2,lstbox
    sh_win=tkinter.Toplevel(win)
    sh_win.geometry("500x500")
    sh_win.title("shopping panel")
    sh_win.resizable(False,False)
  

    #-------------- fetch all products----------------------------------
    
    query='''SELECT * FROM products'''
    result=cnt.execute(query)
    rows=result.fetchall()
    
    #-------------------------Listbox-----------------------------------
    lstbox=tkinter.Listbox(sh_win,width=350)
    lstbox.pack(pady=10)
    #--------------------shop widgets------------------------------
    lbl_id=tkinter.Label(sh_win,text="product ID:")
    lbl_id.pack()

    txt_id=tkinter.Entry(sh_win,width=20)
    txt_id.pack()
    
    lbl_qnt=tkinter.Label(sh_win,text="product QNT:")
    lbl_qnt.pack()
    
    txt_qnt=tkinter.Entry(sh_win,width=20)
    txt_qnt.pack()
    
    lbl_msg2=tkinter.Label(sh_win,text="")
    lbl_msg2.pack()
    
    btn_final_shop=tkinter.Button(sh_win,text="SHOP NOW!",command=final_shop)
    btn_final_shop.pack(pady=10)
    
    
    # lstbox.insert("end", "TEST")
    #-------------------------insert data to listbox--------------------------
    for i in  rows:
        # msg=str(i[0])+"   "+ i[1]+"  price:  "+str(i[2]) +"  QNT:  "+ str(i[3])
        msg=f"{i[0]}-----{i[1]}----price:{i[2]}----QNT:{i[3]}"
        lstbox.insert("end",msg)
        
    
    update_shop()  
    sh_win.mainloop()
    
    
    
def final_shop():
    pid=txt_id.get()
    pqnt=txt_qnt.get()
    if pid=="" or pqnt =="":
        lbl_msg2.configure(text="please fill All the Blanks",fg="red")
        return
    
    query='''SELECT * FROM products WHERE id=?'''
    result=cnt.execute(query,(pid,))
    rows=result.fetchall()
    # print(rows)
    if len(rows)==0:
        lbl_msg2.configure(text="wrong product id ",fg="red")
        return
    real_pqnt=rows[0][3]
    
    if (int(pqnt))>real_pqnt :
        lbl_msg2.configure(text="Not enough product quantity ",fg="red")
        return
# ------------------------------------insert into final shop table--------------------
    query='''INSERT INTO finalShop (uid,pid,qnt)
    VALUES (?,?,?)'''
    cnt.execute(query,(userID,pid,pqnt))
    cnt.commit()
# --------------------------------update products table----------------------------

    new_qnt=real_pqnt-int(pqnt)
    query='''UPDATE products SET qnt=? WHERE id=?'''
    cnt.execute(query,(new_qnt,pid))
    cnt.commit()
    lbl_msg2.configure(text="successfully added to cart",fg="green")
    txt_id.delete(0,"end")
    txt_qnt.delete(0,"end")
    
    
    update_shop()
    
def update_shop():
    
    query = ''' SELECT * FROM products'''
    result = cnt.execute(query)
    rows = result.fetchall()
    lstbox.delete(0,"end")
    for item in rows:
           lstbox.insert("end",f"{item[0]} {item[1]} Price={item[2]} QNT={item[3]}") 
    
def personal_shop():
    
    p_shop = tkinter.Toplevel(win)
    p_shop.title("personal shop")
    p_shop.geometry("400x300")
    p_shop.resizable(False,False)
    
    lstbox1=tkinter.Listbox(p_shop,width=100)
    lstbox1.pack(pady=10)
    
    # query=''' SELECT pname,price,qnt FROM final_shop WHERE '''
    # result=cnt.execute(query,(,))
    # rows=result.fetchall()
    # اینجا باید جدول product رو به جدول final_shop وصل کنیم ولی بلد نبودم ):      
    
    
    # for item in rows:
    #   total_price=item[1]*item[2]
    #   lstbox1.insert("end",f"name:{item[0]}  QNT:{item[2]} total price={total_price}")
    
    
    p_shop.mainloop()

def insert_products():
    pname=txt_pname.get()
    price=txt_price.get()
    qnt1=txt_qnt.get()
    
    
    query='''SELECT * FROM products WHERE pname=?'''
    result=cnt.execute(query,(pname,))
    row=result.fetchone()
    if row:
       lbl_msg3.configure(text="product name already exists!",fg="red")
       return 
    
    if pname=="" or price=="" or qnt1=="":
        lbl_msg3.configure(text="fill all the blanks",fg="red")
        return
    
  
    query = ''' INSERT INTO products (pname,price,qnt) VALUES (?,?,?) '''
    cnt.execute(query,(pname,price,qnt1))
    cnt.commit()
    lbl_msg3.configure(text="product saved successfully!",fg="green")
    txt_pname.delete(0,"end")
    txt_qnt.delete(0,"end")
    txt_price.delete(0,"end")

def admin_panel():
    global txt_pname,txt_price,lbl_msg3,txt_qnt
    admin_win = tkinter.Toplevel(win)
    admin_win.title("admin Panel")
    admin_win.geometry("400x300")
    admin_win.resizable(False,False)
# --------------------------------------------------------------------------
    lbl_pname = tkinter.Label(admin_win,text="product name")
    lbl_pname.pack()
    
    txt_pname = tkinter.Entry(admin_win,width=20)
    txt_pname.pack()
    
    lbl_price = tkinter.Label(admin_win,text="price")
    lbl_price.pack()
    
    txt_price = tkinter.Entry(admin_win,width=20)
    txt_price.pack()
    
    lbl_qnt = tkinter.Label(admin_win,text="quantity")
    lbl_qnt.pack()
    
    txt_qnt = tkinter.Entry(admin_win,width=20)
    txt_qnt.pack()
    
    lbl_msg3=tkinter.Label(admin_win,text="")
    lbl_msg3.pack()
    
    insert_btn=tkinter.Button(admin_win,text="insert product",command=insert_products)
    insert_btn.pack()
    
    
    admin_win.mainloop()


# ----------------------main--------------------------------------------
win=tkinter.Tk()
win.title("login")
win.geometry("400x300")

user_lbl=tkinter.Label(win,text="username")
user_lbl.pack()

user_txt=tkinter.Entry(win,width=25)
user_txt.pack()

pass_lbl=tkinter.Label(win,text="password")
pass_lbl.pack()

pass_txt=tkinter.Entry(win,width=25)
pass_txt.pack()

msg_lbl=tkinter.Label(win,text="")
msg_lbl.pack()

btn_login=tkinter.Button(win,text="login",command=login,width=15)
btn_login.pack()

btn_logout=tkinter.Button(win,text="logout",state="disabled",command=logout,width=15)
btn_logout.pack()

btn_shop=tkinter.Button(win,text="shop",state="disabled",command=shop_win,width=15)
btn_shop.pack()

btn_submit = tkinter.Button(win,text="Submit",command=submit,width=15)
btn_submit.pack()

btn_p_shop=tkinter.Button(win,text="personal shop",state="disabled",command=personal_shop,width=15)
btn_p_shop.pack()

admin_btn=tkinter.Button(win,text="admin Panel",state="disabled",command=admin_panel,width=15)
admin_btn.pack()


win.mainloop()