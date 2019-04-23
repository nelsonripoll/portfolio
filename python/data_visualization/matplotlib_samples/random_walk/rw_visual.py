import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(100000)
rw.fill_walk()

plt.figure(figsize=(10,6))

point_numbers = list(range(rw.num_points))

# plt.plot(rw.x_values, rw.y_values, linewidth=1)
plt.scatter(rw.x_values,
            rw.y_values, 
            c=point_numbers, 
            cmap=plt.cm.Reds, 
            edgecolor='none', 
            s=2)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
