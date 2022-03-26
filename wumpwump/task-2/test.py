""" problem 2"""
# file=open('file2.txt','r').readlines()
# sum=0
# for i in range(80,151):
#     print(i)
#     print(file.count(str(i)+'\n'))
#     sum +=file.count(str(i)+'\n')
# print(sum)
"""end of problem 2"""

"""Test problem 4"""

lst=[1,4,9]
sign=1
sum=0
for i in range(len(lst)):
    sum =sum+(i*sign)
    print(sum)
    print(sign)
    sign *=-1

print(sum)


"""end test problem 4"""

