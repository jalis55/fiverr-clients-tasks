def main():
    """ This program will compute ield goal statistics"""

    try:
        file=open('field_goals.txt','r')
        min=int(file.readline())
        max=int(file.readline())
        counter,sum=0,0
        for line in file:
            line=int(line)
            if min>line:
                min=line
            if max<line:
                max=line
            sum +=line
            counter +=1
        avg=sum/counter
        print("Maximum distance is:%i yards"%max)
        print("Minimum distance is:%i yards"%min)
        print("Average distance is %.2f yards"%avg)


    except FileNotFoundError:
        print("Wrong file name or path")
main()