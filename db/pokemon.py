import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    db="pokemondb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def add(pokemon):
    with connection.cursor() as cursor:
        pokemon_query = f"INSERT into pokemon VALUES ({pokemon['id']}, '{pokemon['name']}', " \
                        f" {pokemon['height']}, {pokemon['weight']})"
        cursor.execute(pokemon_query)
        connection.commit()


def insert_type_pokemon(id, type):
    with connection.cursor() as cursor:
        pokemon_query = f"INSERT into type_poke VALUES ('{type}', {id})"
        cursor.execute(pokemon_query)
        connection.commit()


def delete(pid, trainer):
    with connection.cursor() as cursor:
        pokemon_query = f"DELETE FROM trainer_pokemon WHERE t_name = '{trainer}' AND p_id = {pid}"
        cursor.execute(pokemon_query)
        connection.commit()


def update_pokemon_trainer(pid_n, pid_o, owner):
    with connection.cursor() as cursor:
        pokemon_query = f"UPDATE trainer_pokemon SET p_id = {pid_n} " \
                        f"WHERE  p_id = {pid_o} AND t_name = '{owner}' "
        cursor.execute(pokemon_query)
        connection.commit()


def add_trainer(p_id, t_name):
    try:
        with connection.cursor() as cursor:
            linker_query = f"INSERT INTO trainer_pokemon VALUES({p_id} , '{t_name}')"
            cursor.execute(linker_query)
            connection.commit()
    except Exception as e:
        if e.args[0] != 1062:
            raise e


def get_id(pid):
    with connection.cursor() as cursor:
        linker_query = f"SELECT name FROM pokemon WHERE id = {pid}"
        cursor.execute(linker_query)
        res = cursor.fetchall()
        return res


def get_trainer(t_name):
    with connection.cursor() as cursor:
        query = f"SELECT p.id FROM pokemon AS p JOIN trainer_pokemon AS tp ON tp.p_id = p.id WHERE tp.t_name = '{t_name}'"
        cursor.execute(query)
        res = cursor.fetchall()
        return [i['id'] for i in res]


def get_all(col):
    with connection.cursor() as cursor:
        query = f"SELECT {col} FROM pokemon;"
        cursor.execute(query)
        res = cursor.fetchall()
        return [i[col] for i in res]
        # return res.value()