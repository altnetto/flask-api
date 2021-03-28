from functools import wraps
from flask_restful import request
import jwt
from flask import current_app
from app.models import User


def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        
        if not token:
            return {'error': 'Você não tem permissão para acessar essa rota.'}, 401

        
        if not 'Bearer' in token:
            return {'error': 'O token é inválido'}, 401


        try:
            token_pure = token.replace('Bearer ', '')
            decoded = jwt.decode(jwt = token_pure, key = current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(decoded['id'])


        except:
            print(f'{decoded=}')
            print(f'{current_user=}')
            print(f'{token=}')
            print(f'{token_pure=}')
            return {'error': 'O token é inválido.'}, 403


        return f(current_user = current_user, *args, **kwargs)

    return decorated