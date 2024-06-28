import random
import sys
import pyperclip
import tkinter as tk
from tkinter import ttk
from ast import literal_eval
root = tk.Tk()

root.geometry("300x300")
root.title("Pseudo-Passwordinator")

label = tk.Label(root, text="Pseudo random password generator", font=('Arial',10))
label.pack(padx=10,pady=10)

check_ual = tk.IntVar()
check0 = tk.Checkbutton(root, text="inlcude upper case?", variable=check_ual)
check0.pack()

check_num = tk.IntVar()
check1 = tk.Checkbutton(root, text="inlcude numbers?", variable=check_num)
check1.pack()

check_spec = tk.IntVar()
check3 = tk.Checkbutton(root, text="inlcude special characters?", variable=check_spec)
check3.pack()

label2 = tk.Label(root, text="Choose length", font=('Arial',10))
label2.pack(padx=10,pady=5)

check2= tk.Entry(root)
check2.pack()

progress = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=125)
progress.pack(padx=10, pady=10)

def generate():
    progress['value']=0
    ual=check_ual.get()
    num=check_num.get()
    spec=check_spec.get()
    count=literal_eval(check2.get())
    countstep=100/count
    
    output=""

    list1 = []
    for x in range(97,123):
        list1+=chr(x)
    upper = []
    for x in range(65,91):
        upper+=chr(x)
    numbers = [1,2,3,4,5,6,7,8,9,0]
    special=[]
    for x in range(33,48):
        special+=chr(x)
    for x in range(58,65):
        special+=chr(x)
    for x in range(123,127):
        special+=chr(x)

    if(ual):
        list1+=upper
    if(num):
        list1+=numbers
    if(spec):
        list1+=special
    for x in range(int(count)):
        output+=str(random.choice(list1))
        progress['value'] += countstep
        root.update_idletasks() 

    pyperclip.copy(str(output))

showstate= tk.Button(root, text="generate and copy new password", font=("Arial", 10), command=generate)
showstate.pack(padx=10,pady=10)

showstate= tk.Button(root, text="quit", font=("Arial", 10), command=quit)
showstate.pack(padx=10,pady=10)
root.mainloop()
