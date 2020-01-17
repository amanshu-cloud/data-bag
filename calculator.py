def add(a, b):
    return a+b


def sub(a, b):
    if a > b:
        return a-b
    else:
        return b-a


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def pow(a, b):
    return a ** b


def remainder(a, b):
    return a % b


print("calculator using python\n1-add\n2-subtract\n3-multiply\n4-divide\n5-power\n6-remainder of two nums")
choice = int(input("enter choice : "))
if choice == 1:
    num_1 = int(input("enter num1:"))
    num_2 = int(input("enter num2:"))
    print(f"addition of num1 and num2 is {add(num_1,num_2)}")

elif choice == 2:
    num_1 = int(input("enter subrahend: "))
    num_2 = int(input("enter subtractor : "))
    print(f"subtraction of{num_1} and {num_2} is {sub(num_1,num_2)}")

elif choice == 3:
    num_1 = int(input("enter num_1 : "))
    num_2 = int(input("enter num_2 : "))
    print(f"multiplication of {num_1} and {num_2} is {mul(num_1,num_2)}")

elif choice == 4:
    num_1 = int(input("enter dividend :"))
    num_2 = int(input("enter divisor : "))
    print(f"{num_1}/{num_2} is {div(num_1,num_2)}")

elif choice == 5:
    base = int(input("enter number to be raised: "))
    power = int(input("what power to raise : "))
    print(f"{base} to the power {power} = {pow(base,power)}")

elif choice == 6:
    a = int(input("num_1: "))
    b = int(input("num_2: "))
    print(f"remainder of {a} and {b} is {remainder(a,b)}")
