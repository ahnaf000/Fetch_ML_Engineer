from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import blueprints, database setup, etc. here if you have them
    @app.route('/')
    def home():
        return "Welcome to my Flask app!"

    return app