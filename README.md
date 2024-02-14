# Instalacion

En el contexto del desarrollo de Geco3 (basado en python como lenguaje de programación) se considera Django como base del entorno de desarrollo. Las apps que se desarrollen para interactuar con geco también usaran Django como su entorno de desarrrollo.

El proceso puede consultarse en el documento de [instalación](./documentacion/instalacion/)

//copiar a ese directorio

Para poder trabajar con api-geco es necesario contar con una versión actualizada de python, virtual environments y los paquetes django djangorestframework y requests.

En primer lugar debemos hacer una copia del repositorio en nuestro entorno local y nos movemos a este directorio

```sh
git clone https://github.com/gcastilloh/api-geco.git && cd api-geco
```

Posteriormente debemos de crear un entorno virtual con nombre env:

```sh
ptyhon3 -m venv env
```

Activamos el entorno virtual al ubicarnos en el directorio y usar el comando

```sh
source env/bin/activate
```

Después se procede a instalar los siguientes paquetes django, djangorestframework y requests

```sh
pip install django djangorestframweork requests
```

Añadir detalle

```sh
python manage.py check
```

Añadir detalle

```sh
python manage.py migrate
```

Al correr este código podemos hacer una prueba rápida para comprobar que al identificarnos el token se obtiene correctamente, los diferentes tipos de solicitudes que se pueden hacer al geco3 y las respuestas que se obtienen.

```sh
python test_basico.py
```

Añadir detalle

```sh
python manage.py check
```

Con este comando activamos localmente el servidor de nuestra aplicación en el puerto 8500

```sh
python manage.py runserver 8500
```

En el navegador accesamos

http://127.0.0.1:8500/home
