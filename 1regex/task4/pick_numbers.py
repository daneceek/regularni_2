import re

def pick_numbers(text: str) -> list[int]:
    numbers = [int(match) for match in re.findall(r'\d+', text.replace(' ', ''))]
    
    return numbers
