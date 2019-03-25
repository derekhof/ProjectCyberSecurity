from multiprocessing import Pool
import bs4 as bs
import requests


def handle_local_links(url, link):
    if link.startswith('/'):
        return ''.join([url, link])
    else:
        return link


def get_links(url):
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_local_links(url, link) for link in links]
        return links

    except TypeError as e:
        print(e)
        print('Got a TypeError, probably got a None that we tried to iterate over')
        return []
    except IndexError as e:
        print(e)
        print('We probably did not find any useful links, returning empty list')
        return []
    except AttributeError as e:
        print(e)
        print('Likely got None for links, so we are throwing this')
        return []
    except Exception as e:
        print(str(e))
        # log this error
        return []


def remove_duplicates(data):
    seen = set()
    seen_add = seen.add
    return [x for x in data if not (x in seen or seen_add(x))]


def create_fqdn(url, link):
    if not link.startswith('http'):
        return '/'.join([url, link])
    else:
        return link


def main():
    url = 'http://spidertest.com'
    url = 'https://waarneming.nl'

    # use multiprocessing for speed
    how_many = 50
    # make a processpool
    p = Pool(processes=how_many)
    parse_us = [url for _ in range(how_many)]

    data = p.map(get_links, [link for link in parse_us])
    data = [url for url_list in data for url in url_list]
    data = remove_duplicates(data)
    data = [create_fqdn(url, link) for link in data]
    p.close()

    for link in data:
        print(link)


if __name__ == '__main__':
    main()
