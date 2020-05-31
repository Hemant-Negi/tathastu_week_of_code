  
dict1 = {"Hemant":97 , "Ayush":95, "Malan":88, "kartik":73,"Ajay":74,"Ajay":58,"Ayush":89,"Abhay":97,"Neeru":88}
dict2={}
for keys,values in dict1.items():
    if values not in dict2.values():
        dict2[keys]=values
print("dictionary before removing duplicates: ",dict1)
print("dictionary after removing duplicates : ",dict2)
