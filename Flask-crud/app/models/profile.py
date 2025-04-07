from app.models import db
from datetime import datetime
import uuid

class Perfil(db.Model):
    __tablename__ = 'perfiles'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    rol = db.Column(db.String(50), nullable=False)
    estado_rostro = db.Column(db.String(50), default='pendiente')
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    telefono = db.Column(db.String(15))  # Campo adicional de ejemplo

    # Clave foránea
    usuario_id = db.Column(db.String(36), db.ForeignKey('usuarios.id'), unique=True)
    usuario = db.relationship('Usuario', back_populates='perfil')

    def to_dict(self):
        return {
            'rol': self.rol,
            'estado_rostro': self.estado_rostro,
            'creado_en': self.creado_en.isoformat(),
            'telefono': self.telefono
        }