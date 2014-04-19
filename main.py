import config
from cached import app

app.config.from_object(config)

if __name__ == '__main__':
	port = app.config.get('port', 8000)
	app.run(host='0.0.0.0', port=port, debug=True, use_reloader=False)

