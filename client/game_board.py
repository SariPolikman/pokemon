import tkinter as tki

import random

import requests

from client.utills import is_pokemon_catch

CANVAS_SIZE = 500
IMAGE_SIZE = 70
STEP_SIZE = 5


class MyApp:

    def __init__(self, parent, owner):

        self._parent = parent

        # add a canvas to draw on

        self._canvas = tki.Canvas(parent, width=CANVAS_SIZE, height=CANVAS_SIZE, highlightbackground='blue')

        self._canvas.pack()

        res = requests.get(url=f"http://localhost:3000//pokemons?all=id", verify=False)
        content = res.json()

        self._pokemons_not_own = content
        self.owner_name = owner
        a = requests.get(url=f"http://localhost:3000/pokemons?t_name={self.owner_name}", verify=False).json()

        self._pokemons_not_own = list(set(self._pokemons_not_own) - set(a))
        list_ = ' '.join(map(str, a))

        # add a button
        button_add = tki.Button(parent, text="Add", command=self._add_pokemon, \
                                font=('comicsans', 18), fg='blue', bg='turquoise')
        button_add.pack(side="left", padx=10, pady=10)

        button_up = tki.Button(parent, text="^", command=lambda: self._step("up"), bg='pink', width=4, height=2)
        button_up.pack(side="top", padx=10, pady=10)

        button_down = tki.Button(parent, text="\/", command=lambda: self._step("down"), bg='pink', width=4, height=2)
        button_down.pack(side="bottom", padx=10, pady=10)

        button_right = tki.Button(parent, text=">", command=lambda: self._step("right"), bg='pink', width=4, height=2)
        button_right.pack(side="right", padx=100, pady=10)

        button_left = tki.Button(parent, text="<", command=lambda: self._step("left"), bg='pink', width=4, height=2)
        button_left.pack(side="right", padx=100, pady=10)

        self._balls = {}

        self.images = {i: f"{i}.png" for i in range(1, 9)}
        self.photo = {i: tki.PhotoImage(file=self.images[i]) for i in range(1, 9)}
        print(self.images)
        print(self.photo)

        self.owner_name = owner
        self.list = ["owner.png"]
        self.image_owner = tki.PhotoImage(file="owner.png")  # Use self.image

        self._owner = (self._canvas.create_image(10, 10, image=self.image_owner, anchor=tki.NW))

        self._move()

    def get_new_pokemon(self):
        id = random.choice(self._pokemons_not_own)
        self._pokemons_not_own.remove(id)
        return id

    def _add_pokemon(self):
        x = random.randrange(CANVAS_SIZE - IMAGE_SIZE)
        y = random.randrange(CANVAS_SIZE - IMAGE_SIZE)
        id = self.get_new_pokemon()
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        id_img = random.choice(a)
        self._balls[id] = (self._canvas.create_image(x, y, image=self.photo[id_img], anchor=tki.NW))
        self._balls[id]

    def _move(self):

        for ball in self._balls.values():
            x, y = self._canvas.coords(ball)
            dx = int((random.random() - 0.5) * 5 * STEP_SIZE)
            dy = int((random.random() - 0.5) * 5 * STEP_SIZE)

            if x + dx < 0 or x + IMAGE_SIZE + dx > CANVAS_SIZE:
                dx = 0

            if y + dy < 0 or y + IMAGE_SIZE + dy > CANVAS_SIZE:
                dy = 0

            self._canvas.move(ball, dx, dy)
        self._parent.after(250, self._move)


    def whose_pokemon_catch(self):

        owner_points = {'x': self._canvas.coords(self._owner)[0], 'y': self._canvas.coords(self._owner)[1]}

        for id_, pokemon in self._balls.items():
            poke_points = {'x': self._canvas.coords(pokemon)[0], 'y': self._canvas.coords(pokemon)[1]}

            if is_pokemon_catch(owner_points, poke_points):
                return id_
        return None

    def _step(self, direction):
        x1, y1 = self._canvas.coords(self._owner)

        dy = 0
        dx = 0

        cases = {
            "up": (lambda x, y: (x, y - 10))(dx, dy),
            "down": (lambda x, y: (x, y + 10))(dx, dy),
            "right": (lambda x, y: (x + 10, y))(dx, dy),
            "left": (lambda x, y: (x - 10, y))(dx, dy)
        }

        dx, dy = cases[direction]

        if x1 + dx < 0 or x1 + IMAGE_SIZE + dx > CANVAS_SIZE:
            dx = 0

        if y1 + dy < 0 or y1 + IMAGE_SIZE + dy > CANVAS_SIZE:
            dy = 0

        self._canvas.move(self._owner, dx, dy)

        pokemon_id = self.whose_pokemon_catch()
        if pokemon_id:
            img = tki.PhotoImage(file="yay.png")
            ing_yay = self._canvas.create_image(70, 70, image=img, anchor=tki.NW )
            self._parent.after(5000, lambda: self._canvas.delete(ing_yay))

            requests.post(f"http://localhost:3000/pokemons/{pokemon_id}/{self.owner_name}")

            self._canvas.delete(self._balls[pokemon_id])  # delete pokemon that caught
            self._balls.pop(pokemon_id)
