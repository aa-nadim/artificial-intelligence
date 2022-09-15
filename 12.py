#Calculating sum of the series 4+8+12+....n

n=int(input("Enter the last number :"))
print("Getting the required series: ")
sum=0
for x in range(4,n+1,4):
   sum=sum+x
   print(x,end=', ')
print("\nsum of the series:",sum)