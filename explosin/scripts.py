#importing modules 
import os
import shutil

#define location
path=os.path.dirname(__file__)

#remove function
def remove_directory(dir_name):
    #check directory exits or not
    if dir_name in os.listdir(path):
        try:
            #remove directory
            shutil.rmtree(os.path.join(path,dir_name))
            return f"Directory {dir_name} has removed" #if operation successful
        except OSError as error:
            return error #if operation unsuccessful
    else:
        return f"Error Directory {dir_name} does not exits"
#create function
def create_directory(dir_name):
    try: 
        #create directory

        os.mkdir(os.path.join(path,dir_name))
        return f"New Directory {dir_name} has created" #if operation successful
    except OSError as error: 
        return (error) #if operation unsuccessful
#rename function
def rename_directory(dir_name,new_name):

    if dir_name in os.listdir(path):
        try:
            #check directory exits or not
            source=os.path.join(path,dir_name) #join directory name with path
            destination=os.path.join(path,new_name) #join new directory name with path
            #rename directory
            os.rename(source,destination)
            return f"Directory {dir_name} has renamed to {new_name}" #if operation successful
        except OSError as error:
            return error #if operation unsuccessful
    else:
        return f"Error Directory {dir_name} does not exits"



def main():
    

    while True:
        print("1.Rename Directory")
        print("2.Create New Directory")
        print("3.Delete a Directory")
        print("Press 'Q' to quit")
        choice=input("Enter option:")

        if choice=='1':
            dir_name=input("Enter Directory name to rename:")
            new_name=input("Enter new name:")
            #calling rename function
            print(rename_directory(dir_name,new_name))
            continue
        elif choice=='2':
            dir_name=input("Enter Directory name to create:")
            #calling create function
            print(create_directory(dir_name))
            continue
        elif choice=='3':
            dir_name=input("Enter Directory name to delete:")
            #calling remove function
            print(remove_directory(dir_name))
            continue
        elif choice=='Q':
            break #stop the infinite loop
        else:
            #if user input is wrong 
            print("Invalid input")

#calling main function
main()

# Testing

def testing():


    
    print("Testing create directory function")

    print("Expected result:New Directory khabib has created")
    print(f"Result:{create_directory('khabib')}")
    print("==================================")
    print("Testing Rename Directory function")

    print("Expected result:Directory khabib has renamed to khabib55")
    print(f"Result:{rename_directory('khabib','khabib55')}")
    print("==================================")
    print("Testing Remove Directory function")

    print("Expected result:Directory khabib55 has removed")
    print(f"Result:{remove_directory('khabib55')}")

#calling test function
# testing()


   



