import requests

from log.logs import logger

def get_wikipedia_article(title, lang='ru', format='json'):
    try:
        endpoint = f'https://{lang}.wikipedia.org/w/api.php'
        params = {
            'action': 'query',
            'format': format,
            'titles': str(title),
            'prop': 'extracts',
            'explaintext': True
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        page = next(iter(data['query']['pages'].values()))
        if 'missing' in page or page['extract'] == '':
            return False
        article = page['extract']
        return article
    except requests.exceptions.RequestException as e:
        logger.error(f'Ошибка при получении статьи: {str(e)}')
    except KeyError:
        logger.error('Страница не найдена')
        raise
