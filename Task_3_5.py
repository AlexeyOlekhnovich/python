from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "работа"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "утром", "днем"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    for i in range(n):
        random_nouns = choice(nouns)
        random_adverbs = choice(adverbs)
        random_adjectives = choice(adjectives)
        joke = (f'{random_nouns} {random_adverbs} {random_adjectives}')
        print(joke)
get_jokes(n=9)