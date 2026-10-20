import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from favorite_cmaps import ibmcolorblind, okabe_ito, tol_muted, blue_tan_ramp, green_purple_ramp, red_green_ramp, red_green_ramp_adj, sage_orange, bottlegreen, bottleblue, munsell75yr, historic_glass, historic_glass_alt

def show_cmap(name, cmap, ax):
    """
    Modified from https://matplotlib.org/stable/gallery/color/colormap_reference.html
    """
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    cmap_name = name
    ax.imshow(gradient, aspect='auto', cmap = cmap)
    ax.text(-.01, .5, cmap_name, va='center', ha='right', fontsize=10, transform=ax.transAxes)
    ax.set_axis_off()
    # if out_path == True:
    #     plt.savefig(out_path)


prev_pub_cat = [ibmcolorblind, okabe_ito, tol_muted]
prev_pub_grad = [blue_tan_ramp, green_purple_ramp, red_green_ramp]

my_grad = [sage_orange, bottlegreen, bottleblue, munsell75yr]
my_cat = [historic_glass, historic_glass_alt]

#Previously published categorical color maps

fig, ax = plt.subplots(len(prev_pub_cat), 1)
for i, l, a in zip(prev_pub_cat, ['IBM', 'Okabe-Ito', 'Tol (muted)'], ax.reshape(-1)):
    show_cmap(l, i, a)
plt.tight_layout()
plt.savefig('figures/Categorical.jpg')
plt.close()

#Previously published gradients

fig, ax = plt.subplots(len(prev_pub_grad), 1)
for i, l, a in zip(prev_pub_grad, ['Moreland Blue-Tan', 'Moreland Green-Purple', 'Moreland Red-Green'], ax.reshape(-1)):
    show_cmap(l, i, a)
plt.tight_layout()
plt.savefig('figures/Gradient.jpg')
plt.close()

fig, ax = plt.subplots(len(prev_pub_grad), 1)
for i, l, a in zip(['RdBu', 'PuOr', red_green_ramp_adj], ['MPL RdBu', 'MPL PuOr', 'Adjusted Red-Green'], ax.reshape(-1)):
    show_cmap(l, i, a)
plt.tight_layout()
plt.savefig('figures/Gradient2.jpg')
plt.close()

#My Gradients
fig, ax = plt.subplots(len(my_grad), 1)
for i, l, a in zip(my_grad, ['Sage - Orange', 'Bottle Green', 'Bottle Blue', '7.5 YR'], ax.reshape(-1)):
    show_cmap(l, i, a)
plt.tight_layout()
plt.savefig('figures/MyGradient.jpg')
plt.close()

#My Gradients
fig, ax = plt.subplots(len(my_cat), 1)
for i, l, a in zip(my_cat, ['Historical Glass 1', 'Historic Glass 2'], ax.reshape(-1)):
    show_cmap(l, i, a)
plt.tight_layout()
plt.savefig('figures/MyCategorical.jpg')
plt.close()

#Preview with data

palmer = pd.read_csv('https://raw.githubusercontent.com/allisonhorst/palmerpenguins/refs/heads/main/inst/extdata/penguins.csv')


female = palmer[palmer['sex'] == 'female']
male = palmer[palmer['sex'] == 'male']

fig, ax = plt.subplots(1, 2, sharex = True, sharey = True, figsize = (10, 5))
male.plot.scatter('flipper_length_mm', 'bill_length_mm', c = 'species', cmap = ibmcolorblind, ax = ax[0])
ax[0].set_title('Male')
ax[0].set_xlabel('')
ax[0].set_ylabel('Bill Length (mm)', fontsize = 12)
female.plot.scatter('flipper_length_mm', 'bill_length_mm', c = 'species', cmap = ibmcolorblind, ax = ax[1])
ax[1].set_title('Female')
ax[1].set_xlabel('')
ax[1].set_ylabel('Bill Length (mm)', fontsize = 12)
fig.supxlabel('Flipper Length (mm)', fontsize = 12)
plt.tight_layout()
# plt.show()
plt.savefig("figures/Scatter_example.jpg")
plt.close()