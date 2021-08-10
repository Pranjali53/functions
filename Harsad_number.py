num=42   
rem=sum = 0        
n=num        
while(num>0):    
    rem=num%10    
    sum+=rem    
    num=num//10        
if(n%sum==0):    
    print(n," is a harshad number")    
else:    
    print(n," is not a harshad number")   

x = 42
x_digits = list(str(x)) 
s=0
i=0
while i<len(x_digits):
    s+=int(x_digits[i])
    i+=1
if x%s==0:
    print("harasad")
else:
    print("not harsad")