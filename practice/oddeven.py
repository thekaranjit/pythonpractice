name = input("Please Enter your Name: ")
num = int(input("Please input a number: "))
res = int(num) % 2

if res == 0:
    print("Hey " + name + " You've entered an EVEN number")
    
else:
    print("Hey " + name + " You've entered an ODD number")