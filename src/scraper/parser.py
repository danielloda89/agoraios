import aiohttp

from encode_url import encode_cs2_item_name
import pytest


async def scrap(target_item_name: str):
    line = f"https://steamcommunity.com/market/search/render?norender=1&start=0&count=99&query={target_item_name}"   
    
    async with aiohttp.ClientSession() as session:
        async with session.get(line) as response:
            print(response.status)
            data = await response.text()
            print(data)


@pytest.mark.asyncio
async def test_encoding():
    assert (
        await encode_cs2_item_name("AK-47 | Redline (Field-Tested)")
        == "AK-47%20%7C%20Redline%20%28Field-Tested%29"
    )
    assert (
        await encode_cs2_item_name("AWP | Dragon Lore (Factory New)")
        == "AWP%20%7C%20Dragon%20Lore%20%28Factory%20New%29"
    )
    assert (
        await encode_cs2_item_name("★ Karambit | Doppler (Factory New)")
        == "%E2%98%85%20Karambit%20%7C%20Doppler%20%28Factory%20New%29"
    )
    assert (
        await encode_cs2_item_name("Dreams & Nightmares Case")
        == "Dreams%20%26%20Nightmares%20Case"
    )
