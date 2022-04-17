import dice

def main():
    die1=dice.Die()
    die2=dice.Die()

    final_score=0

    while(1):
        die1_rolled_value=die1.roll()
        die2_rolled_value=die2.roll()

        if die1_rolled_value == die2_rolled_value:
            print("You rolled %d and %d. END OF GAME"%(die2_rolled_value,die2_rolled_value))
            break
        else:

            final_score +=die1_rolled_value + die2_rolled_value
            print("You rolled %d and %d. Score=%d"%(die1_rolled_value,die2_rolled_value,final_score))

    print("Your final score was %d."%final_score)


main()