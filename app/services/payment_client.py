import httpx
from ..config import PAYMENT_SERVICE_URL

async def charge_payment(payload, request_id):

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYMENT_SERVICE_URL}/charge",
            json=payload,
            headers={"X-Request-ID": request_id},
            timeout=5
        )

    return response.json()