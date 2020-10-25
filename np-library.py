import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
print("\n")
print("============= numpy 1D Array =============")
print("\n")
# -------------------------------------------------

# ================ Python 1D Array ================
a = np.array(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])

print(a.size, "\n")
print(a.ndim, "\n")
print(a.shape, "\n")

b = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print(b.dtype, type(b), "\n")

c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(c, "\n")

#  Changing Value
c[0] = 0.0
c[-1] = 9.0
print(c, "\n")

# Slicing
d = c[1:6]
print(d, "\n")

d[3:5] = 400, 500
print(d, "\n")

d[5:5] = 600, 700
print(d, "\n")

# Vector Addition ---------------------------
p = [1, 0]
q = [0, 1]
v = []
for a, b in zip(p, q):
    v.append(a + b)
print(v, "\n")

# Using numpy this is much easier
p = np.array([3, 1])
q = np.array([1, 5])
v = p + q
w = p - q
y = 2 * v
z = p * q
print(v, "\n")
print(w, "\n")
print(y, "\n")
print(z, "\n")

# Dot Product -------------------------------------
# a = 1/2, b = 3/4
# (np.dot) result = 1 * 3 + 2 * 4
# This represents how similar the two vectors are
result = np.dot(p, q)
print(result, "\n")

# Broadcasting -------------------------------------
r = np.array([-3, -2, -1, 0, 1, 2, 3])
s = r + 3
print(r, "\n")
print(s, "\n")

min_s = s.min()
max_s = s.max()
mean_s = s.mean()
print(min_s, "\n")
print(max_s, "\n")
print(mean_s, "\n")

# ------------------------------------------------------
x = np.array([0, np.pi/4, np.pi/2, np.pi])
print(x, "\n")
sin_x = np.sign(x)
print(sin_x, "\n")

# Evenly spaced number using linespace -------------
print(np.linspace(-3, 3, num=2))
print(np.linspace(-3, 3, 2))
print(np.linspace(-3, 3, num=5))
print(np.linspace(-3, 3, 5))
print(np.linspace(-3, 3, num=7))
print(np.linspace(-3, 3, 7))

# u = np.linspace(0, 2*np.pi, 100)
# U = np.sign(u)
# print("\n", U, "\n")
# plt.plot(u, U)
# plt.show()


# -------------------------------------------------
print("\n")
print("============= numpy 2D Array =============")
print("\n")
# -------------------------------------------------

# ================ Python 2D Array ================
m = [[11, 12, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35]]
M = np.array(m)
print(M, "\n")
print(M.ndim, "\n")
print(M.shape, "\n")
print(M.size, "\n")
print(M[0][0], M[1][1], M[2][2],  "\n")
print(M[0, 0], M[1, 1], M[2, 2],  "\n")
print([M[0, 0], M[1, 1], M[2, 2]],  "\n")

# Slicing -----------------
print(M[1, 0:3], "\n")
print(M[0:3, 2], "\n")

# Addition, Multiplication of Array & Matrix -----------------
j = [[1, 2], [3, 4]]
k = [[5, 6], [7, 8]]
J = np.array(j)
K = np.array(k)

print(J, "\n")
print(K, "\n")

JK = J + K
JxK = J * K
print(JK, "\n")
print(JxK, "\n")
print(JK*2, "\n")


g = [[0, 1, 1], [1, 0, 1]]
h = [[1, 1], [1, 1], [-1, 1]]
G = np.array(g)
H = np.array(h)
GH = np.dot(G, H)
print(GH, "\n")










