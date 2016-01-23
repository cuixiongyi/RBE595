import Coordinate
import numpy as np
import math
__author__ = 'xiongyi'

class LineSegment:

    def __init__(self, sx1, sy1, ex1, ey1):
        self.sx = sx1
        self.sy = sy1
        self.ex = ex1
        self.ey = ey1
        self.a = ey1 - sy1
        self.b = sx1 - ex1
        self.c = ex1*sy1-sx1*ey1

    def checkLineSegCross(self, line2):
        pt = LineSegment.segment_intersect(self, line2)
        return pt

    @staticmethod
    def lineSegIntersectFastPreTest(line1, line2):
        l1p1x = line1.sx
        l1p1y = line1.sy
        l1p2x = line1.ex
        l1p2y = line1.ey
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
        l2p1x = line1.sx
        l2p1y = line1.sy
        l2p2x = line1.ex
        l2p2y = line1.ey
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

        # print(l1p1x, l1p1y, l1p2x, l1p2y)
        # print(l2p1x, l2p1y, l2p2x, l2p2y)
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

    @staticmethod
    def segment_intersect(line1, line2) :
        if not LineSegment.lineSegIntersectFastPreTest(line1, line2):
            # print("Seg pre-test pass")
            return None
        xy = LineSegment.line_intersect(line1, line2)
        if xy is None:
            # print("line parllal")

            return None
        xy = LineSegment.__segment_intersect_inner(line1, line2, xy)
        # if xy is None:
            # print('Seg interset inner pass')
        return xy


    @staticmethod
    def __segment_intersect_inner(line1, line2, xy) :

        limit = 10e-6

        if LineSegment.__segment_intersect_helper(line1, xy, limit):
            if LineSegment.__segment_intersect_helper(line2, xy, limit):
                return xy
        return None

    @staticmethod
    def __segment_intersect_helper(line, xy, limit):
        x = xy[0]
        y = xy[1]
        count = 0
        limX = min(math.fabs(x - line.sx), math.fabs(x - line.ex))
        limY = min(math.fabs(y - line.sy), math.fabs(y - line.ey))
        if limX > limit:
            if (line.sx < line.ex) :
                if x < line.sx or x > line.ex:
                    count += 1
                    return False
                    # print( 'exit 1' )
            elif x < line.ex or x > line.sx:
                    count += 1
                    return False

                    # print( 'exit 2' )
        elif limY > limit:
            if line.sy < line.ey:
                if y < line.sy or y > line.ey:
                    return False
            elif y > line.sy or y < line.ey:
                return False
        # else:
        #
        # if count == 2:
        #     return False

        return True

    @staticmethod
    def line_intersect(line1, line2):
        '''Where do lines self and other intersect?
        '''
         #-- 1 --
        # [ if self and other have the same slope ->
        #     raise ValueError
        #   else -> I ]
        if line1.a * line2.b == line2.a * line1.b:
            return None
        #-- 2 --
        # [ x, y  :=  solution to the simultaneous linear equations
        #       (self.a * x + self.b * y = -self.c) and
        #       (other.a * x + other.b * y = -other.c) ]
        a = np.array ( ( (line1.a, line1.b), (line2.a, line2.b) ) , dtype='float64')
        b = np.array ( (-line1.c, -line2.c) , dtype='float64')
        x, y = np.linalg.solve(a,b)

        #-- 3 --
        return (x, y)
