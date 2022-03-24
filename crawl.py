from urllib.parse import urlparse
from lxml import html
import requests

def get_urls_from_string(request, base_url):
    page = html.fromstring(request, base_url)
    page.make_links_absolute(base_url = base_url)
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

def validate_response(resp, url):
    if resp.status_code != 200:
        raise Exception(f"{url} Status code is not 200. Got {resp.status_code}")
    if "text/html" not in resp.headers["content-type"].lower():
        raise Exception(f"{url} did not result in HTML response. Got {resp.headers['content-type']}")


def crawl_page(base_url, url, pages):
    normalized_url = normalize_url(url)
    if normalized_url not in pages:
        pages[normalized_url] = 0
        # print(f"nova url {normalized_url}, hodnota dict = {pages[normalized_url]}")


    if urlparse(base_url).netloc != urlparse(url).netloc:
        # print(f"base netloc:{urlparse(base_url).netloc}, url netloc: {url_netloc}")
        pages[normalized_url] = None
        return
    
    if normalized_url in pages and pages[normalized_url] == None:
        return
    
    if pages[normalized_url] > 0:
        pages[normalized_url] += 1
        # print("url > 0")
        return
    
    response = requests.get(url)
    try:
        validate_response(response, url)
    except Exception as e:
        print(e)
        pages[normalized_url] = None
        return
    
    pages[normalized_url] += 1
    # print("page +1")
    urls = get_urls_from_string(response.content, base_url)
    
    for url in urls:
        crawl_page(base_url, url, pages)
    return pages

