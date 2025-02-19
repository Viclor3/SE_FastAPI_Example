from fastapi import FastAPI
from transformers import pipeline
from models.Item import Item

classifier = pipeline("sentiment-analysis")


def register_routes(app: FastAPI):
    @app.get(
        "/",
        summary="Запуск сервиса",
        description="Возвращает сообщение о запуске FastAPI сервиса.")
    def root():
        return {"message": "FastApi service started!"}

    @app.get("/{text}",
             summary="Анализ тональности текста",
             description="Принимает текст и возвращает его тональность (положительная/отрицательная).")
    def get_params(text: str):
        return classifier(text)

    @app.post("/predict/",
              summary="Предсказание тональности",
              description="Принимает объект Item с текстом и возвращает его тональность.")
    def predict(item: Item):
        return classifier(item.text)
