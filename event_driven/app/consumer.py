from app.event_bus import consume_event

def consume():
    print("[Consumidor] Esperando eventos...")
    consume_event()