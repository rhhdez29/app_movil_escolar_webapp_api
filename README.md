# Backend API – Sistema Escolar Móvil

**API** construida en **Django**, preparada para integrarse con una aplicación móvil/web escolar y desplegarse (en Google Cloud (App Engine)).

---

## Descripción del Proyecto

Este repositorio contiene el **backend** que alimenta una aplicación escolar, proporcionando endpoints para gestionar **usuarios, autenticación, datos académicos** y otros recursos relacionados con el ecosistema escolar.

El proyecto está configurado para ejecutarse como una aplicación **WSGI** dentro de **App Engine Standard**, utilizando un entorno virtual y dependencias declaradas en `requirements.txt`.

---

## Tecnologías Clave

* **Python 3**
* **Django**
* **Django REST Framework** (DRF)
* **MySQL / Cloud SQL** (configurable mediante `my.cnf`)
* **Google App Engine Standard**
* **WSGI**

---

## Configuración y Ejecución Local
Sigue estos pasos para levantar el servidor en tu máquina local:
### 1. Entorno Virtual
Crea y activa el entorno virtual:
```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```
### 2. Instalar dependencias
Instala todas las librerías necesarias:
```bash
pip install -r requirements.txt
```
### 3. Migraciones a la base datos
Aplica las migraciones para preparar la base de datos local:
```bash
python manage.py makemigrations
python manage.py migrate
```
### 4. Ejecutar servidor local
Inicia el servidor de desarrollo de Django:
```bash
python manage.py runserver
```
### 5.  Acceso en navegador
El API estará accesible en tu navegador o cliente API en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Configuración de Base de Datos
El proyecto está diseñado para conectarse a una base de datos MySQL o Cloud SQL.
 - La configuración del cliente es a través del archivo my.cnf.
 - Los parámetros de conexión (como el socket o las credenciales) deben ajustarse en el archivo de settings correspondiente.

---

