
a = int(input("Please input a number: "))

b = int(input("Input a range to check: "))

lst = []

for i in range(b):
    if i % a == 0:
        lst.append(i)
        
    
        
print(lst)