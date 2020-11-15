import re
# Beginning of the BoundingBoxStraightLine class
class BoundingBoxStraightLine:

    def __init__(self, bottomLeftX, bottomLeftY, topRightX, topRightY):
        # Here I am testing that the type error is handled

        list = [bottomLeftX, bottomLeftY, topRightX, topRightY]
        for l in list:
            if type(l) is not float and type(l) is not int and type(l) is not str:
                raise TypeError("only real coordinates number like 1 or 1.0 or 1.4 ..etc are acceptable")

            if type(l) is str and re.match(r'^-?\d+(?:\.\d+)?$', l) is None: # Here only strings which can be numbers are accepted
                raise TypeError("only real coordinates number like 1 or 1.0 or 1.4 ..etc are acceptable")

        # After every thing is okay
        self.bottomLeftX = float(bottomLeftX)
        self.bottomLeftY = float(bottomLeftY)
        self.topRightX = float(topRightX)
        self.topRightY = float(topRightY)
        self.X = 0.0
        self.Y = 0.0
        self.calculateTheDeltas()


    def calculateTheDeltas(self):
        self.X = self.topRightX - self.bottomLeftX
        self.Y = self.topRightY - self.bottomLeftY

    def getDeltaX(self):
        return self.X

    def getDeltaY(self):
        return self.Y
# ending of BoundingBoxStraightLine class