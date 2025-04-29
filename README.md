---
title: Agroshield Crop Recommendation
emoji: 🚀
colorFrom: yellow
colorTo: gray
sdk: gradio
sdk_version: 5.26.0
app_file: app.py
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


# 🌱 AgroShield - AI-Powered Crop Recommendation Model

[![Hugging Face Spaces](https://img.shields.io/badge/Live%20Demo-Hugging%20Face-blue?logo=huggingface)](https://huggingface.co/spaces/dkg-2/Agroshield_Crop_Recommendation)

AgroShield's Crop Recommendation system is an intelligent decision-support tool for farmers. By inputting key soil and climate parameters, the model suggests the most suitable crop to grow, optimizing yield and sustainability.

---

## 🧠 Model Overview

This model uses a **machine learning classification algorithm** (e.g., Random Forest, Decision Tree, or Logistic Regression) trained on agro-climatic data. It analyzes multiple features including:

- Nitrogen, Phosphorus, Potassium (NPK) levels
- pH
- Rainfall
- Temperature
- Humidity

Based on these inputs, it predicts the **best crop to grow** under the given conditions.

---

## 🔍 Use Case

✅ Helps farmers plan crop rotation based on current soil and weather  
✅ Promotes sustainable agriculture  
✅ Can be expanded to integrate weather forecasts or pest/disease alerts

---

## 🧪 Input Parameters

- `Nitrogen` (N)
- `Phosphorus` (P)
- `Potassium` (K)
- `Temperature` (°C)
- `Humidity` (%)
- `pH` (acidity/alkalinity of soil)
- `Rainfall` (mm)

---

## 🔧 Tech Stack

- **Framework**: Scikit-learn / Pandas / NumPy
- **Web UI**: Gradio
- **Deployment**: Hugging Face Spaces
- **Language**: Python 3.x

---

## 🚀 Try It Out

👉 **[Live Demo on Hugging Face Spaces](https://huggingface.co/spaces/dkg-2/Agroshield_Crop_Recommendation)**

---

## 💻 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/AgroShield-Crop-Recommendation.git
cd AgroShield-Crop-Recommendation
pip install -r requirements.txt
python app/app.py
