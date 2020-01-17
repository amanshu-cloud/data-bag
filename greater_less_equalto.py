def compare(a, b):
    if a > b:
        return "num_1 greater than num_2"
    elif a == b:
        return "num_1 equal to num_2"
    else:
        return "num_1 less than num_2"


a = int(input('enter number_1 :'))
b = int(input("compare with ? : "))
print(compare(a, b))
