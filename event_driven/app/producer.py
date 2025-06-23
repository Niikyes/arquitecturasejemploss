from app.event_bus import publish_event

def produce():
    event = input("Escribe un evento (ej: usuario_registrado): ")
    print(f"[Productor] Publicando evento: {event}")
    publish_event(event)