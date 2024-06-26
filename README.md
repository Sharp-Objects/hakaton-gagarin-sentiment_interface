## Status badge

[![We recommend PyCharm](https://www.elegantobjects.org/intellij-idea.svg)](https://www.jetbrains.com/pycharm/)
[![Python CI](https://github.com/Sharp-Objects/hakaton-gagarin-sentiment_interface/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/Sharp-Objects/hakaton-gagarin-sentiment_interface/actions/workflows/main.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Требования к интерфейсу

Чтобы решение проходило автоматические тесты необходимо чтобы:

* run_me должен запускаться командой

```bash
python run_me.py
```

1) Можно менять run_me.py на свое усмотрение, но

* run_me.py должен читать json c текстами из папки data

* run_me.py должен складывать скоры сообщений в results/output_scores.json

* Можно добавлять любые функции в run_me.py, однако, пожалуй, функции run_me.load_data и run_me.save_data лучше не
  менять

2) Формат данных, возвращаемых из final_solution.solution.score_texts, желательно не менять. Хотя формально формат
   вывода тестироваться не будет, тестироваться будет только run_me.py и файл results/output_scores.json (см п.1)

2) Рекомендуем использовать python3.10.12 и версии библиотек из requirements.txt.
   Если для решения Вам необходимы дополнительные библиотеки, то просьба сообщить об этом заранее (чтобы мы могли бы
   проверить их на совместимость с тестирующей системой) с указанием версии, например:

> Хотим jax==0.0.0

# Оценивание

### Работоспособность

* Если решение запускается, то получаете 6 баллов

* Скорость: штраф -1 балл за каждые 10 секунд на инференсе

* No GPU: +1 балл если решение запускается только на CPU

* No internet: +1 балл если решение может запускаться локально, без запросов к сторонним сервисам

### Функциональные требования

$$team\_score = 100 \cdot \left(\frac{1}2 F1Score + \frac 1 2 Accuracy\right),$$

где $F1Score$ - macro-averaged F-score задачи распознавания сущностей, Accuracy - точность распознавания сентимента

$team\_scor$-ы сортируются, обединяются в бакеты шириной 2пп, команды из топ-1 бакета получают 10 баллов, топ-2 - 9 и
т.д.

### Технологичность

* Стиль: 4 балла, если код соответствует стандартам [PEP8](https://peps.python.org/pep-0008/) и проходит тесты mypy и
  flake8

* +1 балл за каждую успешную попытку ускорить модель

* +1 балл за каждый ''перспективный'' подход или идею.

* +1 балл за уникальную идею (которая была предложена не более 2-мя командами)

Обоснование должно быть в папке important_notebooks (может быть в формате jupyter notebook).

### Презентация

* 10 баллов

Баллы можно потерять, если в презентации текста больше, чем картинок, не смогли ответить на какой-нибудь вопрос и пр.

### Потенциал

* На усмотрение эксперта

# Про разметку датасета

### Sentiment

Sentiment score может принимать значения в диапазоне [1 - 5], где

* 1: что-то очень негативное относительно компании или дана рекомендация "продавать"

* 2: что-то скорее негативное, например, вышла отчетность ниже ожиданий, проблемы на каком-нибудь заводе, санкции и пр.

* 3: Нейтральная новость. Важно! Если текст

> "Акция выросла на 40% за день"

Считается нейтральной новостью (т.к. цены акций -
скорее [мартингал](https://en.wikipedia.org/wiki/Martingale_(probability_theory))).

> "Акция выросла на 40% за день, потому что ...

Считается положительной новостью (sentimen\_score > 3), т.к. есть объяснение

* 4: Что-то положительное, например, вышла отчетность выше ожиданий, успехи на каком-нибудь заводе, новый контракт и пр.

* 5: Что-то очень положительное или есть рекомендация "покупать" или "входит в подборку нашух супер-акций"
