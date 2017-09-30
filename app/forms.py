from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, NumberRange

class DelayForm(FlaskForm):
    delay = StringField('Delay', validators=[InputRequired(), NumberRange(min=0, max=None, message='Must be number > 0')])
