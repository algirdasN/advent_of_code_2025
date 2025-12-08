import math
from copy import copy


def consolidate_clusters(clusters):
    clusters_copy = copy(clusters)
    clusters.clear()
    while clusters_copy:
        cluster = clusters_copy.pop()
        for other in clusters_copy:
            if cluster & other:
                clusters_copy.remove(other)
                clusters_copy.append(cluster | other)
                break
        else:
            clusters.append(cluster)


def main():
    with open("data/08.txt") as file:
        junctions = [eval("(" + x + ")") for x in file.read().splitlines()]

    distances = {}
    for index, i in enumerate(junctions):
        for j in junctions[index + 1:]:
            distances[(i, j)] = math.sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 + (i[2] - j[2]) ** 2)

    shortest_distance: list[tuple[tuple, tuple]] = [x[0] for x in sorted(distances.items(), key=lambda x: x[1])]

    clusters: list[set[tuple]] = []

    connections = 1000
    for pair in shortest_distance[:connections]:
        for c in clusters:
            if pair[0] in c or pair[1] in c:
                c.add(pair[0])
                c.add(pair[1])
                break
        else:
            clusters.append(set(pair))

    consolidate_clusters(clusters)
    sorted_clusters = sorted(clusters, key=len, reverse=True)

    print(len(sorted_clusters[0]) * len(sorted_clusters[1]) * len(sorted_clusters[2]))

    while len(clusters) > 1 or len(clusters[0]) < len(junctions):
        pair = shortest_distance[connections]
        for c in clusters:
            if pair[0] in c or pair[1] in c:
                c.add(pair[0])
                c.add(pair[1])
                consolidate_clusters(clusters)
                break
        else:
            clusters.append(set(pair))

        connections += 1

    print(shortest_distance[connections - 1][0][0] * shortest_distance[connections - 1][1][0])


if __name__ == "__main__":
    main()
