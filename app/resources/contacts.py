from flask_restful import Resource


class Contacts(Resource):
    def get(self):
        return {'message': 'Hello World!'}

    
    def post(self):
        pass

    
    def put(self):
        pass

    
    def delete(self):
        pass

    