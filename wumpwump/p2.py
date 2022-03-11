
def largest_factor(num):

    factor_lst=[]

    for i in range(1,num):
        if num%i==0:
            factor_lst.append(i)
        
    return factor_lst[-1]



print(largest_factor(12))