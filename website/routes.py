from flask import Flask, render_template, Blueprint

route = Blueprint('route', __name__)
from .manageDataBase import CDbManager
data_manager = CDbManager()
from .rooms import Rooms

@route.route('/')
def homePage():
    return render_template('home.html')

@route.route('/view-rooms')
def view_rooms():
    all_rooms = data_manager.get_all_rooms()

    return render_template("View-Rooms.html", all_rooms = all_rooms)

@route.route('/view-hotels')
def view_hotels():
    all_hotels = data_manager.get_all_hotels()
    return render_template("View-Hotels.html", all_hotels = all_hotels)

@route.route('/view-rezervations')
def view_rezervations():
    all_rezervation = data_manager.get_all_rezervations()
    return render_template("View-Rezervations.html", all_rezervation = all_rezervation)





