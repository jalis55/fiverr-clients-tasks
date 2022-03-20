
def main():
    

    """This program will calculate the the winning teams for the World Series from 1903 to 2021"""
    
    

    try:
        file=open('world_serise.txt','r')

        print('\t\t*** WORLD SERIES WINNERS ***')
        print("Given the name of a team (e.g., Texas Rangers or New York Yankees),")
        print("this program will determine how many times that team won the")
        print("World Series in 1903-2021.\n")

        team_name = input('Enter the name of the team: ')
        counter=0
        for line in file:
            line=line.rstrip()
            if team_name in line:
                counter +=1

        if counter ==0:
            print("%s never won the World Series."%team_name)
        else:
            print("%s won the World Series %i time."%(team_name,counter))
        file.close()            

    except FileNotFoundError:
        print('Wrong file name or path')

main()