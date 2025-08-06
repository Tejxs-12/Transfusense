# 🧨 TransfuSense – AI-Powered Assistant for Thalassemia Care

TransfuSense is a multilingual, AI-powered assistant designed to support Thalassemia patients, caregivers, and healthcare providers. It helps manage complex lab reports, predicts transfusion timelines, and assists with blood availability through an accessible, intuitive interface — even in low-resource or rural areas.

🔗 Live Demo: [Add your Streamlit/Hugging Face/Website link here]  
📟️ Demo Video: [YouTube or Drive link]  
🏆 Built for: [Hackathon Name] – Theme: Healthcare Innovation for Thalassemia

---

## 🧠 Key Features

✅ OCR Lab Report Reader  
✅ AI-based Report Summarizer (with multilingual output)  
✅ Transfusion Date Predictor using historical patterns  
✅ Multilingual Translation (NLLB / Argos Translate)  
✅ Voice Command Support via Web Speech API  
✅ Responsive UI powered by Streamlit + React (optional)  
✅ Offline/Edge-compatible deployment with Hugging Face models

---

## 🎯 Problem Statement

Every 3–4 weeks, millions of Thalassemia patients must:

📍 Find compatible blood for transfusion  
🔍 Interpret complex lab reports without medical expertise  
🗓️ Predict their next transfusion — often with guesswork

❌ Rural patients and caregivers are left overwhelmed  
❌ Hospitals lack real-time, multilingual AI assistance  
❌ Delays and misinterpretation cost lives

TransfuSense bridges this critical healthcare gap with AI.

---

## 🛠️ Tech Stack

| Layer | Tools/Models |
|-------|--------------|
| Frontend | Streamlit (or React + Tailwind) |
| OCR | PaddleOCR |
| Summarization | DistilBART / BioBERT (via Hugging Face Transformers) |
| Translation | NLLB / Argos Translate |
| Prediction Model | Scikit-learn (RandomForestRegressor) |
| Agentic Flow | Custom Python-based modular tool agent |
| Deployment | Hugging Face Spaces / Streamlit Sharing |
| Data | Synthetic + real anonymized lab data (CSV) |

---

## 🧪 Demo Walkthrough

1. 📄 Upload lab report PDF/image  
2. 🔍 OCR extracts key fields  
3. ✨ AI summarizes & translates output  
4. 🗕️ Predicts next transfusion date  
5. 🎧 Optional voice command interface

🖼️ Screenshots:  
- MoodBoard Muse (UI Concept)  
- Layout Genie (Interactive panel)  
- Transfusion Prediction Chart

---

## 📁 Project Structure

```
transfusense/
│
├── app/
│   ├── main.py                # Streamlit app
│   ├── ocr_tool.py            # OCR processing
│   ├── summarizer.py          # AI summary generator
│   ├── translator.py          # Multilingual support
│   ├── predictor.py           # ML prediction logic
│   └── agent_controller.py    # Modular agent flow
│
├── data/
│   └── sample_transfusion_data.csv
│
├── models/
│   └── transfusion_model.pkl
│
├── ui/
│   └── react-frontend/ (optional)
│
├── assets/
│   └── report_screenshots/, visuals/
│
└── README.md
```

---

## 🚀 Setup Instructions

Clone the repo:

```bash
git clone https://github.com/your-username/transfusense.git
cd transfusense
```

Create virtual environment & install:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

Run app locally:

```bash
streamlit run app/main.py
```

---

## 📊 Sample CSV Data

Included in /data/sample_transfusion_data.csv:

| Date       | Hemoglobin | Ferritin | Last Transfusion | Next Transfusion (Predicted) |
|------------|------------|----------|------------------|-------------------------------|
| 2025-07-01 | 7.2 g/dL   | 1850 ng/mL | 2025-06-01        | 2025-07-28                    |

---

## 🌍 Future Scope

- Integration with e-RaktKosh API (real-time blood inventory)  
- WhatsApp/SMS-based chatbot for rural caregivers  
- Long-term patient monitoring dashboard  
- Offline-first Android app for outreach workers

---

## 👥 Team & Credits

Built by: [Your Name]  
With models from Hugging Face: Mistral 7B, DistilBART, NLLB  
Special thanks to: [Mentors/Hackathon org]  

---

## 📜 License

MIT License – use, share, and improve ❤️
