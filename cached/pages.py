# -*- coding: utf-8 -*-
from flask import Blueprint, Flask, current_app as app
from .model import Post
from .tumblr import crawl_post

pages = Blueprint('pages', __name__)
domain = app.config.get('domain')

@pages.route('/')
@pages.route('/<path:url>')
def post(url=''):
	post = Post.collection.find_one({'url':url})
	if not post:
		post = crawl_post(domain+'/'+url)
	return post
