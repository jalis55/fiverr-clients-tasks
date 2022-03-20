def main():

    """This function will find states and it's population and capital"""

    try:
        myfile = open("states.txt", "r")
        print('This program reads state records from "states.txt".')
        print("Given a state name, I will tell you the population and capital.")
        search_state=input("Enter a state name: ")
        line = myfile.readline()
        capital=None
        population=None
        found=False

        while line !='' and not found:
            line=line.rstrip('\n')
            if search_state==line:
                found=True
                line=myfile.readline().rstrip('\n')
                capital=line
                line=myfile.readline().rstrip('\n')
                population=int(line)
            else:
                for i in range(3):
                    line=myfile.readline()
        myfile.close()
        if found==True:
            print("The population for %s is %i and the capital is %s."%(search_state,population,capital))
        else:
            print("%s was not in the file."%search_state)
          
    except FileNotFoundError:
        print("File not found")


main()
