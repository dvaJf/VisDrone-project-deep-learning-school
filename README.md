Веб-приложение для детекции автотрансопрта на изображениях с дронов на основе датасета VisDrone.

Тут можно протестировать https://cqswte5w2xws6ccceudy4r.streamlit.app/
бекенд тут https://garsdfgtdfgh-dls.hf.space/

## Стек

- **Backend** — FastAPI
- **Frontend** — streamlit
- **ML** — Ultralytics YOLO

## Структура

```
├── backend/
│   └── main.py
│   └── requirements.txt
│   └── Dockerfile
├── frontend/
│   └── main.py
│   └── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
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

### 4. Запустить фронтенд

```bash
streamlit run main.py
```

### Запустить через докер

```bash
docker compose up --build
```

### Настройка env

Переименовать .env_test в .env
Вставить свой токен в HF_TOKEN=
Вставить свою сылку на бекенд в BACKEND_URL=

## API

# `POST /detect`

Детекция объектов на изображении.

| Параметр     | Тип    | Описание                    |
| ------------ | ------ | --------------------------- |
| `file`       | файл   | Изображение (jpg, png)      |
| `model_name` | string | Модель: `nano` или `medium` |
| `conf`       | float  | Порог уверенности (0.0–1.0) |

### ML

## Классы

`car` `van` `truck` `awning-tricycle` `bus` `motor`

## Модели

nano - yolov8m - mAP50 0.415
medium - yolov11x mAP50 0.558
