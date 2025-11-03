name= input("hello welcome to age classification app what is you name: ")
age=int(input(f"welcome {name} i hope you are doing well please fill your age: "))

def classify_person(age):
 if age<12:
    print(f"{name} you are a very cute child")
 elif 13<age<17:
    print(f"{name} you are a teenager")
 elif 18<age<64:
    print(f"{name} you are an adult")
 else:
    print(f"{name} you are a seniro or old adult")
    
classify_person(age)
   