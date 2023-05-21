from tkinter import *
from subprocess import Popen

def open_inventory():
    Popen(["python", "Inventory.py"])

def open_payroll():
    Popen(["python", "Payroll.py"])

# Creating a window
win = Tk()
win.geometry("860x620")
win.minsize(width=560, height=520)
win.title("Restaurant Management System")

# Creating a title and menu frame
titleFrame = Frame(win, bg="#005B96")
titleFrame.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.15)

menuFrame = Frame(win, bg="#6497B1")
menuFrame.place(relx=0.0, rely=0.15, relwidth=1.0, relheight=0.85)

# Creating a title heading
heading = Label(titleFrame, text="Welcome to Bhagubhai Restaurant", font=("Arial", 26, "bold"), bg="#005B96", fg="white")
heading.place(relx=0.5, rely=0.5, anchor=CENTER)

heading2 = Label(menuFrame, text="Admin's Dashboard", font=("Arial", 26, "bold"), bg="#005B96", fg="white")
heading2.place(relx=0.5, rely=0.1, anchor=CENTER)


# Creating a menu
adbk = Button(menuFrame, text="Payroll", command=open_payroll, bg="#E83C3C", fg="white", font=("Arial", 16), width=15)
adbk.place(relx=0.5, rely=0.3, anchor=CENTER)

dltbk = Button(menuFrame, text="Inventory", command=open_inventory, bg="#FFCC33", fg="white", font=("Arial", 16), width=15)
dltbk.place(relx=0.5, rely=0.5, anchor=CENTER)

win.mainloop()
