import numpy as num
__author__ = 'xiongyi'
class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def intersect(self, other):
        '''Where do lines self and other intersect?
        '''
         #-- 1 --
        # [ if self and other have the same slope ->
        #     raise ValueError
        #   else -> I ]
        if self.a * other.b == other.a * self.b:
            raise ValueError("Lines have the same slope.")
        #-- 2 --
        # [ x, y  :=  solution to the simultaneous linear equations
        #       (self.a * x + self.b * y = -self.c) and
        #       (other.a * x + other.b * y = -other.c) ]
        a = num.array ( ( (self.a, self.b), (other.a, other.b) ) )
        b = num.array ( (-self.c, -other.c) )
        x, y = num.linalg.solve(a,b)

        #-- 3 --
        return (x, y)



if __name__ == '__main__':
    line1 = Line(0, 0.5, -2)
    line2 = Line(1, 0, -3)
    print( Line.intersect(line1, line2))
