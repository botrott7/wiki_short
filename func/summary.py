import spacy
from collections import Counter


def summarize_text(text, num_sentences=3, stop_words=None, similarity_criteria='token'):
    """
    Функция принимает текст и извлекает из него резюме.

    Параметры:
    - text (str): Исходный текст, из которого нужно извлечь резюме.
    - num_sentences (int): Опциональный параметр, указывающий количество предложений, которые должны быть в резюме (по умолчанию 3).
    - stop_words (list): Опциональный параметр, указывающий список стоп-слов, которые будут пропускаться в процессе вычисления оценок предложений (по умолчанию None).
    - similarity_criteria (str): Опциональный параметр, указывающий критерий анализа сходства между словами или энтити предложениями (по умолчанию 'token').

    Возвращает:
    - summary (str): Краткое содержание, состоящее из указанного количества предложений, извлеченных из текста.
    """

    if not spacy.util.is_package("ru_core_news_lg"):
        raise ImportError(
            "Модель не найдена. Установите модель 'ru_core_news_lg' с помощью команды 'python -m spacy download ru_core_news_lg'.")

    nlp = spacy.load("ru_core_news_lg")

    if num_sentences <= 0:
        raise ValueError('Число предложений должно быть положительным числом.')

    if stop_words is None:
        stop_words = nlp.Defaults.stop_words
    else:
        stop_words = set(stop_words)

    doc = nlp(text)
    sentence_scores = Counter()

    for sent in doc.sents:
        for token in sent:
            if token.has_vector and token.text.lower() not in stop_words:
                if similarity_criteria == 'token':
                    sentence_scores[sent] += token.similarity(doc)
                elif similarity_criteria == 'frequency':
                    sentence_scores[sent] += 1 / (doc.count_by(spacy.attrs.LOWER)[token.lower] + 1)
                elif similarity_criteria == 'entity':
                    sentence_scores[sent] += len([ent for ent in doc.ents if ent.text == token.text])

    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    summary = ' '.join([str(sent) for sent, _ in sorted_sentences[:num_sentences]])
    return summary
