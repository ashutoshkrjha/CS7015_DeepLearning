# coding: utf-8
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
fig1 = plt.figure(1)
fig2 = plt.figure(2)
fig3 = plt.figure(3)
fig4 = plt.figure(4)
fig5 = plt.figure(5)
fig6 = plt.figure(6)
fig7 = plt.figure(7)
fig8 = plt.figure(8)
ax1 = fig1.gca(projection='3d')
ax2 = fig2.gca(projection='3d')
ax3 = fig3.gca(projection='3d')
ax4 = fig4.gca(projection='3d')
ax5 = fig5.gca(projection='3d')
ax6 = fig6.gca(projection='3d')
ax7 = fig7.gca(projection='3d')
ax8 = fig8.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Q1 = -1*(X+(100*Y)+200)
H11 = 1/(1+np.exp(Q1))
Q2 = -1*(X+(100*Y)-200)
H12 = 1/(1+np.exp(Q2))
Q3 = -1*((100*X)+Y+200)
H13 = 1/(1+np.exp(Q3))
Q4 = -1*((100*X)+Y-200)
H14 = 1/(1+np.exp(Q4))
H21 = H11-H12
H22 = H13-H14
H31 = H21+H22
F = 1/(1+np.exp(-50*H31+100))
surf1 = ax1.plot_surface(X, Y, H11)
surf2 = ax2.plot_surface(X, Y, H12)
surf3 = ax3.plot_surface(X, Y, H13)
surf4 = ax4.plot_surface(X, Y, H14)
surf5 = ax5.plot_surface(X, Y, H21)
surf6 = ax6.plot_surface(X, Y, H22)
surf7 = ax7.plot_surface(X, Y, H31)
surf8 = ax8.plot_surface(X, Y, F)

plt.show()
