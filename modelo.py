from flask_sqlalchemy import SQLAlchemy

# Crear instancia de SQLAlchemy
db = SQLAlchemy()

# Definición del modelo de la base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Usuario %r>' % self.nombre
    
    