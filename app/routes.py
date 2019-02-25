from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	''' variables '''
	user = {'username':'miguel'}
	posts = [
		{
			'author':{'username':'James'},
			'body': 'Beauty and the Beast is the best disney movie!'
		},
		{
			'author':{'username', 'Betty'},
			'body':'Cant wait to see Free solo!'
		}
	]
	return render_template('index.html', user=user, posts=posts)