import aiohttp
import asyncio
import json

import logging
logging.basicConfig(level=logging.INFO)


async def main():
    request_url_semen = "https://steamcommunity.com/inventory/76561198156292503/730/2"
    url = "https://steamcommunity.com/inventory/76561198192913034/730/2"
    async with aiohttp.ClientSession() as session:
        async with session.get(request_url_semen) as respose:
            payload = await respose.json()

            assets = payload.get("assets")
            if isinstance(assets, dict):
                #print("Dict")
                pass            
            if isinstance(assets, list):
                #print("list")
                pass

            for item in assets:
                if isinstance(item,dict):
                    #print(f" {item.get("instanceid"), item.get("classid"), item.get("assetid")} --- Dict")          
                    pass
                if isinstance(item,list):
                    pass
                    #print(f" {item.get("instanceid"), item.get("classid"), item.get("assetid")} --- List")          

            descriptions = payload.get("descriptions")
            logging.info(type(descriptions))
            for ite in descriptions:
               if isinstance(ite, dict):
                logging.info(f"{ite} - Dict")

                         
            if isinstance(ite, list):
                logging.info(f"{ite} - list")
                

asyncio.run(main())