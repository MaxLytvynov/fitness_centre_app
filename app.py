from urllib import request

from flask import Flask

app = Flask(__name__)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return 'Registration form'
    else:
        return 'Enter your name and password'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'Log in form'
    else:
        return 'You have logged'

@app.get('/user_info')
def user_info():
    return 'User info desk'

@app.post('/user_info')
def user_info_change():
    return 'Change your info'

@app.put('/user_info')
def user_info_input():
    return 'Input your info'

@app.route('/funds', methods=['GET', 'POST'])
def funds():
    if request.method == 'GET':
        return 'Balance'
    else:
        return 'Add funds'

@app.route('/reservations', methods=['GET', 'POST'])
def reservations():
    if request.method == 'GET':
        return 'Reservation form'
    else:
        return 'Make your reservation'

@app.route('/reservations/<reservation_id>', methods=['GET', 'PUT', 'DELETE'])
def personal_reservation(reservation_id):
    if request.method == 'GET':
        return f'Your personal {reservation_id}'
    elif request.method == 'PUT':
        return f'Change your {reservation_id}'
    else:
        return f'Delete {reservation_id}'

@app.get('/checkout')
def checkout_total():
    return 'Check out desk'

@app.post('/checkout')
def checkout_change():
    return 'Change checkout services'

@app.put('/checkout')
def checkout_input():
    return 'Add some services to the basket'

@app.get('/fitness_centre')
def fitnes_centre_info():
    return 'Fitness centre info form'

@app.get('/fitness_center/<id>')
def get_fitness_centre_info(id):
    return f'Fitness centre {id} info'

@app.get('/fitness_center/<id>/trainer')
def get_trainer_info(id):
    return f'Fitness centre {id}, information about trainers'

@app.get('/fitness_center/<id>/trainer/<trainer_id>')
def get_trainer_id_info(id, trainer_id):
    return f'Fitness centre {id}. Information about trainer {trainer_id}'

@app.route('/fitness_center/<id>/trainer/<trainer_id>/rating', methods=['GET', 'POST', 'PUT'])
def trainer_rating(id, trainer_id):
    if request.method == 'GET':
        return f'Show rating {trainer_id}'
    elif request.method == 'POST':
        return f'Change the rating {trainer_id}'
    else:
        return f'Enter the rating {trainer_id}'

@app.get('/fitness_center/<id>/services')
def get_services(id)
    return f'Services dashboard {id}'

@app.get('/fitness_center/<id>/services/<service_id>')
def get_services_info(id, service_id):
    return f'Info about {service_id} at fitness centre {id}'

@app.get('/fitness_center/<id>/loyality_programs')
def loyalty_programms(id):
    return f'Info about loyalty programs at fitness centre {id}'





if __name__ == '__main__':
    app.run()


