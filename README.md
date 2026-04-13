# Student Dropout Prediction Web Application

## Overview
A full-stack Student Dropout Prediction web application built with Python (Flask) and a scikit-learn machine learning engine. It features dynamic Tailwind CSS designs, advanced Antigravity UI effects, and Role-Based Access Controls to visualize and manage student risk metrics.

## Requirements
- Python 3.9+ 

## Setup Instructions

1. **Virtual Environment Setup:**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Mac/Linux
   source venv/bin/activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Initialization:**
   The SQLite database is initialized by running migrations. Ensure you are in the project root.
   ```bash
   flask db init
   flask db migrate -m "Initial Schema"
   flask db upgrade
   ```
   *Alternatively, if you are provided with raw `.sql` migration files under `/migrations/`, you can apply them directly to an `app.db` SQLite file.*

4. **Seed Demonstration Data:**
   Run the data seed commands using standard db context or execute the provided seed scripts.

5. **Train the Initial Model:**
   To train the Random Forest Classifier with the underlying dataset, run:
   ```bash
   python -m app.ml.train
   ```

6. **Start Development Server:**
   ```bash
   python run.py
   ```
   Open your browser to `http://localhost:5000`
