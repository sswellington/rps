import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class Graph(object):
        
    def __init__(self):
        self._name = 'Rio Paraíba do Sul'
        self._marker = '.'
        self._color = ['r','darkorange','b','g']


    def set_color(self, color):
        self._color = color

        
    def set_marker(self, marker):
        self._marker = marker
        
        
    def set_header(self, header):
        self._header = header
      
        
    def set_unit(self, unit):
        self._unit = unit

    
    def save(self, path):
        plt.savefig(path + '.pdf', dpi = 300)
        plt.cla()   # Clear axis
        plt.clf()   # Clear figure
        
        
    def heatmap(self, corr, title):
        # Generate a mask for the upper triangle
        mask = np.triu(np.ones_like(corr, dtype=bool))

        # Set up the matplotlib figure
        f, ax = plt.subplots(figsize = (11, 9))

        # Generate a custom diverging colormap
        cmap = sns.diverging_palette(230, 20, as_cmap = True)
        # cmap = sns.color_palette("vlag", as_cmap=True)

        # Draw the heatmap with the mask and correct aspect ratio
        sns.heatmap(corr, mask = mask, cmap = cmap, vmax = 1.0, center = 0,
                    square = True, linewidths = .5)
        
        plt.title(self._name +': '+ title)
        self.save('view/heatmap/pearson-' + title)
        
    
    def heatmap_scatter(self, corr, title):
        # Draw each cell as a scatter point with varying size and color
        g = sns.relplot(
            data=corr,
            x="level_0", y="level_1", hue="correlation", size="correlation",
            palette="vlag", hue_norm=(-1, 1), edgecolor=".7",
            height=10, sizes=(50, 250), size_norm=(-1.0, 1.0),
        )

        # Tweak the figure to finalize
        g.set(xlabel="X", ylabel="Y", aspect="equal")
        g.despine(left=True, bottom=True)
        g.ax.margins(.02)
        
        for label in g.ax.get_xticklabels():
            label.set_rotation(90)
        for artist in g.legend.legendHandles:
            artist.set_edgecolor(".7")
            
        plt.title(self._name +': '+ title)
        self.save('view/heatmap-scatter/pearson-' + title)