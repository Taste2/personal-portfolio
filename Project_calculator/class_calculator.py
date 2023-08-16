'''
This class models a simple calculator

Methods:
    add_ : adds all arguments passed
    diff_: finds the difference of all arguments
    div_ : divides the first argument by the second
    multi_:finds the product of all arguments
    aver_ : finds the average of all arguments passed
'''
class Simple_Calc():
    '''
    Create an instance with no arguments
    '''
    def __init__(self) -> None:
        pass

    def add_(self, *args):
        '''
        add all arguments
        '''
        j = 0
        for i in args:
            j += i
        print("The sum of {} is: {}".format(args, j))

    def diff_(*args):
        '''
        finds the difference of all arguments
        '''
        j = args[0]
        for i in args[1:]:
            j -= i
        print("The difference of {} is: {}".format(args, j))

    def div_(a, b):
        '''
        divides the first argument by the second
        '''
        try:
            j = a / b
            print("{} / {} = {}".format(a, b, j))
        except ZeroDivisionError:
            print("Can't divide by zero")

    def multi_(*args):
        '''
        finds the product of all arguments
        '''
        j = args[0]
        for i in args[1:]:
            j *= i
        print("The product of {} is: {}".format(args, j))

    def aver_(*args):
        '''
        finds the average of all arguments passed
        '''
        j = 0
        for i in args:
            j += i
        av = j / len(args)
        print("Average of {} = {}".format(args, av))