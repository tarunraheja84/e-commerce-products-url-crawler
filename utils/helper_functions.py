import re
from urllib.parse import urlparse

def is_same_domain(url, domains):
    parsed = urlparse(url)
    return parsed.netloc in domains and parsed.scheme in ['http', 'https']

def matches_pattern(parsed_url, patterns):
    path_parts = parsed_url.path.strip("/").split("/")

    if len(path_parts) >= 2:
        second_last = path_parts[-2]
        last = path_parts[-1]

        for pattern in patterns:
            if pattern.startswith("^"):
                if re.match(pattern, last):
                    return True
            elif second_last == pattern:
                return True
    return False
