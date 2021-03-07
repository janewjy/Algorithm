level = {s:0}
parent = {s:None}
i = 1

frontier = [s]
while frontier:
    nextLevel = []
    for u in frontier:
        for v in frontier[u]:
            if v not in level:
                level[v] = i
                parent[v] = u
                nextLevel.append(v)
    i += 1
    frontier = nextLevel
