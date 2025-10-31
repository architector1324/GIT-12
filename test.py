import json
import requests
import datetime
import argparse


QUESTIONS = {
    'en': [
        'Hello, what can you do?',
        'How many planets are in the Solar System?',
        'Create a table of planet masses and radii in SI units',
        'What is the difference between energy and power?',
        # 'Translate "The quick brown fox jumps over the lazy dog" into **[Your language]**',
        'What is 7% of 13,000?',
        'Invent an acronym in English where each letter means something',
        'You’re on Mars. What 3 problems must you solve to survive?',
        'Write a recursive factorial function in Python, C, and Rust',
        'List 3 practical uses for a local AI assistant on a laptop',
        'Convert a borscht recipe into structured JSON: steps, ingredients, cooking time',
        'My faucet is leaking even when turned off. What should I do?'
    ],
    'ru': [
        'Привет, что ты умеешь?',
        'Сколько планет в Солнечной системе?',
        'Составь таблицу масс и радиусов этих планет в СИ',
        'Чем отличается энергия от мощности?',
        'Переведи "The quick brown fox jumps over the lazy dog"',
        'Сколько будет 7% от 13 000?',
        'Придумай 1 аббревиатуру, где каждая буква что-то значит (на русском)',
        'Ты на Марсе. Какие 3 проблемы тебе нужно решить, чтобы выжить?',
        'Напиши рекурсивную функцию факториала на Python, C и Rust',
        'Придумай 3 практических применения локального ИИ на ноутбуке',
        'Преобразуй рецепт борща в JSON: шаги, список покупок, время',
        'Сломался смеситель - капает даже при закрытом кране. Что делать?'
    ]
}


def generate(prompt, model):
    payload = {
        'model': model,
        'prompt': prompt,
        'stream': False,
        'keep_alive': '5m'
    }

    response = requests.post('http://localhost:11434/api/generate', json=payload)
    response.raise_for_status()

    msg = response.json()

    return msg['response']


def test(model, lang, verbose=False):
    # get test
    try:
        test = QUESTIONS[lang]
    except KeyError:
        print(f'Unexpected language: {lang}')
        return None
    
    # test
    if verbose:
        print(f'Testing model [{lang}]: {model}')

    result = []

    for case in test:
        if verbose:
            print(f'User: {case}')

        answer = generate(case, model)

        if verbose:
            print(f'{model.capitalize()}: {answer}')

        result.append({'user': case, str(model): answer})

    return result


def save_md(test_res, output):
    # convert
    out = '# GIT-12\n\n'

    for pair in test_res:
        for name, text in pair.items():
            out += f'---\n\n**{name.capitalize()}:**\n{text}\n\n'

    # save
    with open(output, 'w') as f:
        f.write(out)


# main
if __name__ == '__main__':
    # parse
    parser = argparse.ArgumentParser(description='CLI tool for GIT-12 testing')
    parser.add_argument('model', help='Model name to use')
    parser.add_argument('-l', '--lang', default='en', help='Test language (en, ru)')
    parser.add_argument('-o', '--output', default=None, help='Output markdown file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    args = parser.parse_args()

    output = args.output if args.output else f'{args.model.replace(":", "_")}.md'

    # test
    start = datetime.datetime.now()
    res = test(args.model, args.lang, args.verbose)

    if not res:
        exit(-1)

    duration = datetime.datetime.now() - start

    if args.verbose:
        print(f'Test time: {int(duration.total_seconds())} sec. ({int(duration.total_seconds() / 60)} min.)')

    # save
    save_md(res, output)
