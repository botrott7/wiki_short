import nltk


def evaluate_summary(reference_summary, extracted_summary):
    """Функция evaluatesummary сравнивает два текстовых резюме - referencesummary и extractedsummary и вычисляет их точность, полноту и F1-меру.

    Аргументы:
    - referencesummary: текст, с которым надо сравнить extractedsummary
    - extractedsummary: текст, которое нужно сравнить с referencesummary

    Возвращает:
    - precision: точность (отношение количества верно извлеченных токенов к общему количеству извлеченных источниках)
    - recall: полнота (отношение количества верно извлеченных токенов к общему количеству токенов в referencesummary)
    - f1score: F1-мера (гармоническое среднее точности и полноты)
    """

    reference_tokens = set(nltk.word_tokenize(reference_summary.lower()))
    extracted_tokens = set(nltk.word_tokenize(extracted_summary.lower()))

    true_positives = len(reference_tokens.intersection(extracted_tokens))
    false_positives = len(extracted_tokens - reference_tokens)
    false_negatives = len(reference_tokens - extracted_tokens)

    precision = true_positives / (true_positives + false_positives + 1e-12)
    recall = true_positives / (true_positives + false_negatives + 1e-12)
    f1_score = 2 * (precision * recall) / (precision + recall + 1e-12)

    return precision, recall, f1_score

# import os
# input_file = os.path.join('../articles', 'Мир.txt')
# output_file = os.path.join('../results', 'Мир_summary.txt')
#
# # Пример использования
# with open(input_file, 'r', encoding='utf-8') as file:
#     reference_summary = file.read()
#
# with open(output_file, 'r', encoding='utf-8') as file:
#     extracted_summary = file.read()
#
# precision, recall, f1_score = evaluate_summary(reference_summary, extracted_summary)
# print(f"Точность: {precision:.2f}")
# print(f"Полнота: {recall:.2f}")
# print(f"F1-мера: {f1_score:.2f}")
