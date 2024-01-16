def summ(a, b, c):
    sum = a + b + c
    return sum

def mult(a, b, c):
    multiplication = a * b *c
    return multiplication

def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
def div(a, b):
    return a / b

def read():
    return str(input('Enter whatever string'))
    

def read_float(float_number):
    return float(input(float_number))