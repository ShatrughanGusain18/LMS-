# 🧠 AI in Personalized Learning

**Author:** Shatrughan Gusain  
**Track:** Data Analytics / AI  
**Project Type:** Adaptive Learning LMS using AI  
**Tech Stack:** Python, Streamlit, Hugging Face Transformers, LangChain

---

## 📘 Overview
**AI in Personalized Learning** is an adaptive **Learning Management System (LMS)** that leverages **Artificial Intelligence** to generate personalized math assignments based on learner performance.  
The system automatically adjusts the difficulty level of questions between levels **1–10**, enabling a tailored learning experience for every student.

This project demonstrates how **Large Language Models (LLMs)** like **Mistral-7B**, **Llama-3.1-8B**, and others can be used locally to enhance engagement and automate content creation.

---

## 🚩 Problem Statement
Traditional LMS platforms serve identical content and difficulty levels to all learners, leading to disengagement and ineffective outcomes.  
This project addresses the problem by developing an **AI-powered adaptive LMS** that dynamically adjusts questions based on individual learner performance and response time.

---

## 🎯 Objectives
- Develop a locally deployable AI-based LMS for adaptive learning.  
- Utilize open-source **Large Language Models (LLMs)** for question generation.  
- Build a **Python-Streamlit** based interactive platform for learners.  
- Enable **level-based progression** and performance tracking.

---

## ⚙️ Methodology
The system was developed using **Python 3.13** and key machine learning frameworks from **Hugging Face**.  
Three main modules handle core functionality:

| File | Purpose |
|------|----------|
| `model.py` | Loads and manages the LLM using LangChain + Hugging Face. |
| `generate.py` | Generates a batch of questions based on difficulty level. |
| `app.py` | Streamlit front-end for profile, lecture, and adaptive assignment interface. |

### **Project Workflow**
1. Learner logs in and starts an assignment.  
2. AI generates a batch of 3 questions at the learner’s level.  
3. Based on responses and timing, the system adjusts the next level (up/down).  
4. Progress is stored session-wise and displayed in the dashboard.

---

## 🧩 Tools & Technologies
- **Python 3.13**
- **Streamlit (Frontend UI)**
- **PyTorch + Transformers (LLMs)**
- **LangChain + Hugging Face Hub**
- **SentencePiece, Accelerate**
- **RTX 4070, Ryzen 7 (Local model inference)**

---

## 📦 Requirements

Below are the dependencies required for the project.  
These can be installed using the provided `requirements.txt`.

```text
torch --index-url https://download.pytorch.org/whl/cu121
transformers>=4.37.0
accelerate>=0.26.0
langchain>=0.3.0
langchain-community>=0.2.0
sentencepiece
protobuf==4.25.3
python-dotenv

langchain-huggingface
transformers
huggingface-hub

langchain-core

streamlit==1.49.1
```

Install using:
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-repo-name>.git
   cd AI-in-Personalized-Learning
   ```

2. **Set Up the Environment**
   - Create a `.env` file in the root directory with your Hugging Face token:
     ```bash
     HF_TOKEN=your_huggingface_token_here
     ```

3. **Run Streamlit App**
   ```bash
   streamlit run app.py
   ```

4. **Access in Browser**
   - Go to `http://localhost:8501`  
   - Select **Assignments (Math)** to start the adaptive learning demo.

---

## 🧠 Working Demo
- The app generates **3 questions per batch**.
- Learner’s performance decides if they level up, stay, or level down.
- Each session runs for **10 batches**.
- Adaptive logic ensures a personalized difficulty curve.

---

## 📊 Results & Observations
- Successfully generates math questions locally using LLMs.
- Upgraded from **TinyLlama → Mistral → Llama-3.1-8B**, achieving better question coherence.
- Reduced dependency on APIs; runs entirely offline.
- Demonstrates real-world potential for **AI-powered personalized education**.

---

## 🔮 Future Scope
- Integrate **automated grading** and **real-time performance analytics**.
- Expand subjects beyond math.
- Add **voice-based tutoring** and **NLP feedback**.
- Deploy as a **cloud-based scalable learning platform**.

---

## 🏁 Conclusion
This project demonstrates how **AI can revolutionize personalized learning** by adapting content dynamically to each learner’s capability.  
By leveraging open-source LLMs and modern AI frameworks, we can build powerful, ethical, and scalable education systems for the future.

---

### 👨‍💻 Author
**Shatrughan Gusain**  
AI & Data Analytics Trainer
  
 
