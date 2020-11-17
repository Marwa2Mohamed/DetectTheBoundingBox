#!C:\Users\Marwa Mohamed\anaconda3\pkgs\python-3.7.6-h60c2a47_2\python.exe
print("Content-Type: text/html\n")
import re
import os
from flask import Flask, render_template, redirect, url_for, request
from forms import CoordinatesForm

result = 0.0
bottomLeftX = 0.0
bottomLeftY = 0.0
topRightX = 0.0
topRightY =0.0
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
        StopRightX = float(topRightX)
        SbottomLeftY = float(bottomLeftY)
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

app = Flask(__name__,template_folder='templates')

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/", methods=['GET','POST'])
def main():
    form = CoordinatesForm()
    if form.validate_on_submit():

        global bottomLeftX, bottomLeftY, topRightX, topRightY, result
        bottomLeftX = request.values['bottomLeftX']
        bottomLeftY = request.values['bottomLeftY']
        topRightX = request.values['topRightX']
        topRightY = request.values['topRightY']
        result = findTheSlope(bottomLeftX, bottomLeftY,topRightX, topRightY)
        return redirect(url_for('output'))
    return render_template('index.html', form = form)

@app.route("/output")
def output():
    return str(result)

if __name__ =="__main__":
    app.run(port=8080,debug=True)

#the actual code ends