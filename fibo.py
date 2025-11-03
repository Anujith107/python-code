def calc():
    
    a=5
    b=7
    return a,b
def add():
    return a+b
def sub():
    return a-b
while True:
    print("pess 1 for add ,2 for subtract,3 for stop")
    x=int(input())
    if x==1:
        a,b=calc()
        print(add())
    elif x==2:
        a,b=calc()
        print(sub())
    elif x==3:
        break
    else:
        print('')
calc()
        
        
