from os import getenv
from datetime import datetime

from flask import request, jsonify
from flask_login import login_user, logout_user, current_user
from sqlalchemy.orm.query import Query

from middleware import login_manager, login_required
from models import *

class OperatorController:
    def test_login():
        if current_user.is_authenticated:
            return "kamu telah login"
        else: 
            return "kamu belum login"

    @login_required
    def get_operator_by_id(id: int):
        available = True
        result = Query(UserModel).filter_by(id=id).first()
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
            if data.get('NIP') is None or data.get('password') is None:
                return jsonify(
                    message="data NIP/Password cannot empety"
                )
            
            user = UserModel.query.filter_by(NI=data['NIP']).first()
            if user == None:
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
        data = request.get_json()
        sucess = True
        message = "sucess register new operator"
        try:
            operator = UserModel(**data, create_at=datetime.now(), last_update=datetime.now())
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