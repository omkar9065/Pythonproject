num = int(input("Enter a number: "))
temp = num
order = len(str(num))   # number of digits
total = 0

while temp > 0:
    digit = temp % 10          # extract last digit
    total += digit ** order    # raise digit to power of order and add
    temp //= 10                # remove last digit

if num == total:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
