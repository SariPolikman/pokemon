import json

from flask import Flask, Response, request

import db.pokemon
import db.trainer
import pokeApi

app = Flask(__name__)


@app.route('/')
def home():
    return Response("welcome to pokemon!!!"), 200


@app.route('/pokemons', methods=["POST"])
def add():
    pokemon = request.get_json()
    db.pokemon.add(pokemon)

    return Response(f"pokemon {pokemon['id']} Successfully created"), 201


@app.route('/pokemons')
def get():
    args = dict(request.args)
    print(args)
    cases = {"pid": db.pokemon.get_id, "t_name": db.pokemon.get_trainer, "all": db.pokemon.get_all}

    choise = [key for key in cases.keys() if args.get(key)]
    print(choise)
    arg = args.get(choise[0])
    res = cases[choise[0]](arg)
    return json.dumps(res), 200


@app.route('/pokemons/<pid>/<trainer>', methods=["DELETE"])
def delete(pid, trainer):
    db.pokemon.delete(pid, trainer)

    return Response(f"pokemon {pid} of trainer {trainer} Successfully deleted"), 200


@app.route('/evolve/<pid>/<owner>', methods=["PUT"])
def evolve(pid, owner):
    y = pokeApi.chain(pid)
    chain = y[1]
    old_name = y[0]
    while chain['species']['name'] != old_name:
        chain = chain['evolves_to'][0]
    if not chain['evolves_to']:
        return Response("error - enable to evolve "), 400
    new_name = chain['evolves_to'][0]['species']['name']
    poke = pokeApi.pokemon(new_name)

    try:
        db.pokemon.update_pokemon_trainer(poke['id'], pid, owner)
    except Exception as e:
        if e.args[0] != 1062:
            raise e

    return Response("Successfully evolved"), 200


@app.route('/trainers')
def all_trainers():
    names = db.trainer.get_names()
    print(names)
    return json.dumps(names)


@app.route('/trainers/<p_name>')
def trainers_(p_name):
    names = db.trainer.get_pokemons(p_name)
    print(names)
    return json.dumps(names)


@app.route('/pokemons/<pid>/<trainer>', methods=["POST"])
def add_trainer(pid, trainer):
    db.pokemon.add_trainer(pid, trainer)
    return Response(f"pokemon {pid} of trainer {trainer} Successfully created"), 201


if __name__ == '__main__':
    app.run(port=3000)
