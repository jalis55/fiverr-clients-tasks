import dice

def main():
    die1=dice.Die()
    die2=dice.Die()

    MATCHING_SUM=[2,3,12]

    count=0
    number_of_rolls=1000
    for i in range(number_of_rolls):
        sum=die1.roll() + die2.roll()

        if sum in MATCHING_SUM:
            count +=1

    print("Total number of rolls %i and 2,3,12 occured %i times"%(number_of_rolls,count))




main()