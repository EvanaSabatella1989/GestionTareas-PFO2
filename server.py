from flask import Flask, request, jsonify, g, render_template
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
DATABASE = 'usuarios.db'

# Función para conectar con la base SQLite
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Crear tabla usuarios si no existe
def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Registro de usuario
@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')
    
    if not usuario or not contraseña:
        return jsonify({'error': 'Faltan datos'}), 400
    
    hashed = generate_password_hash(contraseña)
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, password) VALUES (?, ?)", (usuario, hashed))
        db.commit()
        return jsonify({'mensaje': 'Usuario registrado correctamente'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Usuario ya existe'}), 400

# Login de usuario
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({'error': 'Faltan datos'}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT password FROM usuarios WHERE usuario = ?", (usuario,))
    row = cursor.fetchone()

    if row and check_password_hash(row[0], contraseña):
        return jsonify({'mensaje': f'Bienvenido {usuario}'}), 200
    else:
        return jsonify({'error': 'Credenciales inválidas'}), 401

# Página de bienvenida
@app.route('/tareas', methods=['GET'])
def tareas():
    # Solo devuelve un html simple
    # html = """
    # <html>
    #     <head><title>Bienvenido</title></head>
    #     <body>
    #         <h1>Bienvenido al sistema de tareas</h1>
    #         <p>Esta es la página principal para gestionar tareas.</p>
    #     </body>
    # </html>
    # """
    # return render_template_string(html)
    return render_template("index.html")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
