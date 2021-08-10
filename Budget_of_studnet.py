N_O_student=int(input("Number of students:-"))
Expenses=int(input("Ek student ka kharcha:-"))
Expenses_O_OneStudent=Expenses//N_O_student
if Expenses_O_OneStudent<=50000:
    print("Hum budget ke andar hain")
else:
    print("Hum budget ke bahar hain")
    