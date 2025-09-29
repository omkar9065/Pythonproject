# Accept 5 integer values from the user
nums = []

for i in range(5):
    val = int(input(f"Enter integer {i+1}: "))
    nums.append(val)

# Check for duplicates
if len(nums) != len(set(nums)):
    print("DUPLICATES")
else:
    print("ALL UNIQUE")

Output:
Enter integer 1: 23
Enter integer 2: 55
Enter integer 3: 43
Enter integer 4: 23
Enter integer 5: 65
DUPLICATES
