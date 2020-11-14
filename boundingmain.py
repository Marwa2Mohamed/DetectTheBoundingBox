import bounding
from bounding import BoundingBoxStraightLine

# the function starts
def findTheSlope(X, Y):
        if Y == 0:
            raise ValueError("Vertical straight lines aren't boxes")
        if X == 0:
            raise ZeroDivisionError("Horizontal straight lines aren't boxes")
        slope = Y / X
        return slope

# the function ends

# the actual code starts
straightLineBox = BoundingBoxStraightLine(0, 1, 3, 1)
result = findTheSlope(straightLineBox.getDeltaX(), straightLineBox.getDeltaY())
print(result) #justForTesting

#the actual code ends

