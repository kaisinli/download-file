from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired

class DelayForm(FlaskForm):
    delay = IntegerField('Delay', validators=[InputRequired()])
