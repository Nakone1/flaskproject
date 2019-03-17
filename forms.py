from flask_wtf import FlaskForm
from wtfforms import StringField, PasswordField, SubmitField, BooleanField
from wtfforms.validators import DataRequired, Length, Email, EqualTo

#Форма регистрации
class RegistratinForm(FlaskForm):

	username = StringField('Username', 
							validators=[DataRequired(), Length(min=2, max=20)])
	#максимальная длина=20, мин длина= 2, DataRequired() отвечает за то, чтобы поле не было пустым
	email = StringField('Email', 
							validators=[DataRequired(), Email()])
	password = PasswordField('Password' 
							validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password' 
							validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

#форма логина
class LoginForm(FlaskForm):

	email = StringField('Email', 
							validators=[DataRequired(), Email()])
	password = PasswordField('Password' 
							validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')