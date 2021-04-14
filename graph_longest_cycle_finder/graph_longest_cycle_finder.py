import numpy as np
import time

cycles = []
edges = []
n = 0


def read_file(file_name):
    global n

    with open(file_name, "r") as f:
        n = int(f.readline())

        f.readline()  # Read empty line

        adjacency_matrix = []

        for _ in range(n):
            adjacency_matrix.append(f.readline().rstrip().split(" "))

    return np.array(adjacency_matrix).astype(np.int), n


def optimize_adjacency_matrix(adjacency_matrix):  # Remove vertices with degree 0 or 1
    global n

    i = 0
    optimized = True

    while i < n:
        if np.count_nonzero(adjacency_matrix[i] == 1) == 0 or np.count_nonzero(adjacency_matrix[i] == 1) == 1:
            adjacency_matrix = np.delete(adjacency_matrix, i, 0)
            adjacency_matrix = np.delete(adjacency_matrix, i, 1)
            optimized = False
            n -= 1
        i += 1

    if not optimized:
        return optimize_adjacency_matrix(adjacency_matrix)
    else:
        return adjacency_matrix, n


def find_edges(adjacency_matrix):
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] == 1 and [j, i] not in edges:
                edges.append([i, j])

    return np.array(edges)


def find_longest_cycle(path):
    if longest_cycle_length() < n:  # Stop recursion if path of length n is found
        start_vert = path[0]
        next_vert = None

        for edge in edges:
            vert1, vert2 = edge
            if start_vert in edge:
                if vert1 == start_vert:
                    next_vert = vert2
                else:
                    next_vert = vert1

                if next_vert not in path:
                    next_path = [next_vert]
                    next_path.extend(path)
                    find_longest_cycle(next_path)

            elif len(path) > 2 and next_vert == path[-1]:
                if len(path) > longest_cycle_length():
                    print(path)
                    cycles.append(path)


def longest_cycle_length():
    max_ = 0

    for cycle in cycles:
        if len(cycle) > max_:
            max_ = len(cycle)

    return max_


def main():
    global edges
    global cycles
    global n

    file_name = input("Enter the name of the input file: ")
    print()

    start = time.perf_counter()

    adjacency_matrix, n = read_file(file_name)
    print(adjacency_matrix)
    print(n)
    print()

    adjacency_matrix, n = optimize_adjacency_matrix(adjacency_matrix)
    print(adjacency_matrix)
    print(n)
    print()

    edges = find_edges(adjacency_matrix)
    print(edges)
    print()

    for edge in edges:
        find_longest_cycle(edge)
    print()

    print(longest_cycle_length())
    print()

    end = time.perf_counter()
    print("Finished in {:.2f} seconds.".format(end - start))


if __name__ == "__main__":
    main()
