import numpy as np
import matplotlib.pyplot as plt
import subprocess

fig, axs =  plt.subplots(1, 1, figsize=(4, 2.5))
fig.subplots_adjust(top=0.8)
Z = np.array([[1.,2.,3.],[1., 2., 4.],[2, 3.,4.]])
ax = axs
ax.contourf(Z, vmin=0., vmax=10., edgecolors='none')
ax.set_axis_off()
ax.set_title("edgecolor='none'")


fig.suptitle('PDF')
fig.savefig('exampleContour.pdf')
subprocess.call(['convert','-density', '100',
        'exampleContour.pdf', 'exampleContour.pdf.png'])

subprocess.call(['convert','-density', '300',
        'exampleContour.pdf', 'exampleContour.pdf.300.png'])
fig.suptitle('PNG')
fig.savefig('exampleContour.png', dpi=100)

ax.set_facecolor('k')
fig.suptitle('PDF')
fig.savefig('exampleContourBlack.pdf', facecolor='k')
subprocess.call(['convert','-density', '100',
        'exampleContourBlack.pdf', 'exampleContourBlack.pdf.png'])
