
#defining variables, this is having the computer commit a value to memory
#numbers are integers, words or letters are strings
#decimals are floats
#true are false are referred to as booleans
price = 10
price = 20
price = price * 4
#name = 'Josh'
is_true = True

#print(price)
#print(name)
#print(is_true)

class Patient:
    def __init__(patientObject,name,age,new_patient):
        patientObject.name = name
        patientObject.age = age
        patientObject.new_patient = new_patient

    def hello_patient(patient):
        if patient.new_patient:
            print("Hello, my name is "+ patient.name +", I am "+ str(patient.age) +" years old and I am a new patient")
        else:
            print("Hello, my name is "+ patient.name +", I am "+ str(patient.age) +" years old and I am not a new patient")

p_1 = Patient("Joshua", 31, True)
p_2 = Patient("Lindsay", 29, False)



#p_1.hello_patient()
#p_2.hello_patient()

def check_in():
    name = input("What is your name?")
    age = input("What is your age?")
    new = {"yes":True,"no":False}[input("Are your a new Patient? (Yes/No)").lower()]

    new_p = Patient(name, age, new)

    new_p.hello_patient()

check_in()

