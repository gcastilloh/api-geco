# Instalacion

En el desarrollo de Geco4 se considera Django (basado en python como lenguaje de programación), la plataforma empleada para el desarrollo es Visualstudio code. 
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

Añadir detalle

```sh
python test_basico.py
```

Añadir detalle

```sh
python manage.py check
python manage.py runserver 8500
```

En el navegador accesamos

http://127.0.0.1:8500/home
