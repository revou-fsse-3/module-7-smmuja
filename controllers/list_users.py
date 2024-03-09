from flask import Blueprint, render_template, request
from connectors.mysql_connector import Session

from models.user import User
from sqlalchemy import select, or_

from flask_login import current_user, login_required

users_routes = Blueprint('users_routes', __name__)

@users_routes.route('/users', methods=['GET'])
# @login_required
def list_users():
    response_data = dict()

    session = Session()

    try:
        user_query = select(User)

        #Tambahkan filter apabila ada search query
        if request.args.get('query') != None:
            search_query = request.args.get('query')
            user_query = user_query.where(User.name.like(f'% {search_query} %')) 

        users= session.execute(user_query)
        users= users.scalars()
        response_data['users'] = users
        


        # print(users)
    except Exception as e:
        print(e)
        return 'Error Processing Data'

    response_data['name'] = current_user.name
    return render_template('users/list_users.html', response_data = response_data)


@users_routes.route('/users', methods=['POST'])
def user_insert():
    new_user = User(
        name = request.form['name'],
        email = request.form['email'],
        password = request.form['password']
        )
    
    session = Session()
    session.begin()
    try:
       session.add(new_user)
       session.commit()

        
    except Exception as e:
        #Operation failed
       session.rollback()
       print(e)
       return { 'message': 'Insert data gagal'}

    #Operation sukses
    return {'message': 'Input data sukses'}


@users_routes.route('/users/<id>', methods=['DELETE'])
def user_delete(id):
    session = Session()
    session.begin()

    try:
        user_to_delete = session.query(User).filter(User.id==id).first()
        session.delete(user_to_delete)
        session.commit()

    except Exception as e:
        session.rollback()
        print(e)
        return{'message': 'Delete Data Gagal'}

    #Operation sukses
    return {'message': 'Delete Data Sukses'}


@users_routes.route('/users/<id>', methods=['PUT'])
def user_update(id):
    session = Session()
    session.begin()

    try:
        user_to_update = session.query(User).filter(User.id==id).first()
        
        user_to_update.name = request.form['name']
        user_to_update.email = request.form['email']
        user_to_update.password = request.form['password']

        session.commit()

    except Exception as e:
        session.rollback()
        print(e)
        return{'message': 'Update Data Gagal'}

    #Operation sukses
    return {'message': 'UPdate Data Sukses'}
