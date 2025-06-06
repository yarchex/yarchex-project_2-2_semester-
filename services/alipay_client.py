import httpx
from config.settings import settings

async def make_payment(amount: float, order_id: str):
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://openapi.alipay.com/gateway.do",
            params={
                "app_id": settings.ALIPAY_API_KEY,
                "method": "alipay.trade.app.pay",
                "out_trade_no": order_id,
                "total_amount": amount
            }
        )
        return resp.json()
