import json

import pymysql

import db.pokemon
import db.trainer

the_data = open("data.json")
pokemon_data = json.load(the_data)
the_data.close()

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="4321",
    db="pokemondb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def init_insert():
    for pokemon in pokemon_data:
        db.pokemon.add(pokemon)

        db.pokemon.insert_type_pokemon(pokemon['id'], pokemon['type'])

        for trainer in pokemon["ownedBy"]:
            db.trainer.add(trainer)

            pokemon.add_trainer(pokemon['id'], trainer['name'])


init_insert()