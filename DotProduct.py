from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
import matplotlib.pyplot as plt


plt.style.use('dark_background')

fig, ax = plt.subplots()

plt.arrow(*[0,0],*[1,2],head_width=0.2, fill=False, length_includes_head=True)
plt.arrow(*[1,2],*[-3,-4],head_width=0.2, fill=False, length_includes_head=True)
plt.scatter(*[0,0],color='white')
plt.xlim([-2.5,2.5])
plt.ylim([-2.5,2.5])
# ax.set_xlabel('x-axis')
# ax.set_ylabel('y-axis')
# ax.set_title("")

plt.savefig("SimpleVectorAddition_later.png")