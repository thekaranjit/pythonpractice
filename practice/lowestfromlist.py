
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


res = len(a)
new_list=[]

for i in a:
    if i < 5:
        new_list.append(i)
    
 
    
final_res = new_list[::]

print("All the numbers which are less than 5 are: ", final_res)