import requests

BASE_URL = 'http://127.0.0.1:5000'

def registrar(usuario, contraseña):
    r = requests.post(f'{BASE_URL}/registro', json={'usuario': usuario, 'contraseña': contraseña})
    print(r.json())

def login(usuario, contraseña):
    r = requests.post(f'{BASE_URL}/login', json={'usuario': usuario, 'contraseña': contraseña})
    print(r.json())

def ver_tareas():
    r = requests.get(f'{BASE_URL}/tareas')
    print(r.text)

if __name__ == '__main__':
    print("Registrar usuario:")
    registrar('Eva', '12345')

    print("Login usuario:")
    login('Eva', '12345')

    print("Ver tareas:")
    ver_tareas()
