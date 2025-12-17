num = int(input("Enter a number: "))
sum_of_digits = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_digits += digit
    temp //= 10

if num % sum_of_digits == 0:
    print(num, "is a Harshad Number.")
else:
    print(num, "is not a Harshad Number.")