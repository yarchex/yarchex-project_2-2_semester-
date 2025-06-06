import httpx
from config.settings import settings
from utils.logger import logger

async def create_raketa_shipment(order_data: dict):
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                "https://api.raketa.ru/v1/shipments",
                headers={"Authorization": f"Bearer {settings.RAKETA_API_KEY}"},
                json={
                    "order_id": order_data["order_id"],
                    "items": order_data["items"],
                    "destination": order_data["address"]
                }
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        logger.error(f"Raketa API error: {e}")
        raise
