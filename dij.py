def GetNeighbours(gamemap, coordinate, height, width):
    neighbours = []
    mass = [(coordinate[0] - 1, coordinate[1]),
            (coordinate[0] + 1, coordinate[1]),
            (coordinate[0], coordinate[1] - 1),
            (coordinate[0], coordinate[1] + 1)]
    for i in mass:
        if i[0] >= 0 and i[0] < height \
                and 0 <= i[1] < width \
                and gamemap[i[0]][i[1]] != 1:
            neighbours.append(i)

    return neighbours


def BFS(gamemap, start, finish, height, width):
    ochered = [start]
    slov = dict()
    closed = []
    while len(ochered) != 0:
        vershina = ochered.pop(0)
        closed.append(vershina)
        if vershina == finish:
            print(vershina)
            while True:
                if (vershina in slov):
                    vershina = slov[vershina]
                    print(vershina)
                else:
                    break
            return True,
        for j in GetNeighbours(gamemap, vershina, height, width):
            if j not in closed and j not in ochered:
                ochered.append(j)
                slov[j] = vershina
    return False


def popMin(g, ochered):
    m = g[ochered[0]]
    key = ochered[0]
    m_i = 0
    for i in range(1, len(ochered)):
        if g[ochered[i]] < m:
            key = ochered[i]
            m = g[key]
            m_i = i
    ochered.pop(m_i)
    return key


def Dijkstra(gamemap, start, finish, height, width):
    g = dict()
    g[start] = 0
    ochered = [start]
    slov = dict()
    closed = []
    while len(ochered) != 0:
        vershina = popMin(g, ochered)
        closed.append(vershina)
        if vershina == finish:
            print(vershina)
            while True:
                if (vershina in slov):
                    vershina = slov[vershina]
                    print(vershina)
                else:
                    break
            return True,
        for j in GetNeighbours(gamemap, vershina, height, width):
            if j not in closed and j not in ochered:
                ochered.append(j)
                g[j] = g[vershina] + 1
                slov[j] = vershina
            elif j in ochered:
                if g[j] > g[vershina] + 1:
                    g[j] = g[vershina] + 1
                    slov[j] = vershina
    return False


file = r'/Users/nastya/PycharmProjects/олимпиада/pathSA'
mapfile = open(file, mode='r')
height = int(mapfile.readline())
width = int(mapfile.readline())
gamemap = []
for i in range(height):
    LIST = list(map(int, mapfile.readline().split()))
    gamemap.append(LIST)
temps = (mapfile.readline().split())
start = (int(temps[0]), int(temps[1]))
tempf = (mapfile.readline().split())
finish = (int(tempf[0]), int(tempf[1]))
print(Dijkstra(gamemap, start, finish, height, width))
