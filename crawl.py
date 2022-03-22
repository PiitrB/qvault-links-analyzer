from urllib.parse import urlparse
from lxml import html

def get_urls_from_string(string, base_url):
    page = html.fromstring(string, base_url)
    page.make_links_absolute(base_url)
    urls = []
    for elem in page.iter():
        if elem.tag == "a":
            urls.append(elem.get("href"))
    return urls

def normalize_url(url):
    parsed_url = urlparse(url) #parsing URL to blocks defined in urlparse function
    normalized_url = f"{parsed_url.netloc}{parsed_url.path}" #concacenating two blocks that define unique url
    normalized_url = normalized_url.lower() #making all lowercase
    while len(normalized_url) > 0 and normalized_url[-1] == "/": #while last character of URL is /, remove it.
            normalized_url = normalized_url[:-1]
    return normalized_url