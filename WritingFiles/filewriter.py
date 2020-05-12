# this will append all text to the end of the file
file = open("employees.txt", "a")

# using the "w" parameter will overwrite an existing file or create a new one
file2 = open("employees2.txt", "w")

file.write("Toby -> human recources")

file.write("\nKelly -> customer service")

file2.write("David -> manager")

file.close()