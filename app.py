import json

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import app
from database import Game, db



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/addgame', methods=['POST', 'GET'])
def add_game():
    if request.method == "POST":
        name = request.form['name']
        cost = request.form['cost']
        game_description = request.form['text']
        url = request.form['url']
        platform = request.form['platform']
        developers = request.form['developers']
        genre = request.form['genre']
        min_requirements = {'os': request.form['os_min'],
                            'processor': request.form['processor_min'],
                            'ram': request.form['ram_min'],
                            'graphics': request.form['graphics_min'],
                            'directx': request.form['directx_min'],
                            'network': request.form['network_min'],
                            'storage': request.form['storage_min']}
        sug_requirements = {'os': request.form['os_sug'],
                            'processor': request.form['processor_sug'],
                            'ram': request.form['ram_sug'],
                            'graphics': request.form['graphics_sug'],
                            'directx': request.form['directx_sug'],
                            'network': request.form['network_sug'],
                            'storage': request.form['storage_sug']}

        min_requirements = json.dumps(min_requirements)
        sug_requirements = json.dumps(sug_requirements)
        print("Min parameters: " + min_requirements)
        print(type(min_requirements))
        game = Game(name=name, cost=cost, game_description=game_description, url=url,
                    platform=platform, developers=developers, genre=genre, min_requirements=min_requirements,
                    sug_requirements=sug_requirements)
        print(game.id)
        print(request.values)
        try:
            db.session.add(game)
            db.session.commit()
            print('saved')
            return redirect('/index')
        except Exception as e:
            print("There is a mistake!")
            print(e)
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

@app.route('/testgame')
def test():
    games = Game.query.get()
    return render_template('game_page.html')


if __name__ == "__main__":
    app.run(debug=True)
