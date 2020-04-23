import math

def closest_pair(points):

    def distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    min_pair, min_distance = None, float('inf')

    for p1 in points:
        for p2 in points:
            if p1 is p2:
                continue
            dist = distance(p1, p2)
            if dist < min_distance:
                min_pair = (p1, p2)
                min_distance = dist
    return min_pair


pairs = ((0, 0), (2, 2), (1, 2), (6, 7), (6, 6))
print(closest_pair(pairs))