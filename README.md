# NileCrop

[

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)

](https://www.python.org/)
[

![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)

](https://tensorflow.org/)
[

![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?style=flat-square&logo=fastapi&logoColor=white)

](https://fastapi.tiangolo.com/)
[

![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)

](https://scikit-learn.org/)
[

![TFLite](https://img.shields.io/badge/TFLite-Edge_Optimized-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)

](https://tensorflow.org/lite)
[

![License](https://img.shields.io/badge/License-MIT-16A34A?style=flat-square)

](LICENSE)

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
