<div align="center">
  <h1>🌾 NileCrop AI</h1>
  <p><b>Next-Generation Agricultural Intelligence & Edge Computing Ecosystem</b></p>
  <img src="https://img.shields.io/badge/Python-3.12-14354C?style=for-the-badge&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/TensorFlow-2.16-FF6F00?style=for-the-badge&logo=tensorflow" alt="TensorFlow" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI" />
  <img src="https://img.shields.io/badge/TFLite-Edge_Inference-000000?style=for-the-badge&logo=keras" alt="TFLite" />
</div>

<br>

NileCrop is not just a diagnostic tool; it is a comprehensive, production-ready AI ecosystem engineered to bridge the gap between advanced deep learning and real-world agricultural challenges. By deploying highly optimized neural networks directly to the edge, NileCrop empowers local farming communities with sub-second, offline diagnostic capabilities and precision agronomic forecasting.

### 🧠 The Intelligence Layer
At the core of NileCrop lie two distinct, specialized machine learning pipelines designed for scale, accuracy, and localized impact:

**1. Edge-Optimized Vision Engine (Disease Diagnostics)**
Built on a customized `MobileNetV2` architecture, this deep learning model classifies 15 distinct phytopathological conditions with remarkable precision. To ensure democratic access without internet dependency, the model underwent rigorous post-training optimization, compressing the footprint from a heavy **~100MB H5 artifact down to a hyper-efficient ~2.5MB TFLite binary**. The pipeline natively localizes inference outputs, delivering immediate, actionable treatment protocols in Arabic.

**2. Predictive Agronomy Matrix (Crop Recommendation)**
A robust, multi-variable analysis engine that ingests real-time environmental telemetry—including NPK ratios, soil pH, ambient temperature, and humidity—to output high-yield crop recommendations, maximizing resource efficiency and farm profitability.

### ⚡ Architectural Topology
The backend infrastructure is built for high concurrency and low latency, utilizing **FastAPI** as the core ASGI framework. The architecture strictly adheres to clean code principles, separating concerns across modular services, schemas, and RESTful endpoints to ensure maintainability and future scalability.

```text
NileCrop/
├── NileCropBackend/       # High-performance FastAPI Core & Microservices
├── model_1/               # Environment-Aware Predictive ML Pipeline
└── model_2/               # Deep Vision Ecosystem (H5 & TFLite Edge Models)
🚀 Rapid Deployment
The system is designed for frictionless onboarding. Secure your environment, install the dependencies, and launch the inference servers in seconds:

Bash
# 1. Clone the ecosystem
git clone [https://github.com/AshrafAlAsil/NileCrop-Project.git](https://github.com/AshrafAlAsil/NileCrop-Project.git) && cd NileCrop-Project

# 2. Initialize Backend Dependencies
pip install -r NileCropBackend/requirements.txt

# 3. Launch the AI Inference Node
cd model_2/AI && uvicorn disease_api:app --host 0.0.0.0 --port 8000
Architected and engineered by Ashraf Al-Asil for sustainable, AI-driven agriculture.
