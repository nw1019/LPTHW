from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map
import lexicon

app = Flask(__name__)
#Keep the scene's data
@app.route('/game', methods=['GET'])
def game_get():
	if 'scene' in session:
		thescene = map.SCENES[session['scene']]
		return render_template('show_scene.html', scene=thescene)

	else:
		# The user doesn't have a session...
		# What should your code do in response?
		# session.pop('scene')
		return render_template('you_died.html')

@app.route('/game', methods=['POST'])
def game_post():

	userinput = request.form.get('userinput')
	userinput2 = lexicon.clasify(userinput)

	if 'scene' in session:
		if userinput is None:
	# Weird, a POST request to /game with no user input... what should your code do?
			return render_template('you_died.html')
		else:
			currentscene = map.SCENES[session['scene']]
			nextscene = currentscene.go(userinput2)

			if nextscene is None:
		# There's no transition for that user input.
		# what should your code do in response?
				return render_template('you_died.html')
			else:
				session['scene'] = nextscene.urlname
				return render_template('show_scene.html', scene=nextscene)

	else:

		# There's no session, how could the user get here?
		# What should your code do in response?
			return render_template('you_died.html')
# This URL initializes the session with starting values


@app.route('/')
def index():
	session['scene'] = map.START.urlname
	return redirect(url_for('game_get')) # redirect the browser to the url for game_get
app.secret_key = 'replace this with your secret key'
if __name__ == "__main__":
	app.run()
