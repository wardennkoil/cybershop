from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/cyber.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    text = db.Column(db.Text, nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Game %r>' % self.id


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/addgame', methods=['POST', 'GET'])
def add_game():
    if request.method == "POST":
        name = request.form['name']
        cost = request.form['cost']
        text = request.form['text']
        game = Game(name=name, cost=cost, text=text)
        try:
            db.session.add(game)
            db.session.commit()
            print('saved')
            return redirect('/index')
        except:
            print("There is a mistake!")
    else:
        return render_template("addgame.html")


@app.route('/games')
def games_page():
    games = Game.query.all()
    return render_template('games.html', list_of_games=games)


@app.route('/games/<int:id>')
def full_page(id):
    game = Game.query.get(id)
    return render_template('game_page.html', game=game)


if __name__ == "__main__":
    app.run(debug=True)
