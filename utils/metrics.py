from prometheus_client import start_http_server, Counter

REQUESTS = Counter("bot_requests", "Total bot requests")
ORDERS = Counter("orders_created", "Total orders created")

def setup_metrics(port: int = 9090):
    start_http_server(port)
