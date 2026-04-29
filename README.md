# NileCrop 🌿
> **An Intelligent Agricultural Management System powered by AI & Edge Computing.**

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16-orange?style=flat-square&logo=tensorflow)](https://tensorflow.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-v0.110-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)

NileCrop is a comprehensive AI-driven ecosystem designed to empower farmers with data-backed decisions. By integrating advanced machine learning models with a robust backend architecture, NileCrop offers real-time crop recommendation and precision disease diagnosis.

---

## 🚀 Core Capabilities

### 1. Precision Disease Diagnosis (AI Model 2)
Utilizes a **MobileNetV2** architecture optimized for real-world agricultural conditions.
* **Accuracy:** High-fidelity classification across 15 distinct plant/disease categories.
* **Optimization:** Fully converted to **TFLite** (FP16 Quantization) for low-latency edge inference on mobile devices.
* **Localization:** Provides detailed diagnostic reports and treatment plans in Arabic.

### 2. Intelligent Crop Recommendation (AI Model 1)
A multi-variable analysis engine that suggests the optimal crop based on environmental data.
* **Inputs:** Soil NPK levels, Temperature, Humidity, pH, and Rainfall.
* **Impact:** Maximizes agricultural yield and resource efficiency.

### 3. Scalable Backend API
A high-performance RESTful API built with **FastAPI**, featuring modular routing for weather, soil, and AI services.

---

## 🏗️ Project Architecture

```text
NileCrop/
├── model_1/               # Crop Recommendation Module (ML)
├── model_2/               # Plant Disease Module (Deep Learning)
│   └── AI/                # H5 & TFLite models + Inference logic
├── NileCropBackend/       # FastAPI Core Engine (Backend)
├── Docs/                  # Project Documentation & Presentations
└── .gitignore             # Environment & Cache Protection