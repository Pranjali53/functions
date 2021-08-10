Password =input("enter any password:")
Alphabet_C, Alphabet_S, Spacial_C, Digits = 0, 0, 0, 0
if (len(Password) >= 8): 
    for i in Password:  
        if (i.islower()): 
            Alphabet_S+=1            
        if (i.isupper()): 
            Alphabet_C+=1             
        if (i.isdigit()): 
            Digits+=1         
        if(i=='@'or i=='$' or i=='_'): 
            Spacial_C+=1           
if (Alphabet_C>=1 and Alphabet_S>=1 and Spacial_C>=1 and Digits>=1 and Alphabet_C+Alphabet_S+Spacial_C+Digits==len(Password)): 
    print("Valid Password") 
else: 
    print("Invalid Password") 