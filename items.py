import numpy as np


# Based on data from:
# https://bulbapedia.bulbagarden.net/wiki/The_Underground#Item_shapes
# * Need to add 90 deg rotation
# ** Need to add 90, 180, 270 deg rotations


def small_sphere():
    return np.ones((2, 2))


def large_sphere():
    return np.ones((3, 3))


def heart_scale():
    grid = np.ones((2, 2))
    grid[0, 1] = 0
    return grid


def skull_fossil():
    grid = np.ones((4, 4))
    grid[0, 3] = 0
    grid[3, 3] = 0
    return grid


def armor_fossil():
    grid = np.ones((4, 4))
    for i in [0, 1, 3]:
        grid[i, 0] = 0
        grid[i, 3] = 0
    return grid


def dome_fossil():
    grid = np.ones((4, 5))
    grid[0, 3] = 0
    grid[4, 3] = 0
    return grid


def helix_fossil():  # **
    grid = np.ones((4, 4))
    grid[0, 0] = 0
    grid[3, 3] = 0
    return grid


def old_amber():  # *
    grid = np.ones((4, 4))
    grid[0, 0] = 0
    grid[3, 3] = 0
    return grid


def claw_fossil():  # **
    grid = np.ones((5, 4))
    grid[0:3, 0] = 0
    grid[0, 1] = 0
    grid[3:5, 3] = 0
    grid[4, 2] = 0
    return grid


def root_fossil():  # **
    grid = np.ones((5, 5))
    grid[3:5, 0:2] = 0
    grid[2:4, 2] = 0
    for i in [0, 4]:
        grid[i, 4] = 0
    return grid


def red_shard():
    grid = np.ones((3, 3))
    grid[1, 2] = 0
    return grid


def yellow_shard():
    grid = np.ones((3, 4))
    for i in [1, 3]:
        grid[0, i] = 0
    grid[1, 3] = 0
    return grid


def green_shard():
    grid = np.ones((3, 4))
    grid[2, 3] = 0
    return grid


def blue_shard():
    grid = np.ones(3, 3)
    grid[2, 2] = 0
    return grid


def plate():
    return np.ones((3, 4))


def hard_stone():
    return np.ones((2, 2))


def heat_rock():
    grid = np.ones((3, 4))
    for i in [1, 3]:
        grid[0, i] = 0
    return grid


def damp_rock():
    grid = np.ones((3, 3))
    grid[2, 1] = 0
    return grid


def smooth_rock():
    grid = np.ones((4, 4))
    for i in [0, 1, 3]:  # Row 0
        grid[0, i] = 0
    grid[1, 3] = 0  # Row 1
    grid[2, 0] = 0  # Row 2
    for i in [0, 2, 3]:  # Row 3
        grid[3, i] = 0
    return grid


def icy_rock():
    grid = np.ones((4, 4))
    for i in [0, 3]:
        grid[0, i] = 0
    grid[3, 1:3] = 0
    return grid


def fire_stone():
    return np.ones((3, 3))


def water_stone():
    grid = np.ones((3, 3))
    grid[2, 2] = 0
    return grid


def thunderstone():
    grid = np.ones((3, 3))
    grid[0, 0] = 0
    grid[2, 2] = 0
    return grid


def leaf_stone():  # *
    grid = np.ones((4, 3))
    for i in [0, 2]:
        for j in [0, 3]:
            grid[j, i] = 0
    return grid


def moon_stone():  # *
    grid = np.ones((2, 4))
    grid[0, 0] = 0
    grid[1, 3] = 0
    return grid


def sun_stone():
    grid = np.ones((3, 3))
    grid[0, 0] = 0
    grid[0, 2] = 0
    return grid


def oval_stone():
    return np.ones((3, 3))


def everstone():
    return np.ones((2, 4))


def iron_ball():
    return np.ones((3, 3))


def light_clay():
    grid = np.ones((4, 4))
    for i in [1, 3]:
        grid[0, i] = 0
    grid[1, 3] = 0
    for i in [0, 2]:
        grid[3, i] = 0
    return grid


def odd_keystone():
    return np.ones((5, 5))


def revive():
    grid = np.ones((3, 3))
    for i in [0, 2]:
        for j in [0, 2]:
            grid[i, j] = 0
    return grid


def max_revive():
    return np.ones((3, 3))


def star_piece():
    grid = np.ones((3, 3))
    for i in [0, 2]:
        for j in [0, 2]:
            grid[i, j] = 0
    return grid


def rare_bone():  # *
    grid = np.ones((6, 3))
    for i in [1, 2, 3, 4]:
        for j in [0, 2]:
            grid[i, j] = 0
    return grid


if __name__ == "__main__":
    print(rare_bone())
