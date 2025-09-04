file = open("hello.txt","r")
z=0
y=0
x=file.read()

for i in x:
    if i in "he":
        z=z+1
        print(i)
print("no of vowels",z)

for i in x:
    if i in "she":
        y=y+1
        print(i)
print("no of vowels",z)
   
file.close()        