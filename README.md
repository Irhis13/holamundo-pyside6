# holamundo-pyside6

Este proyecto muestra un *Hola Mundo* utilizando PySide6.

------------------------------------------------------------

## Clonación del repositorio

Para obtener el código en tu máquina local, usa los siguientes comandos:

    git clone https://github.com/di-mcgrawhill/holamundo-pyside6.git
    cd holamundo-pyside6/

------------------------------------------------------------

## Instalación de Python3

Es necesario tener **Python3** instalado en el sistema. 

### Linux
Python3 suele venir preinstalado en la mayoría de distribuciones. Para comprobarlo, ejecuta:

    python3 --version

Si no está instalado, descárgalo desde:
https://www.python.org/downloads/

Más información en la documentación oficial:
https://docs.python.org/3/

### Windows
Descarga el instalador desde:
https://www.python.org/downloads/windows/

Guía de instalación en:
https://docs.python.org/3/using/windows.html

### macOS
Descarga el instalador desde:
https://www.python.org/downloads/mac-osx/

Guía de instalación en:
https://docs.python.org/3/using/mac.html

------------------------------------------------------------

## Creación de un entorno virtual (venv)

Se recomienda crear un entorno virtual para aislar las dependencias del proyecto. 

Ejecuta el siguiente comando para crear el entorno virtual:

    python3 -m venv venv

------------------------------------------------------------

## Activación del entorno virtual

Dependiendo del sistema operativo, el comando para activar el entorno virtual varía:

### Linux / macOS

    source venv/bin/activate

### Windows

    venv\Scripts\activate.bat

------------------------------------------------------------

## Instalación de dependencias

Una vez activado el entorno virtual, instala las dependencias ejecutando:

    pip install -r requirements.txt

------------------------------------------------------------

## Ejecución del proyecto

Para ejecutar la aplicación *Hola Mundo*, usa el siguiente comando:

    python3 src/holamundo_pyside6/holamundo.py

Esto abrirá la ventana con el mensaje *Hola Mundo!*.

------------------------------------------------------------

## Notas adicionales

Si tienes problemas con dependencias o ejecución en diferentes sistemas operativos, consulta la documentación de PySide6:

https://doc.qt.io/qtforpython/
