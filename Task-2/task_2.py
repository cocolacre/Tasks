import sys


#read polygon data
#print(len(sys.argv))
if len(sys.argv) == 1:
    fname = 'data.txt'
elif len(sys.argv) == 2:
    fname = sys.argv[1]
#print(fname)


poly = []
def point_within_polygon(x, y, poly, include_edges=True):

    n = len(poly)
    inside = False
    for point in poly:
        if point == [x,y]:
            msg = "Точка - вершина четырехугольника"
            return msg
        
    p1x, p1y = poly[0]
    for i in range(1, n + 1):
        p2x, p2y = poly[i % n]
        if p1y == p2y:
            if y == p1y:
                if min(p1x, p2x) <= x <= max(p1x, p2x):
                    msg = "Точка лежит на сторонах четырехугольника"
                    inside = include_edges
                    return msg
                    break
                elif x < min(p1x, p2x):
                    inside = not inside
        else:  # p1y!= p2y
            if min(p1y, p2y) <= y <= max(p1y, p2y):
                xinters = (y - p1y) * (p2x - p1x) / float(p2y - p1y) + p1x

                if x == xinters:
                    inside = include_edges
                    msg = "Точка лежит на сторонах четырехугольника"
                    return msg
                    break
                if x < xinters:
                    inside = not inside
        p1x, p1y = p2x, p2y
    if inside:
        msg = 'точка внутри четырехугольника'
    else:
        msg = 'точка снаружи четырехугольника'
    return msg

with open(fname, 'r') as f:
    for line in f.readlines():
        poly.append([float(item) for item in line.split(' ')])
#print(poly)

x = float(input('X: '))
y = float(input('Y: '))

res = point_within_polygon(x,y,poly)
print(res)