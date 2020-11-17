from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
class CoordinatesForm(FlaskForm):
    bottomLeftX = StringField("bottomLeftX", validators=[DataRequired()])
    bottomLeftY = StringField("bottomLeftY", validators=[DataRequired()])
    topRightX = StringField("topRightX", validators=[DataRequired()])
    topRightY = StringField("topRightY", validators=[DataRequired()])
    submit = SubmitField('SUBMIT')