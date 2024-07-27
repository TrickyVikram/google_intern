
import cv2
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


i = misc.ascent()

plt.grid(False)
plt.gray()
plt.axis('off')
plt.imshow(i)
plt.show()

i_transformed = np.copy(i)
size_x = i_transformed.shape[0]
size_y = i_transformed.shape[1]