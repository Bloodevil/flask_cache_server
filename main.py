from flask import Flask
from cached.pages import pages

app = Flask(__name__)
app.register_blueprint(pages)
app.config['target_domain'] = "http://eat.beramodes.com"
app.config['server'] = "http://beramodes.com:8000"

if __name__ == '__main__':
	port = app.config.get('port', 8000)
	app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)

