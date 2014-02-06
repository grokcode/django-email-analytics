from urllib import urlencode
from urlparse import parse_qsl, urlsplit, urlunsplit
from bs4 import BeautifulSoup
from collections import OrderedDict
import re



PAT_URL = re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+')

PAT_HREF = re.compile( r'''
                    (?x)( # identify http or https links within href
             (http|https) # make sure we find a resource type
                      :// # ...needs to be followed by colon-slash-slash
                       .* # followed by anyting
                        ) # end of match group
                           ''', re.VERBOSE)


def replace_urls_html(html, params):
    """ 
    Appends analytics tracking to urls found within the src attribute of <a> tags.
    """
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find_all('a', href=PAT_HREF):
        a['href'] = append_tracking(a['href'], params)
    return str(soup)


def replace_urls_text(text, params):
    """
    Appends analytics tracking to urls found within the plain text.
    """
    for url in re.findall(PAT_URL, text):
        text = text.replace(url, append_tracking(url, params))
    return text
 
                                                

def append_tracking(url, params):
    """
    Appends google analytics tracking to the url. Uses existing tracking if present.
    """
     
    scheme, netloc, path, query_string, fragment = urlsplit(url)
    query_params = OrderedDict(parse_qsl(query_string))
    for key, val in params.iteritems():
        if not query_params.get(key):
            query_params[key] = val
    new_query_string = urlencode(query_params, doseq=True)
    return urlunsplit((scheme, netloc, path, new_query_string, fragment))
