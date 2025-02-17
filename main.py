from math import sqrt  #Importerer bare square root fra math biblioteket.

def main():
    while True:  #Infinite loop
        equation = input("What is your equation? ")    #Hva brukeren skal regne ut.
        equation_list = equation.split()    #Splitter equation stringen opp i en liste så index 1 blir hvilken type regneregel som skal brukes.
        if equation.lower() == "stop":  #Sjekker om brukeren vil stoppe programmet.
            break   #Stopper while True loopen.
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

if __name__ == "__main__":
    main()  #Starter programmet.
