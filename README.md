# ✈️ AI Travel Planner (LangGraph + Gemini AI)

An intelligent **AI-powered travel planning web application** that generates personalized travel itineraries using **LangGraph-based workflows** and **Google Gemini AI**, with a modern **Streamlit UI** and optional **email delivery**.

---

## 📌 Project Overview

AI Travel Planner helps users plan trips by simply entering:
- Destination & preferred area  
- Trip duration  
- Budget  
- Travel type  
- Personal interests  

The system then **thinks step-by-step like a travel expert** using a graph-based AI workflow:
1. Analyzes the traveler profile  
2. Recommends hotels  
3. Suggests places to visit  
4. Estimates total trip cost  
5. Produces a structured travel summary  

---
## 🖥️ Application Preview
<img width="1887" height="813" alt="image" src="https://github.com/user-attachments/assets/266b1d81-9e31-40a4-8b62-ecb533aafd67" />


## 🚀 Key Features

- 🧠 **Graph-based AI reasoning** using LangGraph  
- 🌍 Personalized travel plans using **Gemini 2.0 Flash**  
- 🏨 Budget-aware hotel recommendations  
- 📍 Interest-based nearby attractions  
- 💰 Cost estimation with detailed breakdown  
- 📩 Send travel plan via **email (Resend API)**  
- 🕒 Travel history stored per session  
- 🎨 Clean, modern **Streamlit UI**

---

## 🧠 Architecture & Workflow

The project follows a **stateful AI workflow** where each node updates a shared state.

### LangGraph Flow
```text
Analyze Travel Profile
↓
Suggest Hotels
↓
Suggest Places
↓
Estimate Cost
↓
Generate Final Summary
```

Each step is implemented as a **dedicated AI node**, making the system modular, readable, and scalable.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Frontend UI
- **LangGraph** – Graph-based AI workflows
- **LangChain**
- **Google Gemini (gemini-2.0-flash)**
- **Resend API** – Email service
- **python-dotenv** – Environment variable management

---

## 📂 Folder Structure
```text
AI_TRAVEL_PLANNER/
│
├── app.py # Main Streamlit application
├── .env # Environment variables (not committed)
│
├── graph_engine/
│ ├── graph_builder.py # LangGraph workflow definition
│ ├── llm_config.py # Gemini LLM configuration
│ └── nodes.py # AI reasoning nodes
│
├── utils/
│ └── email_sender.py # Email sending logic (Resend API)
│
└── pycache/ # Auto-generated (ignored)

```
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone 
cd TRAVEL_AGENT
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install streamlit langgraph langchain langchain-google-genai python-dotenv resend
```

## 🔐 Environment Variables
```bash
Create a .env file in the root directory:

GOOGLE_API_KEY=your_gemini_api_key
RESEND_API_KEY=your_resend_api_key
```

## ▶️ Run the Application
```bash
streamlit run app.py
```

## Open in browser:
```bash

http://localhost:8501
```

## 🔮 Future Enhancements

- 🗓️ Day-wise itinerary generation

- 🗺️ Google Maps integration

- ✈️ Real flight & hotel APIs

- 👤 User authentication

- ☁️ Cloud deployment (AWS / Azure / GCP)

## 👩‍💻 Author

**Vaishnavi Sainath Pachange**
- Data Science & AI Enthusiast
