def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
while True:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=input("enter operator")
    if(c=="+"):
        print(add(a,b))
    elif(c=="-"):
        print(sub(a,b))
    elif(c=="*"):
        print(mul(a,b))
    elif(c=="/"):
        print(div(a,b))
    elif(c=="%"):
        print(mod(a,b))
    else:
        print("invalid")
    break