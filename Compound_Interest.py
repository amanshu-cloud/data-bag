def compInt(p, r, n, t):
    return (p)*(1+(r/n))**(n*t)


principle = int(input("enter the principle amount:"))
rate = int(input("enter the rate of interest:"))
n = int(input("no of times interest applied per time period:"))
t = int(input("enter time period in years: "))

print(f"compound interest calculated: Rs {int(compInt(principle,rate,n,t))}")
