from math import sqrt

def main():
    while True:
        equation = input("What is your equation? ")
        if equation.lower() == "stop":
            break
        if "+" in equation:
            a = equation.split('+')
            answer = int(a[0])+int(a[1])
            print(answer)
        elif "-" in equation:
            a = equation.split('-')
            answer = int(a[0])-int(a[1])
            print(answer)
        elif "*" in equation:
            a = equation.split('*')
            answer = int(a[0])*int(a[1])
            print(answer)
        elif "/" in equation:
            a = equation.split('/')
            answer = int(a[0])/int(a[1])
            print(answer)
        elif "!" in equation:
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
