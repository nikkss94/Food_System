from tkinter import *
from pathlib import Path
from database import *
from api_controler import *


class UI():
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Food System")
        self.canvas = Canvas(self.tk, width=990, height=600)
        self.canvas.pack()
        self.name = StringVar()
        self.count = StringVar()
        self.result = []
        self.recipe_result = []

    def background(self, name):
        self.bg = PhotoImage(file=convert(name))
        self.canvas.create_image(0, 0, image=self.bg, anchor='nw')

    def start_window(self):
        self.canvas.delete("all")
        self.background("images/notebook.gif")
        self.canvas.create_text(
            450, 160, text="Enter your food:", font=('Tempus Sans ITC', 50), fill="red")
        self.entry()

    def entry(self):
        self.entry_1 = Entry(
            self.tk, textvariable=self.name, width=15, font=('Tempus Sans ITC', 20))
        self.entry_1.place(x=340, y=250)
        self.entry_2 = Entry(
            self.tk, textvariable=self.count, width=2, font=('Tempus Sans ITC', 20))
        self.entry_2.place(x=650, y=250)
        start_button = Button(self.tk, text="Commit", width=10,
                              command=self.get_text_entry, bg="black", fg="white", font=('Tempus Sans ITC', 15))
        start_button_window = self.canvas.create_window(
            850, 250, anchor='n', window=start_button)
        start_button = Button(self.tk, text="→", width=2,
                              command=self.food_search, bg="black", fg="red", font=('Tempus Sans ITC', 15))
        start_button_window = self.canvas.create_window(
            940, 560, anchor='n', window=start_button)

    def food_search(self):
        self.entry_1.destroy()
        self.entry_2.destroy()
        self.canvas.delete("all")
        self.background("images/cook.gif")
        b = BaseControler()
        self.recipe_result = b.findByIngredientsRequest(self.result, 0)
        self.print_recipes()

    def print_recipes(self):
        x = 0
        for recipe in self.recipe_result:
            self.canvas.create_text(
            400, 240 + x, text = recipe.getTitle(), font = ('Tempus Sans ITC', 30), fill = "black")
            x += 50

    def check(self):
        self.textvar = self.name.get()
        self.numbervar = self.count.get()
        f = True
        for i in self.numbervar:
            if i not in "1234567890":
                f = False
        if self.textvar == "" or self.numbervar == "":
            if f:
                return False
        return True

    def get_text_entry(self):
        if self.check():
            self.result += [self.textvar]
            self.textvar = ""
        else:
            self.canvas.create_text(
                500, 400, text = "(please enter food and count)", font = ('Tempus Sans ITC', 10), fill = "red")

    def buttons(self):
        self.canvas.create_text(
            430, 230, text = 'Food', font = ('Tempus Sans ITC', 100), fill = "red")
        self.canvas.create_text(550, 360, text = 'Fridge', font = (
            'Tempus Sans ITC', 100), fill = "white")
        start_button=Button(self.tk, text = "→", width = 2,
                              command = self.start_window, bg = "black", fg = "red", font = ('Tempus Sans ITC', 15))
        start_button_window=self.canvas.create_window(
            940, 560, anchor = 'n', window = start_button)

    def mainloop(self):
        self.tk.mainloop()

    def main(self):
        self.background("images/raw-food.gif")
        self.buttons()
        self.mainloop()


def convert(a):  # take adress 
    p=Path(a).resolve()
    path=str(p)
    rawstr=r"\ "
    path.replace(rawstr[0], "/")
    return path
