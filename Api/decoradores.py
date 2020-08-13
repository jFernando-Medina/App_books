from functools import wraps
from flask import request, jsonify
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

def check_for_token(func):
    @wraps(func)
    def Wrapped(*args,**kwargs):
        token = request.args.get("token")
        if not token:
            return jsonify({"message": "No se encontró token"}), 403
        try:
            data = jwt.decode(token, os.getenv("SECRET_KEY"))
        except:
            return jsonify({"message":"Token vencido, verifica de nuevo"}), 403
        return func(*args, **kwargs)
    return Wrapped
