# 外部モジュール

import requests
import urllib.request
from bs4 import BeautifulSoup

# 問題 1

# 確認済み


# 問題 2

def get_html_content(url):
    html = urllib.request.urlopen(url).read()
    return html


# 問題 3

def get_soup(url):
    soup = BeautifulSoup(get_html_content(url), "lxml")
    return soup


# 問題 4

def get_title(url):
    title = get_soup(url).title.string
    return title

print(get_title("http://requests-docs-ja.readthedocs.io/en/latest/"))
# >>> Requests: 人間のためのHTTP — requests-docs-ja 1.0.4 documentation

# 問題 5

def get_all_links(url):
    a_tags = get_soup(url).find_all("a")
    all_link = {a_tag["href"] for a_tag in a_tags}
    return all_link

print(get_all_links("http://requests-docs-ja.readthedocs.io/en/latest/"))
# >>>
"""
{'user/quickstart/#id6', '#requests-http', 'user/intro/', 'user/advanced/#event-hooks', 'py-modindex/',
 'user/quickstart/#id2', 'user/advanced/#ssl-cert-verification', 'user/advanced/#link-headers',
 'https://flattr.com/thing/442264/Requests', 'api/#request-sessions', 'user/advanced/#proxies',
 'user/quickstart/#id5', 'http://pypi.python.org/pypi/requests', 'user/quickstart/#json',
 'user/authentication/#new-forms-of-authentication', 'genindex/', '#id5', 'user/intro/#id2', '#id1',
 'dev/todo/', 'user/quickstart/#id9', 'user/install/', '#api', 'user/install/#distribute-pip',
 'user/quickstart/#id3', 'community/out-there/', 'user/quickstart/', 'user/install/#id3',
 'user/quickstart/#post', 'user/advanced/', 'dev/authors/', 'user/advanced/#http-verbs',
 'user/quickstart/#url', 'user/quickstart/#id11', 'user/intro/#requests', 'user/quickstart/#id12',
 'user/authentication/#other-authentication', 'user/advanced/#compliance', 'https://gist.github.com/973705',
 'user/quickstart/#id7', 'mailto:me@kennethreitz.com', 'https://www.gittip.com/kennethreitz/',
 'user/advanced/#custom-authentication', 'http://gum.co/RRZc', 'api/#main-interface', '#id2',
 'user/advanced/#streaming-requests', 'community/out-there/#id4', 'http://github.com/kennethreitz/requests',
 '#', 'user/advanced/#keep-alive', 'community/faq/', 'user/quickstart/#id4', 'community/support/',
 '#id4', 'http://github.com/kennethreitz/requests/issues', 'https://github.com/shazow/urllib3',
 'user/authentication/', 'api/', 'user/intro/#apache2', 'user/advanced/#request-and-response-objects',
 'community/updates/', 'user/intro/#id3', 'user/authentication/#basic-authentication', 'user/quickstart/#id10',
 'user/authentication/#digest-authentication', 'user/quickstart/#timeouts', 'user/install/#install',
 'user/install/#cheeseshop', 'user/advanced/#body-content-workflow', 'user/quickstart/#id8', 'dev/philosophy/',
 'user/advanced/#session-objects', 'https://github.com/kennethreitz/requests', '#id3'}
"""




####
