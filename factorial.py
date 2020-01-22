def factorial(num):
    result = 1
    if num != 0 :
        while(num!=0):
            result = result*num
            num-=1
        return result
    else:
        return result

print("The factorial of entered number is", factorial(int(input("enter number :"))))