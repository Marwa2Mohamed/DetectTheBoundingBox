#!C:\Users\Marwa Mohamed\AppData\Local\Programs\Python\Python39\python.exe
print("Content-Type: text/html\n")
import re
from flask import Flask, render_template, request, Response

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



app = Flask(__name__)
@app.route("/", methods=["GET"])
def main():
    if request.method == "GET":
        bottomLeftX = request.args['bottomLeftX']
        bottomLeftY = request.args['bottomLeftY']
        topRightX = request.args['topRightX']
        topRightY = request.args['topRightY']
        result = findTheSlope(float(bottomLeftX), float(bottomLeftY), float(topRightX), float(topRightY))
        print("It worked!")
        return Response("test", status=200,mimetype="text/html")

    else:
        return render_template("index.html")

if __name__ =="__main__":
    app.run(debug=True)

#the actual code ends