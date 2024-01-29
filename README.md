PROYECTO FULL STACK DJANGO / JAVASCRIPT

- Existen dos carpetas Backend y Frontend  en la cual el Backend es realizado con Django y frontend con JS

  INICIALIZAR BACKEND:

- Se descarga el proyecto actual en la cual al momento de descargar el Backend, vamos a proceder a arrancar el servidor y instalar dependencias.

  PASOS:
  - Instalamos Django: pip install Django
  - Verificamos en Settings.py que contenga la configuración y archivo de sqllite. (DATABASES)
  - CMD para ejecutar el backend: python manage.py runserver,  estar atento del puerto a ejecutar ya que tiene que ser http://127.0.0.1:8000/
  - el CMD python manage.py migrate (Para actualizar los modelos bd)
  

INICIALIZAR FRONTEND:

- Comprobamos que contengan las carpetas correspondientes y se inicializa con el index.html dando click derecho y live server
- otro metodo es con el CMD python -m http.server en la cual nos ejecuta el puerto del proyecto, nos dirijimos hacia el buscador predeterminado y colocamos http://localhost:8000/ y
  ya podemos ver el proyecto funcionando.
