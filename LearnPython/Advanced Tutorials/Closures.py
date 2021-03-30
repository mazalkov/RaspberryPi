# https://www.learnpython.org/en/Closures


# your code goes here
def multiplier_of(multiplier):
    
    def evaluator(input_number):
        print(multiplier * input_number)
    return evaluator

multiplywith5 = multiplier_of(5)
multiplywith5(9)
