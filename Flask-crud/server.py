# server.py
from flask import render_template
from app import create_app

app = create_app()

# Ruta para servir el index.html
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    print("🚀 Iniciando servidor Flask...")

    print("\n📍 RUTAS DISPONIBLES:")
    for rule in app.url_map.iter_rules():
        print(f"{rule} -> {rule.endpoint}")

    app.run(debug=True)
