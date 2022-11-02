# BlossedVape Blog
ESPAÑOL // ENGLISH
- Blog dedicado al vapeo // 
blog dedicated to vapes

1. Abrir Git Bash para Windows o una terminal para Linux/Unix. // Open Git Bash for Windows or a terminal for Linux/Unix.

2. Seleccionar alguna carpeta de preferencia // 
Select a preferred folder
>> cd <"carpeta de preferencia // preferred folder">

3. Utilizar este comando en// use this command
>> cd git clone https://github.com/Chiken22/BlossedVape-Blog.git

4. Abrir VS Code // Open VS Code
>> code .

En seguida en VS code damos Ctrl+j o Terminal/New Terminal y ejecutamos los comandos que se muestran a continuación. // 
Then in VS code, Ctrl + j or Terminal/New Terminal and execute the commands shown below.

5. Crear entorno virtual (venv) // Create virtual environment (venv)
(Windows)
>> python manage.py -m venv venv

6. Activar nuestro entorno virtual (venv) // Activate our virtual environment (venv)
>> .\venv\Scripts\activate

7. Instalar las dependencias del blog // Install the blog requirements
>> pip install -r requirements.txt

8. Hacer las migraciones que son una "plantilla" para crear la base de datos con la que trabajará nuestro proyecto de Django // Make the migrations which are a "template" to create the database that our Django project will work with
>> python manage.py makemigrations

9. Se ejecuta la migración para crear la base de datos con la que trabajará nuestro proyecto de Django // The migration is executed to create the database that our Django project will work with
>> python manage.py migrate

10. Se crea el super usuario para nuestro proyecto de Django (Solo si no se ha creado), permitiendonos así entrar a la seccion de admin // 
Create the super-user for our Django project (Only if it has not been created), allowing us to enter on the admin section
>> python manage.py createsuperuser
- Ingrese en la consola Username, Email address y Password // Enter in the console Username, Email address and Password

11. Se levanta el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto http://127.0.0.1:8000/ // The Django server that exposes the service by localhost on port 8000 by default http://127.0.0.1:8000/ is started
>> python manage.py runserver

12. En la parte izquierda están las aplicaciones del blog // On the left table you will see the blog apps

13. Consta de un blog sobre vapes en donde podes crear tu kit, subir tus marcas favoritas para que todos las conozcan y tambien subir sus urls para que visiten dicha marca. //Its a blog about vapes where you can create your kit, upload your favorite brands so everyone would see and know about them. Also, you could upload their urls for people to visit the Official brand page.
Cuenta con un buscador de vapes en el home. // It has a VAPE search engine in the home.
