# Personality Prediction System

This is a web application built with Flask that predicts a candidate's personality based on input data and their resume. It uses machine learning models to make predictions and displays the results on a web page.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/personality-prediction-system.git

2. **Navigate to project directory:**
 cd personality-prediction-system

3. **Install dependencies:**
 pip install -r requirements.txt

4. **Download Spacy model:**
   python -m spacy download en_core_web_sm

5. **Run Flask:**
   python main.py

6. Open your web browser and go to **http://127.0.0.1:5000** to access the application.


**Usage**
Enter the candidate's details and upload their resume on the home page.
Click the "Predict" button to see the predicted personality and the extracted information from the resume.

**Directory Structure**
app.py: Main Flask application file.
templates/: Contains HTML templates for rendering the web pages.
static/: Contains static files such as CSS and JavaScript.
requirements.txt: List of Python dependencies.
