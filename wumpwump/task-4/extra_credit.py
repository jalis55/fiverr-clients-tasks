def main():
    print('This program tests the acronym function.\n')

    string1 = 'Central Intelligence Agency'
    answer1 = 'CIA'
    print('The acronym for %s should be %s.' % (string1, answer1))

    acronym1 = acronym(string1)
    if acronym1 == answer1:
        print('Correct: The acronym is %s' % answer1)
    else:
        print('ERROR: The acronym is %s instead of %s' \
            % (acronym1, answer1))

    string2 = 'random access memory'
    answer2 = 'RAM'
    print('\nThe acronym for %s should be %s.' % (string2, answer2))

    acronym2 = acronym(string2)
    if acronym2 == answer2:
        print('Correct: The acronym is %s' % answer2)
    else:
        print('ERROR: The acronym is %s instead of %s' \
            % (acronym2, answer2))


def acronym(string):
    acronym=''
    string_list=string.upper().split()
    for s in string_list:
        acronym +=s[0]
    return acronym

main()