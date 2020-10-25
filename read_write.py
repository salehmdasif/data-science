with open("data-resource/data.txt", "r") as file:
    print(file.name, file.mode)
    # File can be read inside the indent
    fileContent = file.read()
    # We can print file content inside the indent
    print(fileContent)

    fileLines = file.readlines()
    print(fileLines)

    # Inside the indent file is not closed
    print(file.closed)

# We can also check if the file is close or not, outside the indent
print(file.closed)
# We can also print file content outside the indent
print(fileContent)

with open("data-resource/data2.txt", "w") as file2:
    file2.write("This is a new line A\n")
    file2.write("This is a new line B\n")
    file2.write("This is a new line C\n")
    file2.write("This is a new line D\n")
    file2.write("This is a new line E\n")

with open("data-resource/data2.txt", "r") as file2:
    fileContent = file2.read()
    print(fileContent)

lines = ["Hello!\n", "This is line written with for loop\n", "This is a real fun.\n"]
with open("data-resource/data3.txt", "w") as file3:
    for line in lines:
        file3.write(line)

with open("data-resource/data3.txt", "r") as file3:
    fileContent = file3.read()
    print(fileContent)


newLines = ["Hello!\n", "This is a new line\n", "This is for testing.\n"]
with open("data-resource/data.txt", "r") as readfile:
    with open("data-resource/data4.txt", "w") as writefile:
        for line in newLines:
            writefile.write(line)

with open("data-resource/data4.txt", "r") as writefile:
    fileContent = writefile.read()
    print(fileContent)


with open('data-resource/data4.txt', 'a') as testWriteFile:
    testWriteFile.write("This is line C\n")

with open("data-resource/data4.txt", "r") as writefile:
    fileContent = writefile.read()
    print(fileContent)