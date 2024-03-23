from flask import Flask
from flask import Flask
from modelo import db, Usuario
from controller.home import home_bp
from controller.swamini import swamini_bp
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base_de_datos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configurar la base de datos
db.init_app(app)

with app.app_context():
    db.create_all()
# Crear la base de datos antes de la primera solicitud

app.register_blueprint(home_bp)
app.register_blueprint(swamini_bp)



if __name__ == '__main__':
    # Ejecutar la aplicación Flask
  
    app.run(debug=True)

