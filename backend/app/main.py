from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.schemas import PredictionResponse
from app.mock_model import predict_mock
from app.gradcam_mock import get_gradcam_url

app = FastAPI(title="CotVision API")

# CORS (para el frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir imágenes estáticas (Grad-CAM)
app.mount("/assets", StaticFiles(directory="assets"), name="assets")


@app.post("/predict", response_model=PredictionResponse)
async def predict(image: UploadFile = File(...)):
    _ = image  # no lo usamos aún

    result = predict_mock()
    result["heatmap_url"] = get_gradcam_url()

    return result
