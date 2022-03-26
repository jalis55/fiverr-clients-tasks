def main():
    """The program will find the name rank from text file"""

    try:
        name=input('Enter name to search:')
        in_file1=open('boys_names2000s.txt','r')
        in_file2=open('girls_names2000s.txt','r')


        boys_name_line=in_file1.readline()
        girls_name_line=in_file2.readline()

        boys_name_found=False
        girls_name_found=False

        boys_name_counter=0
        girls_name_counter=0

        while boys_name_line !='' and boys_name_found !=True:
            if name==boys_name_line.rstrip('\n'):
                boys_name_found=True
            boys_name_line=in_file1.readline()
            boys_name_counter +=1
        in_file1.close()
        while girls_name_line !='' and girls_name_found !=True:
            if name==girls_name_line.rstrip('\n'):
                girls_name_found=True
            girls_name_line=in_file2.readline()
            girls_name_counter +=1
        in_file2.close()
        if boys_name_found ==False:
            print("%s did not appear in the list of boys' names."%name)
        else:
            print("%s was #%i for boys' names."%(name,boys_name_counter))
        if girls_name_found ==False:
            print("%s did not appear in the list of girls' names."%name)
        else:
            print("%s was #%i for girls' names."%(name,girls_name_counter))




    except:
        print("File not found or can not be read")

main()