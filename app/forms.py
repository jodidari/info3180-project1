from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired,DataRequired,Email
from flask_wtf.file import FileField,FileAllowed,FileRequired


class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired('Please provide a firstname')])
    lastname = StringField('Last Name', validators=[DataRequired('Please provide a lastname')])
    gender = SelectField('Gender',choices=[('S','Select Gender'),('M','Male'), ('F','Female')],validators=[DataRequired('Select a gender')])
    email = StringField('Email Address', validators=[Email(message='This is not a valid email'), DataRequired('Please provide an email address')])
    location = StringField('Location',validators=[DataRequired('Please enter a location')])
    bio = TextAreaField('Biography',validators=[DataRequired('Please enter a bio')])
    photo= FileField('images', 
    validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'], 'Only jpg,jpeg and png images can be uploaded!')])


   