import re

def find_dates(text):
    pattern = r'\b\d{1,2}\.\d{1,2}\.\d{4}\b'
    
    dates = re.findall(pattern, text)
    
    return dates

