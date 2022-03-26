
def largest_factor(num):
    """ This function will compute the largest factor a number which is less than the number"""
    if num <=0:
        raise ValueError
    for i in range(num-1,0,-1):
        if num%i==0:
            return i
        
def main():
    print('This program demonstrates the largest_factor '  + 'function.\n')

    print('The largest factor of 125 is %d.'  % largest_factor(125))
    print('The largest factor of 27 is %d.' % largest_factor(27))
    print('The largest factor of 12 is %d.'  % largest_factor(12))
    print('The largest factor of 7 is %d.' % largest_factor(7))

    # Checking for invalid value of n
    try:
        largest_factor(0)
    except ValueError as e:
        print('\nlargest_factor threw a ValueError with the message')
        print(e)
main()