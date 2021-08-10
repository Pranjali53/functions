def students(*List_of_students_name):
    for name in List_of_students_name:
        print("Hello", name)
students("Monica", "Luke", "Steve", "John")


def add_numbers(a,b):
    print(a+b)
add_numbers(56,12)


def add_numbers_list(a,b):
    i=0
    while i<len(a):
        print(a[i]+b[i])
        i+=1
a=[50, 60, 10] 
b=[10, 20, 13]
add_numbers_list(a,b)


def check_numbers_list(num1,num2):
    i=0
    while i<len(num1):
        if num1[i]%2==0 and num2[i]%2==0:
            print("both are the even number")
        else:
            print("both are not the even number")
        i+=1
num1=[2, 6, 18, 10, 3, 75]
num2=[6, 19, 24, 12, 3, 87]
check_numbers_list(num1,num2)
