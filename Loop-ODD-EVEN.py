n=int(input("Enter the number of range upto"))
count=1
odd=even=0
while count<=n:
    if count%2==0:
        even+=count
       

    else:
        odd+=count

    count+=1

        

        

print("sum of even no:",even)
print("sum of odd no:",odd)
