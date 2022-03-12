a = ["Yes", "No", "Hello", "Hii", "Bye"]
b = ["Apple", "Banana", "Pineapple"]
print(a)
print(len(a))
print(type(a))
print(a[2])
print(a[2:4])
if "Y" in a:
    print("Yes, available")
else:
    print("Unavailable")
a[1] = "Sanket"
print(a)
a[1:3] = ["Sanjivani", "Kopargaon"]
print(a)
a.insert(2, "Good_Night")
print(a)

a.extend(b)
print(a)

a.remove("Yes")     #to remove Yes
print(a)

a.pop(1)            # to remove index item
print(a)

del a[1]            # to delete the item by its index
print(a)

b.clear()           # the items of the list will get clear, list will be empty
print(b)
