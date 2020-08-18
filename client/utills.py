IMAGE_SIZE = 70


def is_pokemon_catch(loc_ball1, loc_ball2):
    return (loc_ball2['x'] < loc_ball1['x'] < loc_ball2['x'] + IMAGE_SIZE and \
            loc_ball2['y'] < loc_ball1['y'] < loc_ball2['y'] + IMAGE_SIZE)

