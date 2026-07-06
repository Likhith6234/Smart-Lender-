
# Smart Lender – Loan Approval Prediction System

A Machine Learning-based web application that predicts whether a loan application is likely to be approved based on applicant details. The application uses a trained Random Forest model integrated with the Flask web framework to provide instant loan approval predictions through a simple and responsive web interface.

---

# Project Links

| Resource | Link |
|----------|------|
| **Live Demo** | https://your-render-link.onrender.com |
| **GitHub Repository** | https://github.com/your-username/Smart-Lender |

---

# Project Overview

Loan approval is one of the most important processes in the banking sector. Banks receive numerous loan applications every day, making manual verification time-consuming and prone to human error.

The Smart Lender project uses Machine Learning to predict whether a loan application is likely to be approved based on applicant information such as income, education, employment status, loan amount, credit history, and property area.

The project covers the complete Machine Learning lifecycle, including data preprocessing, model training, evaluation, deployment, and user interaction through a Flask web application.

---

# Features

- User-friendly loan application interface
- Real-time loan approval prediction
- Machine Learning-based prediction model
- Input validation for applicant details
- Responsive web interface
- Random Forest prediction model
- Flask backend integration
- Cloud deployment using Render

---

# Machine Learning

The following Machine Learning algorithms were trained and evaluated:

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Gradient Boosting

After comparing the performance of all models, **Random Forest** was selected as the final deployed model because it achieved the highest prediction accuracy.

---

# Technology Stack

| Layer | Technologies |
|--------|--------------|
| Programming Language | Python |
| Web Framework | Flask |
| Machine Learning | Random Forest, Scikit-learn |
| Data Processing | Pandas, NumPy |
| Model Storage | Pickle |
| Frontend | HTML5, CSS3, Jinja2 |
| Development Tools | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |
| Deployment | Render |

---

# Project Structure

```text
Smart-Lender/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
├── rdf.pkl
├── scale1.pkl
├── loan_dataset.csv
│
├── templates/
│   ├── home.html
│   ├── predict.html
│   └── submit.html
│
├── static/
│   ├── main.css
│   └── main.js
│
└── main.ipynb
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/Smart-Lender.git
```

## Navigate to the Project Directory

```bash
cd Smart-Lender
```

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

## Open in Browser

```text
http://127.0.0.1:5000
```

---

# Input Features

The prediction model uses the following applicant details:

1. Gender
2. Married Status
3. Dependents
4. Education
5. Self Employed
6. Applicant Income
7. Co-applicant Income
8. Loan Amount
9. Loan Amount Term
10. Credit History
11. Property Area

---

# Prediction Output

The system predicts one of the following outcomes:

- Loan Will be Approved
- Loan Will Not be Approved

---

# Future Improvements

- Integration with real-time banking databases
- CIBIL score integration
- Aadhaar and PAN verification
- Email and SMS notifications
- Mobile application development
- Loan eligibility score visualization
- Cloud database integration

---

# Deployment

The application is deployed on **Render** and can be accessed through the live demo link.

**Live Application**

https://your-render-link.onrender.com

---

# Authors

- Your Name
- Team Member 2
- Team Member 3
- Team Member 4

---

# License

This project is developed for educational and academic purposes.
