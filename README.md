# GestionTareas-PFO2
PFO2 - Sistema de Gestión de Tareas con Flask y SQLite

## Requisitos

- Python 3.x
- Flask

## Instalación y ejecución

1. Crear entorno virtual (opcional):

python -m venv venv
source venv/bin/activate # en Linux/Mac
venv\Scripts\activate    # en Windows


2. Instalar dependencias:

pip install flask requests

3. Ejecutar el servidor:

python servidor.py

4. Probar con el cliente:

## Endpoints

- POST /registro: Registra un usuario.
- POST /login: Inicia sesión.
- GET /tareas: Muestra una página HTML de bienvenida.

---

## Preguntas Conceptuales

### ¿Por qué hashear contraseñas?

Para proteger la seguridad de los usuarios. Si la base de datos es comprometida, las contraseñas hasheadas no se pueden leer directamente, evitando que terceros accedan a ellas.

### Ventajas de usar SQLite en este proyecto

- Es una base de datos ligera y sin necesidad de servidor.
- Fácil de configurar e integrar.
- Ideal para proyectos pequeños y prototipos.
