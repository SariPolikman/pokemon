import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    db="pokemondb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def find_heaviest_pokemon():
    try:
        with connection.cursor() as cursor:
            query = "SELECT name FROM pokemon WHERE weight = (SELECT max(weight) FROM pokemon)"
            cursor.execute(query)
            result = cursor.fetchall()
            return result[0]['name']


    except Exception as e:
        print(e)


def find_by_type(type_):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT p.name FROM pokemon AS p JOIN type_poke AS tp ON p.id = tp.p_id WHERE tp.type = '{type_}'"
            cursor.execute(query)
            res = cursor.fetchall()
            result = []
            for i in res:
                result.append(i['name'])
            return result


    except Exception as e:
        print(e)


def find_owners(pokemon):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT tp.t_name FROM pokemon AS p JOIN trainer_pokemon AS tp ON tp.p_id = p.id WHERE p.name = '{pokemon}'"
            cursor.execute(query)
            res = cursor.fetchall()
            result = []
            for i in res:
                result.append(i['t_name'])
            return result

    except Exception as e:
        print(e)


def find_roster(roster):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT p.name FROM pokemon AS p JOIN trainer_pokemon AS tp ON tp.p_id = p.id WHERE tp.t_name = '{roster}'"
            cursor.execute(query)
            res = cursor.fetchall()
            result = []
            for i in res:
                result.append(i['name'])
            return result

    except Exception as e:
        print(e)


print(find_heaviest_pokemon())
print(find_by_type("grass"))
print(find_owners("gengar"))
print(find_roster("Loga"))
