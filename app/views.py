from app import app, db
from app.models import Article
from app.forms import ArticleForm

from datetime import datetime
import json
import uuid

from flask import render_template, request, abort
from slugify import slugify


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/create_article', methods=['POST'])
def create_article():
    title = request.form['title']
    signature = request.form['signature']
    body = request.form['body']
    dt = datetime.now()
    slug = slugify('{}-{}-{}-{}-{}-{}'.format(title, dt.month, dt.day,
                                              dt.hour, dt.minute, dt.second))
    owner_id = request.cookies.get('owner_id')
    if owner_id == 'undefined':
        owner_id = str(uuid.uuid4())
    article = Article(title=title, signature=signature, body=body,
                      slug=slug, owner_id=owner_id)
    db.session.add(article)
    db.session.commit()
    return json.dumps({'status': 'OK', 'slug': slug, 'owner_id': owner_id})


@app.route('/<slug>')
def view_article(slug):
    article = Article.query.filter_by(slug=slug).first_or_404()
    user_id = request.cookies.get('owner_id')
    return render_template('article.html', article=article, user_id=user_id)


@app.route('/<slug>/update', methods=['POST', 'GET'])
def update_article(slug):
    article = Article.query.filter_by(slug=slug).first_or_404()
    user_id = request.cookies.get('owner_id')
    if not article.is_owner(user_id):
        abort(401)

    if request.method == 'GET':
        form = ArticleForm(obj=article)
        return render_template('update_article.html', form=form)
    else:
        article.title = request.form['title']
        article.signature = request.form['signature']
        article.body = request.form['body']
        db.session.commit()
        return json.dumps({'status': 'OK', 'slug': slug})
