Веб-приложение для детекции автотрансопрта на изображениях с дронов на основе датасета VisDrone.

## Стек

- **Backend** — FastAPI
- **Frontend** — streamlit
- **ML** — Ultralytics YOLO

## Структура

```
├── backend/
│   └── main.py
├── frontend/
│   └── main.py
├── requirements.txt
└── README.md
```

## Запуск

### 1. Установить зависимости

```bash
pip install -r requirements.txt
```
При первом старте веса скачаются автоматически и закешируются локально.

### 3. Запустить сервер

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

## API

# `POST /detect`

Детекция объектов на изображении.

| Параметр | Тип | Описание |
|---|---|---|---|
| `file` | файл | Изображение (jpg, png) |
| `model_name` | string | Модель: `nano` или `medium` |
| `conf` | float | Порог уверенности (0.0–1.0) |


## Классы

`car`  `van`  `truck` `awning-tricycle`  `bus`  `motor`

### 4. Запустить фронтенд

```bash
streamlit run main.py 
```

### Запустить через докер

```bash
docker compose up --build
```