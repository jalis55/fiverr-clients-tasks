import sys

NUM_LETTERS = 26

def main():
    if len(sys.argv) != 2:
        print('Usage: python frequency.py filename')
        sys.exit(1)

    filename = sys.argv[1]
    print('This program will evaluate the text in the file %s.' \
        % filename)

    counts = NUM_LETTERS * [0]
    total_letters = 0

    try:
        in_file = open(filename, 'r')

        # PUT YOUR CODE HERE

        in_file.close()

        print('\nThe file contained %d letters.\n' % total_letters)

        base = ord('A')
        print('Letter   Count   Percentage')
        for i in range(NUM_LETTERS):
            percentage = counts[i] / total_letters * 100
            print('  %s       %3d      %4.1f%%' \
                % (chr(base + i), counts[i], percentage))

    except IOError:
        print('\nCould not open or read %s.' % filename)

main()
