import os
from func.get_wiki import get_wikipedia_article
from func.summary import summarize_text
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
                print(f'Файл', f'{article_title}.txt', 'добавлен в articles, директории articles')

                input_file = f'articles/{article_title}.txt'
                output_file = f'results/{article_title}_summary.txt'

                if not os.path.exists(input_file):
                    raise FileNotFoundError('Файл не найден.')

                with open(input_file, 'r', encoding='utf-8') as f:
                    text = f.read()

                try:
                    summary = summarize_text(text, num_sentences=3, stop_words=None, similarity_criteria='token')
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(summary)
                    print(f'Ключевые факты сохранены в файл {article_title}.txt, директории results')
                except Exception as e:
                    print('Произошла ошибка при извлечении ключевых фактов:', str(e))

            else:
                print('Страница не найдена')

        except requests.exceptions.RequestException:
            print(f'Ошибка при сохранении статьи')


if __name__ == '__main__':
    main()
