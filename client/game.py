import requests

from client.game_board import MyApp, tki

CANVAS_SIZE = 500

option_owner = requests.get(url='http://localhost:3000//trainers', verify=False).json()


def init_game():
    root = tki.Tk()
    root.title("Pokemon :)")

    canvas = tki.Canvas(width=CANVAS_SIZE * 2.7, height=CANVAS_SIZE, highlightbackground='black')
    canvas.pack()
    img = tki.PhotoImage(file="pokemon.png")
    canvas.create_image(50, 1, image=img, anchor=tki.NW)

    label2 = tki.Label(text="choose trainer:", font=('Helvetica', 12), fg='blue')
    label2.pack(side="top")

    variable = tki.StringVar(root)
    variable.set(option_owner[0])

    opt = tki.OptionMenu(root, variable, *option_owner)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()

    def ok():
        print("owner is", variable.get())
        canvas.destroy()
        label2.destroy()
        opt.destroy()
        button.destroy()
        game = MyApp(root, variable.get())

    button = tki.Button(root, text="START GAME", command=ok)
    button.pack()

    root.mainloop()


init_game()
