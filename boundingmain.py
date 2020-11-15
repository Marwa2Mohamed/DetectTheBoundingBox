import cgi
import re

# the function starts
def findTheSlope(bottomLeftX, bottomLeftY, topRightX, topRightY):

        # Here I am testing that the type error is handled
        list = [bottomLeftX, bottomLeftY, topRightX, topRightY]
        for l in list:
            if type(l) is str and re.match(r'^-?\d+(?:\.\d+)?$', l) is None:  # Here only strings which can be numbers are accepted
                raise TypeError("only real coordinates number like 1 or 1.0 or 1.4 ..etc are acceptable")
            if type(l) is not float and type(l) is not int and type(l) is not str:
                raise TypeError("only real coordinates number like 1 or 1.0 or 1.4 ..etc are acceptable")



        # When checking is ok
        SbottomLeftX = float(bottomLeftX)
        SbottomLeftY = float(bottomLeftY)
        StopRightX = float(topRightX)
        StopRightY = float(topRightY)
        X = StopRightX - SbottomLeftX
        Y = StopRightY - SbottomLeftY

        # Checking that the user draw a box not a straight line
        if Y == 0:
            raise ValueError("Vertical straight lines aren't boxes")
        if X == 0:
            raise ZeroDivisionError("Horizontal straight lines aren't boxes")
        slope = Y / X
        return slope

# the function ends

# the actual code starts
# #!/usr/bin/python
# print ("Content-type:text/html\r\n\r\n")
# form = cgi.FieldStorage()
# bottomLeftX = form.getvalue('bottomLeftX')
# bottomLeftY  = form.getvalue('bottomLeftY')
# topRightX = form.getvalue('topRightX')
# topRightY= form.getvalue('topRightY')
#
# print(bottomLeftX)
# print(bottomLeftY)
# print(topRightX)
# print(topRightY)

result = findTheSlope(0,1,3,7)
print(result) #justForTesting

#the actual code ends

