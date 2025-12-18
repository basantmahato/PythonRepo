file = open("demo.txt", "a")

file.write("Appending new content.\n")
file.write("This is an additional line.\n")
print("Content appended successfully")
file.close()