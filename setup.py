# setup.py
from setuptools import setup, find_packages

setup(
    name="url2ndef",  # Nombre del módulo
    version="1.0",     # Versión
    packages=find_packages(),  # Encuentra todos los paquetes de tu proyecto
    description="Un módulo para procesar URLs y generar NDEF",  # Descripción
    author="bst04",  # Tu nombre
    author_email="brunoooost@proton.me",  # Tu email
    url="https://github.com/brunoooost/url2ndef",  # URL de tu repositorio
    classifiers=[  # Esto es para especificar detalles del proyecto en PyPI
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[  # Aquí puedes listar dependencias si las tienes
        # "requests", 
    ],
)
