from urllib import urlencode
from urlparse import parse_qs, urlsplit, urlunsplit
from bs4 import BeautifulSoup
import re



# PAT_URL = re.compile(  r'''
#                      (?x)( # verbose identify URLs within text
#               (http|https) # make sure we find a resource type
#                        :// # ...needs to be followed by colon-slash-slash
#             (\w+[:.]?){2,} # at least two domain groups, e.g. (gnosis.)(cx)
#                       (/?| # could be just the domain name (maybe w/ slash)
#                 [^ \n\r"]+ # or stuff then space, newline, tab, quote
#                     [\w/]) # resource name ends in alphanumeric or slash
#          (?=[\s\.,>)'"\]]) # assert: followed by white or clause ending
#                          ) # end of match group
#                            ''', re.VERBOSE)

PAT_URL = re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+')

# PAT_URL = re.compile(r'''
#                      (http[s]?  # starts with http or https
#                           ://  # then a colon-slash-slah
#   (?:[a-zA-Z]|[0-9]|[$-_@.&+]  # then this other stuff i uh found on the internet 
#                | [!*\(\),] |   # and am not sure exactly how it works
# (?:%[0-9a-fA-F][0-9a-fA-F]))+)
#                                 ''', re.VERBOSE)

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
    import pdb; pdb.set_trace()
    for url in re.findall(PAT_URL, text):
        text = text.replace(url, append_tracking(url, params))
    return text
 
                                                

def append_tracking(url, params):
    """
    Appends google analytics tracking to the url. Uses existing tracking if present.
    """
     
    scheme, netloc, path, query_string, fragment = urlsplit(url)
    query_params = parse_qs(query_string)
    params.update(query_params)
    new_query_string = urlencode(params, doseq=True)
    return urlunsplit((scheme, netloc, path, new_query_string, fragment))
