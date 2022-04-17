print('---------- Ideal Mechanical Advantage Calculator----------')
print()
def ideal_mechanical_advantage ( length,height):
     return round(length/height,2)
#driver code
length = float(input('enter length in meters \n'))
height = float(input('enter height in meters \n'))
print()
print('the ideal mechanical advantage is ', ideal_mechanical_advantage (length, height))
# end of program
