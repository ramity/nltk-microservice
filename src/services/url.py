import re

def extract_domain(url):
    pattern = r"(?:https?://)?(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,})(?:/.*)?"
    match = re.match(pattern, url)
    if match:
        return match.group(1)
    return None
