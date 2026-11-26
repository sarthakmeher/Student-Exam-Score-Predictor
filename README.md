
# 📘 Student Exam Score Predictor

A machine learning-based application that predicts student exam scores using academic, lifestyle, and behavioral factors.

Built using **Python, Scikit-learn, Pandas, and Streamlit**, this project analyzes student-related data and provides exam score predictions through an interactive web application.

## 🚀 Project Overview

The Student Exam Score Predictor aims to estimate student academic performance based on factors that may influence learning outcomes.

The project uses a dataset containing student information, performs exploratory data analysis, develops a machine learning prediction model, and integrates the trained model into a Streamlit application.

Users can enter their study habits, attendance, sleep patterns, exercise frequency, and other lifestyle information to receive a predicted exam score.

## ✨ Key Features

- **Exam Score Prediction:** Predict student exam scores using a trained machine learning model.
- **Interactive Dashboard:** User-friendly interface built with Streamlit.
- **Study Habits Analysis:** Considers daily study hours and attendance percentage.
- **Lifestyle Factors:** Includes sleep, exercise, and social media usage.
- **Mental Health Input:** Incorporates a self-reported mental health rating.
- **Model Integration:** Loads a previously trained model using Joblib.
- **Performance Categories:** Displays an interpretation of the predicted score.
- **Data Analysis:** Includes exploratory analysis in a Jupyter Notebook.

## 📊 Dataset Information

**Dataset:** `student_performance.csv`

The dataset contains 1,000 student records and 16 columns.

### Dataset Features

| Feature | Description |
|---|---|
| student_id | Unique student identifier |
| age | Student age |
| gender | Student gender |
| study_hours_per_day | Daily study hours |
| social_media_hours | Daily social media usage |
| netflix_hours | Daily Netflix usage |
| part_time_job | Whether the student has a part-time job |
| attendance_percentage | Student attendance percentage |
| sleep_hours | Daily sleep duration |
| diet_quality | Quality of diet |
| exercise_frequency | Exercise frequency per week |
| parental_education_level | Parent's education level |
| internet_quality | Internet access quality |
| mental_health_rating | Self-reported mental health rating |
| extracurricular_participation | Participation in extracurricular activities |
| exam_score | Target variable representing exam score |

## 🧠 Machine Learning Workflow

The project follows a complete machine learning workflow:

1. Load the student performance dataset.
2. Inspect dataset structure and statistical information.
3. Perform data cleaning and preprocessing.
4. Conduct exploratory data analysis.
5. Prepare input features and target variable.
6. Train and evaluate regression models.
7. Save the selected trained model using Joblib.
8. Integrate the model into a Streamlit application.
9. Generate predictions using user-provided inputs.

### Prediction Features

The Streamlit application accepts the following inputs:

- Study hours per day
- Attendance percentage
- Sleep hours
- Exercise frequency per week
- Mental health rating
- Social media hours
- Netflix hours
- Part-time job status

### Target Variable

`exam_score`

The trained regression model estimates the student's expected exam score.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning |
| Joblib | Model serialization and loading |
| Streamlit | Interactive web application |
| Jupyter Notebook | Data analysis and experimentation |

## 📂 Project Structure

```text
Student-Exam-Score-Predictor/
│
├── app.py
│   # Streamlit application for score prediction
│
├── student-analysis.ipynb
│   # Data analysis and machine learning workflow
│
├── student_performance.csv
│   # Student performance dataset
│
├── best_model.pkl
│   # Saved trained prediction model
│
├── label_encoder.pkl
│   # Saved label encoder
│
└── README.md
    # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sarthakmeher/Student-Exam-Score-Predictor.git
```

### 2. Navigate to the Project Directory

```bash
cd Student-Exam-Score-Predictor
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn joblib
```

For reproducible setup, create a `requirements.txt` file containing:

```text
streamlit
pandas
numpy
scikit-learn
joblib
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## 📱 Application Workflow

1. Open the Student Exam Score Predictor application.
2. Enter the student's academic and lifestyle information.
3. Adjust the input sliders and select part-time job status.
4. Click the **Predict Exam Score** button.
5. View the predicted exam score.
6. Review the displayed performance category.

## 🎯 Performance Categories

The application displays the following categories based on the predicted score:

| Predicted Score | Category |
|---|---|
| 85–100 | Excellent Performance |
| 70–84.99 | Good Performance |
| 50–69.99 | Average Performance |
| Below 50 | Needs Improvement |

## 🎯 Project Objectives

- Apply machine learning regression techniques to academic data.
- Understand the factors associated with student performance.
- Perform exploratory data analysis.
- Build a reusable machine learning prediction pipeline.
- Integrate a trained model into a web application.
- Develop an interactive prediction system using Streamlit.

## 🔮 Future Enhancements

- Add visual comparisons of actual and predicted scores.
- Include additional regression models for experimentation.
- Improve model evaluation and performance reporting.
- Add personalized study recommendations.
- Develop student performance trend analysis.
- Deploy the application on Streamlit Community Cloud.

## ⚠️ Disclaimer

This project is developed for educational purposes. Predicted scores are estimates generated by a machine learning model and should not be treated as definitive measures of a student's academic ability.

Lifestyle and mental health inputs are user-reported features and should not be interpreted as medical assessments.

## 👨‍💻 Author

**Sarthak Meher**

- GitHub: [@sarthakmeher](https://github.com/sarthakmeher)
- Repository: [Student Exam Score Predictor](https://github.com/sarthakmeher/Student-Exam-Score-Predictor)

---

⭐ If you find this project useful, consider giving the repository a star!

**Built with Python, Machine Learning, and Streamlit.**
