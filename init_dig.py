import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


def calc_hit(val, sub):
    if val <= sub:
        return 0
    else:
        return val-sub

# Incorporate this function into the hammer and pick methods
def check_indicies(i, j):
    # Returns true for indicies within screen limits
    return i < 0 or j < 0


def show_screen(screen):
    pix_res = 16
    sprite_path = "Sprites/Layer_"

    img_array = np.zeros((10 * pix_res, 13 * pix_res, 3))
    for i in range(10):
        for j in range(13):
            img_array[i * pix_res:(i + 1) * pix_res, j * pix_res:(j + 1) * pix_res] = mpimg.imread(sprite_path + str(screen[i, j]) + ".png")

    plt.axis("off")
    plt.imshow(img_array, interpolation='nearest')
    plt.show()
    return


class MiningScreen:
    def __init__(self):
        self.screen = np.ones((10, 13), dtype=int) * 6

    def hammer(self, y, x):
        # Reduce hit center by 2
        self.screen[y, x] = calc_hit(self.screen[y, x], 2)
        
        neighbor_indicies = [-1, 1]
        # Reduce orthogonal neighbors of center by 2
        for i in neighbor_indicies:
            self.screen[y+i, x] = calc_hit(self.screen[y+i, x], 2)
            self.screen[y, x+i] = calc_hit(self.screen[y, x+i], 2)
        
        # Reduce diagonal neighbors of center by 1
        for j in neighbor_indicies:
            for k in neighbor_indicies:
                self.screen[y+j, x+k] = calc_hit(self.screen[y+j, x+k], 1)
        return self

    def pick(self, y, x):
        # Reduce hit center by 2
        self.screen[y, x] = calc_hit(self.screen[y, x], 2)

        # Reduce orthogonal neighbors of center by 1
        neighbor_indicies = [-1, 1]
        for i in neighbor_indicies:
            self.screen[y+i, x] = calc_hit(self.screen[y+i, x], 2)
            self.screen[y, x+i] = calc_hit(self.screen[y, x+i], 2)
        return self


if __name__ == "__main__":
    # Demo of project
    new_dig = MiningScreen()
    show_screen(new_dig.screen)
    for k in range(7):
        new_dig = new_dig.hammer(3, 3)
        show_screen(new_dig.screen)
