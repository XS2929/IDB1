from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter a valid email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
  submit = SubmitField('Sign up')

class LoginForm(Form):
  email = StringField('Email', validators=[DataRequired("Enter email address"), Email("Enter email address")])
  password = PasswordField('Password', validators=[DataRequired("Enter Password")])
  submit = SubmitField("Sign in")

class HeroForm(Form):
  name = StringField('Name', validators=[DataRequired("Please input hero name.")])
  age = StringField('Age', validators=[DataRequired("Please input hero age.")])
  url = StringField('url', validators=[DataRequired("Please input hero image url.")])
  affiliation = StringField('affiliation', validators=[DataRequired("Please input hero affiliation.")])
  description = StringField('description', validators=[DataRequired("Please input hero description.")])
  submit = SubmitField("Create")

class PlayerForm(Form):
  name = StringField('Name', validators=[DataRequired("Please input player name.")])
  level = StringField('Level', validators=[DataRequired("Please input player level.")])
  url = StringField('url', validators=[DataRequired("Please input player image url.")])
  server = StringField('server', validators=[DataRequired("Please input player server.")])
  submit = SubmitField("Create")

class AchievementForm(Form):
  name = StringField('Name', validators=[DataRequired("Please input achievement name.")])
  description = StringField('description', validators=[DataRequired("Please input achievement description.")])
  type = StringField('type', validators=[DataRequired("Please input achievement type")])
  url = StringField('url', validators=[DataRequired("Please input achievement image url.")])
  submit = SubmitField("Create")

class RewardForm(Form):
  name = StringField('Name', validators=[DataRequired("Please input reward name.")])
  quality = StringField('quality', validators=[DataRequired("Please input reward quality.")])
  cost = IntegerField('cost', validators=[DataRequired("Please input achievement cost")])
  url = StringField('url', validators=[DataRequired("Please input reward image url.")])
  submit = SubmitField("Create")

class DeleteForm(Form):
  name = StringField('Name', validators=[DataRequired("Please input name of entity to delete.")])
  model = StringField('Model', validators=[DataRequired("Please input model/category of entity to delete i.e. Hero, Player, Achievement, Reward.")])
  submit = SubmitField("Delete")
