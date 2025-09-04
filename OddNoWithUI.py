x=int(input("Enter the rage of odd numbers: "))
num = 0
while num < x:
 
 num += 1
 if num % 2 == 0:
   continue
 print(num)