def divisible(low,peak,divider):
    for i in range(low,peak):
        if i%divider==0:
            print(i)


divisible(1,100,7)