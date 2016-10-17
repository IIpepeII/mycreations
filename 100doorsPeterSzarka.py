
def hundreddoors(num): 

#This is the list of the doors in their initial state

    List=["closed"]*num 

    '''In the next loop I defined x on a range of the elemnets for check, and
    in the next (sub)loop I determined z(as an element of List) on a range of x to num
    (when I will use this function num will be the number of the repetiton), step by x too. 
    This process will go through every element of List and check their statement.'''

    for x in range(0,num):
        for z in range(x,num,x+1):
            if List[z]=="closed":
                List[z]="open"
            else:
                List[z]="closed"

    a=[] # a is the list where I collect the good solutions

    for y in range(0,num):
        if List[y]=="open":
            a.append(y+1) #this row fill list a with the good elements 
    print("Opened doors:",end=" ") 
    print(*a , sep=",")  

hundreddoors(100) #The name of 100doors is just a name. You can use this function with every number what you want. 
