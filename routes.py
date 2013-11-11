from run import app

@app.route('/')
def index():
	return "Yo"


if __name__ == '__main__':
	app.run()