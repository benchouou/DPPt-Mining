import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

def check_hit(y,x):
# Verify that hit is not out of bounds
# Verify that hit does not decrease level below 0
    return

class mining_screen:
    def __init__(self):
        self.screen=np.ones((13,10))*6

    def hammer(self, y,x):
        #Reduce hit center by 2
        self.screen[y,x] = self.screen[y,x]-2
        
        neighbor_indicies=[-1, 1]
        #Reduce orthogonal neighbors of center by 2
        for i in neighbor_indicies:
            self.screen[y+i,x]=self.screen[y+i,x]-2
            self.screen[y, x+i] = self.screen[y, x+i] - 2
        
        #Reduce diagonal neighbors of center by 1
        for j in neighbor_indicies:
            for k in neighbor_indicies:
                self.screen[y+j, x+k] = self.screen[y+j, x+k] - 1
        return

    def pick(self, y,x):
        #Reduce hit center by 2
        self.screen[y,x] = self.screen[y,x]-2

        #Reduce orthogonal neighbors of center by 1
        neighbor_indicies=[-1,1]
        for i in neighbor_indicies:
            self.screen[y+i,x]=self.screen[y+i,x]-2
            self.screen[y, x+i] = self.screen[y, x+i] - 2
        return

if __name__ == "__main__":
    #Progress check that layer sprites are displayed properly. Move to function later
    sprite_path="Sprites/Layer_"
    pix_res=16
    
    img_array=np.zeros((10*pix_res, 13*pix_res,3))
    for i in range(10):
        for j in range(13):
            img_array[i*pix_res:(i+1)*pix_res, j*pix_res:(j+1)*pix_res] = mpimg.imread(sprite_path+str(np.random.random_integers(0,6))+".png")

    plt.axis("off")
    plt.imshow(img_array, interpolation='nearest')
    plt.show()
