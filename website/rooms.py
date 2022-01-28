from flask import Blueprint, render_template
from .manageDataBase import CDbManager

rooms = Blueprint('rooms', __name__)
data_manager = CDbManager()

rooms.route('/rooms')
def view_rooms():
    all_rooms = data_manager.get_all_rooms()
    return render_template("home.html")

