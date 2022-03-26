
def main():
    """This program will find the maximum value in a file"""

    print('Given a file name, this program will')
    print('find the maximum value in the file.\n')

    filename = input('Enter the file name: ')

    # Need some code here
    try:
        in_file=open(filename,'r')

        max = float(in_file.readline())
        for line in in_file:
            line=float(line)
            if line > max:
                max=line

        print('\nThe maximum value is %.2f.' % max)

    # Need some code here
    except FileNotFoundError:
        print('Wrong file name or path')

main()