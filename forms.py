from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddPersonForm(FlaskForm):
    title=StringField('Enter details', validators=[DataRequired()])
    submit=SubmitField('Submit')