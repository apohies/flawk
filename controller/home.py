from flask import Blueprint
from modelo import db , Usuario

home_bp = Blueprint('home',__name__)

@home_bp.route("/home/<email>",methods=['GET'])
def home(email):

    visaje : Usuario= Usuario.query.filter_by(email=email).first()

    if visaje is None :
      return "el socio no existe"
    
    else :

     return "el correo del socio es : " + visaje.email