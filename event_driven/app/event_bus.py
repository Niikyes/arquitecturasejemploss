import queue

event_queue = queue.Queue()

def publish_event(event: str):
    event_queue.put(event)

def consume_event():
    while not event_queue.empty():
        event = event_queue.get()
        print(f"[Consumidor] Evento recibido: {event}")