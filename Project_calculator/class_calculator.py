'''
This module is a blueprint / class that models a simple calculator

Methods:
    add_ : adds all arguments passed
    diff_: finds the difference of all arguments
    div_ : divides the first argument by the second
    multi_:finds the product of all arguments
    aver_ : finds the average of all arguments passed
    exp_ : calculates the exponent of first argument by second argument
    sq_root : calculates square root of argument
'''
class Simple_Calc:
    '''
    Create an instance with no arguments
    '''
    def __init__(self) -> None:
        pass

    def add_(*args):
        '''
        add all arguments

        Attr:
        args: variable number of numbers to add
        '''
        j = 0
        for i in args:
            j += i
        return j

    def diff_(*args):
        '''
        finds the difference of all arguments

        Attr:
        args: variable number of numbers to substract
        '''
        j = args[0]
        for i in args[1:]:
            j -= i
        return j

    def div_(a, b):
        '''
        divides the first argument by the second

        Attr:
        a : 
        b :
        '''
        try:
            j = a / b
            return j
        except ZeroDivisionError:
            print("Can't divide by zero")

    def multi_(*args):
        '''
        finds the product of all arguments

        Attr:
        args: variable number of numbers to multiply
        '''
        j = args[0]
        for i in args[1:]:
            j *= i
        return j

    def aver_(*args):
        '''
        finds the average of all arguments passed

        Attr:
        args: variable number of numbers to find average
        '''
        j = 0
        for i in args:
            j += i
        av = j / len(args)
        return av

    def exp_(a, b):
        '''
        calculate the exponent of first argument by second argument

        Attr:
        a : number to calculate exponent on
        b : the exponent
        '''
        try:
            exp = a ** b
            return exp
        except ZeroDivisionError:
            print("You cant raise 0 to a negative power")

    def sq_root(a):
        '''
        calculate square root of argument

        Attr:
        a : number to find its square root
        '''
        root = a ** 0.5
        return root
