# rows = 5
# for i in range(rows):
#     for j in range(i+1):
#         print("*", end = " ")
#     print()

"""
All you need to practice are these 5 lines:

for j in range(rows + 1):

print("* " * j)
print("  " * (rows - j) + "* " * j)
print(" " * (rows - j) + "* " * j)

for j in range(rows, 0, -1):

print(" ".join(str(i) for i in range(1,j+1)))                   this is  [1,2,3]
print(" ".join(chr(i+64) for i in range(1,j+1)))                this is  [A,B,C]
print(" ".join(str(letters_in_string[i]) for i in range(j)))    this is ['p','y','t','h','o','n']

pascal's traingle :- Still pending
floyd's triangle :- Still pending
"""

rows = 5
for j in range(rows + 1):
    print("* " * j)

rows = 5
for j in range(1, rows + 1):
    print("  " * (rows - j) + "* " * j)

rows = 5
for j in range(1, rows + 1):
    print(" " * (rows - j) + "* " * j)

print()
print()

rows = 5
for j in range(rows, 0, -1):
    print("* " * j)

rows = 5
for j in range(rows, 0, -1):
    print(" " * (rows - j) + "* " * j)

rows = 5
for j in range(rows, 0, -1):
    print("  " * (rows - j) + "* " * j)


rows = 5
for j in range(rows+1):
    print(" ".join(str(i) for i in range(1,j+1)))

rows = 5
asci = 64
for j in range(rows+1):
    print(" ".join(chr(i+asci) for i in range(1,j+1)))


check_string = "python"
letters_in_string = [str(individual_char) for individual_char in check_string]
rows = len(letters_in_string)
for j in range(rows+1):
    print(" ".join(str(letters_in_string[i]) for i in range(j)))

print()
print()
#https://www.trytoprogram.com/cpp-examples/pascals-floyds-triangle/
#Floyd's Triangle
print("Floyd's Triangle")
rows = 4
start = 1
for j in range(1, rows + 1):
    print(" ".join(str(i) for i in range(start, start + j)))
    start += j

#Pascals triangle
print()
print("Pascal's Triangle")
rows = 4
for j in range(rows+1):
   print(" " * (rows-j) +
         ' '.join(map(str, str(11**j))))