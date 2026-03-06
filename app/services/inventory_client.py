import httpx
from ..config import INVENTORY_SERVICE_URL

async def reserve_inventory(payload, request_id):
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{INVENTORY_SERVICE_URL}/reserve", 
            json = payload, 
            headers={"X-Request-ID": request_id},
            timeout=5
        )
        
    return response.json()