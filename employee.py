#!/usr/bin/python

import sqlite3


class Employee_data:
    # create connection
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()

    def __init__(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS
        EMPLOYEE(EMPID, EMPNAME,EMPMOBILE,EMPDEPT,EMPADDRESS,EMPEMAIL)""")

    def save_employee(self, command):
        self.cursor.execute(command)
        self.cursor.execute("SELECT * FROM EMPLOYEE")
        print(self.cursor.fetchall())
