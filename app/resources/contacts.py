from flask_restful import Resource, marshal
from app.models import Contact
from app import request, db
from app.schemas import contact_field

class Contacts(Resource):
    def get(self):
        contacts = Contact.query.all()

        return marshal(contacts, contact_field, 'contacts')

    
    def post(self):
        payload = request.only(['name', 'cellphone'])

        name = payload['name']
        cellphone = payload['cellphone']

        contact = Contact(name=name, cellphone=cellphone)

        db.session.add(contact)
        db.session.commit()
 
        return marshal(contact, contact_field, 'contact')
    
    def put(self):
        payload = request.only(['id', 'name', 'cellphone'])
        
        name = payload['name']
        _id = payload['id']
        cellphone = payload['cellphone']

        contact = Contact.query.get(_id)

        if not contact:
            return {'message':'O contato que você está tentando alterar não existe'}

        contact.name = name
        contact.cellphone = cellphone

        db.session.add(contact)
        db.session.commit()

        return marshal(contact, contact_field, 'contact')


    def delete(self):
        payload = request.only(['id'])
        _id = payload['id']

        contact = Contact.query.get(_id)

        if not contact:
            return {'message':'Contato não existe'}

        db.session.delete(contact)
        db.session.commit()
    
        return marshal(contact, contact_field, 'contact')