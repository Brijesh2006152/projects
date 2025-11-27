from tkinter import *

root = Tk()
root.title("calculator")
exp = Entry(root, font=("consolas", 14), borderwidth=2, relief="solid")
exp.grid(row=0, column=0,columnspan=5, pady=10, padx=10, ipadx=5, ipady=5)

# calculator functions

def insert_num(number):
    char_index = len(exp.get())
    exp.insert(char_index, number)

def clear():
    exp.delete(0, END)

def calculate():
    try:
        final_exp = exp.get()
        clear()
        exp.insert(0, f"{eval(final_exp):.10f}")

    except:
        exp.insert(0, "invalid")

# row 1
btn1 = Button(root, text="7", padx=20, pady=10, command=lambda: insert_num(7))
btn2 = Button(root, text="8", padx=20, pady=10, command=lambda: insert_num(8))
btn3 = Button(root, text="9", padx=20, pady=10, command=lambda: insert_num(9))
btn4 = Button(root, text="+", padx=20, pady=10, command=lambda: insert_num('+'))

btn1.grid(row=1 , column=1)
btn2.grid(row=1 , column=2)
btn3.grid(row=1 , column=3)
btn4.grid(row=1 , column=4)

# row 2
btn5 = Button(root, text="4", padx=20, pady=10, command=lambda: insert_num(4))
btn6 = Button(root, text="5", padx=20, pady=10, command=lambda: insert_num(5))
btn7 = Button(root, text="6", padx=20, pady=10, command=lambda: insert_num(6))
btn8 = Button(root, text="-", padx=20, pady=10, command=lambda: insert_num('-'))

btn5.grid(row=2, column=1)
btn6.grid(row=2 , column=2)
btn7.grid(row=2 , column=3)
btn8.grid(row=2 , column=4)

# row 3
btn9 = Button(root, text="1", padx=20, pady=10, command=lambda: insert_num(1))
btn10 = Button(root, text="2", padx=20, pady=10, command=lambda: insert_num(2))
btn11 = Button(root, text="3", padx=20, pady=10, command=lambda: insert_num(3))
btn12 = Button(root, text="*", padx=20, pady=10, command=lambda: insert_num('*'))

btn9.grid(row=3 , column=1)
btn10.grid(row=3 , column=2)
btn11.grid(row=3 , column=3)
btn12.grid(row=3 , column=4)

# row 4
btn13 = Button(root, text=".", padx=20, pady=10, command=lambda: insert_num('.'))
btn14 = Button(root, text="0", padx=20, pady=10, command=lambda: insert_num(0))
btn15 = Button(root, text="=", padx=20, pady=10, command=calculate)
btn16 = Button(root, text="/", padx=20, pady=10, command=lambda: insert_num('/'))

btn13.grid(row=4 , column=1)
btn14.grid(row=4 , column=2)
btn15.grid(row=4 , column=3)
btn16.grid(row=4 , column=4)

# clear button
btn17 = Button(root, text="clear", padx=20, pady=10, command=clear)
btn17.grid(row=5, column=0, columnspan=5)





root.mainloop()

