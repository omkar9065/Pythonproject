# Perfect Number Checker
n = int(input("Enter any number: "))
sum1 = 0

# Find divisors
for i in range(1, n // 2 + 1):  # Only need to check till n//2
    if n % i == 0:
        sum1 += i

# Check if perfect
if sum1 == n and n != 0:
    print(f"{n} is a Perfect number!")
else:
    print(f"{n} is NOT a Perfect number!")
