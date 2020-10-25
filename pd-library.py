import pandas as pd

filePath = "data-resource/fb.csv"
data = pd.read_csv(filePath)

print(data.head(), "\n")
print(data.tail(), "\n")

a = data[["Date"]]
print(a, "\n")

b = data[["Date", "Volume"]]
print(b, "\n")

print(data.describe(), "\n")

# There are three ways to select data from a data frame in Pandas: loc, iloc, and ix.
# ===================================================================================

# ---------------------------------------- #1 ---------------------------------------
# loc is primarily label based; when two arguments are used,
# you use column headers and row indexes to select the data you want.
# loc can also take an integer as a row or column number.
# loc will return a KeyError if the requested items are not found.
# -----------------------------------------------------------------------------------
print(data.loc[0, "High"], "\n")

# Slicing using loc --------------
x = data.loc[0:4, "Date":"Low"]
print(x, "\n")

# ---------------------------------------- #2 ---------------------------------------
# iloc is integer-based.
# You use column numbers and row numbers to get -
# rows or columns at particular positions in the data frame.
# iloc will return an IndexError if the requested indexer is out-of-bounds.
# -----------------------------------------------------------------------------------
print(data.iloc[0, 6], "\n")

# Slicing using iloc --------------
y = data.iloc[0:4, 0:2]
print(y, "\n")

# -------------------------------------- #3*** --------------------------------------
# By default, ix looks for a label.
# If ix doesn't find a label, it will use an integer.
# This means you can select data by using -
# either column numbers and row numbers or column headers and row names using ix.
# In Pandas version 0.20.0 and later, ix is deprecated. ***
# -----------------------------------------------------------------------------------


# ================================ Advance Slicing ==================================
# Selecting The unique value from a column
z = data["Open"].unique()
print(z, "\n")

p = data["Open"] >= 20
print(p, "\n")

q = data[data["Open"] >= 23]
print(q, "\n")

# Save data frame to a new file
q.to_csv("data-resource/larger_than_23.csv")



# ============================= API ===============================
dict_ = {"a": [11, 21, 31], "b": [12, 22, 32], "c": [13, 23, 33]}
df = pd.DataFrame(dict_)

print(df.head(), "\n")
print(df.mean(), "\n")
