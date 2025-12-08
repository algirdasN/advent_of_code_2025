import math


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

    joined_clusters = []
    while clusters:
        cluster = clusters.pop()
        for other in clusters:
            if cluster & other:
                clusters.remove(other)
                clusters.append(cluster | other)
                break
        else:
            joined_clusters.append(cluster)

    sorted_clusters = sorted(joined_clusters, key=len, reverse=True)

    print(len(sorted_clusters[0]) * len(sorted_clusters[1]) * len(sorted_clusters[2]))


if __name__ == "__main__":
    main()
