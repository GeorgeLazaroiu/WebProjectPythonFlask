from flask import Blueprint
from flask import Blueprint, render_template
from .manageDataBase import CDbManager

hotels = Blueprint('hotels', __name__)
data_manager = CDbManager()

@hotels.route('/login')
def view_rooms():
    all_rooms = data_manager.get_all_rooms()

    print(all_rooms)
    var = all_rooms[0][2]
    return render_template("base.html", var = all_rooms)

@hotels.route('/logout')
def logout():
    return "<h1>Logout<h1>"


@hotels.route('/sign-up')
def signup():
    return "<h1>Sign-up<h1>"

