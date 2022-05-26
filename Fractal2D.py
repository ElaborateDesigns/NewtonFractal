import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import sys


A = np.array([[0,1,2,3],[0,1,2,3],[0,1,2,3]])
B = np.zeros(A.shape) #default
B = np.array([[5,5,5,5],[6,6,6,6],[6,7,8,9]])

print(A)
print(B)

class fractal2D:    
  max_nr_of_iterations = 9
  A = np.array([[0,1,2,3],[0,1,2,3],[0,1,2,3]])
  B = np.zeros(A.shape) #default
  B = np.array([[5,5,5,5],[6,6,6,6],[6,7,8,9]])
  
  def shade_color(self, base, val, min, max):
  	"""Shades a base color darker, the more iterations the color is assigned to show."""
  	return tuple(i/(val - min + 1) for i in base)
  	
  def make_cmap(self): 
    """Constructs a custom color map according to the number of base colors and shades of these base colors needed"""
    nr_of_colors = np.max(A)+1
    max_iter = self.max_nr_of_iterations 
    min_iter = np.min(B)
    palette = [(2,0.5,0.5), (0.5,2.0,0.5), (0.5,0.5,2), (3,3,0), (0, 2, 2), (2, 0, 2) ]
    colors = []
    for i in range(0, nr_of_colors): 
      base_color = palette[i]
      for j in range(min_iter, max_iter+1): 
        new_color = self.shade_color(base_color, j, min_iter, max_iter)
        colors.append(new_color)
    print(f"cmap: {colors}")
    return col.LinearSegmentedColormap.from_list("mycmap", colors)
    
  def graph(self):
    """Makes a graph from A, a matrix of root indices, and B, a matrix of iteration counts."""
    C = self.A*(self.max_nr_of_iterations + 1) + self.B
    print(C)
    plt.imshow(C, cmap=self.make_cmap() )
    plt.show()

x = fractal2D()
x.graph()