from lxml import html

def get_urls_from_string(string, base_url):
    page = html.fromstring(string, base_url)
    page.make_links_absolute(base_url)
    urls = []
    for elem in page.iter():
        if elem.tag == "a":
            urls.append(elem.get("href"))
    return urls
