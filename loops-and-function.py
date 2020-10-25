# For Loop
colors = ["red", "pink", "yellow", "green", "blue", "purple", "black"]

# for i in range(0, 7):
#     colors[i] = "white"
# print(colors)

for color in colors:
    print(color)

for color in enumerate(colors):
    print(color)

for i, color in enumerate(colors):
    print(i, color)

# While Loop
oldColors = ["black", "black", "black", "black", "black", "red"]
newColors = []

x = 0
while oldColors[x] == "black":
    newColors.append(oldColors[x])
    x = x + 1
print(newColors)

# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = 0

while year != 1973:
    year = dates[i]
    i = i + 1
    print(year)

print("It took ", i, "repetitions to get out of loop.")

x = [1, 3, 5, 2, 4]
y = sorted(x)
print(y)
print(x)
x.sort()
print(x)


# Function with For Loop ==========================
def printStuff(stuff):
    for o, s in enumerate(stuff):
        print("Number", o, "gains", s, "rating")


numberRatings = [7.5, 8.3, 9.2, 8.6, 7.9]
printStuff(numberRatings)


def addDC(k):
    k = k + "DC"
    return k


a = "AC"
b = addDC(a)
print(b)


def thriller():
    date = 1982
    return date


print(thriller())
Date = 2018
print(Date)


def AcDc(r):
    print(point)
    return point + r


point = 7
v = AcDc(5)

print(point)
print(v)


def PinkFloyd():
    global claimedSales
    claimedSales = "45 million"
    return claimedSales


PinkFloyd()
print(claimedSales)
# =================================================


q=1


def do(t):
    return(t+q)


print(do(1))