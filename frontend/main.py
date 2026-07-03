import streamlit as st
import requests
import base64
from PIL import Image
import io

import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

with st.sidebar:

    model_name = st.radio(
        "Выберите модель",
        options=["nano", "medium"],
        captions=[
            "Быстрая",
            "Точная"
        ]
    )
    conf = st.slider(
        "Порог уверенности",
        min_value=0.1,
        max_value=0.9,
        value=0.5,
        step=0.05,
    )


st.title("Детекция автомобилей")
st.info("Подсказка: загрузите фото машин на дороге")

uploaded_file = st.file_uploader(
    "Загрузи изображение",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Оригинал")
        st.image(uploaded_file, width='stretch')

    if st.button("Запустить детекцию", width='stretch'):

        with st.spinner("Обрабатываем..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/detect",
                    files={"file": uploaded_file.getvalue()},
                    params={"model_name": model_name, "conf": conf}
                )

                if response.status_code == 200:
                    data = response.json()

                    with col2:
                        st.subheader("Результат")
                        img_bytes = base64.b64decode(data["image"])
                        result_img = Image.open(io.BytesIO(img_bytes))
                        st.image(result_img, width='stretch')

                    st.divider()
                    st.subheader(f"Найдено объектов: {data['total']}")

                    class_counts = {}
                    for det in data["detections"]:
                        name = det["class"]
                        class_counts[name] = class_counts.get(name, 0) + 1

                    if class_counts:
                        cols = st.columns(len(class_counts))
                        for i, (cls, count) in enumerate(class_counts.items()):
                            with cols[i]:
                                st.metric(label=cls, value=count)

                else:
                    st.error(f"Ошибка сервера: {response.status_code}")

            except requests.exceptions.ConnectionError:
                st.error("Не могу подключиться к серверу.")