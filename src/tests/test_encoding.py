from src.scraper.encode_url import encode

import asyncio
import pytest

@pytest.mark.asyncio
async def test_encode():
    assert await encode("AK-47 | Redline (Field-Tested)") == "AK-47%20%7C%20Redline%20%28Field-Tested%29"
    assert await encode("AWP | Dragon Lore (Factory New)") == "AWP%20%7C%20Dragon%20Lore%20%28Factory%20New%29"
    assert await encode("★ Karambit | Doppler (Factory New)") == "%E2%98%85%20Karambit%20%7C%20Doppler%20%28Factory%20New%29"
    assert await encode("Dreams & Nightmares Case") == "Dreams%20%26%20Nightmares%20Case"


@pytest.mark.asyncio
async def test_encode_len():
    assert await encode("") == ""