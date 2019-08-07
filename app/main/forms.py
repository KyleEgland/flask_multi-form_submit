#! python
#
# forms.py <= main
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import IntegerField
from wtforms.validators import DataRequired
from wtforms.validators import Length


class UserInfo(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UserContact(FlaskForm):
    email = StringField('Username', validators=[DataRequired()])
    phone = StringField('First Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UserAddr(FlaskForm):
    street = StringField('Street', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField(
        'State',
        validators=[DataRequired(), Length(min=2, max=2)]
    )
    zip = IntegerField('Zip', validators=[DataRequired()])
    submit = SubmitField('Submit')
