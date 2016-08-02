import sqlite3

conn = sqlite3.connect("food_database.db")
cursor = conn.cursor()


def create_clients_table():

    create_query = '''create table if not exists
        food_system(food TEXT,
                protein REAL,
                fats REAL,
                carbohydrates REAL,
                calories REAL)'''

    cursor.execute(create_query)


def add_food(food, protein, fats, carbohydrates, calories):
    food_system = [food, protein, fats, carbohydrates, calories]
    cursor.execute(
        'INSERT INTO food_system VALUES (?, ?, ?, ?, ?)', food_system)
    conn.commit()


create_clients_table()

