import numpy as np

# In Python list we can store any types of data.
# Javascript array = Python list
# But in Python An array contains only same data types.
# Arrays are not like list because lists contains different data types.

"""
a = np.array(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
c = np.array([1, "B", 3, "D", 5, "F", 7, "H", 9, "J"])
print(a)
print(b)
print(c)
print("-------------------------")
"""

myData = np.arange(1, 21)
print("myData is:")
print(myData)
print("-------------------------")

# Default Array Shape in Python First Fill Row Then Fill Column
# myArray = np.reshape(myData, (4, 5))
myArray = myData.reshape(4, 5)
# Array Shape in Python First Fill Row Then Fill Column using -> order = "C" that is same as the default one
# myArray1 = np.reshape(myData, (4, 5), order="C")
myArray1 = myData.reshape((4, 5), order="C")
# Array Shape in Python First Fill Column Then Fill Row using -> order = "F" that will change the  default one
# myArray2 = np.reshape(myData, (4, 5), order="F")
myArray2 = myData.reshape((4, 5), order="F")

print("myArray in default format is: (First Fill Row Then Fill Column)")
print(myArray)
print("-------------------------")
# Access items in matrix using index [row, column] or [row][column]
print(myArray[2][1])
print(myArray[2, 1])
print("-------------------------")
print("myArray[1] is:")
print(myArray[1])
print("-------------------------")
print("myArray[0:2] is:")
print(myArray[0:2])
print("-------------------------")
print("myArray[2:] is:")
print(myArray[2:])
print("-------------------------")
print("myArray[:2] is:")
print(myArray[:2])
print("-------------------------")
print("myArray1 in order='C' same as like default format is: (First Fill Row Then Fill Column) ")
print(myArray1)
print("-------------------------")
print("myArray2 in order='F' is: (First Fill Column Then Fill Row)")
print(myArray2)
print("-------------------------")
print("-------------------------")

# ----------------------------------------------------------
# List in list to array
r1 = ["I", "am", "happy"]
r2 = ["How", "are", "you?"]
r3 = [1, 2, 3]

all_r = [r1, r2, r3]
print(all_r)
print("-------------------------")

np_all_r = np.array(all_r)
print(np_all_r)
print("-------------------------")
