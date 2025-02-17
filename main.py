def main():
    while True:
        equation = input("What is your equation? ")
        if equation.lower() == "stop":
            break
        if "+" in equation:
            print("addition")
        elif "-" in equation:
            print("subtraction")
        elif "*" in equation:
            print("multiplication")
        elif "/" in equation:
            print("division")
        else:
            print("Cannot recognise this type.")


if __name__ == "__main__":
    main()
