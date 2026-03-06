import os

PAYMENT_SERVICE_URL = os.getenv(
    "PAYMENT_SERVICE_URL",
    "http://localhost:8002"
)

INVENTORY_SERVICE_URL = os.getenv(
    "INVENTORY_SERVICE_URL", 
    "http://localhost:8003"
)