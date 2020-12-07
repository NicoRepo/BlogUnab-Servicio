# Blog Unab

_Aqui se encontraran las instrucciones para poder ingresar al sistema del Blog Unab_

## Comenzando 🚀
* **hhttps://github.com/NicoRepo/BlogUnab-Servicio.git* **
* **Mediante este link puede hacer una copia del repositorio**


### Pre-requisitos 📋

* **Python 3.x**
* **Django3.0**
* **Github**
* **virtualenv venv**
* **venv/Scripts/activate.bat**
* **pip3 install -r requirements.txt**

_Antes de Correr el servidor_

* **python manage.py makemigrations**
* **python manage.py migrate**
* **python manage.py runserver**
* **cerrar el servidor, correr el servidor y entrar con las credenciales para que cargue el contenido**

### Credenciales 📋
* [Panel Admin](localhost:8000/admin) - Acceso Administrador
* **Username: admin**
* **Password: adminadmin**

### Puesta en marcha del sistema 🔧
_Para iniciar el sistema localmente ingresar al directorio del proyecto en django, usando la terminal._

* **1- Dentro del directorio raiz ingresar al entorno virtual venv\Scripts\activate.bat**
* **2- Ingresar al directorio blogunabtest**
* **3- Ingresar el comando: python manage.py runserver**
* **4- Copiar el Url en el browser  http://127.0.0.1:8000/**
* **5- Para acceder a la vista blogs, debe identificarce con las credenciales entregadas anteriormente.**


## Construido con 🛠️
_Para esta entrega se usaron las siguientes herramientas_

* [django](https://www.djangoproject.com/) - Framework web usado
* [ckeditor](https://ckeditor.com/) - Usado para enriquecer el contenido de las noticias
* [Microsoft Graph](https://docs.microsoft.com/en-us/graph/tutorials/python) - Implementación de Microsoft Auth
* [Docker](https://www.docker.com/) - Creación de contenedor para carga en AWS


## Integrantes del equipo ✒️

* **Daniel Paredes Acevedo**
* **Alejandro Crisostomo Rojas**
* **Nicolas Maza Cerda**
* **Marcelo Letelier Palomares**
