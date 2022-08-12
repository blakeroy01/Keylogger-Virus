from flask import Flask
from flask_restful import Api
from user_input import UserInput

app = Flask(__name__)

api = Api(app)

api.add_resource(UserInput, '/malware')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port = 5000)