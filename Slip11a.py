x=(1,2,3,4)
y=(3,5,3,1)
z=(2,2,3,1)
print("Original list: ")
print(x)
print(y)
print(z)
print("\nElement-wise sum of the said tuples:")
result=tuple(map(sum,zip(x,y,z)))
print(result)
output:
Original list: 
(1, 2, 3, 4)
(3, 5, 3, 1)
(2, 2, 3, 1)

Element-wise sum of the said tuples:
(6, 9, 9, 6)
