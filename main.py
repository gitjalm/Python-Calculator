from math import sqrt

def main():
    while True:
        equation = input("What is your equation? ")
        equation_list = equation.split()
        if equation.lower() == "stop":
            break
        if equation_list[1] == "+":
            a = equation.split('+')
            answer = int(a[0])+int(a[1])
            print(answer)
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
            if int(equation[0]) <= 0:
                print("Cannot get the square root of numbers that are 0 or less.")
            else:
                a = equation.split('!')
                answer = sqrt(int(a[0]))
                print(answer)
        else:
            print("Cannot recognise this type.")

if __name__ == "__main__":
    main()
