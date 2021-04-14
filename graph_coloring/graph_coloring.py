import time
import numpy as np
from numba import njit


def read_file(file_name):
    with open(file_name, "r") as f:
        n = int(f.readline())

        f.readline()  # Read empty line

        adjacency_matrix = []

        for _ in range(n):
            adjacency_matrix.append(f.readline().rstrip().split(" "))

    return np.array(adjacency_matrix).astype(np.int), n


# n = matrix size
# v = current vertex number
# c = current color to be assigned
# colors = list of verticies and their colors, 0 = no color, 1-2-3.. = other colors
# max_colors = max number of colors to use
# jit = code is optimized to run faster using numba, greatly speeds up calculating big recursions and loops


@njit
def can_color(adjacency_matrix, n, v, colors, c):
    for i in range(n):
        if adjacency_matrix[v][i] == 1 and colors[i] == c:
            return False
    
    return True


@njit
def graph_coloring(adjacency_matrix, n, v, colors, max_colors):
    if (v == n):
        return True
    
    for c in range(1, max_colors + 1):
        if can_color(adjacency_matrix, n, v, colors, c):
            colors[v] = c

            if graph_coloring(adjacency_matrix, n, v + 1, colors, max_colors):
                return True

            colors[v] = 0
                
    return False


@njit
def find_chromatic_number(adjacency_matrix, n, colors):
    for chromatic_number in range(2, n):
        if graph_coloring(adjacency_matrix, n, 0, colors, chromatic_number):
            return chromatic_number

    return n


def main():
    file_name = input("Enter file name: ")
    
    start = time.time()

    adjacency_matrix, n = read_file(file_name)
    colors = np.zeros([n], dtype = int)

    chromatic_number = find_chromatic_number(adjacency_matrix, n, colors)

    end = time.time()

    print("The smallest number of colors needed to color this graph is: {}".format(chromatic_number))
    print("This calculation took {:.4f} seconds".format(end - start))
    

if __name__ == "__main__":
    main()
