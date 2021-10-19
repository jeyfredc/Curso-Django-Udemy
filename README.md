# Curso-Django-Udemy

## Comandos Basicos

- lanzar entorno virtual (python3 -m venv env) (env) es el nombre del entorno se puede nombrar como se quiera

En windows el entorno virtual se escribe el siguiente comando en la terminal `source env/Scripts/activate`

En Linux se escribe `source env/bin/activate`

para desactivar el entorno virtual en ambos casos de escribe en la terminal `deactivate`

Para poder iniciar un proyecto despues de tener el entorno corriendo se debe instalar Django con el comando **pip** es el instalador de paquetes de Python

`pip install django`

Para crear un proyecto en Django se digita en la terminal 

`django-admin startproject +(nombre del proyecto)`

Despues de ejecutar debe aparecer una carpeta con el nombre del proyecto, dentro de esta sale una subcarpeta con el mismo nombre del proyecto, a traves de la terminal podemos ingresar a dicha carpeta y luego lanzar el proyecto con 

`python manage.py runserver`

Esto lanza un host http://127.0.0.1:8000/ donde aparece django corriendo en el navegador

Toda configuración que tenga que ver con el proyecto iran dentro del archivo **settings.py**

El archivo **urls.py** es donde se hace el llamado a todo el codigo que se va haciendo 

Configuraciones que depronto podrian ayudar a mejorar el archivo settings.py que se hacen a partir de Django version 3 en adelante [configuración](https://github.com/django/django/blob/main/django/conf/global_settings.py)

para organizar y optimizar el codigo que viene por defecto en **settings.py** lo que se hace es dividir el archivo en 3

- Un archivo para el entorno local

- Un archivo para el entorno de producción

- Un archivo que lleva las configuraciones basicas de ambos entornos

Entonces lo primero que se hace es crear una carpeta settings  dentro de esta se crea un archivo llamado **base.py**, **local.py** y **prod.py** para que estos archivos puedan ser leidos dentro de la misma carpeta hay que crear un archivo adicional llamado **__init__.py**

Lo que este dentro de **settings.py**, se copia todo a **base.py** pero solo se deja esto 

```
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g!4ki9^kh#5q3l$=fj3s8%*89j((o1n&ge$hl*!43h=yqfysie'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'empleados.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'empleados.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

```

Luego en el archivo **local.py** se deja lo siguiente

```

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

```

Y en el archivo **prod.py** mientras no se genere algo a producción no se deja nada 

Ahora se pasa al archivo local.py y alli se importa todo lo que este en el archivo base con 

`from .base import *`

el asterisco quiere decir que importe todo el punto que esta antes de la palabra base significa que los archivos local y base se encuentran a la misma altura

Para lanzar la aplicación cambia un poco la forma de lanzar porque ahora hay una nueva configuracion de settings para esto ejecutamos

`python manage.py runserver --settings=empleados.settings.local `

--seytings significa la carpeta que va a configurar =empleados significa que es la carpeta del proyecto .settings.local hace referencia a que vamos a trabajar en un ambiente local

Lo que nosotros vamos creando en django son aplicaciones que funcionan independiente y cada una tiene una funcionalidad especifica y para ser organizados a la altura de **manage.py** se debe crear una carpeta llamada **applications**, se puede llamar como se quiera pero es convención llamarla asi, para que Django pueda leer la carpeta se crea el archivo **__init__.py**

para crear una aplicación ingresamos a la carpeta **applications** y en la terminal agregamos el siguiente comando

`django-admin startapp +(nombreDeLaAplicacion)`

Esto creara una carpeta con el nombre de la nueva aplicación dentro de la carpeta **applications**

cada aplicación creada genera varios archivos admin, apps, models, tests, y views

ACTUALIZACION !!! al agregar aplicaciones en un proyecto Django.
IMPORTANTE!!!!
Hola, antes de pasar a la siguiente clase por favor ten en cuenta esta pequeña actualización.

Desde la versión 3.2 de Django cambiaron algunas cosas respecto a las aplicaciones y en especifico respecto al archivo apps.py que se genera al crear una aplicación. 

Sin no toman en cuenta lo que mencionaré más adelante tendrán problemas al agregar una aplicación local al proyecto.

Desde el minuto 1.20 de la siguiente clase, mostramos como agregamos una app local a un proyecto, luego de que agreguen la ruta de su aplicación a la variable que contiene aplicaciones de django INSTALLED_APPS = [] También debemos hacer un paso más.

Nos dirigimos a la aplicación creada y vamos al archivo apps.py dentro encontraremos un código como este:

from django.apps import AppConfig
 
 
class DepartamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'departamento'
aquí, en la variable name, debemos cambiar por la ruta de nuestra aplicación, para el ejemplo quedaría de esta forma:

class DepartamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.departamento'
Este proceso hay que hacerlo para todas las apps que agreguemos a partir de ahora. Con ello ya no tendrán problemas al agregar una app.



DECLARAR URLS CON RE_PATH
Como ultimo cambio, también si revisamos el minuto 9:30 de la siguiente clase, usamos una función llamada re_path para declarar urls dentro de urls, pero esto ya no es necesario desde la versión 3.2, puedes solamente usar la función path, que es la que trae ya django por defecto.

Para que se puedan leer nuevas aplicaciones en el proyecto en el archivo **base.py** en `INSTALLED_APPS` se deben añadir las aplicaciones, si son locales se puede dejar un comentario debajo de la ultima aplicacion que se encuentre de esa variable llamando `# local apps ` y seguido se agregan las aplicaciones indicando entre comillas el nombre de la carpeta que en este caso es `'applications.nombreDeLaAplicacion'` y nuevamente se ejecuta la ruta local en la terminal con 

`python manage.py runserver --settings=empleados.settings.local`

que en este ejemplo empleados es el nombre del proyecto, para no tener que ejecutar la anterior linea debemos cambiar la configuración el el archivo **manage.py** especificamente en la siguiente linea `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empleados.settings')`, al final vemos que dice `empleados.settings`, pero como la configuración cambio ahora seria `empleados.settings.local`, haciendo este cambio ahora si podriamos ejecutar tan solo

`python manage.py runserver`

En cada aplicación que nosotros creemos, vamos a crear un archivo llamado **urls.py** y va a llevar una configuración basica que es la siguiente

```
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(),
]

```

En cada archivo se deben crear las funciones correspondientes a lo que queremos que se ejecute entonces por ejemplo creamos la funcion y en el path especificamos el path y la funcion, un ejemplo basico seria esto

```
from django.contrib import admin
from django.urls import path

def ListarDepartamentos(self):
    print(=========Desde la app listar departamentos=======)

urlpatterns = [
    path('departamento/', ListarDepartamentos),
]

```

Pero para que este archivo pueda ser leido debemos dirigirnos al archivo **urls.py** del proyecto creado y alli hacer una referencia de la carpeta donde se encuentran estos archivos ejemplo

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.departamento.urls')),
    path('', include('applications.persona.urls'))
] 
```

Django tambien puede trabajar con html para esto en la aplicación en el archivo views se puede trabajar vistas genericas y para trabajar con vistas genericas django proporciona una libreria llamada TemplateView, lo que se hace es crear una clase y a esta pasarle como parametro la libreria y luego nombrar el template. Ejemplo

```
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class PruebaView(TemplateView):
    template_name= 'prueba.html'
```

para poder activar esta vista en Django si por ejemplo existe una nueva aplicación se debe agregar a la aplicación el archivo **urls.py**

para poder hacer referencia a esa clase que llamamos Prueba View se debe importar al archivo urls esa vista de esta forma **Nota: Recordar que al hacer un from . el punto indica el mismo nivel del archivo**

Siempre que se trabaje con listas genericas django sugiere que despues de hacer referencia a la clase se debe agregar `as_view()`

```
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
]


```

Ahora solo faltaria incluir la aplicacion en el archivo **urls.py** y dentro de la aplicacion para poder leer el template se debe crear una carpeta llamada **templates** y alli incluir el archivo html llamado `prueba.html`, dentro de este si iria todo el html que se quiera incluior

Para poder tener la logica que proporciona django de Modelo Vista Templates, los templates deben estar en una carpeta separada y no mezclada entre las aplicaciones es por esto que a la altura de **manage.py** debe haber una carpeta llamada **templates** para que esta pueda ser leida y ejecuta se debe instalar una libreria llamada **unipath**, se instala con `pip install unipath`

ACTUALIZACION!! NUEVA VERSION DE DJANGO
Hola, Django lanzo la versión 3.1 y hay pequeños cambios a considerar para evitar errores.

Django 3.1 en cuanto a como va nuestro curso no traerá problemas con excepción de algunos detalles en la configuración y otros temas que ya veras en su momento.

En la siguiente clase puede que al realizar los pasos te muestre un error como este al final de la terminal: 

'NAME': BASE_DIR / 'db.sqlite3',
TypeError: unsupported operand type(s) for /: 'Path' and 'str'
¿Como lo solucionamos?

Simplemente en el archivo local.py de nuestros settings, debes de dirigirte a la parte de DATABASES y cambiarlo por:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}
¿Por què?

Para esta clase instalamos un paquete llamado unipath el cual con la anterior configuración de Django no traía problemas, pero ahora Django usa una nueva configuración en las rutas, tema del que sacaré un video en el canal de youtube explicando mejor porque cambio y que de bueno trae ese cambio.

como instalamos unipath, se debe cambiar en el archivo base la parte de dice

```
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
```

por 

```
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)
```