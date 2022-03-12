a = ("Apple", "Banana", "Mango", "Pineapple")
b = tuple(("Apple", "Banana", "Pineapple"))
print(a)
print(b)
print(type(a))
print(type(b))
print(len(a))

print(a[1])
print(a[-1])
print(a[1:3])

c = input("Enter name=")
if c in a:
    print("Yes, Available")
else:
    print("No, Unavailable")
