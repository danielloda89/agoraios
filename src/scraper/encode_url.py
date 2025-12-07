ascii_symbols = {
  ' ': '%20',
  '%': '%25',
  '&': '%26',
  '+': '%2B',
  '?': '%3F',
  '#': '%23',
  '=': '%3D',
  '/': '%2F',
  '\\': '%5C',
  '"': '%22',
  "'": '%27',
  '<': '%3C',
  '>': '%3E',
  '|': '%7C',  #VERY IMPORTANT for CS2
  ':': '%3A',
  ';': '%3B',
  '@': '%40',
  '(': '%28',  # For wear grades
  ')': '%29',  # For wear grades
  '[': '%5B',
  ']': '%5D',
  '{': '%7B',
  '}': '%7D',
  '`': '%60',
  '^': '%5E',
  '~': '%7E',
  "★" : "%E2%98%85"
}

async def encode(line: str) -> str:
    new_line = ""
    for letter in line:
        new_line+=ascii_symbols.get(letter,letter) # default for get fallback if no letter in dict
    return new_line