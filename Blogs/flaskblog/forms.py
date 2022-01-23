from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField ,PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import  DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistratonForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),  Length(min=2, max=20)])

    email = StringField('Email',validators=[DataRequired(),Email()])

    password = PasswordField('Password',validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validation_username(Self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. please choose a different one.')
            
    def validation_email(Self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. please choose a different one.')
class LoginForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])

    password = PasswordField('Password',validators=[DataRequired()])

    remember = BooleanField('RememberMe')

    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),  Length(min=2, max=20)])

    email = StringField('Email',validators=[DataRequired(),Email()])

    picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('Update')

    def validation_username(Self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. please choose a different one.')
                
    def validation_email(Self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. please choose a different one.')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Post')