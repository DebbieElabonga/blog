from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import Required,DataRequired, Length, Email, EqualTo
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class UploadBlog(FlaskForm):
    title = TextAreaField('Title:',validators=[DataRequired()])
    blog=TextAreaField('Write Blog:',validators=[DataRequired()])
    submit=SubmitField('Post Blog')

class CommentsForm(FlaskForm):
    comment=TextAreaField('Type comment:', validators=[DataRequired()])
    submit=SubmitField('Post Comment')