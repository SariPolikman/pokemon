import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    db="pokemondb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)
def add(trainer):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM trainer WHERE name = '{trainer['name']}'")
        if not cursor.fetchall():
            trainer_query = f"INSERT into trainer VALUES('{trainer['name']}', '{trainer['town']}')"
            cursor.execute(trainer_query)
            connection.commit()


def get_pokemons(p_name):
    with connection.cursor() as cursor:
        query = f"SELECT tp.t_name FROM pokemon AS p JOIN trainer_pokemon AS tp ON tp.p_id = p.id WHERE p.name = '{p_name}'"
        cursor.execute(query)
        res = cursor.fetchall()
        return [i['t_name'] for i in res]


def get_names():
    with connection.cursor() as cursor:
        query = f"SELECT name FROM trainer"
        cursor.execute(query)
        res = cursor.fetchall()
        return [i['name'] for i in res]
        return res

