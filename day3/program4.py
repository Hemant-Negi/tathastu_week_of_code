input_string = input("Enter a string 1 numbers or elements separated by space: ")
userList = input_string.split()
print("user entered following string: "+ str(userList))
i=0
new_list=[]
for x in userList:
    if x not in new_list:
        new_list.append(x)
print("list after removing duplicates: "+str(new_list))
