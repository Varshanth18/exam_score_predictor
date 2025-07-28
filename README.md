# Exam Score Predictor


This project is an interactive **Machine Learning web application** built using **Streamlit** that predicts the **exam score of a student** based on lifestyle and academic inputs. It provides a clean and intuitive user interface for educators, students, or data enthusiasts to visualize the impact of daily routines on exam performance.

---

## 🧩 Features

- 🎯 **Predictive Score Output**: Enter lifestyle and academic variables, and the app instantly predicts the likely exam score.
- 📚 **Input Parameters**:
  - Study hours per day (slider, 0–12 hrs, step 0.5)
  - Attendance percentage (0–100%)
  - Mental health rating (scale 1–10)
  - Sleep hours per day (slider, 0–10 hrs, step 0.5)
  - Part-time job status (Yes/No)
- 🖼️ **Styled UI**:
  - Light blue background for a soothing appearance.
  - Centered layout with larger fonts for readability.
  - Custom button and slider styling using embedded CSS.

---

## 📷 App Preview

> <img width="1919" height="818" alt="image" src="https://github.com/user-attachments/assets/95ec44bb-75c5-4240-8ca4-3dd315eb5407" />


```
📘 Student Exam Score Predictor
-------------------------------------
📚 Study hours per day: [ 4.0 ]
🏫 Attendance percentage: [ 70.0 ]
🧠 Mental health rating: [ 5 ]
😴 Sleep hours per day: [ 7.0 ]
💼 Part-time job: [ No ]

🎯 Predict Exam Score Button

🎓 Predicted exam score: 78.25
```
# requirements
  numpy
  streamlit
  joblib
  scikit-learn
  
---

## 🛠️ Tech Stack

| Layer        | Technology    |
|--------------|----------------|
| Frontend     | Streamlit      |
| Backend      | Scikit-learn   |
| Model Format | `joblib` (`.pkl`) |
| Language     | Python         |

---

## 📦 Installation & Setup

Follow these steps to set up and run the project on your local machine:

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/Gayathri-0811/student-score-predictor.git
cd student-score-predictor
```

### 2. 💾 Create Virtual Environment (Optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate     # For Windows
source venv/bin/activate  # For Linux/Mac
```

### 3. 📌 Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, use:

```bash
pip install streamlit numpy joblib
```

### 4. 🧠 Ensure Model File is Present

Make sure `student_model.pkl` is in the project directory. This is your trained ML model file.

### 5. 🚀 Run the App

```bash
streamlit run app.py
```

The app will automatically open in your default web browser at [http://localhost:8501](http://localhost:8501)


---

## 🤖 About the Model

The model accepts **5 inputs** and returns a **predicted exam score** between 0–100:

| Feature          | Description                                  |
|------------------|----------------------------------------------|
| `study_hours`     | Avg daily study time in hours (0.0 to 12.0) |
| `attendance`      | Attendance percentage (0 to 100)            |
| `mental_health`   | Self-rated (1 to 10)                        |
| `sleep_hours`     | Sleep hours per day (0.0 to 10.0)           |
| `part_time_job`   | 1 for Yes, 0 for No                         |

Model can be built using LinearRegression, RandomForest, etc.  
Training is done separately — this app uses the exported `.pkl` model.

---


