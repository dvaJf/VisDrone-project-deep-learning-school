from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from huggingface_hub import hf_hub_download
from PIL import Image
import io, base64, numpy as np, cv2

HF_REPO_ID = "garsdfgtdfgh/medium"
MODEL_FILES = {"nano": "nano.pt", "medium": "medium.pt"}

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
models = {}

@app.on_event("startup")
async def startup():
    for name, filename in MODEL_FILES.items():
        path = hf_hub_download(repo_id=HF_REPO_ID, filename=filename, local_dir="weights")
        models[name] = YOLO(path)

@app.post("/detect")
async def detect(file: UploadFile = File(...), model_name: str = "medium", conf: float = 0.25):
    if model_name not in models:
        raise HTTPException(400, f"Нет модели '{model_name}'. Доступны: {list(models.keys())}")

    image = Image.open(io.BytesIO(await file.read()))
    results = models[model_name].predict(np.array(image), conf=conf, verbose=False)[0]

    _, buf = cv2.imencode(".jpg", results.plot())

    return {
        "total": len(results.boxes),
        "detections": [{"class": results.names[int(b.cls[0])], "confidence": round(float(b.conf[0]), 2)} for b in results.boxes],
        "image": base64.b64encode(buf).decode(),
    }