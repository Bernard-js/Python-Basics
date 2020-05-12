file = open("employees.txt", "r")
file2 = open("employees.txt", "r")
file3 = open("employees.txt", "r")
file4 = open("employees.txt", "r")
file5 = open("employees.txt", "r")


print(file.readable())

#Use this command to read all the file
print(file.read())

#read the first line of the file
print(file2.readline())
print(file2.readline())

#read each line of the file as an element of a list
print(file3.readlines())
print(file4.readlines()[2])

# print each employee individually using for loops
for employee in file5.readlines():
    print(employee)

file.close()