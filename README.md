# Прогноз погоды

Этот проект представляет собой веб-приложение для получения прогноза погоды в выбранном городе.

### Что было сделано

- Разработка веб-приложения с использованием FastAPI для обработки запросов и предоставления данных о погоде.
- Использование API Open Meteo для получения актуальной погодной информации.
- Использование HTML, CSS и JavaScript для создания пользовательского интерфейса  ввода города.
- Использование Pandas для обработки и загрузки данных из CSV файла с координатами городов.
- Запуск приложения в Docker контейнере для удобства развертывания.(в доработке)

### Используемые технологии

- **FastAPI** - современный веб-фреймворк для Python.
- **HTML, CSS, JavaScript** - для создания интерактивного пользовательского интерфейса.
- **Pandas** - для обработки данных из CSV файла.
- **Docker** - для контейнеризации и упрощения развертывания приложения.

### Как запустить

1. **Склонируйте репозиторий: .
в терминале введите: .
"git clone https://github.com/koposOFF/weather_app.git" .
"cd weather_app" .
"uvicorn main:app --reload" .

Перейдите в браузер и откройте [http://localhost:8000](http://localhost:8000).
