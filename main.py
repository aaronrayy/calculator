#importing needed libraries
from functions import *
import tkinter as tk

#setting up window
root = tk.Tk()
root.geometry("600x600")
root.config(bg="grey")
root.resizable(width=False,height=False)
root.title('calculator')

#output string representing math expression and answer
op = tk.StringVar()

#text field for result
label = tk.Label(root, textvariable=op, width=39, height=5)
label.place(x=100, y=0)

#functions to set output label depending on which button is pressed
def zero():
    s = op.get()
    s += "0"
    op.set(s)
def one():
    s = op.get()
    s += "1"
    op.set(s)
def two():
    s = op.get()
    s += "2"
    op.set(s)
def three():
    s = op.get()
    s += "3"
    op.set(s)
def four():
    s = op.get()
    s += "4"
    op.set(s)
def five():
    s = op.get()
    s += "5"
    op.set(s)
def six():
    s = op.get()
    s += "6"
    op.set(s)
def seven():
    s = op.get()
    s += "7"
    op.set(s)
def eight():
    s = op.get()
    s += "8"
    op.set(s)
def nine():
    s = op.get()
    s += "9"
    op.set(s)
def add():
    s = op.get()
    s += "+"
    op.set(s)
def sub():
    s = op.get()
    s += "-"
    op.set(s)
def div():
    s = op.get()
    s += "/"
    op.set(s)
def mult():
    s = op.get()
    s += "x"
    op.set(s)
def clear():
    s = ""
    op.set(s)

#this function calls the function.py file to parse the string and perform correct operation
def equal():
    s = op.get()
    result = parse(s)
    if(type(result) != int):     #checks if div by 0 occurred
        clear()
        op.set("Error: div by 0")
    else:
        answer = "" + s + " = " + str(result)
        op.set(answer)
        
#loop to place buttons for numbers 1-9
a = 1
b = 1
numarr = [one, two, three, four, five, six, seven, eight, nine]     #list of function names to set as button commnands
for i in range(9):
    tk.Button(root, text=(i+1), font=("Arial", 10), command=numarr[i], bg='white', fg='black', activebackground="black", padx=10, pady=10).place(x=(a*100), y=(b*100))
    a += 1
    if((a-1)%3 == 0):
        a = 1
        b += 1
#set button for zero
tk.Button(root, text="0", font=("Arial", 10), command=zero, bg='white', fg='black', activebackground="white", padx=10, pady=10).place(x=200, y=400)
#set buttons for operators
tk.Button(root, text="+", font=("Arial", 10), command=add, bg='white', fg='black', activebackground="white", padx=10, pady=10).place(x=400, y=100)
tk.Button(root, text="-", font=("Arial", 10), command=sub, bg='white', fg='black', activebackground="white", padx=10, pady=10).place(x=400, y=200)
tk.Button(root, text="/", font=("Arial", 10), command=div, bg='white', fg='black', activebackground="white", padx=10, pady=10).place(x=400, y=300)
tk.Button(root, text="x", font=("Arial", 10), command=mult, bg='white', fg='black', activebackground="white", padx=10, pady=10).place(x=400, y=400)
#set buttons for equals and clear
tk.Button(root, text="=", font=("Arial", 10), command=equal, bg='white', fg='black', activebackground="white", padx=10, pady=10).place(x=400, y=500)
tk.Button(root, text="C", font=("Arial", 10), command=clear, bg='white', fg='black', activebackground="white", padx=10, pady=10).place(x=300, y=500)

root.mainloop()
