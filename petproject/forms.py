from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import InputRequired, URL, NumberRange

class NewPetForm(FlaskForm):

    name = StringField(label="Name:", validators=[InputRequired()])
    species = StringField(label='Species:', validators=[InputRequired()])
    photo_url = StringField(label="Photo URL", validators=[URL()])
    age = IntegerField(label="Age:", validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField(label='Notes:')
    submit = SubmitField()