import axios from 'axios'
import type { PredictionResult } from '../types/prediction'

const API_URL = 'http://localhost:8000'

export async function sendImage(
  image: File
): Promise<PredictionResult> {
  const formData = new FormData()
  formData.append('image', image)

  // MOCK TEMPORAL
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        class: 'Bacterial Blight',
        confidence: 0.91,
        model_used: 'KAN',
        inference_time_ms: 143,
        probabilities: {
          'Bacterial Blight': 0.91,
          'Powdery Mildew': 0.04,
          Aphids: 0.03,
          Healthy: 0.02,
        },
        heatmap_url: null,
        recommendations: [
          'Aplicar tratamiento localizado',
          'Evitar exceso de riego',
        ],
      })
    }, 1200)
  })
}
