def main():
    """This program will count data in a specific range"""
    
    min=int(input("Enter minimum range value:"))
    max=int(input("Enter maximum range value:"))

    while min > max:
        print("Invalid input")
        max=int(input("Enter maximum range value:"))
    
    try:
        file=open('Spurs-19-20.txt','r')
        line=file.readline()
        counter=0
        while line !='':
            line=int(line.rstrip('\n'))
            if min<=line<max+1:
                counter +=1
            line=file.readline()
        print("The Spurs scored between %i and %i points %i times."%(min,max,counter))
    except FileNotFoundError:
        print("File not found or can not be read")

main()



