![python veriosn](https://img.shields.io/badge/python-3.7%2B-blue)
![](https://img.shields.io/badge/test-task-red)

## Решение задания на стажировку

Запущенный прототип по адрeсу - http://short.dasnas.com

<!-- Для запуска на локальном ПК воспользуйтесь инструкцией ниже (Docker-Compose):
1. Клонируйте репозиторий на локальную машину:

    `https://github.com/acecrosser/ozon.git`

2. Перейдите в папку скаченного проекта:

    `cd ozon`

3. Запустите команду docker-compose:

    `docker-compose up -d` -->


### Описание задания на стажировку
**Написать сервис сокращения ссылок.**

**Функциональные требования:**

Реализовать следующие методы API:
1. На вход поступает длинная ссылка, возвращается сокращённая ссылка
    ```
    Request:
    POST /short {"url": "long-url-here"}
    Response:
    {"url": "short-url-here"}
    ```
2. На вход поступает сокращённая ссылка, возвращается полная ссылка
    ```
    Request:
    POST /long {"url": "short-url-here"}
    Response:
    {"url": "long-url-here"}
    ```

**Нефункциональные требования:**

В качестве хранилица использовать РСУБД(postgresql, sqllite)

* Postgresql можно запустить в docker:

    `docker run --rm -p 5432:5432 postgres:10.5`

*В качестве структуры веб сервиса - https://github.com/golang-standards/project-layout
Сервис можно деализовать как стандартной библиотекой(net/http), так и фреймворками gin, echo
Запросы в БД на pure sql, либо https://github.com/Masterminds/squirrel
Короткие ссылки должны основываться на id записи(sequence) в БД, переведённой в систему счисления с алфавитом [A-Za-z0-9]*






