from app import app, db
from app.models import Article
from app.forms import ArticleForm

from datetime import datetime
import json
import uuid

from flask import render_template, request, abort, current_app, redirect
from slugify import slugify


@app.route('/', methods=['POST', 'GET'])
def create_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        dt = datetime.now()
        slug = slugify('{}-{}-{}-{}-{}-{}'.format(form.title, dt.month, dt.day,
                                                  dt.hour, dt.minute, dt.second))
        owner_id = request.cookies.get('owner_id')
        if owner_id == 'undefined':
            owner_id = str(uuid.uuid4())
        article = Article(title=form.title.data, signature=form.signature.data,
                body=form.body.data, slug=slug, owner_id=owner_id)
        db.session.add(article)
        db.session.commit()
        response = current_app.make_response(redirect(slug))
        response.set_cookie('owner_id', owner_id)
        return response
    return render_template('create_article.html', form=form)


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
        form = ArticleForm(request.form)
        if request.method == 'POST' and form.validate():
            article.title = form.title.data
            article.signature = form.signature.data
            article.body = form.body.data
            db.session.commit()
            return redirect(slug)
        return render_template('update_article.html', form=form)
