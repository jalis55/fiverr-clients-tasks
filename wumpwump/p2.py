
def largest_factor(num):

    for i in range(num-1,0,-1):
        if num%i==0:
            return i
        
print(largest_factor(125))