l = float(input("Enter the length: "))
b = float(input("Enter the breadth: "))
r = float(input("Enter the radius: "))

peri_rect = 2*(l+b)
peri_cir = 2*3.14*r
area_rect = l*b
area_cir = 3.14*r*r

print("The perimeter of rectangle: ", peri_rect)
print("The perimeter of circle: ", peri_cir)
print("The area of rectangle: ", area_rect)
print("The area of circle: ", area_cir)
