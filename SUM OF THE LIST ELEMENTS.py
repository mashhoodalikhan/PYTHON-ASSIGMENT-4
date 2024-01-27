a=[]
size=int(input("HOW MANY ELEMENTS YOU WANT TO ENTER5?:"))
for i in range(size):
    val=int(input("ENTER NUMBER:"))
    a.append(val)
sum=0
for i in range(size):
        sum=sum+a[i]
print("SUM OF THE LIST ELEMENTS=",sum)