from urlparse import urlparse


def url_validator(url):
    try:
        result = urlparse(url)
        return True if filter(None, [result.scheme, result.netloc]) else False
    except:
        return False
