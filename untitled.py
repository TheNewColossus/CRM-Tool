import os
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

from faker import Faker

db_path=os.path.join(os.getcwd(),"database","CRM.db")
root = Tk()
root.geometry("1000x600")
root.title("CRM TOOL")
root.iconbitmap(os.path.join(os.getcwd(),"icon","Untitled.ico"))
my_menu = Menu(root)
root.config(menu = my_menu)

#Querying database
def query_database():
    #Clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT * FROM customers")
    results = cur.fetchall()

    #Adding data to Screen
    cnt = 0
    for record in results:
        if cnt % 2 == 0:
            my_tree.insert(parent="",index = "end",iid = cnt,text = "",
            values = (record[0],record[1],record[2],record[3],record[4],record[5],
            record[6],record[7]),tags = ("evenrow",))
        else:
            my_tree.insert(parent="",index = "end",iid = cnt,text = "",
            values = (record[0],record[1],record[2],record[3],record[4],record[5],
            record[6],record[7]),tags = ("oddrow",))
        cnt += 1

    conn.commit()
    conn.close()

def search_records_id():
    lookup_record = int(search_entry.get())
    search.destroy()

    #Clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT * FROM customers WHERE ID = ?",(lookup_record,))
    results = cur.fetchall()

    #Adding data to Screen
    cnt = 0
    for record in results:
        if cnt % 2 == 0:
            my_tree.insert(parent="",index = "end",iid = cnt,text = "",
            values = (record[0],record[1],record[2],record[3],record[4],record[5],
            record[6],record[7]),tags = ("evenrow",))
        else:
            my_tree.insert(parent="",index = "end",iid = cnt,text = "",
            values = (record[0],record[1],record[2],record[3],record[4],record[5],
            record[6],record[7]),tags = ("oddrow",))
        cnt += 1

    conn.commit()
    conn.close()


def search_records_first():
    lookup_record = search_entry.get()
    search.destroy()

    #Clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT * FROM customers WHERE first_name like ?",(lookup_record,))
    results = cur.fetchall()

    #Adding data to Screen
    cnt = 0
    for record in results:
        if cnt % 2 == 0:
            my_tree.insert(parent="",index = "end",iid = cnt,text = "",
            values = (record[0],record[1],record[2],record[3],record[4],record[5],
            record[6],record[7]),tags = ("evenrow",))
        else:
            my_tree.insert(parent="",index = "end",iid = cnt,text = "",
            values = (record[0],record[1],record[2],record[3],record[4],record[5],
            record[6],record[7]),tags = ("oddrow",))
        cnt += 1

    conn.commit()
    conn.close()

def search_records_last():
    lookup_record = search_entry.get()
    search.destroy()

    #Clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT * FROM customers WHERE last_name like ?",(lookup_record,))
    results = cur.fetchall()

    #Adding data to Screen
    cnt = 0
    for record in results:
        if cnt % 2 == 0:
            my_tree.insert(parent="",index = "end",iid = cnt,text = "",
            values = (record[0],record[1],record[2],record[3],record[4],record[5],
            record[6],record[7]),tags = ("evenrow",))
        else:
            my_tree.insert(parent="",index = "end",iid = cnt,text = "",
            values = (record[0],record[1],record[2],record[3],record[4],record[5],
            record[6],record[7]),tags = ("oddrow",))
        cnt += 1

    conn.commit()
    conn.close()

def lookup_records_id():
    global search, search_entry
    search = Toplevel(root)
    search.title("Lookup Records")
    search.geometry("400x200")

    #Label Frame
    search_frame = LabelFrame(search,text = "ID")
    search_frame.pack(padx = 10, pady = 10)

    #Entry box
    search_entry = Entry(search_frame, font = ("Helvetica", 18))
    search_entry.pack(padx = 20, pady = 20)

    #Search Button
    search_button = Button(search, text = "Search Records", command = search_records_id)
    search_button.pack(padx = 20, pady = 20)


def lookup_records_first():
    global search, search_entry
    search = Toplevel(root)
    search.title("Lookup Records")
    search.geometry("400x200")

    #Label Frame
    search_frame = LabelFrame(search,text = "First Name")
    search_frame.pack(padx = 10, pady = 10)

    #Entry box
    search_entry = Entry(search_frame, font = ("Helvetica", 18))
    search_entry.pack(padx = 20, pady = 20)

    #Search Button
    search_button = Button(search, text = "Search Records", command = search_records_first)
    search_button.pack(padx = 20, pady = 20)


def lookup_records_last():
    global search, search_entry
    search = Toplevel(root)
    search.title("Lookup Records")
    search.geometry("400x200")

    #Label Frame
    search_frame = LabelFrame(search,text = "Last Name")
    search_frame.pack(padx = 10, pady = 10)

    #Entry box
    search_entry = Entry(search_frame, font = ("Helvetica", 18))
    search_entry.pack(padx = 20, pady = 20)

    #Search Button
    search_button = Button(search, text = "Search Records", command = search_records_last)
    search_button.pack(padx = 20, pady = 20)

def create_backup():
    from datetime import datetime
    i = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    os.makedirs(os.path.join(os.getcwd(),"backups"),exist_ok = True)
    src = os.path.join(os.getcwd(),"database","CRM.db")
    dst = os.path.join(os.getcwd(),"backups",f"CRM_backup_{i}.db")
    shutil.copy2(src,dst)
    messagebox.showinfo("Attention!","Backup Created Successfully")

#Search menu
search_menu = Menu(my_menu, tearoff = 0)
bkup_menu = Menu(my_menu, tearoff = 0)
my_menu.add_cascade(label = "Search", menu = search_menu)
my_menu.add_cascade(label = "Backup", menu = bkup_menu)
bkup_menu.add_command(label = "Create Backup", command = create_backup)
search_menu.add_command(label = "By ID",command = lookup_records_id)
search_menu.add_separator()
search_menu.add_command(label = "By First Name",command = lookup_records_first)
search_menu.add_separator()
search_menu.add_command(label = "By Last Name",command = lookup_records_last)
search_menu.add_separator()
search_menu.add_command(label = "Reset",command = query_database)

# ~ #GENERATING FAKE DATA
# ~ fake = Faker()
# ~ data = []
# ~ for i in range(25):
    # ~ data.append([i+1,fake.name().split()[0],fake.name().split()[1],
    # ~ fake.phone_number(),fake.address(),fake.city(),fake.state(),
    # ~ int(fake.zipcode())])


#Setting up the database system
#Creating the database or connecting to one that exists
conn = sqlite3.connect(db_path)
cur = conn.cursor()

#Creating a table
cur.execute("""CREATE TABLE if not exists customers (
    ID integer PRIMARY KEY,
    first_name text,
    last_name text,
    phone_no text,
    address text,
    city text,
    state text,
    zipcode text)
    """)

#Adding data to our table
# ~ for record in data:
    # ~ cur.execute("INSERT INTO customers VALUES (:ID,:first_name,:last_name,:phone_no,:address,:city,:state,:zipcode)",
    # ~ {
    # ~ "ID":record[0],
    # ~ "first_name":record[1],
    # ~ "last_name":record[2],
    # ~ "phone_no":record[3],
    # ~ "address":record[4],
    # ~ "city":record[5],
    # ~ "state":record[6],
    # ~ "zipcode":record[7]
    # ~ }

    # ~ )


#Commiting changes
conn.commit()
conn.close()

#Style selection and Treeview Configuration
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview",
background = "#D3D3D3",
foreground = "black",
rowheight=25,
fieldbackground="#D3D3D3")

# Changing selected colour
style.map("Treeview",
background = [("selected","#347083")])


#Frame Creation
tree_frame = Frame(root)
tree_frame.pack(pady=10)

#Scroll Creation
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side = RIGHT,fill = Y)

#Treeview Creation
my_tree = ttk.Treeview(tree_frame,yscrollcommand = tree_scroll.set,
selectmode = "extended")
my_tree.pack()

#Config Scrollbar
tree_scroll.config(command = my_tree.yview)

#Formatting Columns
my_tree["columns"] = ("ID","First Name","Last Name", "Phone No.",
 "Address", "City", "State", "Zipcode")

my_tree.column("#0",width=0,stretch=NO)
my_tree.column("ID",anchor=CENTER,width=100)
my_tree.column("First Name",anchor=W,width=140)
my_tree.column("Last Name",anchor=W,width=140)
my_tree.column("Phone No.",anchor=CENTER,width=140)
my_tree.column("Address",anchor=W,width=190)
my_tree.column("City",anchor=W,width=140)
my_tree.column("State",anchor=W,width=140)
my_tree.column("Zipcode",anchor=CENTER,width=140)

#Formatting Heading
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("ID",text="ID",anchor=CENTER)
my_tree.heading("First Name",text="First Name",anchor=W)
my_tree.heading("Last Name",text="Last Name",anchor=W)
my_tree.heading("Phone No.",text="Phone No.",anchor=CENTER)
my_tree.heading("Address",text="Address",anchor=W)
my_tree.heading("City",text="City",anchor=W)
my_tree.heading("State",text="State",anchor=W)
my_tree.heading("Zipcode",text="Zipcode",anchor=CENTER)


#Striped Row Tags
my_tree.tag_configure("oddrow",background="white")
my_tree.tag_configure("evenrow",background="lightgreen")


#Record Entry Boxes
data_frame = LabelFrame(root,text = "Record")
data_frame.pack(fill = 'x',expand = "yes", padx = 20)

id_label = Label(data_frame,text = "ID")
id_label.grid(row = 0,column = 0, padx = 10, pady = 10)
id_entry = Entry(data_frame)
id_entry.grid(row = 0,column = 1, padx = 10, pady = 10)

fn_label = Label(data_frame,text = "First Name")
fn_label.grid(row = 0,column = 2, padx = 10, pady = 10)
fn_entry = Entry(data_frame)
fn_entry.grid(row = 0,column = 3, padx = 10, pady = 10)

ln_label = Label(data_frame,text = "Last Name")
ln_label.grid(row = 0,column = 4, padx = 10, pady = 10)
ln_entry = Entry(data_frame)
ln_entry.grid(row = 0,column = 5, padx = 10, pady = 10)

ph_label = Label(data_frame,text = "Phone No.")
ph_label.grid(row = 0,column = 6, padx = 10, pady = 10)
ph_entry = Entry(data_frame)
ph_entry.grid(row = 0,column = 7, padx = 10, pady = 10)

ad_label = Label(data_frame,text = "Address")
ad_label.grid(row = 1,column = 0, padx = 10, pady = 10)
ad_entry = Entry(data_frame)
ad_entry.grid(row = 1,column = 1, padx = 10, pady = 10)

ct_label = Label(data_frame,text = "City")
ct_label.grid(row = 1,column = 2, padx = 10, pady = 10)
ct_entry = Entry(data_frame)
ct_entry.grid(row = 1,column = 3, padx = 10, pady = 10)

st_label = Label(data_frame,text = "State")
st_label.grid(row = 1,column = 4, padx = 10, pady = 10)
st_entry = Entry(data_frame)
st_entry.grid(row = 1,column = 5, padx = 10, pady = 10)

zp_label = Label(data_frame,text = "Zipcode")
zp_label.grid(row = 1,column = 6, padx = 10, pady = 10)
zp_entry = Entry(data_frame)
zp_entry.grid(row = 1,column = 7, padx = 10, pady = 10)

#Create table again
def create_again():
    #Setting up the database system
    #Creating the database or connecting to one that exists
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    #Creating a table
    cur.execute("""CREATE TABLE if not exists customers (
    ID integer PRIMARY KEY,
    first_name text,
    last_name text,
    phone_no text,
    address text,
    city text,
    state text,
    zipcode text)
    """)

    conn.commit()
    conn.close()


#Add New Record
def add_record():
    #Updating the database
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO customers VALUES (:ID,:first_name,:last_name,:phone_no,:address,:city,:state,:zipcode)",
            {
                "ID":id_entry.get(),
                "first_name":fn_entry.get(),
                "last_name":ln_entry.get(),
                "phone_no":ph_entry.get(),
                "address":ad_entry.get(),
                "city":ct_entry.get(),
                "state":st_entry.get(),
                "zipcode":zp_entry.get()
            }
        )
    except:
        messagebox.showerror("Error!","Record with ID number already exists")

    conn.commit()
    conn.close()

    #Clearing entry boxes
    id_entry.delete(0,END)
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    ph_entry.delete(0,END)
    ad_entry.delete(0,END)
    ct_entry.delete(0,END)
    st_entry.delete(0,END)
    zp_entry.delete(0,END)

    #Refreshing the interface
    my_tree.delete(*my_tree.get_children())
    query_database()

#Update Record
def update_record():
    selected = my_tree.focus()
    my_tree.item(selected,text = "",values = (id_entry.get(),
    fn_entry.get(),ln_entry.get(),ph_entry.get(),ad_entry.get(),
    ct_entry.get(),st_entry.get(),zp_entry.get()))

    #Updating the database
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""UPDATE customers SET
      first_name = :first_name,
      last_name = :last_name,
      phone_no = :phone_no,
      address = :address,
      city = :city,
      state = :state,
      zipcode = :zipcode

      where ID = :ID""",
      {
        "first_name":fn_entry.get(),
        "last_name":ln_entry.get(),
        "phone_no":ph_entry.get(),
        "address":ad_entry.get(),
        "city":ct_entry.get(),
        "state":st_entry.get(),
        "zipcode":zp_entry.get(),
        "ID":id_entry.get()
      }
      )

    conn.commit()
    conn.close()

    #Clearing entry boxes
    id_entry.delete(0,END)
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    ph_entry.delete(0,END)
    ad_entry.delete(0,END)
    ct_entry.delete(0,END)
    st_entry.delete(0,END)
    zp_entry.delete(0,END)


#Move Row Up
def move_up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row,my_tree.parent(row),my_tree.index(row) - 1)


#Move Row Down
def move_down():
    rows = my_tree.selection()
    for row in rows[::-1]:
        my_tree.move(row,my_tree.parent(row),my_tree.index(row) + 1)


#Clear All Boxes
def clear_ent_boxes():
    id_entry.delete(0,END)
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    ph_entry.delete(0,END)
    ad_entry.delete(0,END)
    ct_entry.delete(0,END)
    st_entry.delete(0,END)
    zp_entry.delete(0,END)


#Selecting a Record
def select_record(eve):
    id_entry.delete(0,END)
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    ph_entry.delete(0,END)
    ad_entry.delete(0,END)
    ct_entry.delete(0,END)
    st_entry.delete(0,END)
    zp_entry.delete(0,END)

    #Grabbing Entry
    selected = my_tree.focus()
    values = my_tree.item(selected,'values')

    #Outputting to Entry Boxes
    id_entry.insert(0,values[0])
    fn_entry.insert(0,values[1])
    ln_entry.insert(0,values[2])
    ph_entry.insert(0,values[3])
    ad_entry.insert(0,values[4])
    ct_entry.insert(0,values[5])
    st_entry.insert(0,values[6])
    zp_entry.insert(0,values[7])

#Deleting a record
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

    #Updating the database
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DELETE from customers WHERE ID="+id_entry.get())

    conn.commit()
    conn.close()

    clear_ent_boxes()
    messagebox.showinfo("","The record has been deleted!")

#Removing many records
def remove_many():
    resp = messagebox.askyesno("Warning!","This will delete ALL SELECTED from the table.\n\nDo you want to continue?")

    if resp == 1:
        x = my_tree.selection()

        #Logic for getting ID's from records
        id_del = [(my_tree.item(i,"values")[0],) for i in x]

        for record in x:
            my_tree.delete(record)

        #Updating the database
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        cur.executemany("DELETE FROM customers WHERE ID = ?",id_del)

        conn.commit()
        conn.close()

        clear_ent_boxes()

#Removing all records
def remove_all():
    resp = messagebox.askyesno("Warning!","This will delete EVERYTHING from the table.\n\nDo you want to continue?")

    if resp == 1:
        for record in my_tree.get_children():
            my_tree.delete(record)

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        cur.execute("DROP TABLE customers")

        conn.commit()
        conn.close()

        clear_ent_boxes()
        #Recreating the table
        create_again()


#Command Buttons
button_frame = LabelFrame(root,text = "Commands")
button_frame.pack(fill = 'x',expand = "yes",padx = 20)

add_button = Button(button_frame,text = "Add Record",
command=add_record)
add_button.grid(row = 0, column = 0, padx = 10, pady = 10)

update_button = Button(button_frame,text = "Update Record",
command = update_record)
update_button.grid(row = 0, column = 1, padx = 10, pady = 10)

remove_one_button = Button(button_frame,text = "Remove One",
command = remove_one)
remove_one_button.grid(row = 0, column = 2, padx = 10, pady = 10)

remove_many_button = Button(button_frame,text = "Remove Many",
command = remove_many)
remove_many_button.grid(row = 0, column = 3, padx = 10, pady = 10)

remove_all_button = Button(button_frame,text = "Remove All Records",
command = remove_all)
remove_all_button.grid(row = 0, column = 4, padx = 10, pady = 10)

mv_up_button = Button(button_frame,text = "Move Up",
command = move_up)
mv_up_button.grid(row = 0, column = 5, padx = 10, pady = 10)

mv_down_button = Button(button_frame,text = "Move Down",
command = move_down)
mv_down_button.grid(row = 0, column = 6, padx = 10, pady = 10)

clear_button = Button(button_frame,text = "Clear Entry Boxes",
command = clear_ent_boxes)
clear_button.grid(row = 0, column = 7, padx = 10, pady = 10)

my_tree.bind("<ButtonRelease-1>",select_record)

#Pulling data from database
query_database()
root.mainloop()
