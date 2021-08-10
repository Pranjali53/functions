def calculator(number_x,number_y,operation):
    if operation=="add":
        output=number_x+number_y
    elif operation=="subtracts":
        output=number_x-number_y
    elif operation=="multiply":
        output=number_x*number_y
    else:
        output=number_x/number_y
    return output
print(calculator(20,25,"add"))
print(calculator(40,3,"subtracts"))
print(calculator(10,4,"multiply"))
print(calculator(40,30,"devide"))


def calculator(number_x,number_y,operation):
    if operation=="add":
        add_result=number_x+number_y
        print(add_result)
    elif operation=="subtracts":
        subtract_result=number_x-number_y
        print(subtract_result)
    elif operation =="multiply":
        multiply_result=number_x*number_y
        print(multiply_result)
    elif operation =="divide":
        divide_result=number_x/number_y
        print(divide_result)
x=int(input("Enter first number"))
y=int(input("Enter second number"))
calculator(x,y,"add")
calculator(x,y,"subtracts")
calculator(x,y,"multiply")
calculator(x,y,"divide")


def list_change(List1,List2):
    i=0
    while i<len(List1):
        print(List1[i]*List2[i])
        i+=1
multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5]) 


def eligible_for_vote():
    if age>=18:
        print("you are eligible")
    else:
        print("Not eligible")
age=int(input("enter age="))
eligible_for_vote()


def showNumbers(limit):
    i=0
    while i<=limit:
        if i%2==0:
            print(i,"even")
        if i%2!=0:
            print(i,"odd")
        i+=1
showNumbers(5)




def sum_of_multiples(limit):
    Sum=0
    i=0
    while i<=limit:
        if i%3==0:
            Sum+=i
        if i%5==0:
            Sum+=i
        i+=1
    print(Sum)
sum_of_multiples(10)