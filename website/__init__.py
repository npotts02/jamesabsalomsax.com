from flask import Flask
app = Flask(__name__)

@app.route('/')
def create_app():
   
    app = Flask(__name__)
    return app