def replace_0to5(num):
    return int(num.replace('0','5'))
num = input("Enter the number you want to check: ")
print("number before replacing : ",num)
print("The number after replacing all 0 to 5: ", replace_0to5(num))
