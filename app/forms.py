from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter a valid email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
  submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired("Enter email address"), Email("Enter email address")])
  password = PasswordField('Password', validators=[DataRequired("Enter Password")])
  submit = SubmitField("Sign in")

class HeroForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired("Please input hero name.")])
  age = StringField('Age', validators=[DataRequired("Please input hero age.")])
  url = StringField('Url', validators=[DataRequired("Please input hero image url.")])
  affiliation = StringField('Affiliation', validators=[DataRequired("Please input hero affiliation.")])
  description = StringField('Description', validators=[DataRequired("Please input hero description.")])
  submit = SubmitField("Submit")

class PlayerForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired("Please input player name.")])
  level = StringField('Level', validators=[DataRequired("Please input player level.")])
  url = StringField('Url', validators=[DataRequired("Please input player image url.")])
  server = StringField('Server', validators=[DataRequired("Please input player server.")])
  submit = SubmitField("Submit")

class AchievementForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired("Please input achievement name.")])
  description = StringField('Description', validators=[DataRequired("Please input achievement description.")])
  type = StringField('Type', validators=[DataRequired("Please input achievement type")])
  url = StringField('Url', validators=[DataRequired("Please input achievement image url.")])
  submit = SubmitField("Submit")

class RewardForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired("Please input reward name.")])
  quality = StringField('Quality', validators=[DataRequired("Please input reward quality.")])
  cost = IntegerField('Cost', validators=[DataRequired("Please input reward cost")])
  url = StringField('Url', validators=[DataRequired("Please input reward image url.")])
  submit = SubmitField("Submit")

class DeleteForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired("Please input name of entity to delete.")])
  model = StringField('Model', validators=[DataRequired("Please input model/category of entity to delete i.e. Hero, Player, Achievement, Reward.")])
  submit = SubmitField("Delete")
