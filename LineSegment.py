import Coordinate

__author__ = 'xiongyi'

class LineSegment:
    def __init__(self):
        self.sx = 0.0
        self.sy = 0.0
        self.ex = 0.0
        self.ey = 0.0

    def __init__(self, sx1, sy1, ex1, ey1):
        self.sx = sx1
        self.sy = sy1
        self.ex = ex1
        self.ey = ey1

    def checkLineSegCross(self, line2):
        line1in = [(self.sx,self.sy), (self.ex,self.ey)]
        line2in = [(line2.sx,line2.sy), (line2.ex,line2.ey)]
        pt = LineSegment.segment_intersect(line1in, line2in)
        return pt

    @staticmethod
    def __lineSegIntersectFastPreTestStep1(line, ptx, pty):
        p1x = line[0][0]
        p1y = line[0][1]
        p2x = line[1][0]
        p2y = line[1][1]
        # make sure p1x < p2x
        if p1x > p2x:
            tmp = p1x
            p1x = p2x
            p2x = tmp
        # make sure p1y < p2y
        if p1y > p2y:
            tmp = p1y
            p1y = p2y
            p2y = tmp

        if p1x < ptx and p2x > ptx:
            if p1y < pty and p2y > pty:
                return True


    @staticmethod
    def lineSegIntersectFastPreTest(line1, line2):
        if LineSegment.__lineSegIntersectFastPreTestStep1(line2, line1[0][0], line1[0][1]):
            return True
        if LineSegment.__lineSegIntersectFastPreTestStep1(line2, line1[1][0], line1[1][1]):
            return True
        return False

    @staticmethod
    def segment_intersect(line1, line2) :
        if not LineSegment.lineSegIntersectFastPreTest(line1, line2):
            return None

        intersection_pt = LineSegment.line_intersect(line1, line2)

        # print( line1[0][0], line1[1][0], line2[0][0], line2[1][0], intersection_pt[0] )
        # print( line1[0][1], line1[1][1], line2[0][1], line2[1][1], intersection_pt[1] )

        if (line1[0][0] < line1[1][0]) :
            if intersection_pt[0] < line1[0][0] or intersection_pt[0] > line1[1][0] :
             # print( 'exit 1' )
             return None
        else :
          if intersection_pt[0] > line1[0][0] or intersection_pt[0] < line1[1][0] :
             # print( 'exit 2' )
             return None

        if (line2[0][0] < line2[1][0]) :
            if intersection_pt[0] < line2[0][0] or intersection_pt[0] > line2[1][0] :
                # print( 'exit 3' )
                return None
        else :
            if intersection_pt[0] > line2[0][0] or intersection_pt[0] < line2[1][0] :
                # print( 'exit 4' )
                return None

        return intersection_pt

    @staticmethod
    def slope(p1, p2) :
        limit =  10e-7
        if p2[0] - p1[0] < limit:
            return 1/limit
        if p2[1] - p1[1] < 10e-7:
            return limit
        return (p2[1] - p1[1]) * 1. / (p2[0] - p1[0])

    @staticmethod
    def y_intercept(slope, p1) :
       return p1[1] - 1. * slope * p1[0]

    @staticmethod
    def line_intersect(line1, line2) :
       min_allowed = 1e-6   # guard against overflow
       big_value = 1e6   # use instead (if overflow would have occurred)
       m1 = LineSegment.slope(line1[0], line1[1])
       # print( 'm1: %d' % m1 )
       b1 = LineSegment.y_intercept(m1, line1[0])
       # print( 'b1: %d' % b1 )
       m2 = LineSegment.slope(line2[0], line2[1])
       # print( 'm2: %d' % m2 )
       b2 = LineSegment.y_intercept(m2, line2[0])
       # print( 'b2: %d' % b2 )
       if abs(m1 - m2) < min_allowed :
          x = big_value
       else :
          x = (b2 - b1) / (m1 - m2)
       y = m1 * x + b1
       y2 = m2 * x + b2
       # print( '(x,y,y2) = %d,%d,%d' % (x, y, y2))
       return (int(x),int(y))
