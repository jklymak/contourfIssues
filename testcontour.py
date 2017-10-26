import numpy as np
import matplotlib.pyplot as plt

fig, axs =  plt.subplots(5, 2, figsize=(9, 9), dpi=200)
fig.subplots_adjust(hspace=0.18, wspace=0.07, top=0.9, bottom=0.02,
        left=0.05, right=0.95)

Z = np.array([[1.,2.,3.],[1., 2., 4.],[2, 3.,4.]])
ax = axs[0, 0]
ax.contourf(Z, vmin=0., vmax=10., edgecolors='none')
ax.set_axis_off()
ax.set_title("edgecolor='none'")

for nn, lw in enumerate([1., 0.2, 0.1, 0.0001]):
    ax = axs[1+nn, 0]
    ax.contourf(Z, vmin=0., vmax=10., edgecolors='face', linewidths=lw)
    ax.set_title("edgecolors='face', linewidths= %1.4f"%lw)
    ax.set_axis_off()

ax = axs[0, 1]
ax.contourf(Z, vmin=0., vmax=10., edgecolors='none', alpha=0.7, linewidths=0.)
ax.set_axis_off()
ax.set_title("alpha=0.7, edgecolors='none'")

for nn, lw in enumerate([1., 0.2, 0.1, 0.0001]):
    ax = axs[1+nn, 1]
    ax.contourf(Z, vmin=0., vmax=10., edgecolors='face', linewidths=lw,
            alpha = 0.7)
    ax.set_title("alpha=0.7, edgecolors='face', linewidths=%1.4f"%lw)
    ax.set_axis_off()



fig.suptitle('EPS')
fig.savefig('testcontour.eps')
fig.suptitle('PDF')
fig.savefig('testcontour.pdf')
fig.suptitle('PNG 50 dpi')
fig.savefig('testcontour50.png', dpi=50)
fig.suptitle('PNG 100 dpi')
fig.savefig('testcontour100.png', dpi=100)
fig.suptitle('PNG 200 dpi')
fig.savefig('testcontour200.png', dpi=200)
fig.suptitle('svg')
fig.savefig('testcontour.svg')

## antialiased?
fig, axs =  plt.subplots(1, 2, figsize=(9, 3), dpi=200)
fig.subplots_adjust(hspace=0.18, wspace=0.07, top=0.9, bottom=0.02,
        left=0.05, right=0.95)

Z = np.array([[1.,2.,3.],[1., 2., 4.],[2, 3.,4.]])
ax = axs[0]
ax.contourf(Z, vmin=0., vmax=10., edgecolors='none')
ax.set_title('AA = False')
ax = axs[1]
ax.contourf(Z, vmin=0., vmax=10., edgecolors='none', antialiased=True)
ax.set_title('AA = True')
fig.suptitle('PDF')
fig.savefig('testcontourAliasing.pdf')
fig.suptitle('PNG 50 dpi')
fig.savefig('testcontour50Aliasing.png', dpi=50)
