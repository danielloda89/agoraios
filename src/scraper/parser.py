from calculations import calculate_median_price
from encode_url import encode_cs2_item_name
import pytest
import asyncio
import json
import aiohttp

async def scrap(target_item_name: str):
    listing_request = f"https://steamcommunity.com/market/listings/730/{encode_cs2_item_name(target_item_name)}/render?currency=1&start=0"
   
    async with aiohttp.ClientSession() as session:
        async with session.get(listing_request) as response:
            data = await response.json()
            
            return data
              

def get_item_data(cs_item):
    price_list = []
    print(cs_item)
    for item in cs_item.get("listinginfo"):    
        price = cs_item["listinginfo"][item].get("converted_price",0)/100
        price_list.append(price)

    return price_list


async def get_market_overview(target_item_name):
    line = f"https://steamcommunity.com/market/priceoverview/?country=RU&currency=1&appid=730&market_hash_name={encode_cs2_item_name(target_item_name)}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(line) as response:
            data = await response.json()
            
            return data


async def check():
    #listing = ["Prisma Case"]
    case = await scrap("Glove Case")
    print(get_item_data(case))
        
   

asyncio.run(check())