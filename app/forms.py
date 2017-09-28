from flask_wtf import FlaskForm
from wtforms import IntegarField
from wtforms.validators import InputRequired

class DelayForm(FlaskForm):
    delay = IntegerField('Delay', validators=[InputRequired()])
