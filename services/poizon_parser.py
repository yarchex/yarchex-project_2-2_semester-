import aiohttp
from bs4 import BeautifulSoup
from utils.cache import cache

@cache(ttl=300)
async def parse_poizon_item(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            soup = BeautifulSoup(await resp.text(), "html.parser")
            return {
                "name": soup.find("h1").text,
                "price": float(soup.find(class_="price").text),
                "sizes": [size.text for size in soup.select(".sizes button")]
            }
