print("Nihad K - SJC22MCA043")
lower=int(input("enter the lowest range:"))
upper=int(input("enter the highest range:"))
print("the prime nos in the range are:")
for number in range (lower,upper + 1):
    if number > 1:
        for i in range (2,number):
            if (number % i)==0:
                print(number)
                break
