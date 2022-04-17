"""Counting characters from list of names"""

name_list = ['Picasso', 'Monet', 'Da Vinci', 'Rembrandt']
character=0

#solution-1
for i in range(len(name_list)):
    character +=len(name_list[i])

#solutin 2
# for name in name_list:
#     character +=len(name)


print("There are %i characters in the list."%character)