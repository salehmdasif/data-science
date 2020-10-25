import matplotlib.pyplot as plt


# Circle ==============================
class Circle(object):
    # here _init_ is a constructor that tells python that there is a new class going to be made
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def AddRadius(self, r):
        self.radius = self.radius + r
        return self.radius

    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()


redCircle = Circle(10, "red")
print("Radius is", redCircle.radius)
print("Color is", redCircle.color)
redCircle.drawCircle()

redCircle.color = "blue"
print("The changed color is", redCircle.color)
redCircle.AddRadius(5)
print("The new radius is", redCircle.radius)
redCircle.drawCircle()

print(dir(redCircle))


# Rectangle ==============================
class Rectangle(object):
    # here _init_ is a constructor that tells python that there is a new class going to be made
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()


greenRectangle = Rectangle(10, 6, 'green')
greenRectangle.drawRectangle()
