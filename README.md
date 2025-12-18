# SIGEPER - Sistema de Gestión de la Reserva Militar

Sistema web para la gestión, trazabilidad y administración de la información de la Reserva Militar del Ejército de Chile.  
Desarrollado con Django y basado en buenas prácticas de arquitectura de software, seguridad y mantenibilidad.

---

## Tabla de Contenidos

- [Características](#características)
- [Arquitectura de Apps](#arquitectura-de-apps)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración Inicial](#configuración-inicial)
- [Uso](#uso)
- [Colores institucionales](#colores-institucionales)
- [Documentación oficial Django](#documentación-oficial-django)

---

## Características

- Gestión de reservistas: fichas, historial, ascensos, medallas y más.
- Administración de actos administrativos y documentos oficiales.
- Mantenedor de datos maestros (grados, ciudades, armas, etc.).
- Sistema de usuarios con roles y doble autenticación (2FA).
- Dashboard y vistas administrativas.
- Arquitectura modular y segura.

---

## Arquitectura de Apps

| App                      | Descripción                                                                                      |
|--------------------------|--------------------------------------------------------------------------------------------------|
| **actos_administrativos** | Gestión de actos administrativos, resoluciones y documentos oficiales.                          |
| **core**                 | Configuración central, utilidades compartidas, vistas base y lógica transversal.                 |
| **mantenedor**           | Mantenedor de datos maestros (grados, armas, ciudades, estados civiles, profesiones, etc.).     |
| **reservistas**          | Información y trazabilidad completa de los reservistas.                                          |
| **usuarios**             | Gestión de usuarios, perfiles, autenticación y permisos.                                         |

---

## Tecnologías Utilizadas

- [Python 3.12+](https://www.python.org/)
- [Django 5.x](https://docs.djangoproject.com/es/5.2/)
- [MySQL / MariaDB](https://www.mysql.com/)
- Bootstrap 5 (para el frontend responsivo)
- Autenticación por correo electrónico y 2FA (opcional)

---

## Requisitos

- Python 3.12 o superior
- MySQL o MariaDB (recomendado)
- MySQL Workbench
- Git
- pip (gestor de paquetes de Python)
- Un entorno virtual recomendado (`env`)

---

## Instalación

Sigue estos pasos para levantar el proyecto SIGEPER en tu entorno local:

### 1. **Clonar el repositorio**
   ```bash
        git clone https://github.com/Jabarona/PROYECTO-SIGEPER---RESERVA-MILITAR.git
        cd PROYECTO-SIGEPER---RESERVA-MILITAR
        
   ```
### 2. **Crear y activar un entorno virtual**
    ```bash
        python -m venv env
        # En Windows:
        env\Scripts\activate
        # En Linux/macOS:
        source env/bin/activate
    ```
### 3.  **Instalar las dependencias**
    ```bash
        pip install -r requirements.txt
    ```
### 4. **Configurar la base de datos**
1. Instalación de MySQL Workbench, MariaDB y MySQL

- Descarga el instalador desde  
  [MySQL Workbench 8.0.43](https://dev.mysql.com/downloads/workbench/)
  [MariaDB V12](https://mariadb.org/download/?t=mariadb&o=true&p=mariadb&r=12.0.1&os=windows&cpu=x86_64&pkg=msi&mirror=archive)
  [MySQL V9 MSI INSTALLER](https://dev.mysql.com/downloads/mysql/?utm_source=chatgpt.com)
  Puedes descargar directamente del DRIVE compartido
  [MySQL y MariaDB](https://drive.google.com/drive/folders/1rjeTtOFPN0ABNUevnnv3Mv25Xwboo0-K)

- Ejecuta el instalador y asegúrate de seleccionar **MySQL Workbench**.
- Completa la instalación y guarda el usuario (`root`), el puerto (`3307 O 3306`) y contraseña que configures.

2. Crear la base de datos SIGEPER en Workbench

- Abre **MySQL Workbench** y conéctate a tu servidor local.
- Haz clic derecho sobre **Schemas** > **Create Schema...**
- Nombra el schema: duoc_sigeper_db

3. Selecciona `utf8mb4_unicode_ci` como collation.
4. Haz clic en **Apply** > **Apply** > **Finish**.


3. Configurar Django para usar la base de datos

Edita el archivo `settings.py` en tu proyecto:

```python
DATABASES = {
 'default': {
     'ENGINE': 'django.db.backends.mysql',
     'NAME': 'sigeper',
     'USER': 'root',    
     'PASSWORD': '',
     'HOST': 'localhost',
     'PORT': '3307', #EL PUERTO VARIA DONDE ESTA INSTALADO MariaDB y 
 }
}
```



### 5. **Aplicar migraciones**
    ```bash
        python manage.py makemigrations
        python manage.py migrate      
    ```

### 6. **Crear un superusuario para acceder al admin**
    ```bash
        python manage.py createsuperuser      
    ```

### 7. **Levantar el servidor de desarrollo**
    ```bash
        python manage.py runserver      
    ```
    Accede a http://127.0.0.1:8000/ para ver el sistema funcionando.

---

## Configuración Inicial
- Accede a /admin para cargar los datos maestros utilizando el superusuario.
- Configura los roles y permisos según corresponda en la app usuarios.
- Personaliza los mantenedores de acuerdo a las necesidades de la institución.
- [Base de datos del sigeper](https://drive.google.com/drive/folders/1QCdJIfamaH_1KLsg7thRFXz2y_qITcG-)

---

## Uso
- El sistema permite registrar, actualizar y consultar toda la información relevante sobre los reservistas y su historial militar.
- Las funciones avanzadas (actos administrativos, trazabilidad, mantenedores) requieren permisos de usuario específicos.

---

## Colores institucionales
Utiliza los siguientes colores para mantener la identidad visual del sistema:
   
    .color1 { color: #4a1913; }
    .color2 { color: #6f301b; }
    .color3 { color: #a05422; }
    .color4 { color: #da8626; }
    .color5 { color: #ffc926; }      
   
---

## Documentación oficial Django

- [Documentación Django 5.x](https://docs.djangoproject.com/es/5.2/?utm_source=chatgpt.com)
- [Documentación sobre Apps en Django](https://docs.djangoproject.com/es/5.2/ref/applications/?utm_source=chatgpt.com)
- [Configuración de settings.py](https://docs.djangoproject.com/es/5.2/ref/settings/?utm_source=chatgpt.com)
- [Clases Basadas en Vistas CBV](https://ccbv.co.uk/)