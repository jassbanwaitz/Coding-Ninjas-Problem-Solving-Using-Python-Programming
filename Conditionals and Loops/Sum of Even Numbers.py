## Read input as specified in the question.
n=int(input())
sum=0
for i in range(n,0,-1):
    if(i%2==0):
        sum=sum+i
print(sum)
