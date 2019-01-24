'''xD'''
import rumgym as rm
g = rm.Grapher()

for i in range(10):
    p = rm.Point(i, i, i)
    g.add(p)

v = rm.Vector(4, 4, 4)
g.add(v)

p1 = rm.Point(10, 0, 0)
v1 = rm.Vector(10, 10, 0)
l = rm.Line(p1, v1)
g.add(l)

p3 = rm.Point(0, 0, 0)
v2 = rm.Vector(2, 4, 1)
v3 = rm.Vector(1, 1, 1)
plane = rm.Plane(p3, v2, v3)
g.add(plane)
g.show()

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# xs = [22,24,25,67]
# ys = [12,12,23,67]
# zs = [-50, -25,-30,-5]
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# ax.scatter(xs, ys, zs)

# plt.show()
