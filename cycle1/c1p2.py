print("Nihad K - SJC22MCA043")
n=int(input("enter the numbers up to you want to print:"))
a = 0
b = 1
for i in range(0,n):
    print(a ,end = " ")
    c= a+b
    a = b
    b = c