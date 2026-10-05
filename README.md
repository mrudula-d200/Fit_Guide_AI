
# 🌸 FitHer AI

### 🚀 https://fitguideai-ftg4x2wbtacngcq6zq62rh.streamlit.app/

👉 [Try FitHer AI](https://fitguideai-ftg4x2wbtacngcq6zq62rh.streamlit.app/)

### Your Personal AI Fitness & Wellness Companion 💪✨

FitHer AI is an AI-powered fitness and wellness web application built with **Streamlit** and the **Groq API**. It provides personalized workout, nutrition, and fitness guidance based on the user's age, height, weight, fitness goal, gym experience, workout frequency, and food preference.

---

## ✨ Features

### 👤 Personalized Fitness Profile

Users can enter:

* Age
* Height
* Weight
* Fitness goal
* Gym experience
* Gym days per week
* Food preference

### 📊 Fitness Calculations

FitHer AI calculates:

* BMI
* BMI category
* Estimated daily calorie requirement
* Estimated protein requirement
* Estimated daily water intake

### 🏋️ Personalized Workout Plans

Workout plans are provided according to the user's experience level:

* Beginner
* Intermediate
* Advanced

The application provides exercises, sets, repetitions, and recommended workout duration.

### 🍎 Nutrition Recommendations

The application provides meal suggestions based on:

* Fitness goal
* Food preference
* Estimated calorie requirement
* Protein requirement

Supported food preferences:

* Vegetarian
* Non-Vegetarian
* Vegan

### 🤖 AI Fitness Chatbot

FitHer AI uses the **Groq API** to provide AI-powered answers about:

* Workouts
* Nutrition
* Muscle building
* Weight management
* Pre-workout food
* Meal planning
* Fitness routines

The chatbot also uses the user's fitness profile to provide more personalized responses.

### 💬 Quick Questions

Users can quickly ask questions such as:

* What should I eat today?
* Give me today's workout
* What should I eat before gym?
* How can I build muscle?
* Give me a 7-day meal plan

---

## 🛠️ Technologies Used

* **Python 3.11.9**
* **Streamlit**
* **Groq API**
* **OpenAI GPT-OSS 20B model through Groq**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Requests**
* **Python-dotenv**
* **LangChain**
* **OpenCV**
* **Pillow**
* **Matplotlib**
* **SQLAlchemy**

---

## 📁 Project Structure

```text
FIT_Guide_AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
└── venv/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project folder

```bash
cd FIT_Guide_AI
```

### 3. Create a virtual environment

```bash
py -3.11 -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Groq API Configuration

FitHer AI uses the Groq API for its AI chatbot.

Create a file named:

```text
.env
```

in the project root directory.

Add:

```text
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your actual Groq API key.

### ⚠️ Important

Never upload your `.env` file or API key to GitHub.

The `.gitignore` file should contain:

```text
.env
venv/
__pycache__/
```

---

## ▶️ Run the Application

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Then run:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 🤖 AI Model

FitHer AI uses the following Groq model:

```text
openai/gpt-oss-20b
```

The model is used to generate personalized responses based on the user's fitness profile and questions.

---

## 🧮 BMI Calculation

BMI is calculated using:

```text
BMI = Weight (kg) / Height² (m)
```

The application categorizes BMI into:

* Underweight
* Normal range
* Overweight
* Obesity range

---

## 🎯 Project Goal

The goal of FitHer AI is to provide an easy-to-use AI-powered fitness companion that helps users understand their fitness profile and receive personalized general guidance about workouts, nutrition, and healthy habits.

---

## ⚠️ Disclaimer

FitHer AI provides general fitness and wellness information and estimates. It is not a substitute for professional medical advice.

Users with medical conditions, injuries, eating disorders, pregnancy-related concerns, or other serious health concerns should consult a qualified healthcare professional.

---

## 👩‍💻 Developer

**Bodige Mrudula**

Built as an AI-powered fitness and wellness project using Python, Streamlit, and Groq API.
