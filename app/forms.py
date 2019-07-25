from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired as Required


class LoginForm(Form):
    """ Login and sign up form """

    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('GO')
