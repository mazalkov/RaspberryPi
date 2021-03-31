# https://www.learnpython.org/en/Decorators


def type_check(correct_type):
    #put code here
    def checker(old_function):
        def new_function(argument):
            if (isinstance(argument, correct_type)):
                return old_function(argument)
            else:
                print("Bad Type")
        return new_function
    return checker

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])
