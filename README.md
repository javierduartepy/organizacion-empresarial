# UTN - Sistema Integral de Gestión Documental

Sistema modular de flujos informáticos, control escalar e interconexión orgánica desarrollado para **ECOM S.A.** bajo el marco de la materia Organización Empresarial.

## 🛠️ Tecnologías Utilizadas
* **Backend:** Django Framework (Python 3.8+)
* **Base de Datos:** PostgreSQL 18
* **Frontend:** Bootstrap 5 & Bootstrap Icons (Capa de presentación modular)
* **Entorno:** Variables de desarrollo locales mediante archivos de configuración

## 📦 Estructura de Módulos (Enfoque TGS)
1. **Jerarquías:** Árbol recursivo de dependencias. Control de la cumbre estratégica (Bloqueo de eliminación del nodo raíz CEO).
2. **Áreas:** Unidades operativas oficiales acopladas uno a uno con la estructura formal. Panel consolidado de recursos.
3. **Personas:** Gestión del talento humano (DNI, Nombre, Apellido, Sector) automatizado con grupos de permisos nativos.
4. **Formularios:** Estandarización de procesos de salida y perfiles de carga (Pasarela de **Comunicación Oblicua**).
5. **Documentos:** Repositorio centralizado con control de activos de retención legal (**Archivado Lógico** y Pileta de Recuperación).

## 🚀 Instalación y Despliegue Local
1. Clonar el repositorio
2. Activar el entorno virtual: `venv\Scripts\activate`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Configurar el archivo de base de datos en `src/core/settings.py`
5. Ejecutar migraciones: `python src/manage.py migrate`
6. Iniciar servidor: `python src/manage.py runserver`
=============================================================
org-empresarial/
│
├── .env                  # Credenciales de Postgres, SECRET_KEY, DEBUG
├── .gitignore
├── requirements.txt      # django, psycopg2-binary, django-environ
│
└── src/                  # Carpeta contenedora del código fuente
    │
    ├── manage.py
    │
    ├── core/             # Configuración central del proyecto Django
    │   ├── __init__.py
    │   ├── settings.py   # Configura BBDD Postgres y carpetas de Apps/Templates
    │   ├── urls.py       # Enrutador global del sistema
    │   └── wsgi.py
    │
    ├── apps/             # Subsistemas de la empresa (Unidad 1: TGS)
    │   │
    │   ├── jerarquia/    # Árbol estructural y lógica del nodo raíz
    │   │
    │   ├── areas/        # Listado de áreas de los nodos, personas de su grupo y sus formularios
    │   │
    │   ├── personas/     # ABM de usuarios (Nombre, Apellido, DNI, Selector de Área)
    │   │
    │   ├── formularios/  # Plantillas de carga (Tipo doc, Área dueña y Áreas destinatarias)
    │   │
    │   └── documentos/   # Repositorio central, lógica de archivado (No delete) y recuperación
    │
    └── templates/        # Capa de presentación con Bootstrap
        ├── base/
        │   └── base.html # Layout general del sistema (Navbar, Sidebar, Estilos Bootstrap)
        │
        ├── jerarquia/
        │   └── estructura_arbol.html
        │
        ├── areas/
        │   └── lista_areas_detalle.html
        │
        ├── personas/
        │   ├── persona_form.html
        │   └── persona_list.html
        │
        ├── formularios/
        │   ├── formulario_form.html
        │   └── formulario_list.html
        │
        └── documentos/
            ├── documento_list.html
            └── documentos_archivados.html
============================================================
