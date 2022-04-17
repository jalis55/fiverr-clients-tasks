import sys
def main():
    # print(sys.argv[1])
    """This program reads multiple values per line and calculate the average"""
    file_name=sys.argv[1]
    print("This program computes the average of the values in %s."%file_name)
    sum=0
    counter=0
    try:
        in_file=open(file_name,'r')
        files=in_file.readlines()


        for file in files:
            file=file.rstrip('\n')
            nums=file.split(" ")
            for num in nums:
                sum +=float(num)
                counter +=1
        avg=sum/counter
        print("The average of the %d values was %.1f."%(counter,avg))
        in_file.close()

    except IOError:
        print("Unable to open the file")

    except ValueError:
        print('Error in converting item to a number.')
        




main()