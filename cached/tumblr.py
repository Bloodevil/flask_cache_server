from model import Post
from datetime import datetime
import requests

def crawl_post(url):
	r = requests.get(url)
	if r.status_code >= 200 and r.status_code <= 300:
		content = r.content.replace(app.config.get('target_domain'), app.config.get('server'))
		post = {'created': datetime.now(),
			'modified': None,
			'url' : url,
			'content' : content}
		Post.collection.save(post)
	else:
		content = r.content
	return content
