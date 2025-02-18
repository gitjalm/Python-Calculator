import tkinter as tk

equation = ""
temp_equation = ""

def on_click(num):
    print("Pressed")

root = tk.Tk()
root.title("Calculator")

lbl = tk.Label(root, text="hala")
lbl.grid(row=0, column=0)

btn0 = tk.Button(root, text="0", command=lambda: on_click("0"))
btn0.grid(row= 5, column=1)

btn1 = tk.Button(root, text="=", command=lambda: on_click(" = "))
btn1.grid(row= 4, column=3)

btn2 = tk.Button(root, text="1", command=lambda: on_click("1"))
btn2.grid(row= 4, column=0)
btn3 = tk.Button(root, text="2", command=lambda: on_click("2"))
btn3.grid(row= 4, column=1)
btn4 = tk.Button(root, text="3", command=lambda: on_click("3"))
btn4.grid(row= 4, column=2)

btn5 = tk.Button(root, text="+", command=lambda: on_click(" + "))
btn5.grid(row= 3, column=3)

btn6 = tk.Button(root, text="4", command=lambda: on_click("4"))
btn6.grid(row= 3, column=0)
btn7 = tk.Button(root, text="5", command=lambda: on_click("5"))
btn7.grid(row= 3, column=1)
btn8 = tk.Button(root, text="6", command=lambda: on_click("6"))
btn8.grid(row= 3, column=2)

btn9 = tk.Button(root, text="-", command=lambda: on_click(" - "))
btn9.grid(row= 2, column=3)

btn10 = tk.Button(root, text="7", command=lambda: on_click("7"))
btn10.grid(row= 2, column=0)
btn11 = tk.Button(root, text="8", command=lambda: on_click("8"))
btn11.grid(row= 2, column=1)
btn12 = tk.Button(root, text="9", command=lambda: on_click("9"))
btn12.grid(row= 2, column=2)

root.mainloop()
