from .usuarios import usuarios_bp

def init_app(app):
    print("✅ Registrando rutas")
    app.register_blueprint(usuarios_bp)
