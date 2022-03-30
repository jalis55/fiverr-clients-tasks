def main():
    """This program will read data which is equal or higher of a specific value"""


    SCORES=30000

    try:
        print("This program displays information from the Hogwarts")
        print("video game tournament. All players with a score of")
        print("30000 or higher are listed below.\n")
        file=open('scores.txt','r')
        line=file.readline()

        while line !='':
            player=line.rstrip('\n')
            line=file.readline()
            score=int(line.rstrip('\n'))

            if score >=SCORES:
                print("%-20s %s "%(player,score))
            line=file.readline()
        
        file.close()
    except:
        print("File not found or can not be read")
main()