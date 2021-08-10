# def Max(a,b,c):
#     if a>b and a>c:
#         print(a)
#     elif b>a and b>c:
#         print(b)
#     else:
#         print(c)
# Max(20,68,53)


# def Sum(List):
#     i=0
#     Sum=0
#     while i<len(List):
#         Sum+=List[i]
#         i+=1
#     return Sum 
# List=[8, 2, 3, 0, 7]
# a=Sum(List)
# print(a)


# def multiply(List):
#     i=0
#     mul=1
#     while i<len(List):
#         mul*=List[i]
#         i+=1
#     return mul
# List=[8, 2, 3, -1, 7]
# M=multiply(List)
# print(M)


# def str_reverse(Str):
#     rev=''
#     i=0
#     while i<len(Str):
#         rev+=Str[i-1]
#         i-=1
#     return rev
# ver=str_reverse("1234abcd")
# print(ver)


# def factorial(num):
#     Fact=1
#     i=1
#     while i<num:
#         Fact*=i
#         i+=1
#     return Fact
# f=factorial(5)
# print(f)


# def Range(num):
#     if num in range(1,10):
#         print("yes, it is in range ",num)
#     else:
#         print("no, it is not there")
# Range(4)

# def str_cal(word):
#     U=0
#     L=0
#     for ch in word:
#         if ch.isupper():
#             U+=1
#         if ch.islower():
#             L+=1
#     print("no of upper case",U)
#     print("no of lower case",L)
# str_cal('The quick Brow Fox')

# def unique_list(List):
#     i=0
#     blank_list=[]
#     while i<len(List):
#         if List[i] not in blank_list:
#             blank_list.append(List[i])
#         i+=1
#     print(blank_list)
# List=[1,2,3,3,3,3,4,5]
# unique_list(List)


# def even_odd(List):
#     i=0
#     while i<len(List):
#         if List[i]%2==0:
#             print("even",List[i])
#         i+=1
# List=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_odd(List)


# def perfect(num):
#     i=1
#     Sum=0
#     while i<num:
#         if num%i==0:
#             Sum+=i
#         i+=1
#     if Sum==num:
#         print("it is a perfact number",num)
#     else:
#         print("it is not")
# N=int(input("enter any number"))
# print(perfect(N))


# def palindrome(Str):
#     org=Str
#     rev=''
#     i=0 
#     j=0
#     while j<len(Str):
#         rev+=Str[i-1]
#         i-=1
#         j+=1
#     if rev==org:
#         print("palindrome")
#     else:
#         print("not palindrome")
# string=input("enter any name:-")
# palindrome(string)


# i=1
# while i<=5:
#     print(str(i)*i)
#     i+=1


# def SortThe_sring():
#     items=[n for n in input().split('-')]
#     items.sort()
#     print('-'.join(items))
# SortThe_sring()

# def makeList():
#     L=list()
#     for s in range(1,30):
#         L.append(s**2)
#     print(L)
# makeList()

# def pangram(Str):
#     Alpha = "abcdefghijklmnopqrstuvwxyz"
#     for char in Alpha:
#         if char not in Str:
#             return False
#     return True
# # if string==True:
# #     print("No")
# # else:
# #     print("Yes")
# string = 'the quick brown fox  over the lazy dog'
# # print(pangram(string))
# if(pangram(string) == True):
#     print("Yes")
# else:
#     print("No")


# def break_into_words(sentence):
#     List=[]
#     c=0
#     while c<len(sentence):
#         List.append(sentence[c])
#         c+=1
#     print(List)
# sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system" 
# new=sentence.split()
# break_into_words(new)