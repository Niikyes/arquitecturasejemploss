# Event-Driven - Ejemplo "Hola Mundo"

Este ejemplo simula un sistema orientado a eventos con un productor y un consumidor usando una cola interna.

## Ejecutar

```bash
python main.py
```

## Flujo

1. El productor genera un evento (por consola).
2. El evento es publicado en una cola.
3. El consumidor lee de la cola y reacciona al evento.

Este patrón es la base de arquitecturas asincrónicas desacopladas.