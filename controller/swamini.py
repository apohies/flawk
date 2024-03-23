from flask import Blueprint,request,jsonify
from modelo import db , Usuario

swamini_bp = Blueprint('swamini',__name__)

@swamini_bp.route("/swamini/home/<email>", methods=['GET'])
def home(email):

    usuario = Usuario(nombre="chepe", email= email)
    db.session.add(usuario)
    db.session.commit()

    return "se guardo a chepe"

@swamini_bp.route("/swamini/socio", methods=['POST'])
def crear_socio():
    
    data=request.json

    if not data :
        return jsonify({"error":"sin datos papa "}),400
    
    else:

        nuevo_usuario = Usuario(nombre=data["nombre"] , email = data["email"])

        db.session.add(nuevo_usuario)
        db.session.commit()

        return jsonify({'mensaje': 'Usuario creado exitosamente', 'id': nuevo_usuario.id}), 201

    
