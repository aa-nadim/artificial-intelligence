sum=0
n=int(input('enter the value: '))
j=1
for i in range(n):
    sum = sum+(1/j)
    print('1/'+str(j),end=', ')
    j=j+1
print("\nSum=",sum)
