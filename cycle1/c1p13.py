def sum_of_digits(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum
try:
    print("NIHAD K - SJC22MCA043")
    num=int(input("Enter a positive number:"))
    if num <= 0:
        print("Please enter a positive number.")
    else:
        while num > 0:
            digit_sum = sum_of_digits(num)
            print(f"{num} - {digit_sum} = {num - digit_sum}")
            num -= digit_sum
except ValueError:
    print("Invalid input. Please enter a valid positive number.")
