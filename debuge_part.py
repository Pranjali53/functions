def employee(name,salary=20000):
        print(name,"your salary is:-",salary)
employee("kartik",30000)
employee("deepak") 


def greet(*names):
    for name in names:
               print("Hello", name)
greet("sonu", "kartik", "umesh", "bijender")
 

def sumofdigits(number):
    sum = 0
    modulus = 0
    while number!=0 :
        modulus = number%10
        sum+=modulus
        number/=10
    return sum
print(sumofdigits(123))


def calculate_sum(a,b):
    sum = a+b
    print(sum)
calculate_sum(4,5)


def multi(a,b):
    multiply=a*b
    return multiply
print(multi(3,4)) 


def Avg(number1,number2,number3):
    avg=number1+number2+number3/3
    print(avg)
Avg(1,3,2)


def voter(age):
    if age < 18:
        print("eligible")
    else:
        print("not eligible")
voter(20)


def distance(kms):
    if kms < 20:
        print("close")
    elif kms < 50:
        print("mediam")
    else:
            Print(far)
distance(20) 

def numbers_less_than_twenty(list):
  counter = 0
  while counter < len(list):
    item = list[counter]
    if item > 20:
      list.remove(item)
    else:
      counter += 1
  return list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
main_list=[12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
num_list_sub_20 = numbers_less_than_twenty(num_list)
print (main_list)
print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20) 

