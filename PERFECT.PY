def perfect():
    j=1
    while j<=1000:   
        s=0
        i=1
        while i<j:
            if j%i==0:
                s+=i
            i+=1
        if s==j:
            print(j,"perfect")
        
        j=j+1


def perfect():
    s=0
    i=1
    while i<n:
        if n%i==0:
            s+=i
        i+=1
    if s==n:
        print("perfect")
    else:
        print("not perfect")
n=int(input("enter any number"))
perfect()