from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'This is the key for the aplications'
    from .rooms import rooms
    from .hotels import hotels


    app.register_blueprint(rooms, url_prefix='/')
    app.register_blueprint(hotels, url_prefix='/hotels')

    return app