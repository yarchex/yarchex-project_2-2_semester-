from celery import Celery
from services.raketa_api import create_raketa_shipment

app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task
def process_order_async(order_data):
    create_raketa_shipment(order_data)
