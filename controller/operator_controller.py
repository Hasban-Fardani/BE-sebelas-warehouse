from os import getenv
from datetime import datetime

from flask import request, jsonify, make_response
from flask_login import login_user, logout_user, current_user
# from sqlalchemy.orm.query import Query

from middleware import login_manager, login_required
from models import *
import peewee as p

class OperatorController:

    def test_login():
        if current_user.is_authenticated:
            return "kamu telah login"
        else: 
            return "kamu belum login"

    def get_all():
        # return [user.__str__() for user in User.select()]
        return {}
    
    @login_required
    def get_operator_by_id(id: int):
        available = True
        result = User.get_by_id(id).first()
        if not result.count():
            available = False

        return jsonify(
            id=id,
            available=available,
            data=result,
        )
    
    def login_operator():
        try:
            data = request.get_json()
            if data.get('NI') is None or data.get('password') is None:
                return jsonify(
                    message="data NI/Password cannot empety"
                )
            
            user = User.select().where(User.NI == data['NI']).first()
            # print(data['NI'], user.name)
            if user is None:
                return jsonify(
                    message="user not found"
                )
            
            if str(data.get('password')) != str(user.password):
                return jsonify(
                    message="wrong password"
                ) 
            
            success = login_user(user)
            return jsonify(
                data=data,
                success=success
            )
        except Exception as e:
            return e.__str__()

    @login_required
    def logout_operator():
        try:
            success = logout_user()
            return jsonify(
                success = success
            )
        except Exception as e:
            return e.__str__()

    @login_required
    def register_operator():
        if current_user.type != "operator": 
            return make_response(status=403, message="yo'ure not admin")
        data = request.get_json()
        sucess = True
        message = "sucess register new operator"
        try:
            operator = User(**data, create_at=datetime.now(), last_update=datetime.now())
            db.session.add(operator)
            db.session.commit()
        except Exception as e:
            sucess = False
            message = e.__str__()

        return jsonify(
            success = sucess,
            message = message,
            data = data
        )