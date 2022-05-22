from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv
import os
import jwt

load_dotenv()

def jwt_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        token = None

        if 'authorization' in request.headers:
            token = request.headers['authorization']

        if not token:
            return jsonify({"error": "Você não tem permissão para acessar esta rota."}), 401

        if not "Bearer" in token:
            return jsonify({"error": "Token Inválido"}), 403 
        try:
            token_pure = token.replace("Bearer ","")
            decoded = jwt.decode(token_pure, os.getenv('CRYPTOGRAPHY_HASH'),algorithms=['HS256'])
            current_user_id = decoded['id'][0]
        except:
            return jsonify({"error": "O token é inválido"}), 403
        return function(current_user_id=current_user_id,*args, **kwargs)


    return wrapper