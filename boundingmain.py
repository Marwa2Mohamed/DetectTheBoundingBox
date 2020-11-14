import bounding
from bounding import BoundingBoxStraightLine
def findTheSlope(X, Y):
    slope = Y / X
    assert slope
    print(slope)
# the function ends
# the actual code
straightLineBox = BoundingBoxStraightLine(0, 1, 3, 7)
findTheSlope(straightLineBox.getDeltaX(), straightLineBox.getDeltaY())
