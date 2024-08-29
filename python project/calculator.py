def add(x,y):
    return x+y
    
def substract(x,y):
    return x-y

def multiply(x,y):
 return x*y

def divied(x,y):
 return x/y


def calculator():
    operation ={
    "+"  : add,
    "-"  : substract,
    "*"  : multiply,
    "/"  : divied,
}
    num1 = int(input("enter first number"))
    for i in operation:
    print(i)    
        