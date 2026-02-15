# Шаблон для Python проектов

Универсальный шаблон для Python приложений.

## Как использовать?

1) Установка зависимостей

```bash
pip install -r requirements.txt
```

2) Установка pre-commit

```bash
pre-commit install
```

3) Радоваться


## Зачем нужен шаблон?

Стандартизация приложений и использование единого стиля кода во всех проекта. Это достигается за счет github actions и pre-commit.
Pre-commit - заставит пройти все линтеры и форматеры перед тем, как ты сможешь сделать коммит.
Github actions - запускают линтеры и тесты для проверки проекта.


## Как работать с Github actions?

Нужен локально установленный Github Runner. Понять что это такое можно по [этому руководству](https://docs.github.com/ru/actions/concepts/runners/self-hosted-runners)
