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
