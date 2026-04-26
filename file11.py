# Writing to a file (creates file if not exists)
file = open("sample.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("File handling in Python.\n")
file.close()


# Reading the file
file = open("sample.txt", "r")
content = file.read()
print("File Content after writing:\n", content)
file.close()


# Appending data to the file
file = open("sample.txt", "a")
file.write("This line is added later.\n")
file.close()


# Reading again after appending
file = open("sample.txt", "r")
content = file.read()
print("File Content after appending:\n", content)
file.close()