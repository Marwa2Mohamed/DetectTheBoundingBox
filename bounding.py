
# Beginning of the BoundingBoxStraightLine class
class BoundingBoxStraightLine:

    def __init__(self, bottomLeftX, bottomLeftY, topRightX, topRightY):
        self.bottomLeftX = bottomLeftX
        self.bottomLeftY = bottomLeftY
        self.topRightX = topRightX
        self.topRightY = topRightY
        self.X = 0
        self.Y = 0
        self.calculateTheDeltas()


    def calculateTheDeltas(self):
        self.X = self.topRightX - self.bottomLeftX
        self.Y = self.topRightY - self.bottomLeftY

    def getDeltaX(self):
        return self.X

    def getDeltaY(self):
        return self.Y
# ending of BoundingBoxStraightLine class