from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/projects/')
def hello():
	return 'The project page'
@app.route('/about')
def show_user_profile(id):
	return 'the about page'


if __name__ == '__main__':
	app.run(debug=True)