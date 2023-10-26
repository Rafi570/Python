def prime_factor(n):
    i=2
    while n>1:
        if n%i==0:
            print(i,end=" ")
            n=n//i
        else:
            i+=1
num=int(input())
prime_factor(num)
