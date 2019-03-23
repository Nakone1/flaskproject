from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flasktest.models import User


#Форма регистрации
class RegistationForm(FlaskForm):
	username = StringField('Имя пользователя', 
							validators = [DataRequired(), Length(min=2, max=20)])
	#максимальная длина=20, мин длина= 2, DataRequired() отвечает за то, чтобы поле не было пустым
	email = StringField('Email почта', 
							validators = [DataRequired(), Email()])
	password = PasswordField('Пароль',
							validators = [DataRequired()])
	confirm_password = PasswordField('Подтверждение пароля' ,
							validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Зарегистрироваться')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Это имя уже занято. Пожалуйста, выберите другое.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email уже занят. Пожалуйста, выберите другое.')


#Форма логина
class LoginForm(FlaskForm):
    email = StringField('Email почта',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')