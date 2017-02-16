from wtforms import Form, StringField, TextAreaField
from wtforms.validators import Length, Required


class ArticleForm(Form):
    title = StringField('Title' , [Length(min=1, max=200,
        message='Title is too small')])
    signature = StringField('Signature', [Length(max=255)])
    body = TextAreaField('Story', [Required(message='Content is empty')])
