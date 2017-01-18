from wtforms import Form, StringField, TextAreaField


class ArticleForm(Form):
    title = StringField('Title')
    name = StringField('Name')
    body = TextAreaField('Story')
