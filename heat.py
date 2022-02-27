import seaborn as sns
import matplotlib.pyplot as plt
import math
from matplotlib import image as im
import numpy as np
def map_heat():
    sns.set_theme(style="white")
    signal_output_data = np.genfromtxt("./data/data.csv", delimiter=',')
    image = im.imread("data/floor_plan.png")
    for i in range(0,len(signal_output_data[:,9])):
        signal_output_data[:,9][i]=round(signal_output_data[:,9][i]*-1)
    clarity_ranking = [46,47, 48,49, 50,51, 52, 53,54,55, 56, 57,58, 59,60]
    palette=sns.color_palette("light:b", as_cmap=True)
    g=sns.kdeplot(x=signal_output_data[:,0], y=signal_output_data[:,1],hue=signal_output_data[:,9],alpha = 1,fill=True,zorder=2, levels=2, palette=palette) #alpha = 0.8,s=100,linewidth=0,hue_order=clarity_ranking,cbar = True
    #g=sns.scatterplot(x=signal_output_data[:,0], y=signal_output_data[:,1],hue=signal_output_data[:,9],alpha = 1,zorder=2, palette=palette)
    g.imshow(image, zorder=1)
    plt.show()
#map_heat()
#{1: [480.0, 300.0, 120, 120, 1, (165, 42, 42)]}