from calculations import calculate_median_price
from encode_url import encode_cs2_item_name
import pytest
import asyncio
import json
import aiohttp

async def scrap(target_item_name: str):
    #line = f"https://steamcommunity.com/market/search/render?&norender=1&start=0&count=99&query={encode_cs2_item_name(target_item_name)}"   
    line2 = f"https://steamcommunity.com/market/listings/730/{encode_cs2_item_name(target_item_name)}/render?currency=1&start=0"
    #line3 = f"https://steamcommunity.com/market/priceoverview/?country=RU&currency=3&appid=578080&market_hash_name={encode_cs2_item_name(target_item_name)}"
    async with aiohttp.ClientSession() as session:
        async with session.get(line2) as response:
            data = await response.json()
            return data
              

def get_item_data(cs_item):
    price_list = []

    for item in cs_item.get("listinginfo"):    
        if cs_item["listinginfo"][item]["currencyid"] != 2003:
            price_list.append(cs_item["listinginfo"][item]["converted_price"]/100)
        else:
            price_list.append(cs_item["listinginfo"][item]["price"]/100)
            
    return price_list




async def check():
    listing = ["Prisma Case"]
    x = await scrap("Prisma Case")
    #print(x)
    prices = get_item_data(x)
    print(prices)
    calculated = calculate_median_price(prices)
    print(calculated)
   

asyncio.run(check())