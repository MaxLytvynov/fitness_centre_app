from flask import Flask, request

import sqlite3

app = Flask(__name__)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
def get_from_db(query, many=True):
    con = sqlite3.connect('db_fitness.app.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute(query)
    if many:
        res = cur.fetchall()
    else:
        res = cur.fetchone()
    con.close()
    return res

def insert_to_db(query):
    con = sqlite3.connect('db_fitness.app.db')
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    con.close()

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return """<form action='/registration' method='post'>
  <label for="login">Log in:</label><br>
  <input type="text" id="login" name="login"><br>
  <label for="password">Password:</label><br>
  <input type="password" id="password" name="password">
  <label for="birth_date">Birth date:</label><br>
  <input type="data" id="birth_date" name="birth_date"><br>
  <label for="phone">Phone:</label><br>
  <input type="password" id="phone" name="phone">
  <input type="submit" value="Submit">
</form>"""
    else:
        form_data = request.form
        insert_to_db(f'INSERT INTO user (login, password, birth_date, phone) VALUES (\'{form_data["login"]}\', \'{form_data["password"]}\', \'{form_data["birth_date"]}\', \'{form_data["phone"]}\')')
        return f'User registered'

@app.get('/user_info')
def user_info():
    res = get_from_db('select * from user')
    return str(res)

@app.post('/user_info')
def user_info_change():
    return 'Change your info'

@app.put('/user_info')
def user_info_input():
    return 'Input your info'

@app.route('/funds', methods=['GET', 'POST'])
def get_funds():
    if request.method == 'GET':
        res = get_from_db('select funds from user')
        return str(res)
    else:
        return 'Add funds'

@app.get('/reservations')
def get_resevations():
    res = get_from_db('select * from reservation')
    return str(res)

@app.post('/reservations')
def post_resevations():
    return 'Make your reservation'

@app.route('/reservations/<reservation_id>', methods=['GET', 'PUT', 'DELETE'])
def personal_reservation(reservation_id):
    if request.method == 'GET':
        res = get_from_db(f'select * from reservation where id={reservation_id}', False)
        return str(res)
    elif request.method == 'PUT':
        return f'Change your {reservation_id}'
    else:
        return f'Delete {reservation_id}'

@app.get('/checkout')
def checkout_total():
    res = get_from_db('select * from checkout')
    return str(res)

@app.post('/checkout')
def checkout_change():
    return 'Change checkout services'

@app.put('/checkout')
def checkout_input():
    return 'Add some services to the basket'

@app.get('/fitness_centre')
def fitnes_centre_info():
    res = get_from_db('select * from fitness_centre')
    return str(res)

@app.get('/fitness_center/<id>')
def get_fitness_centre_info(id):
    res = get_from_db(f'select adress, name from fitness_centre where id={id}', False)
    return str(res)

@app.get('/fitness_center/<id>/trainer')
def get_trainer_info(id):
    res = get_from_db(f"select * from trainer where id={id}", False)
    return str(res)

@app.get('/fitness_center/<id>/trainer/<trainer_id>')
def get_trainer_id_info(id, trainer_id):
    res = get_from_db(f"select * from trainer where id={trainer_id}", False)
    return str(res)

@app.route('/fitness_center/<id>/trainer/<trainer_id>/rating', methods=['GET', 'POST', 'PUT'])
def trainer_rating(id, trainer_id):
    if request.method == 'GET':
        res = get_from_db('select * from rating')
        return str(res)
    elif request.method == 'POST':
        return f'Change the rating {trainer_id}'
    else:
        return f'Enter the rating {trainer_id}'

@app.get('/fitness_center/<id>/services')
def get_services(id):
    res = get_from_db('select * from service')
    return str(res)

@app.get('/fitness_center/<id>/services/<service_id>')
def get_services_info(id, service_id):
    res = get_from_db('select * from service where id={service_id}')
    return str(res)

@app.get('/fitness_center/<id>/loyality_programs')
def loyalty_programms(id):
    return f'Info about loyalty programs at fitness centre {id}'


if __name__ == '__main__':
    app.run()

