input_string1 = input("Enter a list 1 numbers or elements separated by space: ")
userList1 = input_string1.split()
input_string2 = input("Enter a list 2 numbers or elements separated by space: ")
userList2= input_string2.split()
intersection_list=[]
for x in userList1:
    for y in userList2:
        if x==y:
            intersection_list.append(x)
print("intersection of list: "+str(intersection_list))
