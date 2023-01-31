"""
Calculator library containing basic math operations.
"""

def add(first_term, second_term):
    return first_term + second_term

def subtract(first_term, second_term):
    return first_term - second_term

if __name__ == '__main__':
    rc = 1
    try:
        print("addition method")
        print(add(2,3))
        rc = 0
    except Exception as e:
        print('Error: %s' % e, file=sys.stderr)
    


