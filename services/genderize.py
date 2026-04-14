import httpx

GENDERIZE_URL = "https://api.genderize.io"

async def fetch_gender(name: str) :
    async with httpx.AsyncClient() as client:
        response = await client.get(GENDERIZE_URL, params={"name": name})
        return response.json()