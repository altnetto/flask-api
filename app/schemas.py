from flask_restful import fields

contact_field = {
    'id': fields.Integer,
    'name': fields.String,
    'cellphone': fields.String
}