import sys

'''In this function below I determined to print 
not only the second argument but every next argument. 
So, if your name is Princess Consuela Bananahammock and
you would like the program to greet you in this way, 
there's no problem.If I don't use this variable and 
directly want to make string from sys.argv[1:] 
that makes a "Can't convert list object to str implicitly error,
but this way it works correctly. It seems a bit illogic, 
but Im not a professinal( yet!).''' 

def hello_world():
    if len(sys.argv) != 1:
        except_first = sys.argv[1:] 
        print("Hello",*except_first,"!") # I used * because I didn't want it to display the []s
    else:
        print("Hello World!")

hello_world()


