List = [(12,14,4,18),(7,15,22,10),(8,45,5,3),(8,18,21,0)]

print("The List before sorting :",str(List))

num = int(input('enter the index to sort around'))
List.sort(key = lambda x: x[num])

print("the List after sortimg by",num,"th element is :",str(List))
