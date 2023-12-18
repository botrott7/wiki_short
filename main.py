import os
from func.get_wiki import get_wikipedia_article
import requests


def save_article(article, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(article)


def main():
    user_input = input('Введите статьи через запятую: ')
    articles = [article.strip() for article in user_input.split(',')]
    for article_title in articles:
        try:
            article = get_wikipedia_article(article_title)
            if article:
                filename = os.path.join('articles', f'{article_title}.txt')
                save_article(article, filename)
                print(f'Файл', f'{article_title}.txt', 'добавлен в articles')
            else:
                print('Страница не найдена')
        except requests.exceptions.RequestException:
            print(f'Ошибка при сохранении статьи')


if __name__ == '__main__':
    main()
