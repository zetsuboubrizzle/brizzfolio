from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectMultipleField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, AnyOf


class ContactForm(FlaskForm):
    name = StringField('Your Name: (Required)', validators=[DataRequired()])
    email = StringField('Your Email (Required)', validators=[DataRequired(), Email()])
    subject = StringField('Subject')
    message = TextAreaField('Your Message')
    submit = SubmitField('Send Message')