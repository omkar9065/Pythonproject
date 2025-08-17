d={'orange':2,'red':5,'black':7,'blue':9}
print("The given dictionary of colour is",d)
x=input("Enter key to check: ")
y=input("Enter value: ")
if x in d:
    print(x,"is present.")
    d.pop(x)
    d[x]=y
else:
    print(x,"is not Present.")
    d[x]=y
    print("Updated Dictionary: ",d)
