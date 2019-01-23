from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectMultipleField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, AnyOf


class ContactForm(FlaskForm):
    pass