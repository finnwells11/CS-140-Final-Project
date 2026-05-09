from flask import Flask
from views import views

app = Flask(__name__)

app.secret_key = "secretkey" # part of session authentication

app.register_blueprint(views)

if __name__ == '__main__':
    app.run(debug=True, port=5000)