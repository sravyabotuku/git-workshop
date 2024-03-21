# Custom python functions

"""
The function double_number adds the given number to itself.
It takes an integer value as an argument.
"""
def double_number(a):
    print(f'value before double_number(): {a}')
    print(f'value after double_number(): {a+a}')
    return a+a

"""
The function square_number multiplies the given number to itself.
It takes an integer value as an argument.
"""

def square_number(a):
    print(f'value before square_number(): {a}')
    print(f'value after square_number(): {a*a}')
    return a*a
