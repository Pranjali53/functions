Num1=int(input("enter numern1:-"))
Num2=int(input("enter numern2:-"))
Num3=int(input("enter numern3:-"))
if Num3<Num1>Num2:
    print(NUm1,"Num1 is greatest")
elif Num3<Num2>Num1:
    print(Num2,"Num2 is greatest")
else:
    print(Num3,"Num3 is greatest")


factorial=int(input("enter the number:"))
i=1
num=1
while i<=factorial:
    num*=i
    i+=1
print(num)


string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
i=0
new_list=[]
while i<len(string_list):
    if string_list[i] not in new_list:
        new_list.append(string_list[i])
    i+=1
print(new_list)


list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
List=[]
i=0
while i<len(list1):
    if list1[i] in list2:
        List.append(list1[i])
    i+=1
    new_list=sorted(List)
print(new_list)           

          
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
empty=[]
i=0
while i<len(list1):
    j=0
    while j<len(list2):
        if list1[i] not in empty:
            empty.append(list1[i])
        if list2[j] not in empty:
            empty.append(list2[j])
        j+=1
    i=i+1
    List=sorted(empty)
print(List)
