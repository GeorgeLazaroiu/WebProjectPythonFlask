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
    head = {"ID Room", "Number of room", "Price of room", "Number of person in the room", "Confort room"}
    return render_template("View-Rooms.html", head = head, all_rooms = all_rooms)



