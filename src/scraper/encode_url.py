CS2_MARKET_ITEM_URL_NAMES: dict[str, str] = {
    " ": "%20",
    "%": "%25",
    "&": "%26",
    "+": "%2B",
    "?": "%3F",
    "#": "%23",
    "=": "%3D",
    "/": "%2F",
    "\\": "%5C",
    '"': "%22",
    "'": "%27",
    "<": "%3C",
    ">": "%3E",
    "|": "%7C",  # VERY IMPORTANT for CS2
    ":": "%3A",
    ";": "%3B",
    "@": "%40",
    "(": "%28",  # For wear grades
    ")": "%29",  # For wear grades
    "[": "%5B",
    "]": "%5D",
    "{": "%7B",
    "}": "%7D",
    "`": "%60",
    "^": "%5E",
    "~": "%7E",
    "★": "%E2%98%85",
}


def encode_cs2_item_name(item_name: str) -> str:
    encoded_name = ""
    for letter in item_name:
        encoded_name += CS2_MARKET_ITEM_URL_NAMES.get(
            letter, letter
        )  # default for get fallback if no letter in dict

    return encoded_name
