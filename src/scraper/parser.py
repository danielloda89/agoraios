import aiohttp

from encode_url import encode_cs2_item_name
import pytest
import asyncio
import json

async def scrap(target_item_name: str):
    line = f"https://steamcommunity.com/market/search/render?&norender=1&start=0&count=99&query={encode_cs2_item_name(target_item_name)}"   
    line2 = f"https://steamcommunity.com/market/listings/730/{encode_cs2_item_name("M249 | System Lock (Factory New)")}/render?currency=3&start=0"
    async with aiohttp.ClientSession() as session:
        async with session.get(line) as response:
            
            data = await response.json()
            #print(data["results"][0]["sell_price"])
            print(data)

asyncio.run(scrap("Dreams & Nightmares Case"))