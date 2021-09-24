#!/usr/bin/python
from functools import partial
from tkinter import *
from tkinter.messagebox import showinfo

from employee import Employee_data

master = Tk()


def submit(empname, mobile, dept, email, add):
    id = 1
    id = id + 1
    query = "INSERT INTO EMPLOYEE VALUES({},'{}','{}','{}','{}','{}')".format(id, empname.get(), mobile.get(),
                                                                              dept.get(), add.get(), email.get())
    print(query)
    emp = Employee_data()
    emp.save_employee(query)
    popup_showinfo(empname.get())


def popup_showinfo(emp):
    showinfo("Employee "+emp+" added successfully!.")



Label(master, text='Employee Name').grid(row=0)
Label(master, text='Mobile').grid(row=1)
Label(master, text='Email').grid(row=2)
Label(master, text='Department').grid(row=3)
Label(master, text='Address').grid(row=4)

empname = StringVar()
dept = StringVar()
email = StringVar()
mobile = StringVar()
add = StringVar()

e1 = Entry(master, textvariable=empname)
e2 = Entry(master, textvariable=mobile)
e3 = Entry(master, textvariable=email)
e4 = Entry(master, textvariable=dept)
e5 = Entry(master, textvariable=add)
call_result = partial(submit, empname, mobile, dept, email, add)
b1 = Button(master, text="Submit", command=call_result, activeforeground="red", activebackground="pink", pady=10)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
b1.grid(row=5, column=1)

mainloop()
