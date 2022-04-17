def main():
    num=int(input("Enter a positive number: "))
    while num<=0:
        print("The number is negative")
        num=int(input("Enter a positive number: "))
    
    factors=prime_factors(num)
    print("The prime factors of %d is are:"%num,end="")
    print(factors)


   
def prime_factors(num):
    """This function will return the prime factors of a given number"""

    div=2
    facotos=[]

    while div <= num:
        if num % div ==0:
            facotos.append(div)
            num=num/div
        else:
            div +=1
    return facotos
  



main()