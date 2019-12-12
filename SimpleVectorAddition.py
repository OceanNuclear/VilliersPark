from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
import matplotlib.pyplot as plt


plt.style.use('dark_background')

fig, ax = plt.subplots()

plt.arrow(*[0,0],*[1,2],head_width=0.2, fill=False, length_includes_head=True)
plt.arrow(*[0,0],*[-3,-4],head_width=0.2, fill=False, length_includes_head=True)
plt.xlim([-3.5,1.5])
plt.ylim([-4.5,2])
# ax.set_xlabel('x-axis')
# ax.set_ylabel('y-axis')
# ax.set_title("")

plt.savefig("SimpleVectorAddition_starting.png")