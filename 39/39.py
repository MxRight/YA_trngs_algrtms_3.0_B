n = int(input())
graph = []

for block in range(n):
    graph_plane = []
    _empty = input()
    for plane in range(n):
        line = input()
        graph_line = [0 if i == "#" else 1 for i in line]
        if "S" in line:
            cube = (block, plane, line.find("S"))
        graph_plane.append(graph_line)
    graph.append(graph_plane)


def search_path(n, graph, cube):
    if cube[0] == 0:
        return 0
    path = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    z, y, x = cube
    path[z][y][x] = 0
    queue = [list(cube)]
    head = 0

    while True:
        now = queue[head]
        neighs = []
        for step in [-1, 1]:
            for coord in [0, 1, 2]:
                poss_neigh = [i for i in now]
                poss_neigh[coord] = poss_neigh[coord] + step
                z, y, x = poss_neigh
                if z >= n or y >= n or x >= n or z < 0 or y < 0 or x < 0:
                    continue
                if path[z][y][x] == -1 and graph[z][y][x] == 1:
                    if z == 0:
                        return path[now[0]][now[1]][now[2]] + 1
                    neighs.append(poss_neigh)
        for neigh in neighs:
            z, y, x = neigh
            path[z][y][x] = path[now[0]][now[1]][now[2]] + 1
            queue.append(neigh)
        head += 1


print(search_path(n, graph, cube))
