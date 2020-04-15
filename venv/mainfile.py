from tkinter import ttk, BOTTOM
import tkinter as tk
import sqlite3
from datetime import datetime
from datetime import date

def show():


        conn = sqlite3.connect("mission.db")

        cur = conn.cursor()
        cur.execute("SELECT * FROM missions")
        rows = cur.fetchall()
        for i in tree.get_children():
            tree.delete(i)
        for row in rows:
            print(row)  # it print all records in the database

            tree.insert("", tk.END, values=row)

        conn.close()
        connect()






def connect():
    import sqlite3
    conn = sqlite3.connect('mission.db')
    c = conn.cursor()



    c.execute("CREATE TABLE IF NOT EXISTS missions(ID INTEGER PRIMARY KEY AUTOINCREMENT, TheSubject TEXT, TheDetail TEXT, datetime TEXT)")
    conn.commit()
    conn.close()


# Create table

# Insert a row of data
   # c.execute("INSERT INTO Purchases VALUES ('2006-01-05','BUY','RHAT',100)")

# Save (commit) the changes
def Insert(s,ss,sss):

    conn1 = sqlite3.connect('mission.db')
    c = conn1.cursor()
    c.execute("INSERT INTO missions VALUES (?, ?, ?, ?);",(None,s,ss,sss))
# Save (commit) the changes
    conn1.commit()
    conn1.close()




def View():

          conn = sqlite3.connect("mission.db")
          cur = conn.cursor()
          cur.execute("SELECT * FROM mission")
          rows = cur.fetchall()
          for i in tree.get_children():
              tree.delete(i)
          for row in rows:

           print(row) # it print all records in the database

           tree.insert("", tk.END, values=row)

          conn.close()

connect()

#column = ("column1", "column2", "column3", "column4"),


def de(id):
    conn = sqlite3.connect("mission.db")
    cur = conn.cursor()
    sql = 'DELETE FROM missions WHERE id=?'
    cur = conn.cursor()

    cur.execute(sql, id)
    conn.commit()
    show()




root = tk.Tk()
root.geometry("450x600")

tree= ttk.Treeview(root, show='headings')
tree["columns"] = ("#1", "#2", "#3", "#4")
tree.column("#1",width=15)
tree.column("#2",width=100)
tree.column("#3",width=100)
tree.column("#4",width=100)
tree.heading("#1", text=" Id")
tree.heading("#2", text="the subject")
tree.heading("#3", text="Detail")
tree.heading("#4", text="date and time")

#fill='y',
#Insert()

tree.place(x=35, y=200, height=350, width=400)
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
vsb.place(x=16, y=200, height=350)

tree.configure(yscrollcommand=vsb.set)


IPNumber= tk.Label(root, text="detail")
IPNumber.grid(row=4,column=3)



today = date.today()
date= tk.Label(root, text=today)
date.grid(row=2,column=2)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
time= tk.Label(root, text=current_time)
time.grid(row=1,column=2)




MASSAGE= tk.Label(root, text="subject")
MASSAGE.grid(row=6,column=3)

enterIP = tk.Entry(root,width=20)
enterIP.grid(row=5,column=3)

enterMassge = tk.Entry(root,width=50)
enterMassge.grid(row=7,column=3)
def f ():
    st=enterMassge.get()
    det=enterIP.get()
    Insert(s=st,ss=det,sss=today)
    show()


idt = tk.Entry(root,width=10)
idt.grid(row=3,column=1)

def ff():
    deid=idt.get()
    de(deid)




b2 = tk.Button(text="save", command=f)
b2.grid(row=8,column=3)
b3 = tk.Button(text="delete", command=ff)
b3.grid(row=4,column=1)


deletid = tk.Label(root,text="ID")
deletid.grid(row=2,column=1)

show()
root.mainloop()



