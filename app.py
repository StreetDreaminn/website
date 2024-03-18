from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/anime')
def anime():
    return render_template('anime.html')

@app.route('/videogames')
def videogames():
    return render_template('videogames.html')

@app.route('/sports')
def sports():
    return render_template('sports.html')

if __name__ == "__main__":
    app.run(debug=True)