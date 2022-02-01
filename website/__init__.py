from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'This is the key for the aplications'
    from .routes import route
    from .hotels import hotels


    app.register_blueprint( route , url_prefix='/')

    return app