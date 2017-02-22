from wtforms import Form, StringField, TextAreaField
from wtforms.validators import Length, Required


class ArticleForm(Form):
    title = StringField('Title',
                        [Required(message='Content is empty'),
                         Length(max=200,
                                message='Title must be less than 200 characters')])
    signature = StringField('Signature', [Length(max=255)])
    body = TextAreaField('Story', [Required(message='Content is empty')])
