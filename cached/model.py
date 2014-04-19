from minimongo import Model, Index

class Post(Model):
	"""
	Post
		created
		modified
		url
		content
	"""
	class Meta:
		database = 'tumblr'
		collection = 'post'
		indices = (
			Index('created'),
			Index('modified'),
			Index('url')
		)
