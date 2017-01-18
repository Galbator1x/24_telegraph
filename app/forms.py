from wtforms import Form, StringField, TextAreaField


class ArticleForm(Form):
    title = StringField('Title')
    signature = StringField('Signature')
    body = TextAreaField('Story')
