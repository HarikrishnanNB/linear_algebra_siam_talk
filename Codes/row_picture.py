# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 12:32:10 2021

@author: harik
"""


import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-2, 4, 0.01)
y1 = x

#y2 = x + 5


plt.figure(figsize=(10,10))
plt.plot(x,y1,'b', markersize = 10, label='$y=x$')
# plt.plot(x,y2,'r', markersize = 10, label='$y= x+5$')
# plt.plot(1,1, 'ok', markersize = 15)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(True)
plt.xlabel('x', fontsize=30)
plt.ylabel('y', fontsize=30)
plt.ylim(-2, 2)
plt.xlim(-2,2)
plt.legend(fontsize=20)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.tight_layout()

plt.savefig("y_vs_x_2D_3.png", format='png', dpi=300)
plt.show()

