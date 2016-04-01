try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
try:
    from urlparse import parse_qsl, urlsplit, urlunsplit
except ImportError:
    from urllib.parse import parse_qsl, urlsplit, urlunsplit
from bs4 import BeautifulSoup
from collections import OrderedDict
import re


PAT_URL = re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+')

PAT_HREF = re.compile(r'''
                    (?x)( # identify http or https links within href
             (http|https) # make sure we find a resource type
                      :// # ...needs to be followed by colon-slash-slash
                       .* # followed by anyting
                        ) # end of match group
                           ''', re.VERBOSE)


def replace_urls_html(html, params):
    """
    Appends analytics tracking to urls found within the src attribute of
    <a> tags.
    """
    soup = BeautifulSoup(html)
    for a in soup.find_all('a', href=PAT_HREF):
        a['href'] = append_tracking(a['href'], params)
    return str(soup)


def replace_urls_text(text, params):
    """
    Appends analytics tracking to urls found within the plain text.
    """
    for url in re.findall(PAT_URL, text):
        text = text.replace(url, append_tracking(url, params))
    return tex


def append_tracking(url, params):
    """
    Appends google analytics tracking to the url. Uses existing tracking if
    present.
    """

    scheme, netloc, path, query_string, fragment = urlsplit(url)
    query_params = OrderedDict(parse_qsl(query_string))
    try:
        items = params.iteritems()
    except AttributeError:
        items = params.items()
    for key, val in items:
        if not query_params.get(key):
            query_params[key] = val
    new_query_string = urlencode(query_params, doseq=True)
    return urlunsplit((scheme, netloc, path, new_query_string, fragment))
