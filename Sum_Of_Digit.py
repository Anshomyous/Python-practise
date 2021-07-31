mod = int(input("Enter the 5 digit no: "))

a = int(mod % 10) + int((mod/10) % 10) + int((mod/100) %
                                             10) + int((mod/1000) % 10) + int((mod/10000))


print("The sum of digit : ", a)
