def main():
    DESIRED_SUM1 = -2
    DESIRED_SUM2 = 1
    DESIRED_SUM3 = -3

    print('This program tests the alternating_sum function.\n')

    list1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    list2 = [5, 2, 8, 6, 3, 7]
    list3 = [1, 2, 3, 4, 5, 6]

    sum1 = alternating_sum(list1)
    sum2 = alternating_sum(list2)
    sum3 = alternating_sum(list3)

    print('The alternating sum of list1 = %d.' \
        % sum1)
    if sum1 == DESIRED_SUM1:
        print('The alternating sum of list1 is correct.')
    else:
        print(('ERROR: The alternating sum of list1 '
            + 'should be %d.') % DESIRED_SUM1)

    print('\nThe alternating sum of list2 = %d.' \
        % sum2)
    if sum2 == DESIRED_SUM2:
        print('The alternating sum of list2 is correct.')
    else:
        print(('ERROR: The alternating sum of list2 '
            + 'should be %d.') % DESIRED_SUM2)

    print('\nThe alternating sum of list3 = %d.' \
        % sum3)
    if sum3 == DESIRED_SUM3:
        print('The alternating sum of list3 is correct.')
    else:
        print(('ERROR: The alternating sum of list3 '
            + 'should be %d.') % DESIRED_SUM3)


def alternating_sum(lst):
    """This function compute the alternet sum of a list"""
    sign=1
    sum=0

    for i in range(len(lst)):
        sum +=lst[i]*sign
        sign *=-1
        
    return sum


main()
