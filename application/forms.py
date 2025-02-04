from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users
from flask_login import LoginManager, current_user



class PostForm(FlaskForm):
    title = StringField('Title',
        validators=[
                DataRequired(),
                Length(min=4, max=100)
        ]
    )
    content = StringField('Content',
        validators=[
                DataRequired(),
                Length(min=4, max=100)
        ]
    )

    submit = SubmitField('Post Content')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    first_name = StringField('First Name',
        validators=[
                DataRequired(),
                Length(min=4, max=30)
        ]
    )
    last_name = StringField('Last Name',
        validators=[
                DataRequired(),
                Length(min=4, max=30)
        ]
    )
    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(min=4, max=30)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=4, max=30)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')
    submit = SubmitField('Update')
