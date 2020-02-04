from bs4 import BeautifulSoup
import urllib.parse
import urllib.request


def extract_result(g):
    """
    Creates an object with the fields of a result.
    :param g: HTML element result in a Google search
    :return: Dictionary with the fields href, title, breadcrumbs, description and optionally filetype.
    """
    result = {
        'href': g.find('a').get('href'),
        'title': g.find('h3').text,
        'breadcrumbs': g.find('cite').text,
        'description': g.find('span', {'class': 'st'}).text,
    }
    file_type = g.find('span', {'class': 'sFZIhb'})
    if file_type is not None:
        result['filetype'] = file_type.text
    return result


def extract_results(soup):
    """
    Depicts each entry of a search result block in Google.
    :param soup: Parsed HTML results.
    :return: List of results represented in dictionary objects.
    """
    results = []
    srg = soup.find('div', {'class': 'srg'})
    gs = srg.find_all('div', {'class': 'g'})
    for g in gs:
        result = extract_result(g)
        results.append(result)
    return results


def build_request(url, params):
    """
    Builds a request object ready to be sent as a GET to the given url with the query params.
    :param url: URL to send a GET.
    :param params: Query parameters to insert in the URL.
    :return: Request object.
    """
    qs = urllib.parse.urlencode(params)
    full_url = f'{url}?{qs}'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    return urllib.request.Request(full_url, headers=headers)


def search(query):
    """
    Sends a GET request to Google for searching the top 5 results of the given query.
    Complexity: O(n), n is the number of results obtained from Google.
    :param query: Terms to search.
    :return: List of maximum 5 results if any.
    """
    url = 'https://www.google.com/search'
    params = dict(q=query.strip(), num=5)
    req = build_request(url, params)
    with urllib.request.urlopen(req) as res:
        soup = BeautifulSoup(res.read(), 'html.parser')
    return extract_results(soup)
