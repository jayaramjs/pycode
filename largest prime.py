"""Largest prime factor
    Problem 3

    The prime factors of 13195 are 5, 7, 13 and 29."""
    #What is the largest prime factor of the number 600851475143 ?

def prime(n):
    temp=0
    while temp!=1:
        for i in range(2,n+1):
            if n%i==0:
                n=n//i
                l.append(i)
                if n==1:
                    temp=1
                break
b=int(input("enter number"))
l=[]
prime(b)
print(l)
for i in range(len(l)):
    max=l[i]
    if i+1<len(l):
        if l[i+1]>max:
            max=l[i+1]
print(max)


        
