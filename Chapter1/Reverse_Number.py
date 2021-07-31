rev = int(input("Enter the number :"))

a = int(rev/10000)
b = int((rev/1000) % 10)
c = int((rev/100) % 10)
d = int((rev/10) % 10)
e = int(rev % 10)

print(e)
print(d)
print(c)
print(b)
print(a)
