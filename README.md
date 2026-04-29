# NileCrop

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![TFLite](https://img.shields.io/badge/TFLite-Edge_Optimized-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://tensorflow.org/lite)
[![License](https://img.shields.io/badge/License-MIT-16A34A?style=flat-square)](LICENSE)

> **AI-driven precision agriculture for the MENA region — delivering real-time crop intelligence and offline plant disease diagnosis with native Arabic treatment protocols.**

---

## Executive Summary

NileCrop is a production-grade, dual-model AI ecosystem designed to address two of the most critical challenges in modern agriculture: **crop selection under variable environmental conditions** and **early-stage plant disease detection in low-connectivity field environments**.

The system combines a classical machine learning pipeline for multi-variable crop recommendation with a deep learning computer vision model for disease classification — both exposed through a modular FastAPI backend and optimized for edge deployment via TensorFlow Lite. All disease outputs are mapped to a structured Arabic-language knowledge base, returning localized diagnosis and treatment protocols without requiring any external translation layer.

This project was developed as a graduation project at **Delta University for Science and Technology**, under the supervision of **Dr. Eman Salah Salem Ahmed**, academic year 2025–2026.

---

## Table of Contents

- [System Architecture](#system-architecture)
- [AI Models](#ai-models)
  - [Model 1 — Crop Recommendation](#model-1--crop-recommendation)
  - [Model 2 — Plant Disease Diagnosis](#model-2--plant-disease-diagnosis)
  - [Edge Optimization — TFLite Conversion](#edge-optimization--tflite-conversion)
- [Backend Architecture](#backend-architecture)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Running the System](#running-the-system)
- [API Reference](#api-reference)

---

## System Architecture
┌──────────────────────────────────────────────────────────────────┐
│                        Client Layer                              │
│              React PWA  ·  Arabic RTL  ·  Mobile-first          │
└────────────────────────────┬─────────────────────────────────────┘
│  HTTPS / REST
┌────────────────────────────▼─────────────────────────────────────┐
│                   NileCropBackend  (FastAPI)                      │
│                                                                   │
│  /recommend  ──►  Model 1 Pipeline  ──►  Crop Prediction         │
│  /disease    ──►  Model 2 Pipeline  ──►  Arabic Disease Report   │
│  /cities     ──►  PostgreSQL        ──►  Geo-matched Cities      │
│  /analytics  ──►  Aggregated Usage Telemetry                     │
│                                                                   │
│  External:  OpenWeather API  ·  SoilGrids  ·  NASA POWER        │
└───────┬──────────────────────┬───────────────────────────────────┘
│                      │
┌───────▼────────┐   ┌─────────▼──────────────────────────────────┐
│  PostgreSQL    │   │               AI Runtime                    │
│  (Render DB)   │   │  crop_model.pkl  ·  disease_model.tflite   │
│                │   │  scaler.pkl      ·  label_encoder.pkl       │
└────────────────┘   │  Arabic JSON Disease Knowledge Base         │
└────────────────────────────────────────────┘

The backend enforces a **strict separation of concerns**: routers handle HTTP parsing only, services contain all business logic, models define the database schema, and schemas enforce I/O contracts via Pydantic v2.

---

## AI Models

### Model 1 — Crop Recommendation

| Property | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Library | Scikit-Learn 1.4 |
| Input Features | N, P, K, Temperature, Humidity, pH, Rainfall |
| Output | Top-3 crops ranked by posterior probability |
| Training Set | 2,200 samples · 21 crop classes · zero missing values |
| Test Accuracy | **99.55%** |
| F1-Score | **99.55%** (weighted average) |

**Decision Rationale:** Random Forest was selected over gradient boosting and neural alternatives due to its interpretability, low inference latency, and robustness against feature scale variance — a critical property given that the 7 input features span incompatible physical units (ppm, °C, %, mm). The model produces calibrated probability estimates via `predict_proba`, enabling the API to return a ranked confidence distribution rather than a hard single-label prediction.

**Artifacts:**
model_1/
├── crop_model.pkl
├── label_encoder.pkl
├── scaler.pkl
└── Crop_recommendation.csv

---

### Model 2 — Plant Disease Diagnosis

| Property | Value |
|---|---|
| Architecture | MobileNetV2 (Transfer Learning) |
| Framework | TensorFlow 2.16 / Keras |
| Input | RGB image, 224 × 224 px |
| Output Classes | 15 distinct disease classes (Pepper, Potato, Tomato) |
| Base Weights | ImageNet |
| Training Strategy | Two-phase: frozen base → fine-tuned last 20 layers |
| Target Validation Accuracy | ~94% |

**Architecture:**
MobileNetV2 Base  (frozen, ImageNet weights)
│
GlobalAveragePooling2D
│
Dense(256, activation='relu')
│
Dropout(0.5)
│
Dense(15, activation='softmax')

The two-phase training strategy mitigates catastrophic forgetting. Phase 1 trains only the classification head at `lr=1e-3`. Phase 2 unfreezes the final 20 layers and fine-tunes at `lr=1e-4`.

**Artifacts:**
model_2/AI/
├── disease_api.py
├── disease_model.h5
├── disease_model.tflite
├── training_script.py
├── class_indices.json
└── arabic_disease_info.json

---

### Edge Optimization — TFLite Conversion
disease_model.h5   (100 MB · float32 · server inference)
│
│   TFLite Converter + Post-Training Integer Quantization (int8)
▼
disease_model.tflite   (~2.5 MB · int8 · edge inference)

| Metric | H5 Model | TFLite Model |
|---|---|---|
| File Size | ~100 MB | ~2.5 MB |
| Size Reduction | — | **97.5%** |
| Inference Target | Server (GPU / CPU) | Mobile edge (CPU only) |
| Network Required | Yes | **No** |
| Accuracy Delta | Baseline | < 2% degradation |

The 97.5% size reduction enables on-device inference with zero network dependency — critical for Egyptian Delta and remote agricultural field conditions.

**Localization layer:**
```json
{
  "Tomato___Late_blight": {
    "name_ar":        "اللفحة المتأخرة في الطماطم",
    "description_ar": "مرض فطري خطير يصيب أوراق وثمار الطماطم...",
    "treatment_ar":   "1. أزل الأوراق المصابة فوراً\n2. رش بمحلول النحاس أسبوعياً..."
  }
}
```

---

## Backend Architecture
NileCropBackend/
├── main.py                   # App factory · CORS · global exception handler
├── config.py                 # Settings via pydantic-settings (12-factor compliant)
├── database.py               # SQLAlchemy engine · session factory · declarative base
├── requirements.txt
├── routers/
│   ├── recommend.py          # POST /recommend
│   ├── disease.py            # POST /disease
│   ├── cities.py             # GET  /cities
│   └── analytics.py
├── services/
│   ├── weather_service.py
│   ├── soil_service.py       # Deterministic fallback defaults
│   └── disease_lookup.py
├── models/
├── schemas/
└── scripts/
├── create_tables.py
├── seed_cities.py
└── seed_disease_info.py

**Key engineering decisions:**

- AI models loaded at module import time — eliminates per-request cold-start latency.
- Deterministic soil fallback — pipeline never fails due to third-party API unavailability.
- No stack traces in production — global handler returns `{"error": "Internal server error"}`.
- Environment-driven CORS — allowed origins read from settings, not hardcoded.

---

## Repository Structure
NileCrop/
├── model_1/
├── model_2/AI/
├── NileCropBackend/
└── Docs/
├── architecture.png
├── erd.png
└── NileCrop_Master_Plan.xlsx

---

## Installation

**Prerequisites:** Python 3.12, PostgreSQL 15+

```bash
git clone https://github.com/AshrafAlAsil/smart-crop-assistant.git
cd smart-crop-assistant
pip install -r NileCropBackend/requirements.txt
cp .env.example NileCropBackend/.env
# Set DATABASE_URL, SECRET_KEY, ALLOWED_ORIGINS
```

**Initialize the database:**
```bash
python NileCropBackend/scripts/create_tables.py
python NileCropBackend/scripts/seed_cities.py
python NileCropBackend/scripts/seed_disease_info.py
```

---

## Running the System

**Development:**
```bash
uvicorn NileCropBackend.main:app --reload --host 0.0.0.0 --port 8000
```

**Production:**
```bash
uvicorn NileCropBackend.main:app --host 0.0.0.0 --port $PORT --workers 2
```

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## API Reference

### `POST /recommend`

**Request:**
```json
{ "city": "Cairo" }
```
**Response:**
```json
{
  "crops": [
    { "name": "rice",   "confidence": 98.5 },
    { "name": "wheat",  "confidence": 84.2 },
    { "name": "cotton", "confidence": 71.0 }
  ],
  "weather": { "temperature": 28.4, "humidity": 62, "rainfall": 5.1 },
  "soil":    { "N": 50, "P": 38, "K": 42, "ph": 6.8 }
}
```

### `POST /disease`

**Request:** `multipart/form-data` — field: `file` (JPG / PNG, max 5 MB)

**Response:**
```json
{
  "disease_en":     "Tomato___Late_blight",
  "disease_ar":     "اللفحة المتأخرة في الطماطم",
  "confidence":     92.3,
  "description_ar": "مرض فطري خطير يصيب أوراق وثمار الطماطم...",
  "treatment_ar":   "1. أزل الأوراق المصابة فوراً\n2. رش بمحلول النحاس أسبوعياً...",
  "low_confidence": false
}
```

### `GET /cities?q={query}`
Full-text search across 60 Egyptian cities in Arabic and English.

### `GET /health`
Liveness probe. Returns `{"status": "ok", "timestamp": "..."}`.

### `GET /analytics`
Aggregated telemetry: total requests, top-5 crops, top-5 diseases.

---

## License

Released under the [MIT License](LICENSE).Sonnet 4.6AdaptiveClaude
