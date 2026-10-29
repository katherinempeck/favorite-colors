import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap

import numpy as np

#####################################
## Previously published color maps ##
#####################################

#Categorical
#See https://davidmathlogic.com/colorblind
#https://web.archive.org/web/20180503023309/https://www.ibm.com/design/language/resources/color-library
ibmcolorblind = ListedColormap(["#648FFF", "#785EF0", "#DC267F", "#FE6100","#FFB000"])

#https://jfly.uni-koeln.de/color/
okabe_ito = ListedColormap(["#000000", "#E69F00","#56B4E9", "#009E73","#F0E442","#0072B2","#D55E00","#CC79A7"])

#https://sronpersonalpages.nl/~pault/
tol_muted = ListedColormap(["#332288","#117733","#44AA99","#88CCEE","#DDCC77","#CC6677","#AA4499","#882255"])

#Diverging Gradients

# Originally published in:
# Moreland, K. (2009). Diverging color maps for scientific visualization. In International symposium on visual computing (pp. 92-103). Berlin, Heidelberg: Springer Berlin Heidelberg.
# Paper available online: https://www.kennethmoreland.com/color-maps/ColorMaps.pdf

#As far as I can tell, there is not really an equivalent to this diverging color map in Matplotlib
blue_tan_ramp = LinearSegmentedColormap.from_list("moreland_blue-tan", [(0.217, 0.525, 0.910), (0.865, 0.865, 0.865), (0.677, 0.492, 0.093)])
#This cmap is similar to PrGn and PiYG already available in Matplotlib
green_purple_ramp = LinearSegmentedColormap.from_list("moreland_green_purple", [(0.085, 0.532, 0.201), (0.865, 0.865, 0.865), (0.436, 0.308, 0.631)])
#Other diverging gradients published by Moreland have close equivalents in Matplotlib already
#Blue - Red = RdBu
#Purple - Orange = PuOr
#There is no existing red/green diverging colormap
#RdYlGn would be a reasonable approximation (but without the neutral central color)
#This is the implementation of Moreland's red-green map
#Note that this will be problematic as is for individuals with red-green colorblindness 
red_green_ramp = LinearSegmentedColormap.from_list("moreland_red-green", [(0.085, 0.532, 0.201), (0.865, 0.865, 0.865), (0.758, 0.214, 0.233)])
#However, by changing the hue and value of the green and red, we can actually make a color ramp that should be readable for individuals with issues distinguishing these colors
red_green_ramp_adj = LinearSegmentedColormap.from_list("adjusted_red-green", ['#00FF46', (0.865, 0.865, 0.865), '#860835'])
#More neutral colors in the ramp may get a little close for individuals with deuteranopia
#It is also important to consider that even if all colors are distinguishable, if you are using red to indicate "bad" or "low" values, this ramp will still be hard to interpret at a glance

###################
## My color maps ##
###################

#Gradients
sage_orange = LinearSegmentedColormap.from_list("sageorange", ['#191e1c', '#3B5941', '#afc7bd', (0.865, 0.865, 0.865), '#ffcdab', '#d18044', '#4d2903'])

#These gradients are nice color schemes but a bit low contrast
sageforest = LinearSegmentedColormap.from_list("sageforest", [ '#191e1c', '#3B5941', '#afc7bd'])
burntorange = LinearSegmentedColormap.from_list("burntorange", [ '#4d2903', '#d18044', '#ffcdab'])
earthblue = LinearSegmentedColormap.from_list("earthblue", ["#1f305e", "#425fa1", "#91b0dc", "#dce8fa"]) #Note - not included in the README because it's fairly similar to the bottleblue map

#Green gradient inspired by historic bottle glass colors
bottlegreen = LinearSegmentedColormap.from_list("bottlegreen", ["#181e11", "#39452c", "#596b43", "#78925b", "#99b873", "#faffde"])
#Blue gradient inspired by historic bottle glass colors
bottleblue = LinearSegmentedColormap.from_list("bottleblue", ["#174F9E", "#0295bc", "#5db3bf", "#9ed0c9", "#ffffff"])
#Inspired by the 7.5 YR page of the Munsell soil book
#These are approximations of the colors along the value axis (with some variation across the chroma axis to look nice)
#Note - these are not converted directly from the Munsell hue/value/chroma values
munsell75yr = LinearSegmentedColormap.from_list("7.5YR", ["#3F312E", "#583829", "#7D4F35", "#9F6C3F", "#C57D46", "#D4A176", "#D4C7BF"])

#Categorical

#Historic bottle glass colors (black/forest green, cobalt, olive green, amethyst, aqua)
#These should be accesible, but the amethyst and aqua colors are somewhat similar
historic_glass = ListedColormap(["#181E11", "#174F9E", "#4C7738", "#A37C94", "#9ECFC8"])
#Alternate historic bottle glass colors (black/forest green, amber, aqua, amethyst, straw)
#Again, aqua and amethyst are a bit close (the hues and values have been adjusted slightly to make those colors work with the other ones in this cmap)
historic_glass_alt = ListedColormap(["#181E11", "#73431B", "#986E89", "#A2D6D3", "#F4E7D3"])