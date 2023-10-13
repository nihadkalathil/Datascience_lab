print("NIHAD K - SJC22MCA043")
def coprime(a,b):
    hcf = 1
    for i in range(1 , a+1):
        if a%i==0 and b%i==0:
            hcf=i
    return hcf == 1
first = int(input("Enter 1st no:"))
second = int(input("Enter 2nd no:"))
if coprime(first, second):
    print("%d and %d are coprime" %(first, second))
else:
    print("%d and %d are not coprime" % (first, second))
