def palindrome(num):
    num = str(num)
    a = list()
    b = list()
    for i in range(len(num)):
        a.append(num[i])
        a.reverse()
    for i in range(len(a)):
        if a[i]==num[i]:
            return "number is a palindrome"
        else:
            return "not a palindrome"




print(palindrome(4554))