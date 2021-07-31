m1 = float(input("Enter sst marks: "))
m2 = float(input("Enter science marks: "))
m3 = float(input("Enter maths marks: "))
m4 = float(input("Enter english marks: "))
m5 = float(input("Enter computer marks: "))


agg = (m1+m2+m3+m4+m5)/5
per = (m1+m2+m3+m4+m5)/500 * 100

print("The aggregrate marks will be : ", agg)
print("Percentage obtained : ", per)
