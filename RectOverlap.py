import matplotlib.pyplot
__author__ = 'xiongyi'
line1 = [(200, 100), (200, 400)]
line2 = [(190, 190), (210, 210)]
def overlap():
    l1p1x = line1[0][0]
    l1p1y = line1[0][1]
    l1p2x = line1[1][0]
    l1p2y = line1[1][1]
    # make sure p1x < p2x
    if l1p1x > l1p2x:
        tmp = l1p1x
        l1p1x = l1p2x
        l1p2x = tmp
    # make sure p1y < p2y
    if l1p1y > l1p2y:
        tmp = l1p1y
        l1p1y = l1p2y
        l1p2y = tmp
    l2p1x = line2[0][0]
    l2p1y = line2[0][1]
    l2p2x = line2[1][0]
    l2p2y = line2[1][1]
    # make sure p1x < p2x
    if l2p1x > l2p2x:
        tmp = l2p1x
        l2p1x = l2p2x
        l2p2x = tmp
    # make sure p1y < p2y
    if l2p1y > l2p2y:
        tmp = l2p1y
        l2p1y = l2p2y
        l2p2y = tmp

    # line2 rectangle is inside line1 rect
    if l1p1x < l2p2x and l1p2x > l2p1x and l1p1y < l2p2y and l1p2y > l2p1y:
        return True
    # line2 rectangle is inside line1 rect
    if l1p1x > l2p2x and l1p2x < l2p1x and l1p1y > l2p2y and l1p2y < l2p1y:
        return True
    if l1p1x > l2p2x or l1p2x < l2p1x:
        return False
    if l1p1y > l2p2y or l1p2y < l2p1y:
        return False
    return True

if __name__ == '__main__':
    matplotlib.pyplot.plot((line1[0][0],line1[1][0]),(line1[0][1],line1[1][1]))
    matplotlib.pyplot.hold(True)

    matplotlib.pyplot.plot((line2[0][0],line2[1][0]),(line2[0][1],line2[1][1]))
    print(overlap())
    matplotlib.pyplot.show()
