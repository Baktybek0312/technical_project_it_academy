import requests
from bs4 import BeautifulSoup


def habr_articles(request):
    request_page = request.GET.get('page')
    page = 'page1'
    if request_page:
        page = 'page' + str(request_page)
    url = 'https://habr.com/ru/all/' + page
    host = 'https://habr.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    response = requests.get(url,
                            headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    article_list = soup.find_all('div', class_='tm-article-snippet')
    article_list_json = []
    for article in article_list:
        list_teg_p = []
        for p in article.find_all('p'):
            list_teg_p.append(p.text)
        new_article = {
            'title': article.find('h2').text,
            'link': host + article.find('a', class_='tm-article-snippet__title-link')['href'].strip('/'),

        }
        article_list_json.append(new_article)
    return article_list_json

