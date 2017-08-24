import urllib


def get_page(url):
    try:
        f = urllib.urlopen(url)
        page = f.read()
        f.close()
        return page
    except:
        return ''
    return ''
