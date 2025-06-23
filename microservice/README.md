# Microservicio - Ejemplo "Hola Mundo"

Este proyecto muestra un microservicio básico REST usando Flask y Docker.

## Rutas

- `GET /hello` → devuelve un saludo en formato JSON.

## Requisitos

- Python 3.10+
- pip

## Ejecutar localmente

```bash
pip install -r requirements.txt
python app/service.py
```

## Ejecutar con Docker

```bash
docker build -t microservice-hello .
docker run -p 5000:5000 microservice-hello
```