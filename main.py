from math import sqrt  #Importerer bare square root fra math biblioteket.
import tkinter as tk

equation = ""   #Flyttet equation variabel så den kan bli brukt av alle funksjoner og elementer.
temp_equation = ""  #Laget en temp_equation for midlertidlig lagring av infoen så resten ikke blir rørt.

def main(equation):
    equation_list = equation.split()    #Splitter equation stringen opp i en liste så index 1 blir hvilken type regneregel som skal brukes.
    if " " in equation: #Sjekker om det er et mellomrom i equation.
        if equation_list[1] == "+":     #Sjekker om index 1 er et plus tegn.
            a = equation.split('+')     #Lager en ny liste med tallene hver for seg.
            answer = int(a[0])+int(a[1])    #Regner ut å setter sammen svaret.
            print(answer)   #Printer svaret.
        elif equation_list[1] == "-":
            a = equation.split('-')
            answer = int(a[0])-int(a[1])
            print(answer)
        elif equation_list[1] == "*":
            a = equation.split('*')
            answer = int(a[0])*int(a[1])
            print(answer)
        elif equation_list[1] == "/":
            a = equation.split('/')
            answer = int(a[0])/int(a[1])
            print(answer)
        elif equation_list[1] == "!":
            if int(equation[0]) <= 0:   #Sjekker om tallet er lik eller mindre enn 0.
                print("Cannot get the square root of numbers that are 0 or less.")  #Printer en feilmelding til brukeren.
            else:
                a = equation.split('!')
                answer = sqrt(int(a[0]))    #Bruker den importerte funksjonen sqrt til å få kvadratroten til tallet.
                print(answer)
        else:
            print("Cannot recognise this type or incorrect use of spaces.")     #Feilmelding.
    else:
        print("Remember to use correct spaces in between numbers and symbols.")     #Feilmelding.

def button_press(num):  #Funksjonen som blir kalt når du trykker en av knappene som ikke er Backspace eller er lik.
    global temp_equation
    temp_equation += str(num)   #Legger til det tegne som ble trykt på kalkulatoren
    lbl.config(text=temp_equation)  #Oppdaterer teksten på kalkulatoren så du kan se hva du har skrevet allerede.

def equal(info):
    global equation
    global temp_equation
    equation = temp_equation    
    main(equation)

def clear():    #Funksjonen som blir kalt npr brukeren trykker backspace knappen.
    global temp_equation
    temp_equation = " "     #Fjerner alle tegn og tall fra temp_equation.
    lbl.config(text=temp_equation)

root = tk.Tk()
root.title("Calculator")

lbl = tk.Label(root, text="0", height=3)    #Viser tallene og tegnene som allerde har blitt skrevet inn i kalkulatoren.
lbl.grid(row=0, column=0)   #Velger hvor i kalkulatorens grid den befinner seg i.

btn = tk.Button(root, text="Backspace", command=lambda: clear(), height=4, width=8)     #Knapp for å fjerne all forrige data.
btn.grid(row= 5, column=3)

btn = tk.Button(root, text="/", command=lambda: button_press(" / "), height=4, width=8)
btn.grid(row= 5, column=0)
btn = tk.Button(root, text="0", command=lambda: button_press("0"), height=4, width=8)
btn.grid(row= 5, column=1)
btn = tk.Button(root, text="*", command=lambda: button_press(" * "), height=4, width=8)
btn.grid(row= 5, column=2)

btn = tk.Button(root, text="=", command=lambda: equal(temp_equation), height=4, width=8)
btn.grid(row= 4, column=3)

btn = tk.Button(root, text="1", command=lambda: button_press("1"), height=4, width=8)
btn.grid(row= 4, column=0)
btn = tk.Button(root, text="2", command=lambda: button_press("2"), height=4, width=8)
btn.grid(row= 4, column=1)
btn = tk.Button(root, text="3", command=lambda: button_press("3"), height=4, width=8)
btn.grid(row= 4, column=2)

btn = tk.Button(root, text="+", command=lambda: button_press(" + "), height=4, width=8)
btn.grid(row= 3, column=3)

btn = tk.Button(root, text="4", command=lambda: button_press("4"), height=4, width=8)
btn.grid(row= 3, column=0)
btn = tk.Button(root, text="5", command=lambda: button_press("5"), height=4, width=8)
btn.grid(row= 3, column=1)
btn = tk.Button(root, text="6", command=lambda: button_press("6"), height=4, width=8)
btn.grid(row= 3, column=2)

btn = tk.Button(root, text="-", command=lambda: button_press(" - "), height=4, width=8)
btn.grid(row= 2, column=3)

btn = tk.Button(root, text="7", command=lambda: button_press("7"), height=4, width=8)
btn.grid(row= 2, column=0)
btn = tk.Button(root, text="8", command=lambda: button_press("8"), height=4, width=8)
btn.grid(row= 2, column=1)
btn = tk.Button(root, text="9", command=lambda: button_press("9"), height=4, width=8)
btn.grid(row= 2, column=2)

root.mainloop()     #Kjører GUI i en loop.