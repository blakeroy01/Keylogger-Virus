from flask_restful import Resource, reqparse

class UserInput(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('text', type=str, required = True, help = 'This field cannot be blank', location = 'form')
    def post(self):
        print('post')
        data = UserInput.parser.parse_args()
        print(data['text'])
        with open('log.txt', 'a') as f:
            f.write(data['text'])
        return 'success'
    def get(self):
        return 'you have hit the get endpoint'